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

## Configuration

Site configuration can be modified in `_config.yml`.
