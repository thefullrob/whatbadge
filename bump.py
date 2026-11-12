#!/usr/bin/env python3
"""Stamp a new version on whatbadge.com so visitors never see a stale copy.

Run after any change (the GitHub Action runs it automatically on every push):
  python3 bump.py
It writes a fresh version into version.json, the page's site-version tag,
and the ?v= on every video and image the page loads.
"""
import re, json, time, pathlib
root = pathlib.Path(__file__).parent
v = time.strftime('%Y%m%d%H%M%S')
p = root / 'index.html'
s = p.read_text(encoding='utf-8')
s = re.sub(r'<meta name="site-version" content="[^"]*">', f'<meta name="site-version" content="{v}">', s)
s = re.sub(r'((?:ad-[a-z-]+\.mp4|poster-[a-z-]+\.jpg|hero-badges\.jpg|wearing-badge\.jpg))(\?v=\w+)?', rf'\1?v={v}', s)
p.write_text(s, encoding='utf-8')
(root / 'version.json').write_text(json.dumps({'v': v}) + '\n', encoding='utf-8')
print('version', v)
