import telebot
#from sending import *


# Создаем экземпляр бота
bot = telebot.TeleBot('TOKEN_HERE')

 



joinedFile = open('D:\\ras_bot\\joined.txt', 'r')
joinedUsers = set()
for line in joinedFile:
	joinedUsers.add(line.strip())
joinedFile.close()

admins=[761341981]

@bot.message_handler(commands=['sub'])
def startJoin(message):
	if not str(message.chat.id) in joinedUsers:
		joinedFile = open('D:\\ras_bot\\joined.txt', 'a')
		joinedFile.write(str(message.chat.id) + '\n')
		joinedUsers.add(message.chat.id)
	bot.send_message(message.chat.id, 'Отлично!👍\nВы успешно подписались на рассылку!😎')

def mess(message):
	for user in joinedUsers:
		bot.send_message(user, message.text[message.text.find(' '):])

@bot.message_handler(commands=['send'])
def mess(message):
	if message.from_user.id == 761341981:
		for user in joinedUsers:
			bot.send_message(user, message.text[message.text.find(' '):])
	else:
			bot.send_message(message.chat.id, 'У вас нет прав для использования этой команды 👎')

# Функция, обрабатывающая команду /start
@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Я на связи✋\nчтобы подписаться на рассылку пропиши /sub 👍\nпросмотреть список команд /help')
# Получение сообщений от юзера


@bot.message_handler(commands=["help"])
def help(m, res=False):
	bot.send_message(m.chat.id, 'User-команды:\n /sub-Подписаться на рассылку.\n Admind-команды: \n /send-Отправить сообщение всем подписанным пользователям')




# Запускаем бота
bot.polling(none_stop=True, interval=0)
