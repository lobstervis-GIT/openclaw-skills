import sys
import datetime

today = datetime.date.today().strftime("%Y-%m-%d")
learning_content = sys.argv[1] if len(sys.argv) > 1 else "今天沒有特別的學習內容。"

print(f"{today}: {learning_content}")