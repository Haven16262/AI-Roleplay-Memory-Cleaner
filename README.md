# AI-Roleplay-Memory-Cleaner 🧠✨
![License](https://img.shields.io/badge/License-MIT-yellow.svg)
![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![No Dependencies](https://img.shields.io/badge/Dependencies-None-success.svg)

[中文](#中文) |[English](#english)

---

<h2 id="中文">🇨🇳 中文说明</h2>

**一个将 LLM 导出记录压缩为高密度 txt 的轻量级脚本。**


在与大语言模型（如 Gemini, Claude, ChatGPT）进行长期角色扮演或深度对话时，导出的 JSON 记录往往极其庞大，包含大量冗余数据（如模型思考过程、系统提示词、多余的空行等）。这会导致在重新“喂”给模型恢复记忆时，白白消耗数十万 Token 额度。
本项目旨在将臃肿的 JSON 聊天记录，极致压缩为纯净、高密度的 TXT 文本，最大化节省您的上下文窗口（Context Window）！

### ✨ 核心功能
- **自动过滤思考过程**：智能剔除模型生成时的 `thought` 或 `isThought` 思维链，只保留最终对话。
- **极致换行压缩**：将连续的多个空行 `\n\n\n` 压缩为单个换行 `\n`，消除文本间隙。
- **自定义角色映射**：支持将原有的 `user` 和 `model` 标签映射为您和您的 AI 伴侣的专属名字。
- **本地安全化**：纯本地运行，不依赖任何第三方库，绝对保护您的私密对话记忆。

### 🚀 快速开始
1. 把你的聊天记录导出为 JSON 文件（例如 `input_chat_history.json`）
2. 下载本仓库中的 `ai_studio_code.py` 文件
3. 用文本编辑器打开脚本，修改顶部的**配置区域**：
```python
INPUT_FILE = r"input_chat_history.json"      # 你的导出文件路径
OUTPUT_FILE = r"compressed_memory.txt"       # 压缩后保存路径
USER_NAME = ""                             # 你的名字
MODEL_NAME = ""                            # AI 的名字
```
4. 运行脚本：
```bash
python ai_studio_code.py
```
5.完成后会在同目录生成 compressed_memory.txt，即可直接用于恢复记忆！

### 📋 注意事项

- 脚本会自动跳过模型的思考过程（thought / isThought）
- 支持中文和英文对话
- 输出文件采用紧凑格式，极大节省 Token
- 如需修改角色名，只需改配置区域即可，无需改代码

### 📚 项目文件

- ai_studio_code.py —— 主压缩脚本
- LICENSE —— MIT 协议
- README.md —— 本说明文件

### 📚 更多文档
- [详细使用指南](docs/使用指南.md)

<h2 id="english">🇬🇧 English README</h2>

**A lightweight script that compresses exported LLM chat logs into high-density txt files.**

When doing long-term roleplay or deep conversations with LLMs (Gemini, Claude, ChatGPT, etc.), exported JSON logs are often extremely bloated with redundant data (thinking processes, system prompts, extra blank lines). This wastes hundreds of thousands of tokens when restoring memory.
This lightweight tool compresses bloated JSON chat logs into pure, high-density TXT, maximizing your Context Window!

### ✨ Key Features
- Filter Thinking Processes: Automatically removes thought or isThought chains
- Extreme Newline Compression: Turns multiple \n\n\n into single \n
- Custom Role Mapping: Map user/model to your and your AI companion’s names
- Local & Secure: Runs completely offline with zero dependencies

### 🚀 Quick Start
1.Export your chat history as JSON  
2.Download ai_studio_code.py from this repository  
3.Open the script and edit the Configuration Area at the top:  

```Python
INPUT_FILE = r"input_chat_history.json"
OUTPUT_FILE = r"compressed_memory.txt"
USER_NAME = "Your Name"
MODEL_NAME = "AI's Name"
```
4.Run:
```bash
Bashpython ai_studio_code.py
```
5.The compressed compressed_memory.txt will be generated in the same folder.

### 📋 Notes

- The script automatically skips model thinking processes 
- Works with both Chinese and English conversations
- Output is highly compact to save tokens

### 📚 More documents
- [Detailed User Guide](docs/使用指南.md)


Author: Haven (Jinan University - AI Major)  
License: MIT
