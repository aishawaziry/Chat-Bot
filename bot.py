from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from cleaner import clean_corpus

Train_FILE = "bot_train.txt"

chatbot = ChatBot("Chatpot")

trainer = ListTrainer(chatbot)
cleaned = clean_corpus(Train_FILE)
trainer.train(cleaned)
exit_conditions = (":q", "quit", "exit")
while True:
    query = input("> ")
    if query in exit_conditions:
        break
    else:
        print(f" {chatbot.get_response(query)}")