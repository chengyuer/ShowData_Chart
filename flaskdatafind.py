import os

from flask import Flask, render_template
from DealData import *
app = Flask(__name__)

@app.route('/diaplay/')
def hello_world():
    return render_template("5.html")


# @app.route('/<name>') #get
# def get_data(name):
    # return str(csdn.search2(name))

# @app.route('/DataDisplay/')
# def home():
#     data = GetData()
#     data.create_charts().render(r"F:/flaskprogramm/templates/3.html")
#     if os.path.exists(r"F:/flaskprogramm/templates/3.html"):
#        return render_template("3.html")#homepage.html在templates文件夹下



if __name__ == '__main__':
    app.run()
