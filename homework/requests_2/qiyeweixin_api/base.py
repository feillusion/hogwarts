import requests


class Base:

    #获取对应类的access_token
    def get_token(self,corpid:str,contact_secret:str):
        self.token = requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={contact_secret}").json()['access_token']
        self.s = requests.Session()
        self.s.params = {'access_token':self.token}
        return self

    #根据参数调用api
    def send(self,*args,**kwargs):
        return  self.s.request(*args,**kwargs).json()