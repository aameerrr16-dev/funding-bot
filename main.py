
import os
from telethon import TelegramClient, events, Button

# البيانات الجديدة الخاصة بك
API_ID = 30408566
API_HASH = 'f92c18e8aa38024eb6e8f4ea0417e2c0'
BOT_TOKEN = '8743792430:AAGnc2STZJQ_tylbv7osyr7qQjLTQAbJBgw'

# إنشاء جلسة البوت
bot = TelegramClient('bot_session', API_ID, API_HASH).start(bot_token=BOT_TOKEN)

# الأمر /start والأزرار الرئيسية
@bot.on(events.NewMessage(pattern='/start'))
async def start_handler(event):
    buttons = [
        [Button.inline("➕ إضافة حساب جديد", data="add_account")],
        [Button.inline("🚀 بدء حملة النقل", data="start_transfer")],
        [Button.inline("ℹ️ معلومات البوت", data="info")]
    ]
    await event.respond("أهلاً بك في بوت نقل أعضاء التليجرام! 🚀\nاختر من القائمة أدناه:", buttons=buttons)

# التفاعل مع الأزرار
@bot.on(events.CallbackQuery)
async def callback_handler(event):
    if event.data == b"add_account":
        await event.respond("يرجى إرسال رقم الهاتف مع رمز الدولة لإضافة الحساب.")
    elif event.data == b"start_transfer":
        await event.respond("أرسل معرّفات الكروبات بالشكل التالي:\n`@source_group @target_group`")
    elif event.data == b"info":
        await event.respond("بوت نقل الأعضاء يعمل بنجاح سحابياً 24/7 ⚡")

print("Bot is running...")
bot.run_until_disconnected()
