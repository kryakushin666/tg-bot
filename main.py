import telebot
import random

from telebot import types

bot = telebot.TeleBot("5237715711:AAHMbuqD7dSKTyQuhxF-nZVqlcMzeBmWkGM")

main_text_uslugi = "домашний интернет: fttb, подключение многоквартирных домов.\nкоммутатор-роутер-приставка-телевизор.\nздание обслуживают 2 кабеля, в квартиру заходит только 1\nподключение по витой паре, скорость 90-100 Мбит/с\nGPON подключение частных домов.\nоптоволокно заходит в дом, кабель подключается к онт терминалу.\nоборудование в доме по витой паре\nинсталляционный платеж 3-12 тысяч, при подключении камеры бесплатно\n\nWINK\nинтерактивное тв, 250+ каналов и 60000+ фильмов и сериалов\nWINK ИТВ, обычная приставка, подключение по витой паре. \nподключает любой телевизор, в сумме можно подключить до 3-х.\nаренда от 10р в месяц\nWINK ОНЛАЙН приложение, устанавливаемое на смарт-телевизор. \nдостаточно ввести код активации, сказанный техником и можно пользоваться всеми функциями тв.\nприложение бесплатное, скачать может любой человек.\nWINK+ премиальная приставка на базе андроид, к любому телевизору подключение по вай фай. \nделает из любого телевизора смарт-тв.\nесть вай фай,блютуз, голосовое управление, свой магазин приложений.\nрассрочка 250/24 только нашим клиентам, собственность 6000 любому человеку.\n\nмобильная связь\nработаем на вышках теле2, реализована функция переноса номера с любого оператора через мнп.\nдля переноса нужен положительный баланс на сим карте и полное совпадение паспортных данных\nклиент заполняет бланк мнп, вписывает данные паспорта, номер переносится в течение 5-7 рабочих дней\nвыкупили теле2 в 2016 году, самое большое покрытие по России\n\nвидеонаблюдение \n\nвнешнюю камеру ставим на улицу и в подъезд, для нее нужен инжектор стоимостью 1300\nустановка 1800\n350/24 нашим клиентам\n7690 всем\n2150 первый взнос при рассрочке\nвнутренние камеры только в помещение, подключается по вай фай\n350/24 нашим клиентам\n4990 всем\nчтобы клиент не переплачивал можно приобрести внутреннюю камеру и поставить на подоконник\nна всех камерах есть датчики движения и звука, просмотр записи идет через приложение\nархив записи на 7 дней 350р/мес, при покупке камеры в рассрочку на период рассрочки бесплатно\nв собственность бесплатный архив на полгода\nесли не оплачивать архив за 350, просматривать камеры можно будет в режиме онлайн, это бесплатно\n\nмаруся\nумная колонка с голосовым помощником\nрассказывает детям сказки, ставит фоновые шумы\nрассрочка 400/24+1800 первый взнос только нашим клиентам\n8990 всем клиентам \n\nгарантия\nзащита от повреждения оборудования, 30р/мес, за каждую гарантию агент получает +100 к зп и плюсик в карму\n\nмультирум подключение до 3-х тв, каждый доп.телик 1р/мес\n\nтехники работают 9.00-21.00 в любой день, подключим клиента даже в праздники\nподключение бесплатное кроме чс и тарифов по акции\n\nмобильная связь не считается за услугу, работает как повышающий коэффициент\nза смену тарифа не платят, только за допродажу\nпример: у клиента только инет ртк, агент допродал тв+сим. заплатят разницу в цене по кэфу 1.5\nесли инет+тв от ртк продаем оборудование - камеры, винк+, марусю, роутеры"

