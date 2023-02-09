#! /usr/bin/env python
# -*- coding: utf-8 -*-

import telegram
import json
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.types import InputMedia
from aiogram.utils import executor

TOKEN = "5960220760:AAG0FZ1aDjk1jA7SzhfiFA2BsVaBn1NT4HM"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
prof_gens = [
    ["https://pogruzchik.dp.ua/storage/preview/geemka.jpg", "<b>Дизельний генератор (56 кВт) KKWC60GF</b>\n\nЦіна: 12700$\n\n<b>Кількість фаз:</b> 3 фази, чотири дроти\n<b>Максимальна потужність (кВт): 60/75</b>\n<b>Двигун: Weichai - WP4.1D66E200</b>\n<b>Об\'єм паливного бака (л): 90</b>\n<b>Витрати палива (г/кВт.г): 208</b>\n<b>Безперервний час роботи (г):</b> 11\n<b>Габаритні розміри ДхШхВ (мм):</b> 2200*900*1500\n<b>Тип пального:</b> Дизель\n<b>Напруга (В):</b> 400/230\n<b>Номінальна потужність (кВт):</b> 56/70\n<b>Охолодження:</b> Водяне\n<b>Вага (кг):</b> 960\n<b>Рівень шуму (Дб):</b> 72/7\n<b>Рівень захисту:</b> IP 22\n<b>Об\'єм баку мастила (л):</b> 14\n\n<a href=\"https://pogruzchik.dp.ua/generator_item/geemka-kkwc60gf\">Детальніше</a>"],
    ["https://pogruzchik.dp.ua/storage/preview/geemka.jpg", "<b>Дизельний генератор (66 кВт) KKWC90GF</b>\n\nЦіна: 13715$\n\n<b>Кількість фаз:</b> 3 фази, чотири дроти\n<b>Максимальна потужність (кВт):</b> 72/90\n<b>Двигун:</b> Weichai - WP4.1D80E200\n<b>Об\'єм паливного бака (л):</b> 100\n<b>Витрати палива (г/кВт.г):</b> 235\n<b>Безперервний час роботи (г):</b> 11\n<b>Габаритні розміри ДхШхВ (мм):</b> 2450*1000*1600\n<b>Тип пального:</b> Дизель\n<b>Напруга (В):</b> 400/230\n<b>Номінальна потужність (кВт):</b> 66/82\n<b>Охолодження:</b> Водяне\n<b>Вага (кг):</b> 1180\n<b>Рівень шуму (Дб):</b> 73/7\n<b>Рівень захисту:</b> IP 22\n<b>Об\'єм баку мастила (л):</b> 14\n\n<a href=\"https://pogruzchik.dp.ua/generator_item/geemka-kkwc90gf\">Детальніше</a>"],
    ["https://pogruzchik.dp.ua/storage/preview/geemka.jpg", "<b>Дизельний генератор (90 кВт) KKWF120GF</b>\n\nЦіна: 14700$\n\n<b>Кількість фаз:</b> 3 фази, чотири дроти\n<b>Максимальна потужність (кВт):</b> 100/125\n<b>Двигун:</b> Ricardo - R6105AZLD\n<b>Об\'єм паливного бака (л):</b> 150\n<b>Витрати палива (г/кВт.г):</b> 218\n<b>Безперервний час роботи (г):</b> 10\n<b>Габаритні розміри ДхШхВ (мм):</b> 2800*1070*1600\n<b>Тип пального:</b> Дизель\n<b>Напруга (В):</b> 400/230\n<b>Номінальна потужність (кВт):</b> 90/112\n<b>Охолодження:</b> Водяне\n<b>Вага (кг):</b> 1250\n<b>Рівень шуму (Дб):</b> 76/7\n<b>Рівень захисту:</b> IP 22\n<b>Об\'єм баку мастила (л):</b> 22\n\n<a href=\"https://pogruzchik.dp.ua/generator_item/geemka-kkwf120gf\">Детальніше</a>"]
]
all_gens = [
    ["https://pogruzchik.dp.ua/storage/preview/DG7000.jpg", "<b>Дизельний генератор Newland DG7000</b>\n\nЦіна: 1370$\n\n<b>Кількість фаз:</b> 1\n<b>Максимальна потужність (кВт):</b> 5.5\n<b>Двигун:</b> 188F\n<b>Об\'єм паливного бака (л):</b> 12.5\n<b>Габаритні розміри ДхШхВ (мм):</b> 740*490*670\n<b>Тип пального:</b> Дизель\n<b>Напруга (В):</b> 220V/50Hz\n<b>Номінальна потужність (кВт):</b> 5\n<b>Охолодження:</b> Повітряне\n<b>Вага (кг):</b> 105\n\n<a href=\"https://pogruzchik.dp.ua/generator_item/newland-dg7000\">Детальніше</a>"],
    ["https://pogruzchik.dp.ua/storage/preview/DG7000.jpg", "<b>Дизельний генератор Newland DG9000</b>\n\nЦіна: 1580$\n\n<b>Кількість фаз:</b> 1\n<b>Максимальна потужність (кВт):</b> 7.5\n<b>Двигун:</b> 195F\n<b>Об'єм паливного бака (л):</b> 12.5\n<b>Габаритні розміри ДхШхВ (мм):</b> 760*500*640\n<b>Тип пального:</b> Дизель\n<b>Напруга (В):</b> 220V/50Hz\n<b>Номінальна потужність (кВт):</b> 7\n<b>Охолодження:</b> Повітряне\n<b>Вага (кг):</b> 117\n\n<a href=\"https://pogruzchik.dp.ua/generator_item/newland-dg9000\">Детальніше</a>"],
    ["https://pogruzchik.dp.ua/storage/preview/NL3000.jpg", "<b>Бензиновий генератор Newland NL3000</b>\n\nЦіна: 540$\n\n<b>Кількість фаз:</b> 1<b>Максимальна потужність (кВт):</b> 2.6\n<b>Двигун:</b> 170F\n<b>Об\'єм паливного бака (л):</b> 15\n<b>Габаритні розміри ДхШхВ (мм):</b> 690*525*550\n<b>Тип пального:</b> Бензин\n<b>Напруга (В):</b> 220V/50hz\n<b>Номінальна потужність (кВт):</b> 3\n<b>Охолодження:</b> Повітряне\n<b>Вага (кг):</b> 40\n\n<a href=\"https://pogruzchik.dp.ua/generator_item/newland-nl3000\">Детальніше</a>"],
    ["https://pogruzchik.dp.ua/storage/preview/NL3000.jpg", "<b>Бензиновий генератор Newland NL6500</b>\n\nЦіна: 1000$\n\n<b>Кількість фаз:</b> 1<b>Максимальна потужність (кВт):</b> 5.5\n<b>Двигун:</b> 190F\n<b>Об\'єм паливного бака (л):</b> 25\n<b>Габаритні розміри ДхШхВ (мм):</b> 690*525*550\n<b>Тип пального:</b> Бензин\n<b>Напруга (В):</b> 220V/50hz\n<b>Номінальна потужність (кВт):</b> 5\n<b>Охолодження:</b> Повітряне\n<b>Вага (кг):</b> 72\n\n<a href=\"https://pogruzchik.dp.ua/generator_item/newland-nl6500\">Детальніше</a>"],
    ["https://pogruzchik.dp.ua/storage/preview/NL3000.jpg", "<b>Бензиновий генератор Newland NL8500</b>\n\nЦіна: 1220$\n\n<b>Кількість фаз:</b> 1<b>Максимальна потужність (кВт):</b> 7.5\n<b>Двигун:</b> 192F\n<b>Об\'єм паливного бака (л):</b> 25\n<b>Габаритні розміри ДхШхВ (мм):</b> 690*525*550\n<b>Тип пального:</b> Бензин\n<b>Напруга (В):</b> 220V/50hz\n<b>Номінальна потужність (кВт):</b> 7\n<b>Охолодження:</b> Повітряне\n<b>Вага (кг):</b> 86\n\n<a href=\"https://pogruzchik.dp.ua/generator_item/newland-nl8500\">Детальніше</a>"],
    ["https://pogruzchik.dp.ua/storage/preview/geemka.jpg", "<b>Дизельний генератор (56 кВт) KKWC60GF</b>\n\nЦіна: 12700$\n\n<b>Кількість фаз:</b> 3 фази, чотири дроти\n<b>Максимальна потужність (кВт): 60/75</b>\n<b>Двигун: Weichai - WP4.1D66E200</b>\n<b>Об\'єм паливного бака (л): 90</b>\n<b>Витрати палива (г/кВт.г): 208</b>\n<b>Безперервний час роботи (г):</b> 11\n<b>Габаритні розміри ДхШхВ (мм):</b> 2200*900*1500\n<b>Тип пального:</b> Дизель\n<b>Напруга (В):</b> 400/230\n<b>Номінальна потужність (кВт):</b> 56/70\n<b>Охолодження:</b> Водяне\n<b>Вага (кг):</b> 960\n<b>Рівень шуму (Дб):</b> 72/7\n<b>Рівень захисту:</b> IP 22\n<b>Об\'єм баку мастила (л):</b> 14\n\n<a href=\"https://pogruzchik.dp.ua/generator_item/geemka-kkwc60gf\">Детальніше</a>"],
    ["https://pogruzchik.dp.ua/storage/preview/geemka.jpg", "<b>Дизельний генератор (66 кВт) KKWC90GF</b>\n\nЦіна: 13715$\n\n<b>Кількість фаз:</b> 3 фази, чотири дроти\n<b>Максимальна потужність (кВт):</b> 72/90\n<b>Двигун:</b> Weichai - WP4.1D80E200\n<b>Об\'єм паливного бака (л):</b> 100\n<b>Витрати палива (г/кВт.г):</b> 235\n<b>Безперервний час роботи (г):</b> 11\n<b>Габаритні розміри ДхШхВ (мм):</b> 2450*1000*1600\n<b>Тип пального:</b> Дизель\n<b>Напруга (В):</b> 400/230\n<b>Номінальна потужність (кВт):</b> 66/82\n<b>Охолодження:</b> Водяне\n<b>Вага (кг):</b> 1180\n<b>Рівень шуму (Дб):</b> 73/7\n<b>Рівень захисту:</b> IP 22\n<b>Об\'єм баку мастила (л):</b> 14\n\n<a href=\"https://pogruzchik.dp.ua/generator_item/geemka-kkwc90gf\">Детальніше</a>"],
    ["https://pogruzchik.dp.ua/storage/preview/geemka.jpg", "<b>Дизельний генератор (90 кВт) KKWF120GF</b>\n\nЦіна: 14700$\n\n<b>Кількість фаз:</b> 3 фази, чотири дроти\n<b>Максимальна потужність (кВт):</b> 100/125\n<b>Двигун:</b> Ricardo - R6105AZLD\n<b>Об\'єм паливного бака (л):</b> 150\n<b>Витрати палива (г/кВт.г):</b> 218\n<b>Безперервний час роботи (г):</b> 10\n<b>Габаритні розміри ДхШхВ (мм):</b> 2800*1070*1600\n<b>Тип пального:</b> Дизель\n<b>Напруга (В):</b> 400/230\n<b>Номінальна потужність (кВт):</b> 90/112\n<b>Охолодження:</b> Водяне\n<b>Вага (кг):</b> 1250\n<b>Рівень шуму (Дб):</b> 76/7\n<b>Рівень захисту:</b> IP 22\n<b>Об\'єм баку мастила (л):</b> 22\n\n<a href=\"https://pogruzchik.dp.ua/generator_item/geemka-kkwf120gf\">Детальніше</a>"]
]
pobut_gens = [
    ["https://pogruzchik.dp.ua/storage/preview/DG7000.jpg", "<b>Дизельний генератор Newland DG7000</b>\n\nЦіна: 1370$\n\n<b>Кількість фаз:</b> 1\n<b>Максимальна потужність (кВт):</b> 5.5\n<b>Двигун:</b> 188F\n<b>Об\'єм паливного бака (л):</b> 12.5\n<b>Габаритні розміри ДхШхВ (мм):</b> 740*490*670\n<b>Тип пального:</b> Дизель\n<b>Напруга (В):</b> 220V/50Hz\n<b>Номінальна потужність (кВт):</b> 5\n<b>Охолодження:</b> Повітряне\n<b>Вага (кг):</b> 105\n\n<a href=\"https://pogruzchik.dp.ua/generator_item/newland-dg7000\">Детальніше</a>"],
    ["https://pogruzchik.dp.ua/storage/preview/DG7000.jpg", "<b>Дизельний генератор Newland DG9000</b>\n\nЦіна: 1580$\n\n<b>Кількість фаз:</b> 1\n<b>Максимальна потужність (кВт):</b> 7.5\n<b>Двигун:</b> 195F\n<b>Об'єм паливного бака (л):</b> 12.5\n<b>Габаритні розміри ДхШхВ (мм):</b> 760*500*640\n<b>Тип пального:</b> Дизель\n<b>Напруга (В):</b> 220V/50Hz\n<b>Номінальна потужність (кВт):</b> 7\n<b>Охолодження:</b> Повітряне\n<b>Вага (кг):</b> 117\n\n<a href=\"https://pogruzchik.dp.ua/generator_item/newland-dg9000\">Детальніше</a>"],
    ["https://pogruzchik.dp.ua/storage/preview/NL3000.jpg", "<b>Бензиновий генератор Newland NL3000</b>\n\nЦіна: 540$\n\n<b>Кількість фаз:</b> 1<b>Максимальна потужність (кВт):</b> 2.6\n<b>Двигун:</b> 170F\n<b>Об\'єм паливного бака (л):</b> 15\n<b>Габаритні розміри ДхШхВ (мм):</b> 690*525*550\n<b>Тип пального:</b> Бензин\n<b>Напруга (В):</b> 220V/50hz\n<b>Номінальна потужність (кВт):</b> 3\n<b>Охолодження:</b> Повітряне\n<b>Вага (кг):</b> 40\n\n<a href=\"https://pogruzchik.dp.ua/generator_item/newland-nl3000\">Детальніше</a>"],
    ["https://pogruzchik.dp.ua/storage/preview/NL3000.jpg", "<b>Бензиновий генератор Newland NL6500</b>\n\nЦіна: 1000$\n\n<b>Кількість фаз:</b> 1<b>Максимальна потужність (кВт):</b> 5.5\n<b>Двигун:</b> 190F\n<b>Об\'єм паливного бака (л):</b> 25\n<b>Габаритні розміри ДхШхВ (мм):</b> 690*525*550\n<b>Тип пального:</b> Бензин\n<b>Напруга (В):</b> 220V/50hz\n<b>Номінальна потужність (кВт):</b> 5\n<b>Охолодження:</b> Повітряне\n<b>Вага (кг):</b> 72\n\n<a href=\"https://pogruzchik.dp.ua/generator_item/newland-nl6500\">Детальніше</a>"],
    ["https://pogruzchik.dp.ua/storage/preview/NL3000.jpg", "<b>Бензиновий генератор Newland NL8500</b>\n\nЦіна: 1220$\n\n<b>Кількість фаз:</b> 1<b>Максимальна потужність (кВт):</b> 7.5\n<b>Двигун:</b> 192F\n<b>Об\'єм паливного бака (л):</b> 25\n<b>Габаритні розміри ДхШхВ (мм):</b> 690*525*550\n<b>Тип пального:</b> Бензин\n<b>Напруга (В):</b> 220V/50hz\n<b>Номінальна потужність (кВт):</b> 7\n<b>Охолодження:</b> Повітряне\n<b>Вага (кг):</b> 86\n\n<a href=\"https://pogruzchik.dp.ua/generator_item/newland-nl8500\">Детальніше</a>"],
 ]
