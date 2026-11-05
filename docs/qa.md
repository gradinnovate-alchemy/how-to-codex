# Review log — 2026-11-05

## Research

Read official Quickstart, Build skills, AGENTS.md and Scheduled tasks pages. Old developers.openai.com/codex links redirected to ChatGPT Learn. Wrote original Traditional Chinese explanations and linked relevant official sources. Product menu labels are explicitly version-dependent.

## Iteration 1

Built eight chapters, full prompt examples, chapter search, local progress, clipboard action, responsive navigation, imagegen cover and Matplotlib 220 dpi diagram. Published public organization repository and GitHub Actions Pages deployment.

## Iteration 2

Observed the compact mobile diagram and reviewed the collapsed navigation behavior. Added a link to open the original high-resolution PNG. Set collapsed mobile sidebar visibility to hidden so its controls are excluded from keyboard focus.

Both implementation deployments completed successfully:

- https://github.com/gradinnovate-alchemy/how-to-codex/actions/runs/41966527019
- https://github.com/gradinnovate-alchemy/how-to-codex/actions/runs/41966613104

## Public-site verification

URL: https://gradinnovate-alchemy.github.io/how-to-codex/

- 390 × 844 mobile and 1280 × 900 desktop inspected visually in browser.
- Both PNG assets fully loaded, including deployment under /how-to-codex/.
- No horizontal overflow: mobile document width 375 for innerWidth 390; desktop 1265 for innerWidth 1280 (scrollbar accounts for difference).
- Search with Skill filters matching chapter content. Unmatched search shows empty state.
- Mobile menu expands, chapter selection collapses it, aria-expanded becomes false.
- Copy Skill example verified via browser clipboard, matching frontmatter.
- Chapter completion changes progress to 1 / 8 and survives reload; test checkmark reset afterward.
- High-resolution diagram link present on final public page.
- Browser console error log empty.
- Local HTML fragment targets and referenced assets all exist.
- JavaScript syntax check passes.
- Tracked text files contain no GitHub PAT patterns. Credential loaded only into process environment from user-specified keystore.

Evidence: pages-mobile.jpg and pages-desktop.jpg in this directory.

## Limits

The computer-control tool explicitly forbids controlling Codex.app. No real Codex conversation screenshot was captured. Conversation blocks are labeled teaching illustrations. Cover is labeled AI-generated. No recurring background automation was created; this was a bounded research/build/deploy/review loop.
