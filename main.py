import telebot
from config import *
from markup import *
import os
import sqlite3 as sq
from telebot import custom_filters


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_name = os.path.join(BASE_DIR, 'main.db')
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start_mess(message):
    if len(message.text) > 6:
        referer_id = int(message.text.split(' ')[1])
    else:
        referer_id = 0
    connect = sq.connect(db_name)
    cursor = connect.cursor()
    cursor.execute('SELECT * FROM users WHERE chat_id=? ;', [message.from_user.id])
    info = cursor.fetchall()
    if not info:
        cursor.execute('INSERT INTO users(name,chat_id,referals) VALUES(?,?,?);',
                       [message.from_user.first_name, message.from_user.id, referer_id])
        referer_info = cursor.fetchall()
        if referer_info:
            cursor.execute('UPDATE users SET `referals` = ? WHERE chat_id = ?;', [referer_info[0][0] + 1, referer_id])
        connect.commit()
        cursor.close()
        connect.close()
    bot.send_message(message.from_user.id, f"Botdan foydalanish uchun kanalga a'zo bo'ling {channel_link}", reply_markup=markup_1)



@bot.message_handler(func=lambda message: True, content_types=['text'])
def mess_hand(message):
    chat_id = message.chat.id
    if message.text == "Asosiy kanalimiz 💬":
        bot.send_message(chat_id, "ATOMIC CRYPTO UZ👇 obuna bo'lish esizdan chiqmasin va do'stlaringizga yuboring Hali hammasi oldinda", reply_markup=main_channel())
    elif message.text == "Trading darsliklar 📹":
        bot.send_message(chat_id, "Trading darsliklar 👇 obuna bo'lish esizdan chiqmasin va do'stlaringizga yuboring Hali hammasi oldinda",
                         reply_markup=channel_lesson())
    elif message.text == "Do'st taklif qilish ➕":
        bot.send_message(chat_id, f"Do'stlaringizga yuboring va bepul signallar oling😉",
                         reply_markup=get_share_key(chat_id))
    elif message.text == "Taklif qilingan do'stlar 📈":
        referrals_count = get_referrals_count(chat_id)
        bot.send_message(chat_id, f"Sizning taklif qilingan do'stlaringiz soni: {referrals_count}")
    elif message.text == "Bepul skalping signallar":
        referrals_count = get_referrals_count(chat_id)
        if referrals_count >= 5:
            bot.send_message(chat_id, f"Signalni kuting")
            bot.register_next_step_handler(message, handle_new_channel_post)
        else:
            bot.send_message(chat_id, f"siz 5 tadan kam odam qo'shgansiz, szda hozir {referrals_count} do'st taklif qilingan \
             https://t.me/{BOT_NAME}?start={chat_id}",
                             reply_markup=get_share_key(chat_id))
    elif message.text == "VIPKANAL  Haqida 💎":
        bot.send_message(chat_id, "Welcome to the VIP Channel!\n\n" +
                          "Bizning VIP kanalda halol coinlarda ishlaymiz.. Insha Allah|\n\n" +
                          "Vipda har kuni kamida 2 ta bo'ladi ko'p bo'lsa 10 tagacha\n\n" +
                          "Bozor holatiga qarab 🚀\n\n" +
                          "Uzoq muddatga va qisqa muddatga signallar bo'ladi.🤝\n\n" +
                          "Garant oyiga 100% profit o'rtacha hisoblaganda.\n\n" +
                          "Siz tradingda ma'lumotingiz bo'lishi kerak 🔥\n\n" +
                          "Vipga kirish majburiy emas ‼️\n\n" +
                          "Agarda foyda olomasangiz to'lovingiz qaytariladi 🤝\n\n" +
                          "Murojjat uchun @Atomic_crypto\n\n" +
                          "Hozirgi narxi 20 USDT\n\n" +
                          "Tolov tizimlari\n\n" +
                          "Binance id 🆔\n\n" +
                          "Elektron trc-20\n" +
                          "Karta to'lov 💳")
    elif message.text == "Bot haqidaℹ️":
        bot.send_message(chat_id, "🤖 Botimiz haqida malumot\n\n" +
                          "ATOMIC_CRYPTO asosiy vazifasi sizga tahlilarizga va uzoq muddat va qisqa muddatga signallar beriladi..💰\n\n" +
                          "Bizning yo'nalishimiz SPOT va Halol coinlarda ishlaymiz📌\n\n" +
                          "💡 Trading hozirda eng rivojlanvotgan soxadir.\n\n" +
                          "📚 Aslo unutmang FOMOga berilmang va hech qachon taslim bo'lmang\n\n" +
                          "🔍 Siz qaysi yo'nalishda ekanligizi bilib oling")


@bot.channel_post_handler(chat_id=[-1002032308872], content_types=['text', 'photo', 'video'])
def handle_new_channel_post(message):

    connect = sq.connect(db_name)
    cursor = connect.cursor()
    cursor.execute("SELECT chat_id FROM users")
    user_ids = [row[0] for row in cursor.fetchall()]

    for user_id in user_ids:
        bot.copy_message(chat_id=user_id, from_chat_id="@signalchanelltest100", message_id=message.message_id)

bot.add_custom_filter(custom_filters.ChatFilter())



def get_referrals_count(user_id):
    connect = sq.connect(db_name)
    cursor = connect.cursor()
    cursor.execute('SELECT referals FROM users WHERE chat_id=?;', [user_id])

    result = cursor.fetchone()
    referrals_count = result[0] if result is not None else 0

    connect.close()
    return referrals_count

# #
# # # bu cod botni siklda iwlatiwga javob b
if DEBUG:
    bot.delete_webhook()
    bot.infinity_polling()

