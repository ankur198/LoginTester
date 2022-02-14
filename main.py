# %%
import datetime
import os
import sys
import time
import dotenv
from ldapLogin import tryLdap
from jiraLogin import tryJira

dotenv.load_dotenv()

filePath = f'run/log.txt'
os.makedirs('run', exist_ok=True)

try:
    host = os.environ['host']
    port = os.environ['port']
    username = os.environ['username']
    password = os.environ['password']
    mode = os.environ['mode']
except Exception as e:
    print("Error: Configuration not set properly")
    print(e)
    sys.exit(-1)

config = {
    "host": host,
    "port": port,
    "username": username,
    "password": password,
    "mode": mode
}
# %%
print("Using config:", config)

# %%
while True:
    result = False
    if mode == 'ldap':
        result = tryLdap(host, port, username, password)
    elif mode == 'jira':
        result = tryJira(host, port, username, password)
        
    result = 'failed' if result is False else 'success'
    
    with open(filePath, 'a') as f:
        dataToWrite = f'{datetime.datetime.now().isoformat()}\t{result}'
        print(dataToWrite)
        f.write(f'{dataToWrite}\n')

    time.sleep(10)
# %%
