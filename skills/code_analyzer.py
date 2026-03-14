import sys
import os
import subprocess

def analyze_code(repo_name):
    try:
        # 1. 檢查 repo 是否存在
        if not os.path.exists(repo_name):
            print(f"倉庫 {repo_name} 不存在。")
            return "倉庫不存在"

        # 2. 使用 pylint 進行程式碼分析 (假設程式碼是 Python)
        command = f"pylint {repo_name}"
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()

        # 3. 提取解耦合相關的訊息 (這部分需要根據 pylint 的輸出格式調整)
        analysis_result = stdout.decode("utf-8")
        decoupling_issues = []
        for line in analysis_result.splitlines():
            if "耦合" in line or "dependency" in line.lower():
                decoupling_issues.append(line)

        # 4. 如果沒有發現問題，返回提示
        if not decoupling_issues:
            return "未發現明顯的解耦合問題。"

        # 5. 返回分析結果
        return "\n".join(decoupling_issues)

    except Exception as e:
        return f"分析出錯: {e}"

if __name__ == "__main__":
    repo_name = sys.argv[1] if len(sys.argv) > 1 else ""
    result = analyze_code(repo_name)
    print(result)