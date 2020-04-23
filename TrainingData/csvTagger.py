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

with open(trainingFileName+"Tagged.csv", 'w', newline='',encoding='utf-8') as file:
    print(trainingFileName+"Tagged.csv")


reader = csv.reader(file, delimiter=',')
for row in reader:
    print(row[0])


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