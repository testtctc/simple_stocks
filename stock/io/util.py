# encoding=utf-8
import os
from stock.util import find_project_root
import re
import  pandas as pd
import logging


class CodeConvert():
    #"所有的股票代码"
    data=None
    codepattern = re.compile(r"(\w{2,2}\.?)?(\d{6.6})")
    def __init__(self,code):

        if not self.data:
            self.data=self.load_data()
        self.code=self.codepattern.search(code).group(3)

    @classmethod
    def load_data(cls):
        project_root= find_project_root()
        path = os.path.join(project_root,"data","codes.csv")
        cls.data = pd.read_csv(path)
        logging.info(cls.data.columns)

    @classmethod
    def refresh_data(cls):
        """刷新股票数据"""
        cls.data=None
        cls.data=cls.load_data()

    def to_dot_code(self):
        row = self.data[self.data["raw_code"]==self.code].first()
        return  row["market"]  + "." + self.code


class DateConvert():
    """日志转换器"""
    pattern= ""