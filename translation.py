from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

class Translation(object):

    START_TEXT = """
مرحبا بك  {} , في بوت تحميل الفديوهات  من اليوتيوب.. قم بارسال رابط  الفديو  المراد  تحميله. او اضغط /help للمساعدة 

#تطوير @abujooood

"""
    HELP_TEXT = """
<b><u>طريقة التحميل من البوت </u></b>
➠ قم بارسال رابط لفديو اليوتيوب لتحميله من اليوتيوب الى تلقرام .

<b><u>ضبط صورة صغرة </u></b>
➠ قم بارسال اي صورة وساجعلها صورة مصغرة للفديو .

<b><u>حذف الصورة المصغرة </u></b>
➠ استخدم الامر  /delthumb لحذف الصورة المصغرة .

<b><u>عرض الصورة المصغرة الحالية </u></b>
➠ اضغط  /showthumb لعرض الصورة المصغرة الحالية .

تم التطوير بواسطة  @abujooood
"""
    ABOUT_TEXT = """
- **اسم البوت  :** `بوت التحميل من اليوتيوب `
- **مطور البوت  :** [ابوجود](https://telegram.me/abujooood)
- **قناة البوت  :** [بوتات انصار الله ](https://t.me/YeBotat)
- **حالة البوت  :** `مجاني للابد `
- **مجموعة الدعم  :** [اضغط هنا ](https://t.me/botatAnsarAllah)
- **اللغة  :** [بايثون ](https://python.org)
- **المكتبة  :** [Pyrogram v1.2.0](https://pyrogram.org)
- **السيرفر  :** [Heroku](https://heroku.com)
"""
    START_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('قناة البوت ', url='https://telegram.me/YeBotat'),
        InlineKeyboardButton(' مطور البوت  ', url='https://telegram.me/abujooood')
        ],[
        InlineKeyboardButton('مساعدة ', callback_data='help'),
        InlineKeyboardButton('حول البوت ', callback_data='about'),
        InlineKeyboardButton('اغلاق ', callback_data='close')
        ]]
    )
    HELP_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('الرئيسية ', callback_data='home'),
        InlineKeyboardButton('حول البوت', callback_data='about'),
        InlineKeyboardButton('اغلاق', callback_data='close')
        ]]
    )
    ABOUT_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('الرئيسية ', callback_data='home'),
        InlineKeyboardButton('مساعدة', callback_data='help'),
        InlineKeyboardButton('اغلاق', callback_data='close')
        ]]
    )
    BLOCK_LIST_TEXT = "هذا الرابط محظور لا استطيع تحميلة .\n\nتكلم مع  @abujooood"
    FORMAT_SELECTION = """<b>قم باختيار الصيغة المناسبة :</b> <a href='{}'>حجم الفديو قد يكون تقريبي </a>
    
ارسل لي الصورة المصغرة اذا ترغب بذلك .
تستطيع باي وقت الضغط على  /delthumb لحذف الصورة المصغرة الحالية ."""
    CHECKING_LINK = "<code>جاري فحص الرابط </code>⏳"
    BANNED_USER_TEXT = "<code>انت محظور من استخدام البوت !</code>"
    SET_CUSTOM_USERNAME_PASSWORD = """اذا تريد النسخة المدفوعة , ارسل لي بيانات الاشتراك كالتالي:
الرابط  | اسم الملف  | اسم المستخدم  | كلمة المرور"""
    DOWNLOAD_START = "<code>تم تحميل الفديو الى السرفر الخاص بالبوت ...</code>"    
    UPLOAD_START = "<code>جاري رفع الفديو الى تلقرام ...</code>"
    AFTER_SUCCESSFUL_UPLOAD_MSG_WITH_TS = "تم التحميل في  {} ثواني . \n\nتم الرفع في  {} ثواني ."
    RCHD_TG_API_LIMIT = "تم التحميل في  {} ثواني .\nحجم الفديو : {}\nالمعذرة . انا لا , استطيع تحميل الفديوهات التي حجمها اكبر من  1.95جيجا  بسبب قيود تلقرام s."
    CUSTOM_CAPTION_UL_FILE = "<b>انضم لقناتنا  :-</b> @YeBotat"
    SLOW_URL_DECED = "للاسف هذا الرابط يبدو رابط بطيء للغاية . , انا ماني فاضي احمل هذا الفديو . استخدم رابط فديو سريع :==> ادخل  https://shrtz.me/PtsVnf6 واجلب رابط سريع ,وانا سوف اقوم بارساله لك ."
    NO_VOID_FORMAT_FOUND = "<code>{}</code>"
    REPORT_SITE_TEXT = "<code>نأسف لعدم التحميل في هذا الموقع هنا لأن هذا الموقع يقوم بالإبلاغ عن البوت .</code>"
    SOMETHING_WRONG = "<code> حدث خطأ. حاول مرة اخرى .</code>"
    FORCE_SUBSCRIBE_TEXT = "<code>المعذرة عزيزي يجب عليك الاشتراك في قناة البوت كي تستطيع استخدامي  😌😉....</code>"
    FREE_USER_LIMIT_Q_SZE = "المعذرة صديقي ,المستخدم المجاني يستطيع تنزيل فديو واحد كل    {} دقيقة . الرجاء المحاولة بعد {} ثواني ."
