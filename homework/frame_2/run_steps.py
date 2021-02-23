import yaml


def run_steps(fun):
    def run(*args,**kwargs):
        #获取实例
        instance = args[0]
        #获取page_path(步骤驱动文件路径)
        page_path = fun(*args)
        #获取method(执行哪个方法)
        method = fun(*args,page_path=page_path)
        #获取所有数据
        with open(page_path,'r',encoding='utf-8') as f:
            datas = yaml.safe_load(f)
        #提取对应方法的步骤
        steps = datas[method]
        #逐个执行步骤
        for step in steps:
            #动作类型
            action = step['action']
            #使用参数补全参数化的locator地址
            while '${}' in step['locator'][1]:
                step['locator'][1]= step['locator'][1].replace('${}',args[step['locator_replace'][0]])
                del step['locator_replace'][0]
            #如果是点击操作就执行click方法
            if action == 'click':
                instance.click(step['locator'])
            #如果是输入操作就执行sendkeys方法
            if action == 'sendkeys':
                #根据step['keys']中的数字获取对应索引的args参数，作为输入内容(参数化)
                keys = args[step['keys'][0]]
                instance.sendkeys(step['locator'],keys)
            #如果是获取多个元素的文本内容就执行gettexts方法，并返回结果列表
            if action == 'gettexts':
                return instance.gettexts(step['locator'])
        #返回其他页面实例
        return fun(*args,page_path=page_path,method=method)
    return run
