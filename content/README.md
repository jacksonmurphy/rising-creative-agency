# Music release updater

This repo includes a GitHub Actions workflow that rebuilds the homepage music section from `content/music-releases.json`.

## How to update future music releases

1. Add or replace cover images in `assets/`
2. Edit `content/music-releases.json`
3. Commit the changes to `main`
4. GitHub Actions regenerates `index.html`
5. Cloudflare Pages auto-deploys the updated site

## Files involved

- `content/music-releases.json` — source of truth for the music section
- `scripts/update_music_section.py` — generator script
- `.github/workflows/update-site-from-music-content.yml` — workflow

## Manual run

In GitHub, go to **Actions** → **Update site from music content** → **Run workflow**.