diesel_gens = [
    ["https://pogruzchik.dp.ua/storage/preview/DG7000.jpg", "<b>Дизельний генератор Newland DG7000</b>\n\nЦіна: 1370$\n\n<b>Кількість фаз:</b> 1\n<b>Максимальна потужність (кВт):</b> 5.5\n<b>Двигун:</b> 188F\n<b>Об\'єм паливного бака (л):</b> 12.5\n<b>Габаритні розміри ДхШхВ (мм):</b> 740*490*670\n<b>Тип пального:</b> Дизель\n<b>Напруга (В):</b> 220V/50Hz\n<b>Номінальна потужність (кВт):</b> 5\n<b>Охолодження:</b> Повітряне\n<b>Вага (кг):</b> 105\n\n<a href=\"https://pogruzchik.dp.ua/generator_item/newland-dg7000\">Детальніше</a>"],
    ["https://pogruzchik.dp.ua/storage/preview/DG7000.jpg", "<b>Дизельний генератор Newland DG9000</b>\n\nЦіна: 1580$\n\n<b>Кількість фаз:</b> 1\n<b>Максимальна потужність (кВт):</b> 7.5\n<b>Двигун:</b> 195F\n<b>Об'єм паливного бака (л):</b> 12.5\n<b>Габаритні розміри ДхШхВ (мм):</b> 760*500*640\n<b>Тип пального:</b> Дизель\n<b>Напруга (В):</b> 220V/50Hz\n<b>Номінальна потужність (кВт):</b> 7\n<b>Охолодження:</b> Повітряне\n<b>Вага (кг):</b> 117\n\n<a href=\"https://pogruzchik.dp.ua/generator_item/newland-dg9000\">Детальніше</a>"]
]
fuel_gens = [
    ["https://pogruzchik.dp.ua/storage/preview/NL3000.jpg", "<b>Бензиновий генератор Newland NL3000</b>\n\nЦіна: 540$\n\n<b>Кількість фаз:</b> 1\n<b>Максимальна потужність (кВт):</b> 2.6\n<b>Двигун:</b> 170F\n<b>Об\'єм паливного бака (л):</b> 15\n<b>Габаритні розміри ДхШхВ (мм):</b> 690*525*550\n<b>Тип пального:</b> Бензин\n<b>Напруга (В):</b> 220V/50hz\n<b>Номінальна потужність (кВт):</b> 3\n<b>Охолодження:</b> Повітряне\n<b>Вага (кг):</b> 40\n\n<a href=\"https://pogruzchik.dp.ua/generator_item/newland-nl3000\">Детальніше</a>"],
    ["https://pogruzchik.dp.ua/storage/preview/NL3000.jpg", "<b>Бензиновий генератор Newland NL6500</b>\n\nЦіна: 1000$\n\n<b>Кількість фаз:</b> 1\n<b>Максимальна потужність (кВт):</b> 5.5\n<b>Двигун:</b> 190F\n<b>Об\'єм паливного бака (л):</b> 25\n<b>Габаритні розміри ДхШхВ (мм):</b> 690*525*550\n<b>Тип пального:</b> Бензин\n<b>Напруга (В):</b> 220V/50hz\n<b>Номінальна потужність (кВт):</b> 5\n<b>Охолодження:</b> Повітряне\n<b>Вага (кг):</b> 72\n\n<a href=\"https://pogruzchik.dp.ua/generator_item/newland-nl6500\">Детальніше</a>"],
    ["https://pogruzchik.dp.ua/storage/preview/NL3000.jpg", "<b>Бензиновий генератор Newland NL8500</b>\n\nЦіна: 1220$\n\n<b>Кількість фаз:</b> 1\n<b>Максимальна потужність (кВт):</b> 7.5\n<b>Двигун:</b> 192F\n<b>Об\'єм паливного бака (л):</b> 25\n<b>Габаритні розміри ДхШхВ (мм):</b> 690*525*550\n<b>Тип пального:</b> Бензин\n<b>Напруга (В):</b> 220V/50hz\n<b>Номінальна потужність (кВт):</b> 7\n<b>Охолодження:</b> Повітряне\n<b>Вага (кг):</b> 86\n\n<a href=\"https://pogruzchik.dp.ua/generator_item/newland-nl8500\">Детальніше</a>"]
]


