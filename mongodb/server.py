from flask import Flask
from flask import render_template
from flask import request
import pymongo
 
client = pymongo.MongoClient('mongodb://127.0.0.1:27017/')
db =client.test # database test
#db = client['test]
collection = db.register
#collection = db['register']

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/s')

def log():
    return render_template('tianxie.html')
@app.route('/m')
def cg():
    name = request.args.get("name")
    gender = request.args.get("gender")
    phone = request.args.get("Phone")
    department = request.args.get("Dept.")
    register = {'姓名':name, '性别':gender,'手机':phone, '部门':department}
    result = collection.insert_one(register)
    print(register)
    return render_template('fanhui.html')


app.run()