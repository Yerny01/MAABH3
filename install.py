#!/usr/bin/env python3
import sys

def main():
    version = sys.argv[1] if len(sys.argv) > 1 else "v0.0.0"
    print(f"[install.py] 当前版本号：{version}")
    print("[install.py] 已存在 install 目录，跳过构建步骤")

if __name__ == "__main__":
    main()
