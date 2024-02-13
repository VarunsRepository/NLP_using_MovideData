from msilib.schema import File
from os import system
from flask import Flask, render_template 
import pandas as pd


# to start the app
# Activate the enviroment : .\MovieApp\Scripts\activate
# Type in the command     : MovieApp.py 

with open(r'C:\Users\Varun\OneDrive\NLP_using_MovideData-main\Test data\Movie_Names_Only.txt', 'r') as f:
    lines = f.readlines()    
Names_array = lines

Data = pd.read_csv(r"C:\Users\Varun\OneDrive\NLP_using_MovideData-main\Test data\extracted_movies_2021.csv")
Data_values = Data.values

#JSON_object = Data.to_json


#contentTobeSent = Names_array
contentTobeSent = Data_values

app = Flask(__name__)


@app.route('/')
def Start_Animation():
    return render_template("Start_Animation.html", content=contentTobeSent, pageheader="IMDb's Top 100 for 2021")

@app.route('/<username>')
def profile(username):
    URL_to_Go = "Start_Animation." + username +  ".html"
    return render_template(URL_to_Go, content=contentTobeSent)
 


if __name__ == "__main__":
    app.run(debug = True)


