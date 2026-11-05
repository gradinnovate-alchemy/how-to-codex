# How to Codex

12 章繁體中文 Codex 實作手冊，從第一次任務、Agent 概念、AGENTS.md、Skill 設計，到自動化、網路基礎與部署迴圈。

- Website: https://gradinnovate-alchemy.github.io/how-to-codex/
- 純 HTML/CSS/JS，無建置依賴。
- 本機啟動：`python3 -m http.server 8765`
- Push 到 main 由 GitHub Actions 部署 Pages，只發布網站與 assets。
- 流程圖重建：安裝 matplotlib 後執行 `python3 scripts/diagram.py`。
- 進度儲存在訪客瀏覽器 localStorage，沒有後端、分析追蹤或註冊。

## 來源

查證日期：2026-11-05（Asia/Taipei）。官方頁面：

- https://learn.chatgpt.com/docs/quickstart
- https://learn.chatgpt.com/docs/build-skills
- https://learn.chatgpt.com/docs/agent-configuration/agents-md
- https://learn.chatgpt.com/docs/automations?surface=app

OpenAI 舊 Codex 文件網址目前會導向部分上述頁面；本手冊有區分宿主與能力限制。此為獨立學習教材，非官方文件。

## 素材

- `assets/workshop.png`：內建 imagegen 生成，插畫概念為紙雕 Agent 工作坊（路徑、工具、驗證關卡）。完整提示見 `docs/assets.md`。
- `assets/agent-loop.png`：Matplotlib，220 dpi，概念流程圖；非產品內部架構。
- 教學對話是明確標示的示意。電腦控制工具禁止操作 Codex App，因此本版沒有真實產品對話截圖。
- 網站瀏覽器驗證截圖見 `docs/`，不包含私人桌面或憑證。

## 更新迴圈

1. 查詢並閱讀官方來源，記錄查證日期。
2. 選定具體學習任務、更新內容與素材。
3. 本機檢查導覽、互動、桌面與手機畫面。
4. Commit/push，確認 Actions 與公開 Pages。
5. 依真實畫面修正，更新 `docs/qa.md`。

本次執行一個有完成條件的迴圈，沒有建立持續背景排程。

## 研究用例

新增 LaTeX 國科會計畫書與 PDF 輸出、GRB 歷年公開成果報告蒐集、PDF 證據分析、Semantic Scholar API 論文檢索。範例為操作說明，本次未實際蒐集報告、呼叫文獻搜尋 API 或製作申請文件。