@dp.message_handler(commands=['start'])
async def process_start_command(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*[types.KeyboardButton(name) for name in ['Генератори', 'Послуги']])
    keyboard.add(*[types.KeyboardButton(name) for name in ['FAQ', 'Лишити заявку']])
    await bot.send_message(message.chat.id,
                           'Вас вітає сервісний центр генераторів Logistic Forklift. Кнопки внизу екрану відповідають за навігацію по окремим розділам нашого боту.\n\n"Генератори" - тут Ви зможете ознайомитись із каталогом наших генераторів та обрати саме той що Вам підходить.\n\n"Послуги" - в цьому розділі Ви зможете ознайомитись із послугами, що пропонує наша компанія.\n\n"FAQ" - тут Ви зможете найти відповіді на питання та поради по експлуатації і підбору генератора.\n\n"Лишити заявку" - якщо Ви хочете щоб наш менеджер зателефонував Вам, просто натисніть цю кнопку і лишіть свої контакти.',
                           reply_markup=keyboard)


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply("Напиши мне что-нибудь, и я отпрпавлю этот текст тебе в ответ!")


@dp.message_handler(content_types=['text'])
async def echo_message(msg: types.Message):
    if msg.text.lower() == 'лишити заявку':
        await geophone(msg)
    elif msg.text.lower() == 'до головного меню':
        await main_menu(msg)
    elif msg.text.lower() == 'генератори':
        await courses_list(msg)
    elif msg.text.lower() == 'послуги':
        await services_list(msg)
    elif msg.text.lower() == 'faq':
        await faq_list(msg)


async def courses_list(message):
    key = types.InlineKeyboardMarkup(row_width=1)
    but_1 = types.InlineKeyboardButton(text="Всі генератори", callback_data="all_gens")
    but_2 = types.InlineKeyboardButton(text="Побутові (3-7 кВт)", callback_data="pobut_gens")
    but_4 = types.InlineKeyboardButton(text="Промислові(25-150 кВт)", callback_data="professional_gens")
    but_5 = types.InlineKeyboardButton(text="Бензинові", callback_data="fuel_gens")
    but_6 = types.InlineKeyboardButton(text="Дизельні", callback_data="diesel_gens")
    key.add(but_1, but_2, but_4, but_5, but_6)
    await bot.send_message(message.chat.id, 'В нашому каталозі є як промислові, так і побутові моделі генераторів різної потужності. Оберіть тип генератора або перейдіть до повного каталогу зі допомогою кнопки "Всі генератори"', reply_markup=key)


