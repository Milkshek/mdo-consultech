# MDO Consultech portfolio — implementation plan

**Goal:** Deliver the approved bilingual one-page freelance portfolio, with LinkedIn and both supplied CVs.

**Architecture:** Buildless static HTML at `/` and `/en/`, shared CSS and progressively enhanced JavaScript. A small Python generator keeps both translations and structural markup in sync. Works on GitHub Pages without a server-side runtime.

**Design approved in conversation:** Bordeaux #7c0f1a, warm cream, gold details, serif display type. Header navigation, introductory hero with supplied emblem, three services (websites, applications, technical leadership), three CV-backed experience summaries, Build/Solve/Evolve approach, LinkedIn and two PDF downloads. No form, invented results, analytics or public phone/email.

**Execution:** Inline, in the existing empty repository. No separate checkout needed because there is no existing work to isolate.

- [x] Add a static acceptance check for both languages, local asset/link integrity, sections, PDF downloads, and no forms. Run before implementation to confirm absent pages fail.
- [x] Copy original logo and both PDF files; retain original filenames only in provenance documentation, use stable public URLs.
- [x] Generate complete translated documents from `scripts/build.py`; include language alternates, titles, descriptions, skip links, and semantic headings.
- [x] Implement responsive `assets/site.css`: spacious editorial composition, fluid headline, grid-to-single-column transitions, legible contrasts, visible keyboard focus, reduced-motion support.
- [x] Adapt the small liquid vector-field pattern from liquid-logo to the emblem only in `assets/logo.js`, retaining MIT attribution. Use the original image as fallback. Stop rendering offscreen, in hidden tabs and for reduced motion; expose a pause control. Keep content independent of animation and JavaScript.
- [x] Check both pages in a real browser at desktop/mobile widths; test language and navigation links, downloads, pause, reduced motion, disabled WebGL, and console errors.
- [x] Open the completed local preview; document build/preview commands and factual content sources. Do not push or publish without a deployment request.

**Verification:** `python3 scripts/build.py`; `python3 -m unittest discover -s tests`; browser inspection and functional tests against `python3 -m http.server 4173 --bind 127.0.0.1`.

## Verification result

2026-09-26: static acceptance checks and JavaScript syntax check pass. Chromium browser checks pass for both languages at 320, 360, 390, 768, 1024 and 1440px: no horizontal overflow; language switching, section anchors, four download interactions, pause/resume, reduced motion, WebGL fallback, JavaScript-disabled content, and no page/resource errors. Full-page FR/EN desktop/mobile screenshots inspected. Code review findings (decorative-ring overflow and PDF language metadata) corrected. Local preview open; files remain uncommitted and unpublished.
