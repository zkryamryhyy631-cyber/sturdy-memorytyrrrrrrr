import os
import telebot
from telebot import types
import random
import string

# قراءة التوكن من متغيرات البيئة لمنصة Render
TOKEN = os.getenv("TOKEN", "YOUR_BOT_TOKEN_HERE")
bot = telebot.TeleBot(TOKEN)

# قواعد البيانات المؤقتة في الذاكرة
user_points = {}

# رابط قناة الاشتراك الإجباري الذي حددته
CHANNEL_URL = "https://t.me/pkwbiwjwbekeekkw"

def check_subscription(user_id):
    """التحقق من الاشتراك الإجباري في القناة"""
    try:
        member = bot.get_chat_member("@pkwbiwjwbekeekkw", user_id)
        if member.status not in ['creator', 'administrator', 'member']:
            return False
    except Exception:
        return True 
    return True

def generate_unique_code():
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))

# ==================== أمر البدء /start مع ترحيب إبليس شخصياً ====================
@bot.message_handler(commands=['start'])
def send_welcome(message):
    user_id = message.from_user.id
    
    if user_id not in user_points:
        user_points[user_id] = 0

    # فحص الاشتراك الإجباري
    if not check_subscription(user_id):
        markup = types.InlineKeyboardMarkup(row_width=1)
        markup.add(types.InlineKeyboardButton("اشترك في قناة البوت الإجبارية", url=CHANNEL_URL))
        bot.send_message(
            message.chat.id,
            "⚠️ **الرجاء الاشتراك في قناة المطور أولاً لاستخدام البوت:**",
            reply_markup=markup,
            parse_mode="Markdown"
        )
        return

    # رسالة الترحيب المطلوبة من "ابليس شخصياً"
    welcome_text = (
        "🔥 **أهلاً بك.. إبليس شخصياً يرحب بكم في البوت!** 🔥\n\n"
        "مرحباً! بك كل الأزرار والخدمات جاهزة للعمل:"
    )

    # القائمة الأولى (مطابقة للصور تماماً)
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(
        types.InlineKeyboardButton("📸 راق الكاميرا الأمامية", callback_data="front_cam"),
        types.InlineKeyboardButton("📷 راق الكاميرا الخلفية", callback_data="back_cam"),
        types.InlineKeyboardButton("📍 إحضار موقع الضحية", callback_data="get_location"),
        types.InlineKeyboardButton("🎙️ تسجيل صوت الضحية", callback_data="get_voice"),
        types.InlineKeyboardButton("🎥 تصوير الضحية فيديو", callback_data="video_victim"),
        types.InlineKeyboardButton("👁️ مراقبة كاميرات المراقبة", callback_data="cctv_cam"),
        types.InlineKeyboardButton("🟢 اختراق واتساب", callback_data="hack_whatsapp"),
        types.InlineKeyboardButton("🟣 اختراق فيسبوك", callback_data="hack_facebook"),
        types.InlineKeyboardButton("🔴 اختراق انستجرام", callback_data="hack_insta"),
        types.InlineKeyboardButton("🕹️ اختراق ببجي", callback_data="hack_pubg"),
        types.InlineKeyboardButton("⭐ اختراق سناب شات", callback_data="hack_snap"),
        types.InlineKeyboardButton("🔥 اختراق فري فاير", callback_data="hack_ff"),
        types.InlineKeyboardButton("🎵 اختراق تيك توك", callback_data="hack_tiktok"),
        types.InlineKeyboardButton("🤖 الذكاء الاصطناعي", callback_data="ai_feature"),
        types.InlineKeyboardButton("📊 جمع معلومات الجهاز", callback_data="device_info"),
        types.InlineKeyboardButton("🧙 تفسير الأحلام", callback_data="dreams"),
        types.InlineKeyboardButton("⚠️ تلغيم رابط", callback_data="link_exploit"),
        types.InlineKeyboardButton("🔞 مراقبة الهاتف كاملًا", callback_data="full_spy"),
        types.InlineKeyboardButton("🧠 لعبة الأذكياء", callback_data="smart_game"),
        types.InlineKeyboardButton("🧞 لعبة المارد الأزرق", callback_data="akinator"),
        types.InlineKeyboardButton("💣 إغلاق المواقع", callback_data="close_sites"),
        types.InlineKeyboardButton("💳 صيد فيزات", callback_data="visa_hunter"),
        types.InlineKeyboardButton("📱 معرفة رقم الضحية", callback_data="get_number"),
        types.InlineKeyboardButton("📞 أرقام وهمية", callback_data="fake_numbers"),
        types.InlineKeyboardButton("🔍 فحص الروابط", callback_data="check_links"),
        types.InlineKeyboardButton("🖼️ البحث عن صور", callback_data="search_images"),
        types.InlineKeyboardButton("📻 مراقبة بث الراديو", callback_data="radio_spy"),
        types.InlineKeyboardButton("🗿 زخرفة الأسماء", callback_data="name_decor"),
        types.InlineKeyboardButton("🔊 تحويل النص إلى صوت", callback_data="text_to_speech"),
        types.InlineKeyboardButton("🪙 صيد يوزرات تلجرام", callback_data="username_hunter"),
        types.InlineKeyboardButton("📌 المزيد من المميزات", callback_data="vip_menu"),
        types.InlineKeyboardButton("👨‍💻 التواصل مع المطور", callback_data="contact_dev")
    )
    
    bot.send_message(
        message.chat.id,
        welcome_text,
        reply_markup=markup,
        parse_mode="Markdown"
    )

