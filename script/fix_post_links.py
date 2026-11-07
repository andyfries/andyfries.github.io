#!/usr/bin/env python3
"""Lint Markdown posts for links to other posts that should use Jekyll's post_url tag.

Finds inline links like [text](https://andyfries.com/why-write/) or [text](/why-write)
and reference definitions like [ref]: /why-write/ that point at a published post in
_posts/, and rewrites them to [text]({% post_url 2026-06-12-why-write %}).
Anchors (#section) are preserved after the tag. Links inside fenced code blocks and
inline code spans are ignored. Links to non-post pages (e.g. /why-write-original/,
/puzzles/) are left alone. Links to unknown slugs are reported, not changed.

Usage:
  fix_post_links.py [--fix] [--site-root DIR] FILE...
Without --fix, reports findings and exits 1 if any link needs changing.
"""
import argparse
import re
import sys
from pathlib import Path

DOMAINS = r"(?:https?://)?(?:www\.)?andyfries\.com"
# URL target: optional own-domain prefix, then a single-segment path /slug[/][#anchor]
TARGET = re.compile(rf"^(?:{DOMAINS})?/(?P<slug>[A-Za-z0-9_-]+)/?(?P<anchor>#[^\s)]*)?$")
INLINE = re.compile(r"(?P<pre>\]\()(?P<url>[^)\s]+)(?P<post>\))")
REFDEF = re.compile(r"^(?P<pre>\s{0,3}\[[^\]]+\]:\s*)(?P<url>\S+)(?P<post>.*)$")
CODE_SPAN = re.compile(r"`[^`]*`")
POST_FILE = re.compile(r"^(\d{4}-\d{2}-\d{2})-(.+)\.(?:md|markdown|html)$")


def load_posts(site_root: Path) -> dict:
    """Map slug -> post_url name (filename without extension) for _posts/."""
    posts = {}
    for f in sorted((site_root / "_posts").glob("*")):
        m = POST_FILE.match(f.name)
        if m:
            posts[m.group(2)] = f.stem
    return posts


def fix_text(text: str, posts: dict, self_stem: str):
    changes, unknown = [], []
    out_lines = []
    in_fence = False

    def rewrite(m, lineno):
        url = m.group("url")
        t = TARGET.match(url)
        if not t:
            return m.group(0)
        slug, anchor = t.group("slug"), t.group("anchor") or ""
        if slug in posts:
            name = posts[slug]
            new = f"{{% post_url {name} %}}{anchor}"
            changes.append((lineno, url, new))
            return f"{m.group('pre')}{new}{m.group('post')}"
        # Absolute links to our own domain that don't match a post are worth flagging;
        # bare relative paths are often pages (about, puzzles) so only flag absolute ones.
        if re.match(DOMAINS, url) and slug != self_stem:
            unknown.append((lineno, url))
        return m.group(0)

    for lineno, line in enumerate(text.splitlines(keepends=True), 1):
        if line.lstrip().startswith(("```", "~~~")):
            in_fence = not in_fence
            out_lines.append(line)
            continue
        if in_fence:
            out_lines.append(line)
            continue
        # Protect inline code spans from rewriting.
        spans = []
        def stash(m):
            spans.append(m.group(0))
            return f"\x00{len(spans) - 1}\x00"
        work = CODE_SPAN.sub(stash, line)
        if REFDEF.match(work):
            work = REFDEF.sub(lambda m: rewrite(m, lineno), work, count=1)
        else:
            work = INLINE.sub(lambda m: rewrite(m, lineno), work)
        work = re.sub(r"\x00(\d+)\x00", lambda m: spans[int(m.group(1))], work)
        out_lines.append(work)
    return "".join(out_lines), changes, unknown


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("files", nargs="+", type=Path)
    ap.add_argument("--fix", action="store_true", help="rewrite files in place")
    ap.add_argument("--site-root", type=Path, default=Path.cwd(), help="Jekyll site root (default: cwd)")
    args = ap.parse_args()

    posts = load_posts(args.site_root)
    if not posts:
        print(f"error: no posts found in {args.site_root / '_posts'}", file=sys.stderr)
        return 2

    pending = 0
    for path in args.files:
        text = path.read_text(encoding="utf-8")
        new_text, changes, unknown = fix_text(text, posts, path.stem)
        for lineno, old, new in changes:
            verb = "fixed" if args.fix else "needs post_url"
            print(f"{path}:{lineno}: {verb}: {old} -> {new}")
        for lineno, url in unknown:
            print(f"{path}:{lineno}: warning: own-domain link matches no published post: {url}")
        if changes:
            if args.fix:
                path.write_text(new_text, encoding="utf-8")
            else:
                pending += len(changes)
    if pending:
        print(f"{pending} link(s) need post_url. Re-run with --fix to rewrite.")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
