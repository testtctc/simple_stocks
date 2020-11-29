# encoding=utf-8
import os


def find_project_root():
    """项目的绝对路"""
    return os.path.dirname(os.path.dirname(__file__))