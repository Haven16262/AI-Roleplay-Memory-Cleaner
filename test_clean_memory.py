import json
import os
import tempfile
import unittest

import clean_memory


class TestFindAllMessages(unittest.TestCase):
    """测试递归消息搜刮函数"""

    def test_simple_list_of_messages(self):
        data = [
            {"role": "user", "parts": [{"text": "Hello"}]},
            {"role": "model", "parts": [{"text": "Hi there"}]},
        ]
        result = []
        clean_memory.find_all_messages(data, result)
        self.assertEqual(len(result), 2)

    def test_nested_dict_with_role(self):
        data = {"role": "user", "parts": [{"text": "Nested"}]}
        result = []
        clean_memory.find_all_messages(data, result)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["role"], "user")

    def test_deeply_nested_structure(self):
        data = {
            "history": {
                "conversations": [
                    {"role": "user", "parts": [{"text": "Q1"}]},
                    {"role": "model", "parts": [{"text": "A1"}]},
                ]
            }
        }
        result = []
        clean_memory.find_all_messages(data, result)
        self.assertEqual(len(result), 2)

    def test_empty_structure(self):
        result = []
        clean_memory.find_all_messages({}, result)
        self.assertEqual(len(result), 0)

    def test_dict_without_role(self):
        data = {"metadata": {"version": "1.0"}, "messages": []}
        result = []
        clean_memory.find_all_messages(data, result)
        self.assertEqual(len(result), 0)


class TestFullPipeline(unittest.TestCase):
    """集成测试：完整压缩流程"""

    def setUp(self):
        self.tmp_dir = tempfile.mkdtemp()
        self.original_input = clean_memory.INPUT_FILE
        self.original_output = clean_memory.OUTPUT_FILE
        self.original_user = clean_memory.USER_NAME
        self.original_model = clean_memory.MODEL_NAME

    def tearDown(self):
        clean_memory.INPUT_FILE = self.original_input
        clean_memory.OUTPUT_FILE = self.original_output
        clean_memory.USER_NAME = self.original_user
        clean_memory.MODEL_NAME = self.original_model

    def test_basic_conversation(self):
        input_path = os.path.join(self.tmp_dir, "test_input.json")
        output_path = os.path.join(self.tmp_dir, "test_output.txt")

        data = [
            {"role": "user", "parts": [{"text": "Hello, how are you?"}]},
            {"role": "model", "parts": [{"text": "I'm doing great!"}]},
        ]
        with open(input_path, "w", encoding="utf-8") as f:
            json.dump(data, f)

        clean_memory.INPUT_FILE = input_path
        clean_memory.OUTPUT_FILE = output_path
        clean_memory.USER_NAME = "Player"
        clean_memory.MODEL_NAME = "Assistant"

        clean_memory.clean_chat_history()

        self.assertTrue(os.path.exists(output_path))
        with open(output_path, "r", encoding="utf-8") as f:
            content = f.read()

        self.assertIn("Player: Hello, how are you?", content)
        self.assertIn("Assistant: I'm doing great!", content)

    def test_thought_filtering(self):
        input_path = os.path.join(self.tmp_dir, "test_thought.json")
        output_path = os.path.join(self.tmp_dir, "test_thought_out.txt")

        data = [
            {
                "role": "model",
                "parts": [
                    {"text": "Let me think...", "thought": True},
                    {"text": "Here is my answer."},
                ],
            }
        ]
        with open(input_path, "w", encoding="utf-8") as f:
            json.dump(data, f)

        clean_memory.INPUT_FILE = input_path
        clean_memory.OUTPUT_FILE = output_path

        clean_memory.clean_chat_history()

        with open(output_path, "r", encoding="utf-8") as f:
            content = f.read()

        self.assertNotIn("Let me think", content)
        self.assertIn("Here is my answer.", content)

    def test_is_thought_filtering(self):
        input_path = os.path.join(self.tmp_dir, "test_is_thought.json")
        output_path = os.path.join(self.tmp_dir, "test_is_thought_out.txt")

        data = [
            {
                "role": "model",
                "parts": [
                    {"text": "Internal reasoning", "isThought": True},
                    {"text": "Public response."},
                ],
            }
        ]
        with open(input_path, "w", encoding="utf-8") as f:
            json.dump(data, f)

        clean_memory.INPUT_FILE = input_path
        clean_memory.OUTPUT_FILE = output_path

        clean_memory.clean_chat_history()

        with open(output_path, "r", encoding="utf-8") as f:
            content = f.read()

        self.assertNotIn("Internal reasoning", content)
        self.assertIn("Public response.", content)

    def test_blank_line_compression(self):
        input_path = os.path.join(self.tmp_dir, "test_blanks.json")
        output_path = os.path.join(self.tmp_dir, "test_blanks_out.txt")

        data = [
            {"role": "user", "parts": [{"text": "Line one\n\n\n\nLine two"}]},
        ]
        with open(input_path, "w", encoding="utf-8") as f:
            json.dump(data, f)

        clean_memory.INPUT_FILE = input_path
        clean_memory.OUTPUT_FILE = output_path

        clean_memory.clean_chat_history()

        with open(output_path, "r", encoding="utf-8") as f:
            content = f.read()

        self.assertNotIn("\n\n", content)

    def test_non_role_entries_keep_original_name(self):
        input_path = os.path.join(self.tmp_dir, "test_system.json")
        output_path = os.path.join(self.tmp_dir, "test_system_out.txt")

        data = [
            {"role": "system", "parts": [{"text": "Session started."}]},
        ]
        with open(input_path, "w", encoding="utf-8") as f:
            json.dump(data, f)

        clean_memory.INPUT_FILE = input_path
        clean_memory.OUTPUT_FILE = output_path

        clean_memory.clean_chat_history()

        with open(output_path, "r", encoding="utf-8") as f:
            content = f.read()

        self.assertIn("system: Session started.", content)


if __name__ == "__main__":
    unittest.main()
