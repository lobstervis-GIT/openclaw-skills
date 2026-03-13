import sys
import os

repo = 'lobstervis-GIT/bakery-seat-system'

def push_file(path, content, message):
    try:
        print(f'嘗試推送檔案: {path}')
        result = default_api.github_push_file(repo=repo, path=path, content=content, message=message)
        print(f'推送成功: {path}')
        print(result)
    except Exception as e:
        print(f'推送失敗: {path}')
        print(e)


if __name__ == '__main__':
    filename = sys.argv[1]
    filepath = os.path.join('./', filename)
    try:
        with open(filepath, 'r') as f:
            content = f.read()
        print(f'成功讀取檔案: {filename}')
        if filename == 'README.md':
            push_file(filename, content, '專案概述、技術架構(Cloudflare Workers+D1)、座位模型、API規劃')
        elif filename == 'src/domain/types.ts':
            push_file(filename, content, '核心型別定義(Seat, Stay, StaySeat, TakeoutOrder, BufferRule)')
        elif filename == 'src/domain/overlap.ts':
            push_file(filename, content, '時間重疊判定邏輯')
        elif filename == 'src/domain/segment-finder.ts':
            push_file(filename, content, '連續座位區段搜尋演算法')
        elif filename == 'wrangler.toml':
            push_file(filename, content, 'Cloudflare Workers 基本配置')
        else:
            print(f'不支援的檔案類型: {filename}')
    except FileNotFoundError:
        print(f'找不到檔案: {filename}')
    except Exception as e:
        print(f'讀取檔案失敗: {filename}')
        print(e)