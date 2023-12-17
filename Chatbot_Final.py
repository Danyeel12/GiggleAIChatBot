from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Create a new instance of a ChatBot
bot = ChatBot('GiggleBot')

# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(bot)

# Train the chatbot based on the english corpus
trainer.train("chatterbot.corpus.english")
trainer.train("chatterbot.corpus.english.greetings")
trainer.train("chatterbot.corpus.english.conversations")
trainer.train("chatterbot.corpus.english.emotion")
trainer.train("chatterbot.corpus.english.history")
trainer.train("chatterbot.corpus.english.money")
trainer.train("chatterbot.corpus.english.literature")
trainer.train("chatterbot.corpus.english.humor")
trainer.train("chatterbot.corpus.english.botprofile")
trainer.train("chatterbot.corpus.english.sports")
trainer.train("chatterbot.corpus.english.trivia")
trainer.train("chatterbot.corpus.english.politics")

# Define some greetings

greetings = ['hi', 'hello', 'hey', 'greetings']

# Function to check for exit conditions
def is_exit_command(user_input):
    return user_input.lower() in ['q', 'quit', 'exit', 'x']

# Function to check for greetings
def is_greeting(user_input):
    return user_input.lower() in greetings

# Start chatting
while True:
    try:
        user_input = input("User: ")

        # Check for exit command
        if is_exit_command(user_input):
            print("GiggleBot: Goodbye!")
            break

        # Check for greeting
        if is_greeting(user_input):
            print("GiggleBot:: Hello! How can I assist you today?")
            continue

        bot_response = bot.get_response(user_input)
        print(f"GiggleBot: {bot_response}")

    except(KeyboardInterrupt, EOFError, SystemExit):
        break
