from flask import Flask
from flask import render_template
from flask import request
import csv

with open("签到表单.csv", 'a',newline='') as f:
    csvwriter= csv.writer(f,dialect='excel')
    csvwriter.writerow(['名字','性别', '电话', '部门'])
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
    print(name, gender, phone, department)
    with open("签到表单.csv", 'a', newline='') as f:
        csvwriter= csv.writer(f,dialect='excel')
        csvwriter.writerow([name, gender, phone, department])
    return render_template('fanhui.html')

app.run()