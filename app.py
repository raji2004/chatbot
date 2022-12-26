from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer

app = Flask(__name__)

bot = ChatBot("Candice")
conversation = [
    "Hello" ,
    "Hi there!",
    "How are you doing?",
    "I'm doing great.",
    "That is good to hear",
    "Thank you.",
    "You're welcome.",
    "who made you" "who created you" "who is your maker",
    "raji is my maker",
    "Are you a robot?" ,
    "yes i am",
    "what do you like?" "likes?",
    "anime,music and so on",
    "whats your name",
    "i am candace",
    "what are you",
    "a robot"
]

trainer = ListTrainer(bot)

trainer.train(conversation)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(bot.get_response(userText))

app.run()
