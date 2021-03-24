import json

from flask import Flask, request
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)

#本地不装mysql了，用sqlite凑合一下。。
app.config['SQLALCHEMY_DATABASE_URI'] = r'sqlite:///F:\projects\hogwarts\homework\backend\backend.db'
db = SQLAlchemy(app)

#测试用例表
class TestCase(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    steps = db.Column(db.String(1000), unique=False, nullable=True)
    expect = db.Column(db.String(200), unique=False, nullable=True)
    def __repr__(self):
        data = {'id':self.id,'name':self.name,'steps':self.steps,'expect':self.expect}
        return str(data)

#测试任务表
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    casesid = db.Column(db.String(1000), unique=False, nullable=False)
    description = db.Column(db.String(1000), unique=False, nullable=True)
    def __repr__(self):
        data = {'id':self.id,'name':self.name,'caseid':self.casesid,'description':self.description}
        return str(data)

#测试用例操作
class TestCaseService(Resource):
    #根据名称查询测试用例
    def get(self):
        name = request.args.get('name',None)
        if name:
            testcases = TestCase.query.filter_by(name=name).all()
        else:
            testcases = TestCase.query.all()

        datas = []
        for testcase in testcases:
            datas.append(eval(str(testcase)))
        res = {
            'msg' : 'success',
            'datas' : datas
        }
        return res

    #新增测试用例
    def post(self):
        testcase = TestCase(
            id=request.json.get("id"),
            name=request.json.get('name'),
            steps=json.dumps(request.json.get("steps")),
            expect=request.json.get("expect")
        )
        res = {}
        if testcase.name == '':
            res['msg'] = '用例名称不能为空'
        else:
            db.session.add(testcase)
            db.session.commit()
            res['msg'] = '添加成功'
        testcases = TestCase.query.all()
        datas = []
        for testcase in testcases:
            datas.append(eval(str(testcase)))
        res['datas']= datas
        return res

    #根据id更新测试用例
    def put(self):
        testcase = TestCase(
            id=request.json.get("id"),
            name=request.json.get('name'),
            steps=json.dumps(request.json.get("steps")),
            expect=request.json.get("expect")
        )
        case = TestCase.query.filter_by(id=testcase.id).first()
        res = {}
        if case:
            if case.name == '':
                res['msg'] = '用例名称不能为空'
            else:
                case.name = testcase.name
                case.steps = testcase.steps
                case.expect = testcase.expect
                db.session.commit()
                res['msg'] = '更新成功'
        else:
            res['msg'] = 'Id不存在'
        testcases = TestCase.query.all()
        datas = []
        for testcase in testcases:
            datas.append(eval(str(testcase)))
        res['datas']= datas
        return res

    #更加id删除测试用例
    def delete(self):
        id = request.json['id']
        testcase = TestCase.query.filter_by(id=id).first()
        res = {}
        if testcase:
            db.session.delete(testcase)
            db.session.commit()
            res['msg'] = '删除成功'
        else:
            res['msg']= 'Id不存在'
        testcases = TestCase.query.all()
        datas = []
        for testcase in testcases:
            datas.append(eval(str(testcase)))
        res['datas']= datas
        return res

#测试任务操作
class TaskService(Resource):
    def get(self):
        name = request.args.get('name', None)
        if name:
            tasks = Task.query.filter_by(name=name).all()
        else:
            tasks = Task.query.all()

        datas = []
        for task in tasks:
            datas.append(eval(str(task)))
        res = {
            'msg': 'success',
            'datas': datas
        }
        return res

    def post(self):
        task = Task(
            id=request.json.get("id"),
            name=request.json.get('name'),
            casesid=json.dumps(request.json.get("casesid")),
            description=request.json.get("description")
        )
        res = {}
        if task.name == '':
            res['msg'] = '任务名称不能为空'
        elif task.casesid == 'null':
            res['msg'] = '没有添加用例'
        else:
            db.session.add(task)
            db.session.commit()
            res['msg'] = '添加成功'
        tasks = Task.query.all()
        datas = []
        for task in tasks:
            datas.append(eval(str(task)))
        res['datas']= datas
        return res

    def put(self):
        task = Task(
            id=request.json.get("id"),
            name=request.json.get('name'),
            casesid=json.dumps(request.json.get("casesid")),
            description=request.json.get("description")
        )
        res = {}
        ta_sk = Task.query.filter_by(id=task.id).first()
        if ta_sk:
            if task.name == '':
                res['msg'] = '任务名称不能为空'
            elif task.casesid == 'null':
                res['msg'] = '没有添加用例'
            else:
                ta_sk.name = task.name
                ta_sk.casesid = task.casesid
                ta_sk.description = task.description
                db.session.commit()
                res['msg'] = '更新成功'
        else:
            res['msg'] = '任务id不存在'
        tasks = Task.query.all()
        datas = []
        for task in tasks:
            datas.append(eval(str(task)))
        res['datas']= datas
        return res

    def delete(self):
        id = request.args.get('id')
        res = {}
        task = Task.query.filter_by(id=id).first()
        if task:
            db.session.delete(task)
            db.session.commit()
            res['msg'] = '删除成功'
        else:
            res['msg'] = '任务不存在'
        tasks = Task.query.all()
        datas = []
        for task in tasks:
            datas.append(eval(str(task)))
        res['datas']= datas
        return res



api.add_resource(TestCaseService, '/testcase')
api.add_resource(TaskService, '/task')

if __name__ == '__main__':
    app.run(debug=True)