from pathlib import Path


# -------------------------- Telegram --------------------------

# https://my.telegram.org
API_ID = 167221
API_HASH = 'd5b7611fbfe69992793d5652446c0e95'
PHONE = '+380960699699'
# Your tg channel. Example: https://t.me/povestkin_kr
CHANNEL = 'contest'

# -------------------------- Вконтакте --------------------------

REPOST_VK = True
VK_ACCESS_TOKEN = ''
VK_GROUP_ID = 123456789

# -------------------------- Instagram --------------------------

REPOST_INST = True
PROXY = '192.177.161.145:64112:E8w3dfDk:5WhCCFFu'
INST_LOGIN = 'povestki.kr'
INST_PASSWORD = 'Boss2329d'

# -------------------------- Не разбираешься - не трогай! --------------------------

BASE_DIR = Path(__file__).parent
FILES_DIR = BASE_DIR.joinpath('files')
LOGS_DIR = BASE_DIR.joinpath('logs')

PROXY = PROXY or None
VK_ACCESS_TOKEN = VK_ACCESS_TOKEN or None

paths = [
    FILES_DIR,
    LOGS_DIR,
]

for path in paths:
    path.mkdir(exist_ok=True)
