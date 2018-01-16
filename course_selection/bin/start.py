# 程序启动文件
import sys, os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from src import core

if __name__ == '__main__':
    core.func()