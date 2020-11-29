# encoding=utf-8
from  stock.io.all_stock import  get_all_stockcode_in_china


def test_get_all_stockcode_in_china():
    stocks=get_all_stockcode_in_china()
    assert len(stocks) != 0