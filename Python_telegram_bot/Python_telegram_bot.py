import telebot # импорт библиотеки для телеги
import pyowm #импорт библиотеки погоды
from pyowm.utils.config import get_default_config # импорт конфига для языков


bot = telebot.TeleBot('Тут нужно указать API бота') # API для бота
@bot.message_handler(content_types=['text']) 
def send_echo(message):
    # запись данных о погоде
    config_dict = get_default_config()
    config_dict['language'] = 'ru'  # your language here
    owm = pyowm.OWM('594549d1efa72beefda55cc2acbe9428', config_dict)
    mgr = owm.weather_manager()
    observation = mgr.weather_at_place(message.text)
    w = observation.weather.detailed_status
    temp_dict_celsius = observation.weather.temperature('celsius')['temp']
    wind_dict_in_meters_per_sec = observation.weather.wind()['speed']
    # ответ бота
    answer = 'В городе '+ message.text+' сейчас '+ w + '\n'
    answer += 'Температура ' + str(round(temp_dict_celsius))+' градусов по Цельсию'+ '\n'
    answer += 'Скорость ветра '+str(wind_dict_in_meters_per_sec) + ' м/c.'+ '\n'
    if temp_dict_celsius<10:
        answer += 'Одевай тёплую ветровку и брюки!'
    elif temp_dict_celsius>=10 and temp_dict_celsius <=20:
        answer += 'Одевай лёгкую ветровку и лёгкие штаны!'
    elif temp_dict_celsius>20:
        answer += 'Одевай футболку и лёгкие брюки или шорты: на улице тепло!'

    bot.send_message(message.chat.id, answer)

bot.polling(none_stop=True)