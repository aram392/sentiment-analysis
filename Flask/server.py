from flask import Flask, render_template 
from flask_socketio import SocketIO, send, emit
from threading import Thread, Event
import time
from random import random
import praw
import pickle

#setup for reddit comment stream
reddit = praw.Reddit(client_id='IvGvwGotLBLBaA',
                    client_secret='kWWiOZ2LvKDy5gUyElLIOWrClAc',
                    username='HopefulHawk6',  
                    password='Wallstreetbets',
                    user_agent='wsbcomp')
sub = reddit.subreddit('wallstreetbets')


#mnb model
f = open('MultinomialNB.pickle', 'rb')
MultinomialNB = pickle.load(f)
f.close()
f = open('CountVectorizer.pickle', 'rb')
CV = pickle.load(f)
f.close()

#flask and socketio setup
app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'
socketio = SocketIO(app,cors_allowed_origins="*")
thread = Thread()
thread_stop_event = Event()


@socketio.on('connect', namespace='/test')
def test_connect():
    global thread
    print('Client connected')
    #Start thread for streaming comments
    if not thread.isAlive():
        print("Starting Thread")
        thread = socketio.start_background_task(runCommentThread)

def runCommentThread():
    print("Making random numbers")
    while not thread_stop_event.isSet():  
        for comment in sub.stream.comments():
            try:
                commentBody=str(comment.body)
                score=int(MultinomialNB.predict(CV.transform([commentBody])))
                data = {'comment': commentBody, 'score': score} 
                socketio.emit('tcp_data', {'data': data})
            except praw.exceptions.PRAWException as e:
                print(e)
            

@socketio.on('message')
def handleMessage(msg):
	print('Message: ' + msg)
	send(msg, broadcast=True)
msg1 = 'hey'

@app.route('/')
def index():
    #only by sending this page first will the client be connected to the socketio instance
    return render_template('index.html')


if __name__ == '__main__':
    socketio.run(app)