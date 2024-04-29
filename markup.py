from telebot import types

from config import BOT_NAME

markup_1=types.ReplyKeyboardMarkup(resize_keyboard=True)
markup_1.add(types.KeyboardButton(text='Asosiy kanalimiz 💬'),types.KeyboardButton(text="Do'st taklif qilish ➕"),
             types.KeyboardButton(text="Taklif qilingan do'stlar 📈"),types.KeyboardButton(text="Trading darsliklar 📹"),
             types.KeyboardButton(text="VIPKANAL  Haqida 💎"),types.KeyboardButton(text='Bot haqidaℹ️'),types.KeyboardButton(text='Bepul skalping signallar'))

def main_channel():
    channel_link = types.InlineKeyboardMarkup()
    channel_link.add(types.InlineKeyboardButton(text="ATOMIC CRYPTO", url='https://t.me/atomic_cryptouz'))
    return channel_link


def channel_lesson():
    lesson = types.InlineKeyboardMarkup()
    lesson.add(types.InlineKeyboardButton(text="Trading darsliklar", url='https://t.me/atomic_darslik'))
    return lesson


def get_share_key(chat_id):
    share_url_key =types.InlineKeyboardMarkup()
    share_url_key.add(types.InlineKeyboardButton(text='Do\'stlarga ulashish',url=f'https://t.me/share/url?url=https://t.me/{BOT_NAME}?start={chat_id}'))
    return share_url_key


