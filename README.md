# andyfries.github.io

Personal blog and website built with Jekyll.

## Local Development

### Prerequisites

- Ruby (3.0 or higher)
- Bundler (`gem install bundler`)

### Running the Site Locally

1. Install dependencies:
   ```bash
   bundle install
   ```

2. Start the Jekyll server:
   ```bash
   bundle exec jekyll serve
   ```

3. Open your browser to [http://localhost:4000](http://localhost:4000)

The server will automatically rebuild the site when you make changes to files.

### Adding New Posts

Create a new file in the `_posts` directory with the format:
```
YYYY-MM-DD-title-of-post.md
```

Include front matter at the top:
```yaml
---
layout: post
title: "Your Post Title"
---
```

### Working with Drafts

Drafts are unpublished posts stored in the `_drafts` folder.

1. Create a draft (no date prefix needed):
   ```bash
   _drafts/my-draft-post.md
   ```

2. Preview drafts locally:
   ```bash
   bundle exec jekyll serve --drafts
   ```

3. Publish a draft by moving it to `_posts` and adding the date prefix:
   ```bash
   mv _drafts/my-draft-post.md _posts/2025-10-25-my-draft-post.md
   ```

## Configuration

Site configuration can be modified in `_config.yml`.