internet = "Домашний интернет: fttb, подключение многоквартирных домов.\nкоммутатор-роутер-приставка-телевизор\nздание обслуживают 2 кабеля, в квартиру заходит только 1\nподключение по витой паре, скорость 90-100 Мбит/с\nGPON подключение частных домов.\nоптоволокно заходит в дом, кабель подключается к онт терминалу.\nоборудование в доме по витой паре\nинсталляционный платеж 3-12 тысяч, при подключении камеры бесплатно"
wink = "WINK\nинтерактивное тв, 250+ каналов и 60000+ фильмов и сериалов\nWINK ИТВ, обычная приставка, подключение по витой паре. \nподключает любой телевизор, в сумме можно подключить до 3-х.\nаренда от 10р в месяц\nWINK ОНЛАЙН приложение, устанавливаемое на смарт-телевизор. \nдостаточно ввести код активации, сказанный техником и можно пользоваться всеми функциями тв.\nприложение бесплатное, скачать может любой человек.\nWINK+ премиальная приставка на базе андроид, к любому телевизору подключение по вай фай. \nделает из любого телевизора смарт-тв.\nесть вай фай,блютуз, голосовое управление, свой магазин приложений.\nрассрочка 250/24 только нашим клиентам, собственность 6000 любому человеку."
mvno = "Мобильная связь\nработаем на вышках теле2, реализована функция переноса номера с любого оператора через мнп.\nдля переноса нужен положительный баланс на сим карте и полное совпадение паспортных данных\nклиент заполняет бланк мнп, вписывает данные паспорта, номер переносится в течение 5-7 рабочих дней\nвыкупили теле2 в 2016 году, самое большое покрытие по России"
video = "Видеонаблюдение\nвнешнюю камеру ставим на улицу и в подъезд, для нее нужен инжектор стоимостью 1300\nустановка 1800\n350/24 нашим клиентам\n7690 всем\n2150 первый взнос при рассрочке\nвнутренние камеры только в помещение, подключается по вай фай\n350/24 нашим клиентам\n4990 всем\nчтобы клиент не переплачивал можно приобрести внутреннюю камеру и поставить на подоконник\nна всех камерах есть датчики движения и звука, просмотр записи идет через приложение\nархив записи на 7 дней 350р/мес, при покупке камеры в рассрочку на период рассрочки бесплатно\nв собственность бесплатный архив на полгода\nесли не оплачивать архив за 350, просматривать камеры можно будет в режиме онлайн, это бесплатно"
marusya = "Маруся\nумная колонка с голосовым помощником\nрассказывает детям сказки, ставит фоновые шумы\nрассрочка 400/24+1800 первый взнос только нашим клиентам\n8990 всем клиентам "
garant = "Гарантия\nзащита от повреждения оборудования, 30р/мес, за каждую гарантию агент получает +100 к зп и плюсик в карму"
tech = "Мультирум подключение до 3-х тв, каждый доп.телик 1р/мес\nтехники работают 9.00-21.00 в любой день, подключим клиента даже в праздники\nподключение бесплатное кроме чс и тарифов по акции\n\nмобильная связь не считается за услугу, работает как повышающий коэффициент\nза смену тарифа не платят, только за допродажу\nпример: у клиента только инет ртк, агент допродал тв+сим. заплатят разницу в цене по кэфу 1.5\nесли инет+тв от ртк продаем оборудование - камеры, винк+, марусю, роутеры"

markupV2 = types.InlineKeyboardMarkup(row_width=1)
item1V2 = types.InlineKeyboardButton("Домашний интернет", callback_data='internet2')
item2V2 = types.InlineKeyboardButton("WINK", callback_data='wink2')
item3V2 = types.InlineKeyboardButton("Мобильная связь", callback_data='mvno2')
item4V2 = types.InlineKeyboardButton("Видеонаблюдение", callback_data='video2')
item5V2 = types.InlineKeyboardButton("Маруся", callback_data='marusya2')
item6V2 = types.InlineKeyboardButton("Гарантия", callback_data='garant2')
item7V2 = types.InlineKeyboardButton("Тарифы", callback_data='tarif2')
item8V2 = types.InlineKeyboardButton("Технические работы", callback_data='tech2')

markupV2.add(item1V2, item2V2, item3V2, item4V2, item5V2, item6V2, item7V2, item8V2)


@bot.message_handler(commands=['start'])
def welcome(message):
    # keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item2 = types.KeyboardButton("🎲 Продукт")

    markup.add(item2)

    bot.send_message(message.chat.id,
                     "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот, который поможет тебе разобраться с работой..".format(
                         message.from_user, bot.get_me()),
                     parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type == 'private':
        if message.text == '🎲 Продукт':
            bot.send_message(message.chat.id, "Что нужно?", reply_markup=markupV2)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'internet':
                bot.send_message(call.message.chat.id, internet)
            elif call.data == 'wink':
                bot.send_message(call.message.chat.id, wink)
            elif call.data == 'mvno':
                bot.send_message(call.message.chat.id, mvno)
            elif call.data == 'video':
                bot.send_message(call.message.chat.id, video)
            elif call.data == 'marusya':
                bot.send_message(call.message.chat.id, marusya)
            elif call.data == 'garant':
                bot.send_message(call.message.chat.id, garant)
            elif call.data == 'tech':
                bot.send_message(call.message.chat.id, tech)
            elif call.data == 'tarif':
                bot.send_photo(call.message.chat.id, "https://i.imgur.com/aligt5u.jpg")

            elif call.data == 'internet2':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=internet,
                                      reply_markup=markupV2)
            elif call.data == 'wink2':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=wink,
                                      reply_markup=markupV2)
            elif call.data == 'mvno2':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=mvno,
                                      reply_markup=markupV2)
            elif call.data == 'video2':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=video,
                                      reply_markup=markupV2)
            elif call.data == 'marusya2':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=marusya,
                                      reply_markup=markupV2)
            elif call.data == 'garant2':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=garant,
                                      reply_markup=markupV2)
            elif call.data == 'tech2':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=tech,
                                      reply_markup=markupV2)
            elif call.data == 'tarif2':
                bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
                bot.send_photo(call.message.chat.id, "https://i.imgur.com/aligt5u.jpg")
                bot.send_message(chat_id=call.message.chat.id, text="Выберите нужный пункт", reply_markup=markupV2)

    except Exception as e:
        print(repr(e))


# RUN
bot.polling(none_stop=True)
