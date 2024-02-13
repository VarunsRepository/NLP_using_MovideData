from msilib.schema import File
from os import system
from flask import Flask, render_template 

# to start the app
# Activate the enviroment : .\MovieApp\Scripts\activate
# Type in the command     : MovieApp.py 

with open(r'C:\Users\Varun\OneDrive\NLP_using_MovideData-main\Test data\Movie_Names_Only.txt', 'r') as f:
    lines = f.readlines()    
Names_array = lines


app = Flask(__name__)


@app.route('/')
def Start_Animation():
    return render_template("Start_Animation.html", content=Names_array)


if __name__ == "__main__":
    app.run(debug = True)


