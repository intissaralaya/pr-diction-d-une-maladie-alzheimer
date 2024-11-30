# Importation des bibliothèques nécessaires
from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Initialisation de l'application Flask
app = Flask(__name__)

# Initialisation du chatbot
chatbot = ChatBot('ChatBot')
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("chatterbot.corpus.english")

# Définition des routes pour l'application web
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(chatbot.get_response(userText))

# Exécution de l'application Flask si ce fichier est le point d'entrée principal
if __name__ == "__main__":
    app.run()
