import telebot 
import webbrowser

bot = telebot.TeleBot('6592923965:AAEIeb25-IgwOT3oDjb30CGK07LcijcO1KQ')

@bot.message_handler(commands=["site", "website"])
def site(message):
    webbrowser.open("https://core.telegram.org/api")

@bot.message_handler(commands=["start"])
def main(message):
    bot.send_message(message.chat.id, f"Welcome, {message.from_user.first_name} {message.from_user.last_name}" )

@bot.message_handler()
def info(message):
    if message.text.lower() == "welcome":
        bot.send_message(message.chat.id, f"Welcome, {message.from_user.first_name} {message.from_user.last_name}") 
    elif message.text.lower() == "id":
        bot.reply_to(message, f"ID: {message.from_user.id}")

bot.polling(none_stop=True, interval=0)


