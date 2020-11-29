# encoding=utf-8
from stock.util import find_project_root
import logging

def test_current_project_dir():
    logging.info("==========current project  dir=============")
    path=find_project_root()
    assert len(path) != 0