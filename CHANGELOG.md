# 更新日志 / CHANGELOG

All notable changes to this project will be documented in this file.

## [Unreleased]
### Added
- 新增 `CONTRIBUTING.md` 贡献指南
- 优化 `.gitignore`，适配轻量级 Python 脚本项目
- 将脚本重命名为 `clean_memory.py`，提升可读性
- 完善 README.md，增加徽章、清晰的快速开始步骤和中英文双语支持

### Changed
- 改进代码结构和注释，提升维护性
- 更新配置区域说明，让用户更容易自定义角色名称

### Fixed
- 修复部分 JSON 结构下提取文本不完整的问题
- 优化换行压缩逻辑，减少多余空行

## [v0.1.0] - 2026-04-12
### Added
- 初始版本发布
- 核心功能：自动过滤 `thought` / `isThought` 思维链
- 支持自定义用户和 AI 角色名称映射
- 极致换行压缩，将多余空行压缩为单个换行
- 纯本地运行，无任何第三方依赖
- 支持 Gemini、Claude、ChatGPT 等主流模型导出的 JSON 记录

### Key Features
- 输入：JSON 聊天记录
- 输出：高密度纯净 TXT 文件
- 目标：大幅节省上下文窗口 Token

---

**格式说明**：
- `[Unreleased]` 部分用于记录正在进行中的修改
- 每次发布新版本时，请将 `[Unreleased]` 中的内容移动到具体版本号下方
- 建议每次重要修改后都在 `[Unreleased]` 下添加条目

---

**Author**: Haven (Jinan University - AI Major)  
**License**: MIT