async def professional_gens(message):
    key = types.InlineKeyboardMarkup(row_width=3)
    but_1 = types.InlineKeyboardButton(text="←", callback_data="prev_gen")
    but_2 = types.InlineKeyboardButton(text="1/10", callback_data="page_number")
    but_3 = types.InlineKeyboardButton(text="→", callback_data="next_gen")
    but_4 = types.InlineKeyboardButton(text="Консультація(лишити заявку)", callback_data="leave_contacts")
    key.add(but_1, but_2, but_3, but_4)
    await bot.send_photo(message.chat.id,
                         'https://certification.dp.ua/wp-content/uploads/2020/08/prof-prev-870x440.jpg',
                         caption='<b>Погрузчик грузоподъемностью 5 тонн</b> - ₴500\n\nВилочный погрузчик грузоподъемностью 5 тонн – надежная машина специального назначения для сладских хозяйств, производственных, сельскохозяйственных и других предприятий.\n\n<a href="https://certification.dp.ua/courses/5-ton/">Перейти к курсу</a>',
                         parse_mode="HTML", reply_markup=key)


async def swiper_next_prof(message, item):
    key = types.InlineKeyboardMarkup(row_width=3)
    but_1 = types.InlineKeyboardButton(text="←", callback_data="prev_prof")
    but_2 = types.InlineKeyboardButton(text=item+"/3", callback_data=item)
    but_3 = types.InlineKeyboardButton(text="→", callback_data="next_prof")
    but_4 = types.InlineKeyboardButton(text="Консультація(лишити заявку)", callback_data="leave_contacts")
    key.add(but_1, but_2, but_3, but_4)
    await bot.edit_message_caption(chat_id=message.chat.id,
                                   message_id=message.message_id,
                                   caption=prof_gens[int(item) - 1][1],
                                   parse_mode="HTML", reply_markup=key)
    # await bot.edit_message_media(chat_id=message.chat.id,
    #                               message_id=message.message_id,
    #                               media=prof_gens[int(item) - 1][0],
    #                               reply_markup=key)


async def swiper_prev_prof(message, item):
    print(item)
    key = types.InlineKeyboardMarkup(row_width=3)
    but_1 = types.InlineKeyboardButton(text="←", callback_data="prev_prof")
    but_2 = types.InlineKeyboardButton(text=item+"/3", callback_data=item)
    but_3 = types.InlineKeyboardButton(text="→", callback_data="next_prof")
    but_4 = types.InlineKeyboardButton(text="Консультація(лишити заявку)", callback_data="leave_contacts")
    key.add(but_1, but_2, but_3, but_4)
    await bot.edit_message_caption(chat_id=message.chat.id,
                                   message_id=message.message_id,
                                   caption=prof_gens[int(item) - 1][1],
                                   parse_mode="HTML", reply_markup=key)
    # await bot.edit_message_media(chat_id=message.chat.id,
    #                               message_id=message.message_id,
    #                               media=prof_gens[int(item) - 1][0],
    #                               reply_markup=key)


async def swiper_next_pobut(message, item):
    key = types.InlineKeyboardMarkup(row_width=3)
    but_1 = types.InlineKeyboardButton(text="←", callback_data="prev_pobut")
    but_2 = types.InlineKeyboardButton(text=item+"/5", callback_data=item)
    but_3 = types.InlineKeyboardButton(text="→", callback_data="next_pobut")
    but_4 = types.InlineKeyboardButton(text="Консультація(лишити заявку)", callback_data="leave_contacts")
    key.add(but_1, but_2, but_3, but_4)
    await bot.edit_message_media(chat_id=message.chat.id,
                                 message_id=message.message_id,
                                 media=json.dumps({'type': 'photo', 'media': pobut_gens[int(item) - 1][0]}),
                                 reply_markup=key)
    await bot.edit_message_caption(chat_id=message.chat.id,
                                   message_id=message.message_id,
                                   caption=pobut_gens[int(item) - 1][1],
                                   parse_mode="HTML", reply_markup=key)



async def swiper_prev_pobut(message, item):
    print(item)
    key = types.InlineKeyboardMarkup(row_width=3)
    but_1 = types.InlineKeyboardButton(text="←", callback_data="prev_pobut")
    but_2 = types.InlineKeyboardButton(text=item+"/5", callback_data=item)
    but_3 = types.InlineKeyboardButton(text="→", callback_data="next_pobut")
    but_4 = types.InlineKeyboardButton(text="Консультація(лишити заявку)", callback_data="leave_contacts")
    key.add(but_1, but_2, but_3, but_4)
    await bot.edit_message_media(chat_id=message.chat.id,
                                 message_id=message.message_id,
                                 media=json.dumps({'type': 'photo', 'media': pobut_gens[int(item) - 1][0]}),
                                 reply_markup=key)
    await bot.edit_message_caption(chat_id=message.chat.id,
                                   message_id=message.message_id,
                                   caption=pobut_gens[int(item) - 1][1],
                                   parse_mode="HTML", reply_markup=key)


async def swiper_next_all(message, item):
    key = types.InlineKeyboardMarkup(row_width=3)
    but_1 = types.InlineKeyboardButton(text="←", callback_data="prev_all")
    but_2 = types.InlineKeyboardButton(text=item+"/8", callback_data=item)
    but_3 = types.InlineKeyboardButton(text="→", callback_data="next_all")
    but_4 = types.InlineKeyboardButton(text="Консультація(лишити заявку)", callback_data="leave_contacts")
    key.add(but_1, but_2, but_3, but_4)
    await bot.edit_message_media(chat_id=message.chat.id,
                                 message_id=message.message_id,
                                 media=json.dumps({'type': 'photo', 'media': all_gens[int(item) - 1][0]}),
                                 reply_markup=key)
    await bot.edit_message_caption(chat_id=message.chat.id,
                                   message_id=message.message_id,
                                   caption=all_gens[int(item) - 1][1],
                                   parse_mode="HTML", reply_markup=key)



async def swiper_prev_all(message, item):
    print(item)
    key = types.InlineKeyboardMarkup(row_width=3)
    but_1 = types.InlineKeyboardButton(text="←", callback_data="prev_all")
    but_2 = types.InlineKeyboardButton(text=item+"/8", callback_data=item)
    but_3 = types.InlineKeyboardButton(text="→", callback_data="next_all")
    but_4 = types.InlineKeyboardButton(text="Консультація(лишити заявку)", callback_data="leave_contacts")
    key.add(but_1, but_2, but_3, but_4)
    await bot.edit_message_media(chat_id=message.chat.id,
                                 message_id=message.message_id,
                                 media=json.dumps({'type': 'photo', 'media': all_gens[int(item) - 1][0]}),
                                 reply_markup=key)
    await bot.edit_message_caption(chat_id=message.chat.id,
                                   message_id=message.message_id,
                                   caption=all_gens[int(item) - 1][1],
                                   parse_mode="HTML", reply_markup=key)


async def swiper_next_fuel(message, item):
    key = types.InlineKeyboardMarkup(row_width=3)
    but_1 = types.InlineKeyboardButton(text="←", callback_data="prev_fuel")
    but_2 = types.InlineKeyboardButton(text=item+"/3", callback_data=item)
    but_3 = types.InlineKeyboardButton(text="→", callback_data="next_fuel")
    but_4 = types.InlineKeyboardButton(text="Консультація(лишити заявку)", callback_data="leave_contacts")
    key.add(but_1, but_2, but_3, but_4)
    await bot.edit_message_caption(chat_id=message.chat.id,
                                   message_id=message.message_id,
                                   caption=fuel_gens[int(item) - 1][1],
                                   parse_mode="HTML", reply_markup=key)


