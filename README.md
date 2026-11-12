# WHAT™ landing page

The website at https://whatbadge.com, served by GitHub Pages from this repository.

- `index.html` is the whole page. The `CONFIG` block near the bottom holds the Stripe reservation link, the email sign-up form address and the survey link; fill those in to switch them on.
- The commercials and images sit next to it.
- `CNAME` tells GitHub Pages to serve the site at whatbadge.com.

## Updates show up right away

Every push to `main` runs `bump.py` (via the GitHub Action in `.github/workflows`). It stamps a new version on the page and on each video and image, so visitors with an old copy cached get the new one automatically on their next visit, with no refresh needed. To do it by hand: `python3 bump.py`, then commit and push.
