from aiogram import types
from loader import dp

from keyboards.user.inline import start_keyboard, menu_keyboard


texts = {
    '0': 'Здравствуй, дорогой первокурскик, рады тебя видеть в стенах нашего вуза. Эти кнопочки помогут тебе быстрее освоится в вузе, всего тебе хорошего!!!',
    '1': """
ул. Большая Морская 67, ауд. 11-18 
(ПН-ПТ 10:00 17:00)
""",
    '2': """
Документы:
Приписное удостоверение/военный билет и его копия (1,2)
Паспорт и его копия (2,3, 5 страницы)
Если из СПб, то еще свидетельство о регистрации (прописка)
На отдельном листе написать: ФИО, дату рождения и телефоны родителей, 
предыдущее место учёбы (год окончания, населённый пункт, регион), номер группы, 
язык изучаемый в школе, контактный номер телефона.
ул. Большая Морская 67, ауд. 12-33 
Связаться можно по телефону +7 (812) 312-50-60 или через электронную почту 
fvi@guap.ru
Пн, вт, чт, пт - с 13:00 до 16:00

""",
    '3': """
Гастелло 15 (ауд. 11-02), Ленсовета 14 (ауд. 21-07), 12 факультет (СПО) - отдай 
документы Спутнику.
с 10:00 до 15:00
Документы: 
Копия паспорта
Копия ОМС
Копия СНИЛС
Оригинал справки 086-у
Копия прививочного сертификата (если нет, то оригинал справки 063-у)
Оригинал флюорографии (если нет отметки в справке 086-у)
""",
    '4': """
Назначается студентам, закрывшим сессию на 4\5, также являющимися:
Детьми-сиротами и детьми, оставшимися без попечения родителей.
Детьми-инвалидами, инвалидами 1 и 2 группы, инвалидами с детства.
Студентами, подвергшимися воздействию радиации вследствие катастроф.
Студентами, являющимися инвалидами в следствие военной травмы, ветеранами 
боевых действий.
Студентами, получившими государственную социальную помощь.
Размер выплат – 3000 руб/мес.
""",
    '5': """
Отдел по работе в общежитиях: Пивцаев Михаил Юрьевич +7 (812) 494 70 37 // 
4947095@guap.ru ул. Большая Морская 67, ауд. 52-50а

Общежитие №1 - пр. Маршала Жукова, 24
Секционный тип - 4 секции - 6 комнат в секции - 2 человека в комнате
2400 руб/месяц

Общежитие №2 - ул. Передовиков, 13к1
Квартирный тип - 18 квартир - 2-3 комнаты в квартире - 2-3 человека в комнате
2400 руб/месяц

Общежитие №3 - ул. Варшавская, 8
Коридорный тип - 2 крыла - 8 комнат в крыле - 3 человека в комнате
2400 руб/месяц

МСГ - Новоизмайловский проспект, 16к1
Коридорный тип - 25 комнат на этаже - 3-4 человека в комнате
3900 руб/месяц
""",
    '6': """
Институт №1: 
Директор - Майоров Николай Николаевич aerospace1@guap.ru
(812)494-70-12,(812)571-16-89
Б.Морская67,ауд.52-14
Заместитель директора по младшим курсам - Кузнецова Надежда Александровна 
maslova1@guap.ru, (812)708-42-02
Гастелло 15,ауд.13-11

Институт №2
Директор - Бестугин Александр Роальдович zlata@aanet.ru, (812)571-19-89
Б.Морская67,ауд.52-36
Заместитель директора по младшим курсам - Андреева Екатерина Владимировна 
fresgas@guap.ru, (812)371-64-35
Гастелло 15,ауд.13-05

Институт №3
Директор - Шишлаков Владислав Федорович shishlakov@guap.ru, (812)494-70-31
Б.Морская67,ауд.21-17
Заместитель директора по младшим курсам - Полякова Татьяна Геннадьевна, 
3dekanat@guap.ru (812)708-39-33
Гастелло 15,ауд.13-02

Институт №4
Директор - Татарникова Татьяна Михайловна dept4@aanet.ru, (812)494-70-40
Б.Морская67,ауд.52-36
Заместитель директора по младшим курсам - Малинина Ирина Георгиевна 
dept4g@aanet.ru, (812)708-39-43
Гастелло 15,ауд.13-06





Институт ФПТИ:
Директор - Фролова Елена Александровна dek_ibmp@guap.ru, (812)494-70-55,(812)708-
38-59
Б.Морская67,ауд.23-21;
Заместитель директора по младшим курсам - Пушкина Вера Павловна (812)708-38-59
Гастелло 15,ауд.13-01


Гуманитарный факультет (6 факультет)
Декан - Лосев Константин Викторович losev@guap.ru, (812)494-70-61,(812)373-20-02
Б.Морская67,ауд.53-06:
Телефон деканата +7 (812) 494-70-61
E-mail деканата secretariat@hf-guap.ru

Гастелло, ауд. 14-07:
Телефон деканата +7 (812) 708-43-45
E-mail деканата secretariat@hf-guap.ru
про зама на младших курсах инфы на сайте нет

Институт 8:
Директор - Будагов Артур Суренович dean8@aanet.ru, (812)315-50-47
Б.Морская67,ауд.52-54
про зама на младших курсах инфы на сайте нет

Факультет СПО (факультет 12)
Декан - Поляков Сергей Леонидович (812)387-48-88,(812)387-32-92,(812)494-70-87
Московский 149в,ауд.312;
Б.Морская67,ауд.14-45
""",
    '7': """
Действия: 
Заполни форму - forms.gle/AzrwLBBTNrTgSuC87 
Найди себя в списках в группе ВК Профкома
Оформи карту через сайт - zakaz.ltkarta.ru или на кассу метро с паспортом и 
студенческим 
Забери карту на выбранной станции
""",
    '8': """
На Большой Морской, 67 - точно есть
На Гастелло, 15 - тут тоже точно есть
На Ленсовета, 14 - тут тем более есть
""",
    '9': """
ул. Большая Морская, д. 67, лит. А, каб. 23-03
Мобильный телефон: +7(812)494-70-07
Почта: stud_ok@guap.ru
""",
    '10': """
Справки об обучении заказываются через личный кабинет ГУАП.
При необходимости указывается организация, куда нужно предоставить справку. 
Готовую справку можно получить через три рабочих дня (не считая дня заказа) в отделе 
кадров обучающихся Б. Морская 67, каб 23-03.
Режим работы: пн, вт, чт, пт 9:00-10:00 и 14:00-16:30, среда 14:00-15:00
По возникшим вопросам обращаться по телефону (812) 494-70-07.
""",
}


@dp.message_handler(commands='start')
async def start(message: types.Message) -> None:
    await message.answer(texts['0'], reply_markup=await start_keyboard())


@dp.message_handler(lambda m: m.text == 'профком хуйня')
async def true(message: types.Message):
    await message.edit_text('Верно мыслишь, дорогой!')


@dp.callback_query_handler(lambda c: c.data.isdigit())
async def menu(call: types.CallbackQuery) -> None:
    await call.message.edit_text(
        texts[call.data],
        reply_markup=await menu_keyboard()
    )

@dp.callback_query_handler(lambda c: c.data == 'back')
async def back_to_start(call: types.CallbackQuery):
    await call.message.edit_text(texts['0'], reply_markup=await start_keyboard())