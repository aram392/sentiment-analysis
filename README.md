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