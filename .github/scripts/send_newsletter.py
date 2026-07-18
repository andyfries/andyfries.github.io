#!/usr/bin/env python3
"""Create a Buttondown *draft* for each newly added blog post.

Reads the full-content feed (_site/newsletter.xml), matches it against the
post files added in this push (passed as CLI args), and POSTs a draft email
per matched post. Drafts are never sent automatically — you review and send
from the Buttondown dashboard.
"""
import html
import json
import os
import re
import sys
import urllib.error
import urllib.request

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
        slug = slug_from_url(link.group(1))
        entries[slug] = {
            "title": html.unescape(title.group(1).strip()),
            # feed content is xml-escaped HTML; unescape once back to real HTML
            "body": html.unescape(content.group(1).strip()),
        }
    return entries


def create_draft(api_key, subject, body):
    payload = json.dumps(
        {"subject": subject, "body": body, "status": "draft"}
    ).encode()
    req = urllib.request.Request(
        API_URL,
        data=payload,
        method="POST",
        headers={
            "Authorization": f"Token {api_key}",
            "Content-Type": "application/json",
        },
    )
    with urllib.request.urlopen(req) as resp:
        return resp.status


def main():
    api_key = os.environ.get("BUTTONDOWN_KEY")
    if not api_key:
        sys.exit("BUTTONDOWN_KEY is not set")

    added_posts = [p for p in sys.argv[1:] if p.startswith("_posts/")]
    if not added_posts:
        print("No newly added posts in this push; nothing to draft.")
        return

    with open(FEED_PATH, encoding="utf-8") as f:
        entries = parse_feed(f.read())

    for path in added_posts:
        slug = slug_from_post_filename(path)
        entry = entries.get(slug)
        if not entry:
            print(f"WARN: no feed entry found for {path} (slug '{slug}'); skipping")
            continue
        try:
            status = create_draft(api_key, entry["title"], entry["body"])
            print(f"Drafted '{entry['title']}' (HTTP {status})")
        except urllib.error.HTTPError as e:
            print(f"ERROR drafting '{entry['title']}': HTTP {e.code} {e.read().decode()}")
            sys.exit(1)


if __name__ == "__main__":
    main()