async def swiper_prev_fuel(message, item):
    print(item)
    key = types.InlineKeyboardMarkup(row_width=3)
    but_1 = types.InlineKeyboardButton(text="←", callback_data="prev_fuel")
    but_2 = types.InlineKeyboardButton(text=item+"/3", callback_data=item)
    but_3 = types.InlineKeyboardButton(text="→", callback_data="next_fuel")
    but_4 = types.InlineKeyboardButton(text="Консультація(лишити заявку)", callback_data="leave_contacts")
    key.add(but_1, but_2, but_3, but_4)
    await bot.edit_message_caption(chat_id=message.chat.id,
                                   message_id=message.message_id,
                                   caption=fuel_gens[int(item) - 1][1],
                                   parse_mode="HTML", reply_markup=key)


async def swiper_next_diesel(message, item):
    key = types.InlineKeyboardMarkup(row_width=3)
    but_1 = types.InlineKeyboardButton(text="←", callback_data="prev_diesel")
    but_2 = types.InlineKeyboardButton(text=item+"/2", callback_data=item)
    but_3 = types.InlineKeyboardButton(text="→", callback_data="next_diesel")
    but_4 = types.InlineKeyboardButton(text="Консультація(лишити заявку)", callback_data="leave_contacts")
    key.add(but_1, but_2, but_3, but_4)
    await bot.edit_message_caption(chat_id=message.chat.id,
                                   message_id=message.message_id,
                                   caption=fuel_gens[int(item) - 1][1],
                                   parse_mode="HTML", reply_markup=key)


async def swiper_prev_diesel(message, item):
    print(item)
    key = types.InlineKeyboardMarkup(row_width=3)
    but_1 = types.InlineKeyboardButton(text="←", callback_data="prev_diesel")
    but_2 = types.InlineKeyboardButton(text=item+"/2", callback_data=item)
    but_3 = types.InlineKeyboardButton(text="→", callback_data="next_diesel")
    but_4 = types.InlineKeyboardButton(text="Консультація(лишити заявку)", callback_data="leave_contacts")
    key.add(but_1, but_2, but_3, but_4)
    await bot.edit_message_caption(chat_id=message.chat.id,
                                   message_id=message.message_id,
                                   caption=fuel_gens[int(item) - 1][1],
                                   parse_mode="HTML", reply_markup=key)


async def services_list(message):
    key = types.InlineKeyboardMarkup(row_width=2)
    but_1 = types.InlineKeyboardButton(text="Встановлення", callback_data="installing")
    but_2 = types.InlineKeyboardButton(text="Обслуговування", callback_data="repair")
    but_4 = types.InlineKeyboardButton(text="Консультація(лишити заявку)", callback_data="leave_contacts")
    key.add(but_1, but_2, but_4)
    await bot.send_message(message.chat.id, "Яка послуга Вас цікавить?", reply_markup=key)


async def faq_list(message):
    key = types.InlineKeyboardMarkup(row_width=1)
    but_1 = types.InlineKeyboardButton(text="Який термін доставки генератора?", callback_data="сourse_price")
    but_2 = types.InlineKeyboardButton(text="Як правильно обрати генератор?", callback_data="сourse_time")
    but_3 = types.InlineKeyboardButton(text="Як безпечно користуватись генератором?", callback_data="start_time")
    key.add(but_1, but_2, but_3)
    await bot.send_message(message.chat.id, "Питання, що можуть Вас зацікавити:", reply_markup=key)


