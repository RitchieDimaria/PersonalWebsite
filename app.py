from flask import Flask, render_template,request,jsonify
from solve import *
app = Flask(__name__)

grid =[[0,4,0, 7,0,1, 0,0,0],
       [8,0,7, 0,4,0, 6,0,0],
       [0,5,0, 0,0,9, 0,0,0],

       [0,0,2, 0,0,0, 8,0,0],
       [0,8,0, 5,7,2, 0,6,0],
       [0,0,5, 0,0,0, 1,0,0],

       [0,0,0, 8,0,0, 0,5,0],
       [0,0,1, 0,6,0, 4,0,9],
       [0,0,0, 9,0,3, 0,7,0],
]
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/aboutme')
def about_me():
    return render_template('aboutme.html')

@app.route('/solve',methods=['POST'])
def solveTable():
    data = request.get_json()
    table = data['table']
    solvedTables,moreSolutions = findAllTables(table)
    return jsonify(
        {"Tables":solvedTables,
         "more":moreSolutions
                    })

if __name__ == "__main__":
    app.run(debug=True)