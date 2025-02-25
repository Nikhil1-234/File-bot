# (©)Codexbotz
# Recode by @kang_culiknee


import logging
import os
from logging.handlers import RotatingFileHandler

# Bot token dari @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6531864524:AAFloVwfs1HBhAR4ij9uvFGYrOQ0Gn6KVFI")

# API ID Anda dari my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "22299340"))

# API Hash Anda dari my.telegram.org
API_HASH = os.environ.get("API_HASH", "09b09f3e2ff1306da4a19888f614d937")

# ID Channel Database
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1001896877147"))

# OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "5380609667"))

# NAMA OWNER
OWNER = os.environ.get("OWNER", "naruto_n4")

# Database
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://ns9136994H14CtuSoVnUUtS2@cluster0.7bozzb1.mongodb.net/?retryWrites=true&w=majority")

# Username CH & Group
CHANNEL = os.environ.get("CHANNEL", "vvslh_pro")
GROUP = os.environ.get("GROUP", "vvslh_pro")

# ID dari Channel Atau Group Untuk Wajib Subscribenya
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1001954599807"))
FORCE_SUB_GROUP = int(os.environ.get("FORCE_SUB_GROUP", "-1001504456678"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

# Pesan Awalan /start
START_MSG = os.environ.get(
    "START_MESSAGE",
    "<b>Hello {first}</b>\n\n<b>Saya dapat menyimpan file pribadi di Channel Tertentu dan pengguna lain dapat mengaksesnya dari link khusus.</b>",
)
try:
    ADMINS = [int(x) for x in (os.environ.get("ADMINS", "5380609667").split())]
except ValueError:
    raise Exception("Daftar Admin Anda tidak berisi User ID Telegram yang valid.")

# Pesan Saat Memaksa Subscribe
FORCE_MSG = os.environ.get(
    "FORCE_SUB_MESSAGE",
    "<b>Hello {first}\n\nAnda harus bergabung di Channel/Grup saya Terlebih dahulu untuk Melihat File yang saya Bagikan\n\nSilakan Join Ke Channel & Group Terlebih Dahulu</b>",
)

# Atur Teks Kustom Anda di sini, Simpan (None) untuk Menonaktifkan Teks Kustom
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

# Setel True jika Anda ingin Menonaktifkan tombol Bagikan Kiriman Saluran Anda
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == "True"

ADMINS.append(OWNER_ID)
ADMINS.append(5396158379)
ADMINS.append(1996472517)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(levelname)s] - %(name)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[
        RotatingFileHandler(LOG_FILE_NAME, maxBytes=50000000, backupCount=10),
        logging.StreamHandler(),
    ],
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