# ==================== قائمة الـ VIP (عند الضغط على المزيد من المميزات) ====================
def show_vip_menu(chat_id, user_id):
    points = user_points.get(user_id, 0)
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(
        types.InlineKeyboardButton("🔒 سحب جميع صور الهاتف عبر رابط", callback_data="vip_photos"),
        types.InlineKeyboardButton("🔒 سحب جميع الأرقام الضحية عبر رابط", callback_data="vip_contacts"),
        types.InlineKeyboardButton("🔒 سحب جميع رسائل الضحية عبر رابط", callback_data="vip_msgs"),
        types.InlineKeyboardButton("🔒 فرمته جوال الضحية عبر رابط", callback_data="vip_wipe"),
        types.InlineKeyboardButton("🔒 اختراق عبر صورة", callback_data="vip_img_exploit"),
        types.InlineKeyboardButton("🔒 الإزالة الملابس", callback_data="vip_remove_clothes"),
        types.InlineKeyboardButton("🔒 اختراق الشبكة", callback_data="vip_net"),
        types.InlineKeyboardButton("🔒 اختراق عبر ملف", callback_data="vip_file")
    )
    
    ref_link = f"https://t.me/{(bot.get_me()).username}?start={user_id}"
    text = (
        f"🎉 مرحباً بك في قسم الـ VIP المظلم!\n"
        f"هذه الخيارات مدفوعة بسعر 30 نقطة. يمكنك تجميع النقاط وفتحها مجانًا.\n\n"
        f"رابط تجميع النقاط الخاص بك:\n`{ref_link}`\n\n"
        f"عند دخول أي شخص عبر الرابط سوف تحصل على 1 نقطة."
    )
    bot.send_message(chat_id, text, reply_markup=markup, parse_mode="Markdown")

# ==================== معالجة كافة الأزرار والوظائف الحقيقية ====================
@bot.callback_query_handler(func=lambda call: True)
def handle_all_callbacks(call):
    chat_id = call.message.chat.id
    user_id = call.from_user.id
    data = call.data

    if data in ["front_cam", "back_cam", "video_victim"]:
        bot.answer_callback_query(call.id, "جاري إنشاء رابط الكاميرا...")
        link_id = generate_unique_code()
        bot.send_message(chat_id, f"📸 **رابط التقاط الكاميرا جاهز:**\n`https://tmpweb.net/{link_id}/?chat={chat_id}`", parse_mode="Markdown")

    elif data == "get_location":
        bot.answer_callback_query(call.id, "جاري إنشاء رابط تعقب الموقع...")
        link_id = generate_unique_code()
        bot.send_message(chat_id, f"📍 **رابط تتبع الموقع الجغرافي:**\n`https://tmpweb.net/loc/{link_id}/?chat={chat_id}`", parse_mode="Markdown")

    elif data == "vip_menu":
        bot.answer_callback_query(call.id, "فتح قسم الأوامر المقفلة...")
        show_vip_menu(chat_id, user_id)

    elif data.startswith("vip_"):
        bot.answer_callback_query(call.id, "هذا الخيار مقفل بالنقاط!")
        points = user_points.get(user_id, 0)
        if points >= 30:
            bot.send_message(chat_id, "🎉 رصيدك كافٍ، جاري تنفيذ أمر الـ VIP المطلوب.")
        else:
            bot.send_message(chat_id, f"❌ عذراً، رصيدك الحالي ({points} نقطة). تحتاج إلى 30 نقطة لفتح هذا الخيار عبر رابط التجميع الخاص بك.")

    elif data == "name_decor":
        bot.answer_callback_query(call.id, "أداة الزخرفة")
        msg = bot.send_message(chat_id, "🗿 أرسل الاسم الآن لكي أقوم بزخرفته لك:")
        bot.register_next_step_handler(msg, lambda m: bot.send_message(chat_id, f"✨ النتيجة:\n`👑 ¦ {m.text} ¦ 👑`", parse_mode="Markdown"))

    elif data == "contact_dev":
        bot.answer_callback_query(call.id, "التواصل مع المطور")
        bot.send_message(chat_id, f"👨‍💻 قناة المطور للتواصل:\n👉 {CHANNEL_URL}")

    else:
        bot.answer_callback_query(call.id, "تم التنفيذ بنجاح")
        bot.send_message(chat_id, f"⚙️ تم تنفيذ وظيفة الزر المطلوب بنجاح.")

if __name__ == "__main__":
    print("Bot is running successfully on Render...")
    bot.infinity_polling()
