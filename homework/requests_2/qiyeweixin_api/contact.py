from homework.requests_2.qiyeweixin_api.base import Base


class Contact(Base):

    #调用Contact类下方法是执行
    def token(self):
        corpid = 'ww51bb78344d7cccdf'
        contact_secret = '_9UzNkQk_8WxwWGkK-eSKo4xz1m8xwKAkx8rniYURH8'
        #获取通讯录的access_token并放入session中
        return self.get_token(corpid,contact_secret)

    #创建成员
    def create_member(self,data):
        return self.send('post',f'https://qyapi.weixin.qq.com/cgi-bin/user/create',json=data)

    #更新成员
    def update_member(self,data):
        return self.send('post',f'https://qyapi.weixin.qq.com/cgi-bin/user/update',json=data)

    #获取成员信息
    def get_member(self,userid):
        return self.send('get',f'https://qyapi.weixin.qq.com/cgi-bin/user/get?userid={userid}')

    #删除成员
    def delete_member(self,userid):
        return self.send('get',f'https://qyapi.weixin.qq.com/cgi-bin/user/delete?userid={userid}')