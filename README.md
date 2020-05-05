# r/WallStreetBets Sentiment Analysis

## To run locally

* Create a virtual environment on which to run this by

  -`python -m venv venv` on windows
  -`python3 -m venv venv` on mac
* Activate the virtual environment
  - `\env\Scripts\activate.bat` on windows
  - `source env/bin/activate` on mac

* Install dependencies
  - `pip install -r requirements.txt`

* run whatever python program from its folder, not root directory

## Running server in local
*Go to /Flask
-in your terminal run
-export FLASK_APP=server.py
-flask run
-go to localhost:5000



======================
how to label/tag comments

1.Get a csv of a comment thread by going to
/DataCollection

running 
python DataCollectionDisscussion.py
will give csvs of recent discussion posts

2.choose a csv file and move it to 
/TrainingData folder

3.choose tagging method
run 
python csvTagger.py "filename.csv"          for pos,neg,neutral
python csvRatingTagger.py "filename.csv"    for 1-5 ranking
