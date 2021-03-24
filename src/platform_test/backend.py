import json

from flask import Flask, request
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)


app.config['SQLALCHEMY_DATABASE_URI'] = r'sqlite:///F:\projects\hogwarts\src\platform_test\benkend.db'
db = SQLAlchemy(app)


class TestCase(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    steps = db.Column(db.String(1000), unique=False, nullable=True)
    expect = db.Column(db.String(200), unique=False, nullable=True)

    def __repr__(self):
        return '<Testcase %r>' % self.name

class TestCaseService(Resource):
    def get(self):
        return 'chaxueyongli'

    def post(self):
        testcase = TestCase(
            id=request.json.get("id"),
            name=request.json.get('name'),
            steps=json.dumps(request.json.get("steps")),
            expect=json.dumps(request.json.get("expect"))
        )

        db.session.add(testcase)
        db.session.commit()

        testcases = TestCase.query.all()
        return [str(testcase) for testcase in testcases]


    def put(self):
        return 'xiugaiyongli'
    def delete(self):
        return 'shanchuyongli'

api.add_resource(TestCaseService, '/testcase')

if __name__ == '__main__':
    app.run(debug=True)