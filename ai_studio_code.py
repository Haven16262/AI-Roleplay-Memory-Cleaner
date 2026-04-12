import json
import os
import re
import sys
from pathlib import Path

# ================= 配置区域（请在这里修改） =================
INPUT_FILE = r"input_chat_history.json"   # 支持 .json 或 .txt 文件
OUTPUT_FILE = r"compressed_memory.txt"    # 输出文件

# 自定义角色名称映射
USER_NAME = ""      # 你的名字
MODEL_NAME = ""     # AI 的名字
# ===========================================================

def is_json_file(file_path):
    return str(file_path).lower().endswith('.json')

def load_chat_data(file_path):
    """根据文件类型加载数据"""
    path = Path(file_path)
    if not path.exists():
        print(f"❌ 错误：找不到输入文件 {file_path}")
        print("   请将你的聊天记录文件放到项目目录，并修改 INPUT_FILE 配置")
        sys.exit(1)

    try:
        if is_json_file(path):
            with open(path, 'r', encoding='utf-8') as f:
                return json.load(f)
        else:
            # TXT 文件直接按行读取
            with open(path, 'r', encoding='utf-8') as f:
                lines = f.readlines()
            return lines
    except Exception as e:
        print(f"❌ 读取文件失败：{e}")
        sys.exit(1)

def find_all_messages(data, collected_list):
    """递归查找 JSON 中的所有消息"""
    if isinstance(data, dict):
        if 'role' in data:
            collected_list.append(data)
        for key, value in data.items():
            find_all_messages(value, collected_list)
    elif isinstance(data, list):
        for item in data:
            find_all_messages(item, collected_list)

def clean_chat_history():
    print("🧠 AI-Roleplay-Memory-Cleaner 启动...\n")

    data = load_chat_data(INPUT_FILE)

    print(f"✅ 成功读取输入文件: {INPUT_FILE}")

    with open(OUTPUT_FILE, 'w', encoding='utf-8') as out:
        if is_json_file(INPUT_FILE):
            # 处理 JSON 文件
            all_messages = []
            find_all_messages(data, all_messages)
            print(f"   找到 {len(all_messages)} 条消息，开始压缩...")

            for entry in all_messages:
                role = entry.get('role', 'unknown')
                parts = entry.get('parts', [])

                final_text = ""

                if not parts and 'text' in entry:
                    final_text = entry['text']
                elif parts:
                    if isinstance(parts, str):
                        final_text = parts
                    elif isinstance(parts, list):
                        for part in parts:
                            if isinstance(part, dict) and (part.get('thought') is True or part.get('isThought') is True):
                                continue
                            text_chunk = part.get('text', '') if isinstance(part, dict) else str(part)
                            if text_chunk:
                                final_text += text_chunk

                if final_text and final_text.strip():
                    name = USER_NAME if role == "user" else MODEL_NAME if role == "model" else role
                    clean_content = final_text.strip()
                    clean_content = re.sub(r'\n+', '\n', clean_content)
                    out.write(f"{name}: {clean_content}\n\n")

        else:
            # 处理 TXT 文件（直接去重空行并输出）
            print("   检测到 TXT 输入，直接进行换行压缩...")
            prev_line = ""
            for line in data:
                line = line.strip()
                if line and line != prev_line:   # 去重连续相同行
                    out.write(line + "\n\n")
                    prev_line = line

    output_size = os.path.getsize(OUTPUT_FILE) / 1024
    print(f"🎉 压缩完成！")
    print(f"   输出文件：{OUTPUT_FILE}")
    print(f"   文件大小：{output_size:.1f} KB")
    print(f"   已为你节省大量上下文 Token，享受纯净记忆吧！✨")

if __name__ == "__main__":
    clean_chat_history()
