

import yaml

#查询元素处理黑名单
def find_blacklist(fun):
    def run(*args,**kwargs):
        #执行查询操作
        try:
            #查询到就返回元素
            return fun(*args,**kwargs)
        #异常（未查询到）就进行黑名单处理
        except Exception as e:
            instance = args[0]
            #获取黑名单
            with open('../find_blacklist.yaml','r',encoding='utf-8') as f:
                datas = yaml.safe_load(f)
                black_list = datas['xueqiu']
            #遍历黑名单
            for black in black_list:
                #查找黑名单元素
                ele = instance.driver.find_elements(*black)
                #如果找到黑名单元素，就点击处理
                if len(ele)>0:
                    ele[0].click()
                    #处理后再次查找元素
                    return fun(*args,**kwargs)
            #没有找到黑名单，就抛出异常
            raise e
    return run