#This should take in a csv file and iterate through the comments and ask you to tag the comment
#then will create a new csv with tags
import sys
import os
import csv
import pathlib
import click
import csv
from csv import writer
from os import path
try:
    trainingFileName = sys.argv[1]
except IndexError:
    print("No csv file specified run with:")
    print("pyhton csvTagger.py FILENAME.csv")
    exit()

def clear():
    os.system( 'cls' )  

file= pathlib.Path(trainingFileName)
if file.exists():
        print(trainingFileName+"exists")
else:
    print("CSV file doesnt exist")
    exit()

with open("taggedCSV/"+trainingFileName+"Tagged.csv", 'w', newline='',encoding='utf-8') as file:
    print(trainingFileName+"Tagged.csv")

# file = open(os.path.join(trainingFileName), "rU")
# reader = csv.reader(file, delimiter=',')
# for row in reader:
#     print(row)

with open(trainingFileName, encoding="utf8") as csvfile:
    with open("taggedCSV/"+trainingFileName+"RatingTagged.csv",'a+',newline='',encoding='utf-8') as csvfile2:
        csvwriter=writer(csvfile2)
        csvreader = csv.reader(csvfile, delimiter=",")
        for row in csvreader:
            print(row[0])
            print("                   bearish   neutral     bullish")
            click.echo('Choose a range:     [1<-   2    3     4    ->5 ]', nl=False)
            c = click.getchar()
            click.echo()
            if c == '1':
                answer='1'
            elif c == '2':
                answer='2'
            elif c == '3':
                answer='3'
            elif c == '4':
                answer='4'    
            elif c == '5':
                answer='5'   
            else:
                answer='null'
                break    
            row=[str(row[0]),str(row[1]),str(row[2]),answer]
            print(row)
            csvwriter.writerow(row)
            clear()

# while True:

#     click.echo('Left Arrow BEAR - Right Arrow BULL - Space to SAVE', nl=False)
#     c = click.getchar()
#     click.echo()
#     if c == 'àM':
#         click.echo('right')
#     elif c == 'àK':
#         click.echo('left')
#     elif c == 'àP':
#         click.echo('down')
#     elif c == ' ':
#         click.echo("Saving")
#         break    
#     else:
#         click.echo(c)

# def writeRow():
#     row=[str(comment.body),str(comment.score),comment.id]