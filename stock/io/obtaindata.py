# encoding=utf-8
import baostock as bs
import pandas as pd
import logging
import datetime

class BaoData():
    @classmethod
    def get_dailiy_info(cls,stock:str,start_date,end_date):
        """获取每日收盘数据"""


        # 登陆系统
        lg = bs.login()
        # 显示登陆返回信息
        logging.info('login respond  error_msg:' + lg.error_msg)

        rs = bs.query_history_k_data_plus(stock,
                                          "date,code,open,high,low,close,preclose,volume,amount,adjustflag,turn,tradestatus,pctChg,isST",
                                          start_date=start_date, end_date='end_date',
                                          frequency="d", adjustflag="3")

        # 登出系统
        bs.logout()

        return  rs


