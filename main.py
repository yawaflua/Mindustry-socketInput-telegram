 # in your server config socketInput should be default (localhost)


from datetime import datetime
import os
import sys
import logging
from aiogram import *
from aiogram.types import ContentType



BOT_TOKEN = ''
bot = Bot(token=BOT_TOKEN, parse_mode="HTML")
dp = Dispatcher(bot)

main_path = __file__.replace(os.path.basename(__file__), '')
with open(f'{main_path}/run_server.sh', 'r+') as file: fileShReplace = file.read(); file.close()
with open(f'{main_path}/run_server.sh', 'w+') as file: file.close()
with open(f'{main_path}/run_server.sh', 'r+') as file: file.write(fileShReplace.replace('echo "config socketInput true" | ', ''))
logging.basicConfig(level=logging.INFO)
logFormatter = logging.Formatter("%(asctime)s [%(threadName)-12.12s] %(message)s")
rootLogger = logging.getLogger()
consoleHandler = logging.StreamHandler()
consoleHandler.setFormatter(logFormatter)
rootLogger.addHandler(consoleHandler)
rootLogger.info("Start")

def server_connect(text):
    a = os.popen(f'echo "{text}" | nc 0.0.0.0 6859')
    os.popen('exit')
    return a

@dp.message_handler(content_types= ContentType.TEXT)
async def command(message: types.message):
    if not os.path.isfile(f'{main_path}/config/logs/copy-log.log'): file = open(f'{main_path}/config/logs/copy-log.log', 'x'); file.close()
    with open(f'{main_path}/config/logs/log-0.txt', 'r') as file:
        with open(f'{main_path}/config/logs/copy-log.log', 'r+') as file2: 
            file2.write(file.read())
            file2.close()
        file.close()
    with open(f'{main_path}/config/logs/log-0.txt', 'w+') as file:
            file.close()
    now = datetime.now()
    date_time = now.strftime("%m-%d-%Y %H:%M:%S")
    server_connect(message.text)
    rootLogger.info(message.text)
    await message.reply('Command entried!')
    with open(f'{main_path}/config/logs/log-0.txt', mode='r') as file:
        text = file.read().replace("<", '(').replace(">", ')').replace(f"[{date_time}]", '').replace('Received command socket connection: localhost/127.0.0.1:6859', '').replace('Lost command socket connection: localhost/127.0.0.1:6859', '').replace('[I]', '').encode('utf8')
        if len(text) > 4096:
            for x in range(0, len(text), 4096):
                await message.answer(text[x:x+4096].decode('utf8'))
        else:
            try:
                await message.answer(text.decode('utf8'))
            except:
                await message.answer(f'Server don`t reply.')
        with open(f'{main_path}/config/logs/log-0.txt', 'w+') as file:
            file.close()
        file.close()
    
    



try:
    executor.start_polling(dp, skip_updates=False)
except Exception:
    sys.exit()
