from msilib.schema import File
from os import system
from flask import Flask, render_template 
import pandas as pd
from pymongo import MongoClient

# to start the app
# Activate the enviroment : .\MovieApp\Scripts\activate

# Type in the command     : MovieApp.py 

#with open(r'C:\Users\Varun\OneDrive\NLP_using_MovideData-main\Test data\Movie_Names_Only.txt', 'r') as f:
#    lines = f.readlines()    
#Names_array = lines
#contentTobeSent = Names_array


#Data = pd.read_csv(r"C:\Users\Varun\OneDrive\NLP_using_MovideData-main\Test data\extracted_movies_2021.csv")
#Data_values = Data.values
##contentTobeSent = Data_values

#JSON_object = Data.to_json

uri = "mongodb://JohnnyBravo:88J9QRtAlYZKP8VG@ac-dmpukmw-shard-00-00.a65kbvv.mongodb.net:27017,ac-dmpukmw-shard-00-01.a65kbvv.mongodb.net:27017,ac-dmpukmw-shard-00-02.a65kbvv.mongodb.net:27017/?ssl=true&replicaSet=atlas-wk529e-shard-0&authSource=admin&retryWrites=true&w=majority"

#This uri can be thought of as the connection string, it contains 3 main parts 
# 1. mongodb:// this is a required prefix to identify that this is a string in the standard connection format.
# 2. username:password@ Optional. Authentication credentials.
# 3. host[:port]The host (and optional port number) where the mongod instance (or mongos instance for a sharded cluster)
# is running. You can specify a hostname, IP address, or UNIX domain socket. Specify as many hosts as appropriate for your deployment topology: 
# 4. /defaultauthdb Optional. The authentication database to use if the connection string includes username:password@ authentication credentials 
# but the authSource option is unspecified.

#using the test sample DS of 100 movies of 2021
#client = MongoClient(uri )
#movies_Data = client["MovieData"]
#Movie_List_Page = movies_Data.MovieListPage#
#Collection_using_Pandas = movies_Data.MovieListPage  
##Collection_using_Pandas = movies_Data.Collection_using_Pandas  #
##contentTobeSent = [x for x in Collection_using_Pandas.find({})]
#contentTobeSent = [x for x in Collection_using_Pandas.find({}, {'_id': False} )]

client = MongoClient(uri )
movies_Data = client["Movie_complete_Collection"]
#Movie_List_Page = movies_Data.Collection_using_Pandas

#Collection_using_Pandas = movies_Data.Movie_complete_Collection  
Collection_using_Pandas = movies_Data.complete_Collection_primary  
 
#contentTobeSent = [x for x in Collection_using_Pandas.find({}, {'_id': False}).limit(50)]

contentTobeSent =  [x for x in movies_Data.complete_Collection_primary.aggregate(
   [
      { "$limit" : 100 },
      {
         "$project": {
            "_id" : 0,
            "Movie_Title" :{ "$ifNull": [ "$Movie_Title", "Movie_Title N/A" ] },
            "Year" : { "$ifNull": [ "$Year", "Year N/A" ] },
            "Directors" : { "$ifNull": [ "$Directors", "Directors N/A" ] },
            "Synopsis" : { "$ifNull": [ "$Synopsis", "Synopsis N/A" ] },
            "Actors_or_Stars" : { "$ifNull": [ "$Actors_or_Stars", "Actors_or_Stars N/A" ] },
            "votes_Received" : { "$ifNull": [ "$votes_Received", "votes_Received N/A" ] },
            "gross_Earnings" : { "$ifNull": [ "$gross_Earnings", "gross_Earnings N/A" ] },
            "Ratings" :{ "$ifNull": [ "$Ratings", "Ratings N/A" ] },
            "Runtime" : { "$ifNull": [ "$Runtime", "Runtime N/A" ] },
            "Motion_picture_content_rating" : { "$ifNull": [ "$Motion_picture_content_rating", "Motion_picture_content_rating N/A" ] },
         }
      }
   ]
)]


app = Flask(__name__)


@app.route('/')
def start_Page():
#def Start_Animation():
    return render_template("Start_Animation.html", content=contentTobeSent, pageheader="IMDb's Top 100 for 2021 movies")

@app.route('/<username>', methods = ['GET', 'POST'])
def profile(username):
    URL_to_Go = "Start_Animation." + username +  ".html"
    return render_template(URL_to_Go, content=contentTobeSent)
 
@app.route('/Test_page1', methods = ['GET', 'POST'])
def Test_page1():
#def Start_Animation():
    return ("Tis is just a test page")
 
 



if __name__ == "__main__":
    app.run(debug = True)


