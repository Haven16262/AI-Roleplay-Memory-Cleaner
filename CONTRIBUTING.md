# 如何贡献 / Contributing to AI-Roleplay-Memory-Cleaner

感谢你对 **AI-Roleplay-Memory-Cleaner** 的兴趣！🎉  
这个轻量级工具旨在帮助大家更高效地管理与大语言模型的长期角色扮演记忆，欢迎任何形式的贡献。

## 📋 可以贡献的内容
- 修复 Bug 或优化压缩逻辑
- 新增功能（例如：批量处理文件夹内所有 JSON 文件、按日期分割记忆、支持更多模型的导出格式等）
- 改进输出格式（让 TXT 更易读或进一步节省 Token）
- 优化 README 文档、添加更多语言版本
- 提交使用中的问题和改进建议

## 🚀 本地开发与测试流程

1. Fork 本仓库并克隆到本地
   ~~~bash
   git clone https://github.com/Haven16262/AI-Roleplay-Memory-Cleaner.git
   cd AI-Roleplay-Memory-Cleaner
   ~~~

2. （可选）创建虚拟环境
   ~~~bash
   python -m venv venv
   # Windows:
   venv\Scripts\activate
   # macOS/Linux:
   source venv/bin/activate
   ~~~

3. 运行测试
   ~~~bash
   python clean_memory.py
   ~~~

4. 测试建议场景：
   - 包含 `thought` / `isThought` 的 Gemini/Claude/ChatGPT 导出记录
   - 中英文混合的长对话
   - 超大 JSON 文件（几万行以上）

## 📝 提交 Pull Request 流程

1. 创建功能分支（请使用有意义的名称）
   ~~~bash
   git checkout -b feature/batch-processing-support
   ~~~

2. 进行修改并提交
   - 保持配置区域清晰易懂
   - 添加必要的中文注释
   - 如果修改了功能，请同步更新 `README.md` 和 `CHANGELOG.md`

3. 推送并创建 Pull Request
   - 清晰描述修改内容和理由
   - 最好附上压缩前后的文件大小 / Token 节省对比

## 🛠️ 代码风格建议
- 使用 Python 3.8+
- 配置区域保持简单直观，用户修改时无需阅读核心代码
- 优先考虑兼容不同大模型的导出 JSON 格式
- 输出 TXT 文件在保证极致压缩的同时，尽量保持可读性

## ❓ 提问与 Issue
如果你在使用中遇到问题，请在 Issue 中提供以下信息：
- 使用的是哪个模型导出的 JSON（Gemini / Claude / ChatGPT 等）
- 输入 JSON 文件大致大小
- 遇到的具体现象或错误信息
- （可选）压缩前后的示例片段

---

**再次感谢每一位贡献者！**  
你的每一次改进，都能帮助更多角色扮演爱好者获得更干净、高效的记忆管理体验。

Happy Cleaning! 🧠✨  

—— Haven (Jinan University - AI Major)
