import json
import os
import re

# ================= 配置区域 / Configuration Area (Users please modify here) =================
INPUT_FILE = r"input_chat_history.json"  # 大模型导出聊天记录路径 / Path to the exported LLM chat log
OUTPUT_FILE = r"compressed_memory.txt"   # 压缩后的输出文件路径 / Path for the compressed output file

# 自定义角色名称映射 / Custom role name mapping (Change to your and your AI partner's names)
USER_NAME = "User"    # 用户的名字 / User's name
MODEL_NAME = "AI"     # AI 的名字 / AI's name
# =========================================================================================

# 递归搜刮器 / Recursive scraper
def find_all_messages(data, collected_list):
    if isinstance(data, dict):
        if 'role' in data:
            collected_list.append(data)
        for key, value in data.items():
            find_all_messages(value, collected_list)
    elif isinstance(data, list):
        for item in data:
            find_all_messages(item, collected_list)

def clean_chat_history():
    print(f"🔍 正在读取 / Reading: {INPUT_FILE}")
    
    try:
        with open(INPUT_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
            
        all_messages =[]
        find_all_messages(data, all_messages)
        
        print(f"✅ 找到 {len(all_messages)} 条记录，启动【核能压缩】模式... / Found {len(all_messages)} records, starting [Nuclear Compression] mode...")
        
        with open(OUTPUT_FILE, 'w', encoding='utf-8') as out:
            for entry in all_messages:
                role = entry.get('role', 'unknown')
                parts = entry.get('parts',[])
                final_text = ""
                
                # --- 提取逻辑 / Extraction logic ---
                if not parts and 'text' in entry:
                    final_text = entry['text']
                
                if parts:
                    if isinstance(parts, str):
                        final_text = parts
                    elif isinstance(parts, list):
                        for part in parts:
                            is_thought = False
                            if isinstance(part, dict):
                                is_thought = part.get('thought') is True or part.get('isThought') is True
                            
                            if is_thought: continue
                            
                            text_chunk = ""
                            if isinstance(part, str): text_chunk = part
                            elif isinstance(part, dict): text_chunk = part.get('text', '')
                            
                            if text_chunk:
                                final_text += text_chunk
                
                # --- 核心修改：使用自定义变量 / Core modification: Using custom variables ---
                if final_text and final_text.strip():
                    if role == "user": name = USER_NAME
                    elif role == "model": name = MODEL_NAME
                    else: name = role
                    
                    # 1. 去掉首尾空白 / Remove leading and trailing whitespace
                    clean_content = final_text.strip()
                    
                    # 2. 去掉内部多余的空行 / Remove extra blank lines internally
                    clean_content = re.sub(r'\n+', '\n', clean_content)
                    
                    # 3. 写入：紧凑排列 / Write: Compact layout
                    out.write(f"{name}: {clean_content}\n")

        print(f"🎉 压缩完毕！现在的密度堪比中子星！ / Compression complete! The density is now comparable to a neutron star!")
        print(f"文件已生成 / File generated: {OUTPUT_FILE}")
        
    except Exception as e:
        print(f"❌ 错误 / Error: {e}")

if __name__ == "__main__":
    clean_chat_history()
