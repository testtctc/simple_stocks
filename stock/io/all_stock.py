#encoding=utf-8
from lxml import  etree
import requests
import logging
import pandas as pd
from stock.util import find_project_root
import os

def get_all_stockcode_in_china():
    """
    获取所有股票代码
    """
    result=[]
    import re
    pattern = re.compile(r"\w{2,2}\d{6,6}")
    """获取所有股票代码"""
    url="https://hq.gucheng.com/gpdmylb.html"
    try:
        res = requests.get(url)
    except Exception as e:
        logging.info(e)
        return  result
    content=res.content.decode("utf-8")
    tree =etree.HTML(content)
    stockurls = tree.xpath("//section[@class='stockTable']//a")
    for u in stockurls:
        try:
            company_name = u.xpath("./text()")[0].split("(")[0].replace(" ", "")
            url=u.attrib["href"]
            code=pattern.search(url).group(0)
            result.append((code,company_name,url))
        except Exception as e:
            logging.info(e)

    if len(result) !=0:
        #将数据写入到磁盘
        data=pd.DataFrame(result,columns=["code","company_name","url"])
        data["raw_code"]=data["code"].map(lambda x: x[2:])
        data["market"]=data["code"].map(lambda x: x[:2])
        project_root= find_project_root()
        path=os.path.join(project_root,"data","codes.csv")
        data.to_csv(path)
    return result