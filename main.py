# %%
import datetime
import os
import time
from ldap3 import Server, Connection, ALL, NTLM

import dotenv

dotenv.load_dotenv()

filePath = f'run/{datetime.datetime.now().strftime("%d-%m-%Y-%H-%M-%S")}.txt'
os.makedirs('run', exist_ok=True)
# %%
server = Server(os.environ['host'], port=int(os.environ['port']), get_info=ALL)

# %%
while True:
    username = 'unknown'
    try:
        conn = Connection(
            server,
            user=os.environ['user'],
            password=os.environ['password'],
            auto_bind=True)
        username = conn.extend.standard.who_am_i()
        conn.unbind()
    except:
        username = 'unknown'

    with open(filePath, 'a') as f:
        dataToWrite = f'{datetime.datetime.now().isoformat()}\t{username}'
        print(dataToWrite)
        f.write(f'\n{dataToWrite}')

    time.sleep(10)
# %%