@dp.callback_query_handler(lambda c: True)
async def inline(c):
    if c.data == 'back_to_list':
        await faq_list(c.message)
    if c.data == 'сourse_price':
        key = types.InlineKeyboardMarkup(row_width=1)
        but_1 = types.InlineKeyboardButton(text="<- Назад до питань", callback_data="back_to_list")
        key.add(but_1)
        await bot.send_message(c.message.chat.id, "<b>Який термін доставки генератора?</b>\n\nДоставка відбувається протягом 90 днів з моменту замовлення.", parse_mode="HTML", reply_markup=key)
    if c.data == 'сourse_time':
        key = types.InlineKeyboardMarkup(row_width=1)
        but_1 = types.InlineKeyboardButton(text="<- Назад до питань", callback_data="back_to_list")
        key.add(but_1)
        await bot.send_message(c.message.chat.id,
                               "<b>Як правильно обрати генератор?</b>\n\nДо 3000 Вт: найкраще підходить для базових генераторів і підходить для живлення холодильника та деяких джерел світла, але, ймовірно, не для чогось іншого.\n\nДо 6000 Вт: чудово підходить для інверторних генераторів середнього розміру та для одночасного ввімкнення кількох приладів, включно з холодильником, освітленням, телевізором, ноутбуком і, можливо, іншими приладами.\n\nДо 10 000 Вт: ваш вибір це портативного генератора або великий інверторний генератор, оскільки ви можете увімкнути холодильник, мікрохвильову піч, кондиціонер, обігрівач, водонагрівач і, можливо, більше пристроїв.\n\nДо 20 000 Вт: для такого типу потужності портативні та/або інверторні генератори не є найкращим варіантом. Вам краще переоцінити свій список необхідних речей, або ви можете розглянути можливість інвестувати в промисловий генератор.\n\nІнша річ, про яку слід пам’ятати, це те, що деякі прилади (наприклад, кондиціонери) також вимагають «стрибку» потужності, щоб почати роботу. Якщо ви забудете врахувати цю імпульсну потужність (також відому як початкова потужність, яка залежить від приладу), ваші розрахунки будуть некоректні, а ваш генератор може не працювати належним чином.\n\nЯкщо ви сумніваєтеся, завжди можете зателефонувати до нас і прокунсультуватись, ми дамо відповідь на ваші запитання та допоможемо підібрати генератор належним чином.",
                               parse_mode="HTML", reply_markup=key)
    if c.data == 'start_time':
        key = types.InlineKeyboardMarkup(row_width=1)
        but_1 = types.InlineKeyboardButton(text="<- Назад до питань", callback_data="back_to_list")
        key.add(but_1)
        await bot.send_message(c.message.chat.id,
                               "<b>Як безпечно користуватись генератором?</b>\n\nПро безпеку генератора потрібно знати багато, але є золоте правило. Ви ніколи — ні за яких обставин — не повинні використовувати його вдома. Включаючи ваш підвал, балкон і гараж, оскільки обидві ці зони безпосередньо приєднані до будинку.\n\nПричина? Генератори створюють монооксид вуглецю (CO), газ без кольору та запаху, який може призвести до смерті всього за 5 хвилин за певних рівнів через вплив.\n\nЩоб бути максимально обережними та зменшити ризик отруєння вуглекислим газом, генератори повинні весь час працювати у повністю відкритих, добре провітрюваних приміщеннях. Крім того, ви можете додатково встановити датчики CO по всьому будинку.\n\nПроте недостатньо просто використовувати один датчик на вулиці. Загроза отруєння вуглекислим газом через використання генератора настільки висока, що вам також потрібно переконатися, що пристрій знаходиться щонайменше на 20 футів від вашого будинку чи будівлі, коли він працює. Обов’язково розмістіть вихлопну трубу двигуна подалі від будь-яких дверей, вікон або блоків кондиціонерів, оскільки це може допомогти зменшити ризик впливу CO.",
                               parse_mode="HTML", reply_markup=key)
    if c.data == 'main_course':
        key = types.InlineKeyboardMarkup(row_width=2)
        but_1 = types.InlineKeyboardButton(text="Записаться", callback_data="geophone")
        but_2 = types.InlineKeyboardButton(text="К другим курсам", callback_data="other_courses")
        key.add(but_1, but_2)
        await bot.send_photo(c.message.chat.id, 'https://certification.dp.ua/wp-content/uploads/2020/05/main-prev-870x440.jpg', caption='<b>Основной курс</b> - ₴4,500\n\nОсновной курс – это курс обучения на вилочном погрузчике. Теорию можно пройти как самостоятельно ,так и  в нашем центре обучения В обучение входит 20% теории и 80% практики. Теория заключается в самостоятельном изучении онлайн лекций с помощью своего смартфона, планшета или компьютера и после изученного материала прохождения онлайн тестов. Затем, вы, с полученным онлайн сертификатом, можете приступить к практическим занятиям.\n\nНеобходимые документы для поступления:\n1. Ксерокопия паспорта\n2. Ксерокопия идентификационного кода\n3. Сертификат от нарколога\n4. Сертификат от психолога\n5. Две фотографии размера 3*4\n\nПосле окончания курса Вы получаете удостоверение с профессией "Водитель погрузчика", дополнение к удостоверению - пластиковую карту ГОС образца с переводом на английском языке.\n\n<a href="https://certification.dp.ua/courses/main-course/">Перейти к курсу</a>', parse_mode="HTML", reply_markup=key)
    if c.data == 'installing':
        key = types.InlineKeyboardMarkup(row_width=1)
        but_1 = types.InlineKeyboardButton(text="Лишити заявку", callback_data="geophone")
        key.add(but_1)
        await bot.send_photo(c.message.chat.id,
                             'https://pogruzchik.dp.ua/storage/preview/photo_2023-01-30_09-29-49.jpg',
                             caption='Компанія Logistic Forklift виконує встановлення, монтаж, підключення і налагодження дизель-генераторів та бензинових електростанцій по всій території України.\nНаші переваги:\n- Оперативно приїжджаємо в обумовлений час\n- Робота виконується досвідченими майстрами\n- Гарантія на встановлення 1 рік\n- Безкоштовна консультація\n- Проводимо технічне обслуговування та виконуємо ремонт вашої техніки.\n\nЄ питання? Потрібна консультація? Бажаєте здійснити підключення генератора? Звертайтесь!',
                             parse_mode="HTML", reply_markup=key)
    if c.data == 'repair':
        key = types.InlineKeyboardMarkup(row_width=1)
        but_1 = types.InlineKeyboardButton(text="Лишити заявку", callback_data="geophone")
        key.add(but_1)
        await bot.send_photo(c.message.chat.id,
                             'https://pogruzchik.dp.ua/storage/preview/photo_2023-01-30_09-29-46.jpg',
                             caption='Компанія Logistic Forklift проводить технічне обслуговування та виконує ремонт генераторів. Всю роботу виконують досвідчені майстри.',
                             parse_mode="HTML", reply_markup=key)
    if c.data == 'professional':
        key = types.InlineKeyboardMarkup(row_width=2)
        but_1 = types.InlineKeyboardButton(text="Записаться", callback_data="geophone")
        but_2 = types.InlineKeyboardButton(text="К другим курсам", callback_data="other_courses")
        key.add(but_1, but_2)
        await bot.send_photo(c.message.chat.id,
                             'https://certification.dp.ua/wp-content/uploads/2020/08/prof-prev-870x440.jpg',
                             caption='<b>Профессионал</b> - ₴8,500\n\nКурс «Профессионал» –  это курс который состоит из обучения основного курса, обучение на электроштабелере «Ричтрак» и погрузчике грузоподъемностью от 5 тонн. Курс профессионал можно пройти в г.Днепр. Этот курс даст возможность обучиться и работать на основных видах складской погрузочной техники и расширит ваши профессиональные навыки как  водителя погрузчика.\n\n<a href="https://certification.dp.ua/courses/professional/">Перейти к курсу</a>',
                             parse_mode="HTML", reply_markup=key)
    if c.data == 'electroshtabeller':
        key = types.InlineKeyboardMarkup(row_width=2)
        but_1 = types.InlineKeyboardButton(text="Записаться", callback_data="geophone")
        but_2 = types.InlineKeyboardButton(text="К другим курсам", callback_data="other_courses")
        key.add(but_1, but_2)
        await bot.send_photo(c.message.chat.id,
                             'https://certification.dp.ua/wp-content/uploads/2018/08/shtab2-1-1-870x440.jpg',
                             caption='<b>Электроштабеллер</b>\n\nЭлектроштабелер Ричтрак – вид складской техники, применяемый в основном в закрытых помещениях со стеллажной системой, с высотой работы более 6 метров. Основная задача Ричтрака – штабелеровка и подъем грузов на высоту и паллет с грузом на высокие стеллажи. Вилочный погрузчик так же может выполнять функции штабелирования, но все же он больше предназначен для перемещения грузов по складу и территории. В нашем центре Вы можете обучится на электроштабелере Ричтрак в г.Днепр, после основного курса обучения.\n\nПреимущества Ричтрака:\n – Эффективная работа на большой высоте\n – Производительность и скорость,точность укладки грузов\n – Выдвижная мачта ,обеспечивающая манёвренность в тесном пространстве\n – Высокоэффективная работа при низком уровне затрат.\n\n<a href="https://certification.dp.ua/courses/electroshtabeler/">Перейти к курсу</a>',
                             parse_mode="HTML", reply_markup=key)
    if c.data == 'richtrack':
        key = types.InlineKeyboardMarkup(row_width=2)
        but_1 = types.InlineKeyboardButton(text="Записаться", callback_data="geophone")
        but_2 = types.InlineKeyboardButton(text="К другим курсам", callback_data="other_courses")
        key.add(but_1, but_2)
        await bot.send_photo(c.message.chat.id,
                             'https://certification.dp.ua/wp-content/uploads/2018/08/shtab2-870x440.jpg',
                             caption='<b>Ричтрак</b>- ₴3,500\n\nЭлектроштабелер Ричтрак – вид складской техники, применяемый в основном в закрытых помещениях со стеллажной системой, с высотой работы более 6 метров. Основная задача Ричтрака – штабелеровка и подъем грузов на высоту и паллет с грузом на высокие стеллажи. Вилочный погрузчик так же может выполнять функции штабелирования, но все же он больше предназначен для перемещения грузов по складу и территории. В нашем центре Вы можете обучится на электроштабелере Ричтрак в г.Днепр, после основного курса обучения.\n\nПреимущества Ричтрака:\n – Эффективная работа на большой высоте\n – Производительность и скорость,точность укладки грузов\n – Выдвижная мачта ,обеспечивающая манёвренность в тесном пространстве\n – Высокоэффективная работа при низком уровне затрат.\n\n<a href="https://certification.dp.ua/courses/richtrack/">Перейти к курсу</a>',
                             parse_mode="HTML", reply_markup=key)
    if c.data == 'reattestat':
        key = types.InlineKeyboardMarkup(row_width=2)
        but_1 = types.InlineKeyboardButton(text="Записаться", callback_data="geophone")
        but_2 = types.InlineKeyboardButton(text="К другим курсам", callback_data="other_courses")
        key.add(but_1, but_2)
        await bot.send_photo(c.message.chat.id,
                             'https://certification.dp.ua/wp-content/uploads/2020/11/workers.jpg',
                             caption='<b>Переаттестация</b> - ₴350\n\nПредлагаем услугу переаттестации и аттестации уже опытных водителей погрузчиков. Процесс переаттестации:\n Практическая часть вождение на вилочном погрузчике.\n\nСрок готовности документации от 2 до 4-х рабочих дней. Документы необходимые для переаттестации:\n 1. Удостоверение “Водитель погрузчика”\n 2. Копии паспорта.\n 3. Копии идентификационного кода.\n\n<a href="https://certification.dp.ua/courses/pereattestacia/">Перейти к курсу</a>',
                             parse_mode="HTML", reply_markup=key)
    if c.data == 'forklift_5t':
        key = types.InlineKeyboardMarkup(row_width=2)
        but_1 = types.InlineKeyboardButton(text="Записаться", callback_data="geophone")
        but_2 = types.InlineKeyboardButton(text="К другим курсам", callback_data="other_courses")
        key.add(but_1, but_2)
        await bot.send_photo(c.message.chat.id,
                             'https://certification.dp.ua/wp-content/uploads/2020/08/prof-prev-870x440.jpg',
                             caption='<b>Погрузчик грузоподъемностью 5 тонн</b> - ₴500\n\nВилочный погрузчик грузоподъемностью 5 тонн – надежная машина специального назначения для сладских хозяйств, производственных, сельскохозяйственных и других предприятий.\n\n<a href="https://certification.dp.ua/courses/5-ton/">Перейти к курсу</a>',
                             parse_mode="HTML", reply_markup=key)
    if c.data == 'professional_gens':
        key = types.InlineKeyboardMarkup(row_width=3)
        but_1 = types.InlineKeyboardButton(text="←", callback_data="prev_prof")
        but_2 = types.InlineKeyboardButton(text="1/3", callback_data="1")
        but_3 = types.InlineKeyboardButton(text="→", callback_data="next_prof")
        but_4 = types.InlineKeyboardButton(text="Консультація(лишити заявку)", callback_data="leave_contacts")
        key.add(but_1, but_2, but_3, but_4)
        await bot.send_photo(c.message.chat.id,
                             'https://pogruzchik.dp.ua/storage/preview/geemka.jpg',
                             caption='<b>Дизельний генератор (56 кВт) KKWC60GF</b>\n\nЦіна: 12700$\n\n<b>Кількість фаз: 3 фази, чотири дроти</b>\n<b>Максимальна потужність (кВт): 60/75</b>\n<b>Двигун: Weichai - WP4.1D66E200</b>\n<b>Об\'єм паливного бака (л): 90</b>\n<b>Витрати палива (г/кВт.г): 208</b>\n<b>Безперервний час роботи (г):</b> 11\n<b>Габаритні розміри ДхШхВ (мм):</b> 2200*900*1500\n<b>Тип пального:</b> Дизель\n<b>Напруга (В):</b> 400/230\n<b>Номінальна потужність (кВт):</b> 56/70\n<b>Охолодження:</b> Водяне\n<b>Вага (кг):</b> 960\n<b>Рівень шуму (Дб):</b> 72/7\n<b>Рівень захисту:</b> IP 22\n<b>Об\'єм баку мастила (л):</b> 14\n\n<a href="https://pogruzchik.dp.ua/generator_item/geemka-kkwc60gf">Детальніше</a>',
                             parse_mode="HTML", reply_markup=key)
    if c.data == 'pobut_gens':
        key = types.InlineKeyboardMarkup(row_width=3)
        but_1 = types.InlineKeyboardButton(text="←", callback_data="prev_pobut")
        but_2 = types.InlineKeyboardButton(text="1/5", callback_data="1")
        but_3 = types.InlineKeyboardButton(text="→", callback_data="next_pobut")
        but_4 = types.InlineKeyboardButton(text="Консультація(лишити заявку)", callback_data="leave_contacts")
        key.add(but_1, but_2, but_3, but_4)
        await bot.send_photo(c.message.chat.id,
                             'https://pogruzchik.dp.ua/storage/preview/DG7000.jpg',
                             caption='<b>Дизельний генератор Newland DG7000</b>\n\nЦіна: 1370$\n\n<b>Кількість фаз:</b> 1\n<b>Максимальна потужність (кВт):</b> 5.5\n<b>Двигун:</b> 188F\n<b>Об\'єм паливного бака (л):</b> 12.5\n<b>Габаритні розміри ДхШхВ (мм):</b> 740*490*670\n<b>Тип пального:</b> Дизель\n<b>Напруга (В):</b> 220V/50Hz\n<b>Номінальна потужність (кВт):</b> 5\n<b>Охолодження:</b> Повітряне\n<b>Вага (кг):</b> 105\n\n<a href=\"https://pogruzchik.dp.ua/generator_item/newland-dg7000\">Детальніше</a>',
                             parse_mode="HTML", reply_markup=key)
    if c.data == 'diesel_gens':
        key = types.InlineKeyboardMarkup(row_width=3)
        but_1 = types.InlineKeyboardButton(text="←", callback_data="prev_diesel")
        but_2 = types.InlineKeyboardButton(text="1/2", callback_data="1")
        but_3 = types.InlineKeyboardButton(text="→", callback_data="next_diesel")
        but_4 = types.InlineKeyboardButton(text="Консультація(лишити заявку)", callback_data="leave_contacts")
        key.add(but_1, but_2, but_3, but_4)
        await bot.send_photo(c.message.chat.id,
                             'https://pogruzchik.dp.ua/storage/preview/DG7000.jpg',
                             caption='<b>Дизельний генератор Newland DG7000</b>\n\nЦіна: 1370$\n\n<b>Кількість фаз:</b> 1\n<b>Максимальна потужність (кВт):</b> 5.5\n<b>Двигун:</b> 188F\n<b>Об\'єм паливного бака (л):</b> 12.5\n<b>Габаритні розміри ДхШхВ (мм):</b> 740*490*670\n<b>Тип пального:</b> Дизель\n<b>Напруга (В):</b> 220V/50Hz\n<b>Номінальна потужність (кВт):</b> 5\n<b>Охолодження:</b> Повітряне\n<b>Вага (кг):</b> 105\n\n<a href=\"https://pogruzchik.dp.ua/generator_item/newland-dg7000\">Детальніше</a>',
                             parse_mode="HTML", reply_markup=key)
    if c.data == 'fuel_gens':
        key = types.InlineKeyboardMarkup(row_width=3)
        but_1 = types.InlineKeyboardButton(text="←", callback_data="prev_fuel")
        but_2 = types.InlineKeyboardButton(text="1/3", callback_data="1")
        but_3 = types.InlineKeyboardButton(text="→", callback_data="next_fuel")
        but_4 = types.InlineKeyboardButton(text="Консультація(лишити заявку)", callback_data="leave_contacts")
        key.add(but_1, but_2, but_3, but_4)
        await bot.send_photo(c.message.chat.id,
                             'https://pogruzchik.dp.ua/storage/preview/NL3000.jpg',
                             caption='<b>Бензиновий генератор Newland NL3000</b>\n\nЦіна: 540$\n\n<b>Кількість фаз:</b> 1\n<b>Максимальна потужність (кВт):</b> 2.6\n<b>Двигун:</b> 170F\n<b>Об\'єм паливного бака (л):</b> 15\n<b>Габаритні розміри ДхШхВ (мм):</b> 690*525*550\n<b>Тип пального:</b> Бензин\n<b>Напруга (В):</b> 220V/50hz\n<b>Номінальна потужність (кВт):</b> 3\n<b>Охолодження:</b> Повітряне\n<b>Вага (кг):</b> 40\n\n<a href=\"https://pogruzchik.dp.ua/generator_item/newland-nl3000\">Детальніше</a>',
                             parse_mode="HTML", reply_markup=key)
    if c.data == 'all_gens':
        key = types.InlineKeyboardMarkup(row_width=3)
        but_1 = types.InlineKeyboardButton(text="←", callback_data="prev_all")
        but_2 = types.InlineKeyboardButton(text="1/8", callback_data="1")
        but_3 = types.InlineKeyboardButton(text="→", callback_data="next_all")
        but_4 = types.InlineKeyboardButton(text="Консультація(лишити заявку)", callback_data="leave_contacts")
        key.add(but_1, but_2, but_3, but_4)
        await bot.send_photo(c.message.chat.id,
                             'https://pogruzchik.dp.ua/storage/preview/DG7000.jpg',
                             caption='<b>Дизельний генератор Newland DG7000</b>\n\nЦіна: 1370$\n\n<b>Кількість фаз:</b> 1\n<b>Максимальна потужність (кВт):</b> 5.5\n<b>Двигун:</b> 188F\n<b>Об\'єм паливного бака (л):</b> 12.5\n<b>Габаритні розміри ДхШхВ (мм):</b> 740*490*670\n<b>Тип пального:</b> Дизель\n<b>Напруга (В):</b> 220V/50Hz\n<b>Номінальна потужність (кВт):</b> 5\n<b>Охолодження:</b> Повітряне\n<b>Вага (кг):</b> 105\n\n<a href=\"https://pogruzchik.dp.ua/generator_item/newland-dg7000\">Детальніше</a>',
                             parse_mode="HTML", reply_markup=key)
    if c.data == 'geophone':
        await geophone(c.message)
    if c.data == 'leave_contacts':
        await geophone(c.message)
    if c.data == 'next_prof':
        item_num = str(int(c.message.reply_markup.inline_keyboard[0][1].callback_data)+1)
        if int(item_num) > 3:
            item_num = '1'
        await swiper_next_prof(c.message, item_num)
    if c.data == 'prev_prof':
        item_num = str(int(c.message.reply_markup.inline_keyboard[0][1].callback_data)-1)
        if int(item_num) < 1:
            item_num = '3'
        await swiper_prev_prof(c.message, item_num)
    if c.data == 'next_pobut':
        item_num = str(int(c.message.reply_markup.inline_keyboard[0][1].callback_data)+1)
        if int(item_num) > 5:
            item_num = '1'
        await swiper_next_pobut(c.message, item_num)
    if c.data == 'prev_pobut':
        item_num = str(int(c.message.reply_markup.inline_keyboard[0][1].callback_data)-1)
        if int(item_num) < 1:
            item_num = '5'
        await swiper_prev_pobut(c.message, item_num)
    if c.data == 'next_diesel':
        item_num = str(int(c.message.reply_markup.inline_keyboard[0][1].callback_data)+1)
        if int(item_num) > 2:
            item_num = '1'
        await swiper_next_diesel(c.message, item_num)
    if c.data == 'prev_diesel':
        item_num = str(int(c.message.reply_markup.inline_keyboard[0][1].callback_data)-1)
        if int(item_num) < 1:
            item_num = '2'
        await swiper_prev_diesel(c.message, item_num)
    if c.data == 'next_fuel':
        item_num = str(int(c.message.reply_markup.inline_keyboard[0][1].callback_data)+1)
        if int(item_num) > 3:
            item_num = '1'
        await swiper_next_fuel(c.message, item_num)
    if c.data == 'prev_fuel':
        item_num = str(int(c.message.reply_markup.inline_keyboard[0][1].callback_data)-1)
        if int(item_num) < 1:
            item_num = '3'
        await swiper_prev_fuel(c.message, item_num)
    if c.data == 'next_all':
        item_num = str(int(c.message.reply_markup.inline_keyboard[0][1].callback_data)+1)
        if int(item_num) > 8:
            item_num = '1'
        await swiper_next_all(c.message, item_num)
    if c.data == 'prev_all':
        item_num = str(int(c.message.reply_markup.inline_keyboard[0][1].callback_data)-1)
        if int(item_num) < 1:
            item_num = '8'
        await swiper_prev_all(c.message, item_num)
    if c.data == 'other_courses':
        await courses_list(c.message)


