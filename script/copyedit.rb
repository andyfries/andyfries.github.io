#!/usr/bin/env ruby
# frozen_string_literal: true

# script/copyedit.rb — deterministic copy-editing normalizations for posts.
#
# Runs the mechanical, non-judgment fixes so the editor pass can focus on prose:
#   1. Rewrites internal cross-links to other posts into Jekyll's {% post_url %}
#      idiom, so a broken slug fails the build instead of shipping a dead link.
#      Handles absolute (https://andyfries.com/slug/) and root-relative (/slug/)
#      forms, preserves any #anchor, and leaves a link alone if its slug doesn't
#      map to a real post (e.g. a standalone page).
#   2. Strips trailing whitespace from the end of every line.
#
# Usage:
#   ruby script/copyedit.rb _posts/2026-08-30-abolishing-human-code-review.md [more files...]
#
# Idempotent: running it twice makes no further changes. Reports what it did.

require "pathname"

ROOT = Pathname.new(__dir__).join("..").expand_path
POSTS_DIR = ROOT.join("_posts")

# Build slug => dated basename (sans .md) map, e.g.
#   "embracing-difficulty" => "2026-05-17-embracing-difficulty"
def post_slug_map
  map = {}
  Dir.glob(POSTS_DIR.join("*.md")).each do |path|
    base = File.basename(path, ".md")
    slug = base.sub(/\A\d{4}-\d{2}-\d{2}-/, "")
    map[slug] = base
  end
  map
end

# Absolute self-links: ](https://andyfries.com/slug/#anchor)
ABSOLUTE = %r{\]\(https?://(?:www\.)?andyfries\.com/([a-z0-9\-]+)/?(\#[a-z0-9\-]+)?\)}
# Root-relative self-links: ](/slug/#anchor)
ROOT_RELATIVE = %r{\]\(/([a-z0-9\-]+)/?(\#[a-z0-9\-]+)?\)}

def rewrite_links(content, slug_map)
  converted = []
  skipped = []

  replacer = lambda do |match, slug, anchor|
    base = slug_map[slug]
    if base
      converted << slug
      "]({% post_url #{base} %}#{anchor})"
    else
      skipped << slug
      match # leave untouched — not a known post (e.g. a standalone page)
    end
  end

  content = content.gsub(ABSOLUTE) { replacer.call($~[0], $1, $2 || "") }
  content = content.gsub(ROOT_RELATIVE) { replacer.call($~[0], $1, $2 || "") }

  [content, converted, skipped]
end

def strip_trailing_ws(content)
  count = content.each_line.count { |l| l =~ /[ \t]+(\r?\n|\z)/ }
  [content.gsub(/[ \t]+(?=\r?\n|\z)/, ""), count]
end

files = ARGV
if files.empty?
  warn "usage: ruby script/copyedit.rb <file.md> [more...]"
  exit 1
end

slug_map = post_slug_map
changed_any = false

files.each do |file|
  unless File.file?(file)
    warn "skip (not a file): #{file}"
    next
  end

  original = File.read(file)
  content, converted, skipped = rewrite_links(original, slug_map)
  content, ws_lines = strip_trailing_ws(content)

  if content == original
    puts "#{file}: no changes"
    next
  end

  File.write(file, content)
  changed_any = true
  puts "#{file}:"
  puts "  links -> post_url: #{converted.length} (#{converted.uniq.join(", ")})" unless converted.empty?
  puts "  trailing whitespace stripped from #{ws_lines} line(s)" if ws_lines.positive?
  unless skipped.empty?
    puts "  left alone (slug not a known post): #{skipped.uniq.join(", ")}"
  end
end

exit(changed_any ? 0 : 0)
