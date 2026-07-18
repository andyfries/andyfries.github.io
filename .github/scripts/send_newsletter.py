#!/usr/bin/env python3
"""Create a Buttondown email for each given blog post.

Reads the full-content feed (_site/newsletter.xml), matches it against the
post files passed as CLI args, and POSTs one email per matched post. The
BUTTONDOWN_STATUS env var controls the outcome: "draft" saves it for review,
"about_to_send" sends it to subscribers immediately (irreversible).
"""
import html
import json
import os
import re
import sys
import urllib.error
import urllib.request
from urllib.parse import urlsplit

FEED_PATH = "_site/newsletter.xml"
API_URL = "https://api.buttondown.com/v1/emails"

ENTRY_RE = re.compile(r"<entry>(.*?)</entry>", re.S)
TITLE_RE = re.compile(r"<title>(.*?)</title>", re.S)
LINK_RE = re.compile(r'<link href="(.*?)"', re.S)
CONTENT_RE = re.compile(r'<content type="html">(.*?)</content>', re.S)


def slug_from_post_filename(path):
    """_posts/2026-07-18-inputs-not-outputs.md -> inputs-not-outputs"""
    name = os.path.basename(path)
    name = re.sub(r"\.(md|markdown|html)$", "", name)
    return re.sub(r"^\d{4}-\d{2}-\d{2}-", "", name)


def slug_from_url(url):
    """https://andyfries.com/inputs-not-outputs/ -> inputs-not-outputs"""
    return url.rstrip("/").rsplit("/", 1)[-1]


def parse_feed(text):
    entries = {}
    for block in ENTRY_RE.findall(text):
        title = TITLE_RE.search(block)
        link = LINK_RE.search(block)
        content = CONTENT_RE.search(block)
        if not (title and link and content):
            continue
        url = link.group(1)
        slug = slug_from_url(url)
        entries[slug] = {
            "title": html.unescape(title.group(1).strip()),
            "url": url,
            # feed content is xml-escaped HTML; unescape once back to real HTML
            "body": html.unescape(content.group(1).strip()),
        }
    return entries


def absolutize_links(body, url):
    """Rewrite root-relative href/src (e.g. "/why-write") to absolute URLs.

    Root-relative links resolve fine on the site but break in email clients,
    which have no base domain. Derives the origin from the post's own URL and
    skips protocol-relative ("//host") and already-absolute links.
    """
    parts = urlsplit(url)
    base = f"{parts.scheme}://{parts.netloc}"
    return re.sub(
        r'(href|src)="(/(?!/)[^"]*)"',
        lambda m: f'{m.group(1)}="{base}{m.group(2)}"',
        body,
    )


def browser_header(url):
    """Email-only note linking back to the web version of the post."""
    display = re.sub(r"^https?://", "", url).rstrip("/")
    return (
        f'<blockquote><p><em>If you\'d prefer reading this in a browser, go to '
        f'<a href="{url}">{display}</a>.</em></p></blockquote>\n\n'
    )


def create_email(api_key, subject, body, status):
    # status "draft" = save for review; "about_to_send" = send to subscribers now.
    payload = json.dumps(
        {"subject": subject, "body": body, "status": status}
    ).encode()
    headers = {
        "Authorization": f"Token {api_key}",
        "Content-Type": "application/json",
    }
    if status == "about_to_send":
        # Buttondown requires explicit confirmation to send (not just draft) via API.
        headers["X-Buttondown-Live-Dangerously"] = "true"
    req = urllib.request.Request(
        API_URL,
        data=payload,
        method="POST",
        headers=headers,
    )
    with urllib.request.urlopen(req) as resp:
        return resp.status


def main():
    api_key = os.environ.get("BUTTONDOWN_KEY")
    if not api_key:
        sys.exit("BUTTONDOWN_KEY is not set")

    status = os.environ.get("BUTTONDOWN_STATUS", "draft")
    if status not in ("draft", "about_to_send"):
        sys.exit(f"Unexpected BUTTONDOWN_STATUS '{status}' (want 'draft' or 'about_to_send')")
    verb = "Sent" if status == "about_to_send" else "Drafted"

    added_posts = [p for p in sys.argv[1:] if p.startswith("_posts/")]
    if not added_posts:
        print("No posts given; nothing to do.")
        return

    with open(FEED_PATH, encoding="utf-8") as f:
        entries = parse_feed(f.read())

    for path in added_posts:
        slug = slug_from_post_filename(path)
        entry = entries.get(slug)
        if not entry:
            print(f"WARN: no feed entry found for {path} (slug '{slug}'); skipping")
            continue
        body = browser_header(entry["url"]) + absolutize_links(entry["body"], entry["url"])
        try:
            code = create_email(api_key, entry["title"], body, status)
            print(f"{verb} '{entry['title']}' (HTTP {code})")
        except urllib.error.HTTPError as e:
            print(f"ERROR ({verb.lower()}) '{entry['title']}': HTTP {e.code} {e.read().decode()}")
            sys.exit(1)


if __name__ == "__main__":
    main()