async def geophone(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_phone = types.KeyboardButton(text="Надіслати номер телефону", request_contact=True)
    button_back = types.KeyboardButton(text="До головного меню")
    keyboard.add(button_phone, button_back)
    await bot.send_message(message.chat.id, "Натисніть кнопку 'Надіслати номер телефону' і ми невдовзі зателефонуємо Вам",
                           reply_markup=keyboard)


async def geophone_course(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_phone = types.KeyboardButton(text="Отправить номер телефона", request_contact=True)
    button_back = types.KeyboardButton(text="В главное меню")
    keyboard.add(button_phone, button_back)
    if 'Основной курс' in message.caption:
        await bot.send_message(message.chat.id,
                               "Нажмите на кнопку 'Отправить номер телефона' и мы вскоре свяжемся с Вами для записи на Основной курс",
                               reply_markup=keyboard)
    elif 'Профессионал' in message.caption:
        await bot.send_message(message.chat.id,
                               "Нажмите на кнопку 'Отправить номер телефона' и мы вскоре свяжемся с Вами для записи на курс Профессионал",
                               reply_markup=keyboard)
    elif 'Электроштабеллер' in message.caption:
        await bot.send_message(message.chat.id,
                               "Нажмите на кнопку 'Отправить номер телефона' и мы вскоре свяжемся с Вами для записи на курс Электроштабеллер",
                               reply_markup=keyboard)
    elif 'Ричтрак' in message.caption:
        await bot.send_message(message.chat.id,
                               "Нажмите на кнопку 'Отправить номер телефона' и мы вскоре свяжемся с Вами для записи на курс Ричтрак",
                               reply_markup=keyboard)
    elif 'Переаттестация' in message.caption:
        await bot.send_message(message.chat.id,
                               "Нажмите на кнопку 'Отправить номер телефона' и мы вскоре свяжемся с Вами для записи на курс Переаттестация",
                               reply_markup=keyboard)
    elif 'Погрузчик 5 тонн' in message.caption:
        await bot.send_message(message.chat.id,
                               "Нажмите на кнопку 'Отправить номер телефона' и мы вскоре свяжемся с Вами для записи на курс Погрузчик 5 тонн",
                               reply_markup=keyboard)


async def main_menu(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*[types.KeyboardButton(name) for name in ['Генератори', 'Послуги']])
    keyboard.add(*[types.KeyboardButton(name) for name in ['FAQ', 'Лишити заявку']])
    await bot.send_message(message.chat.id,
                           'Вітаємо, оберіть один з розділів, або натисніть "Лишити заявку" і наш оператор зателефонує Вам.',
                           reply_markup=keyboard)


@dp.message_handler(content_types=['contact'])
async def read_contact_phone(message):
    send_email(message.contact.first_name, message.contact.last_name, message.contact.phone_number, message.reply_to_message.text)



def send_email(name, surname, phone, message_text):
    import smtplib

    FROM = 'tester.testupwork@gmail.com'
    TO = ['fluffko@gmail.com']
    # if 'Основной курс' in message_text
    if 'Основной курс' in message_text:
        SUBJECT = 'Запись на Основной курс через Telegram'
    elif 'Профессионал' in message_text:
        SUBJECT = 'Запись на курс Профессионал через Telegram'
    elif 'Электроштабеллер' in message_text:
        SUBJECT = 'Запись на курс Электроштабеллер через Telegram'
    elif 'Ричтрак' in message_text:
        SUBJECT = 'Запись на курс Ричтрак через Telegram'
    elif 'Переаттестация' in message_text:
        SUBJECT = 'Запись на курс Переаттестация через Telegram'
    elif 'Погрузчик 5 тонн' in message_text:
        SUBJECT = 'Запись на курс Погрузчик 5 тонн через Telegram'
    else:
        SUBJECT = 'Заявка на дзвінок через Telegram'
    TEXT = 'Ім`я: ' + name + ' ' + surname + '\nТелефон: ' + phone

    # Prepare actual message
    message = """From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login('tester.testupwork@gmail.com', 'ztyhkytkicvvjfjf')
    server.sendmail(FROM, TO, message.encode('utf-8'))
    server.close()
    print('successfully sent the mail')


if __name__ == '__main__':
    executor.start_polling(dp)
