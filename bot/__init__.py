#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @Hillard_Har | @AlbertEinsteinTG

import os
import logging
import time

from logging.handlers import RotatingFileHandler

from .translation import Translation

#force sub config

FORCESUB_CHANNEL = os.environ.get("FORCESUB_CHANNEL", "BOTS_Infinity")

#Add photo to filter (infinity)

MASSAGE_PHOTO = os.environ.get("TEXT_MEG_PH", "https://telegra.ph/file/4759cfdc7db115d190b93.jpg")

# Change Accordingly While Deploying To A VPS
APP_ID = int(os.environ.get("APP_ID", "4626470"))

API_HASH = os.environ.get("API_HASH", "d0b545107dfacaccf94de87d9732c4f1")

AUTH_USER = os.environ.get("AUTH_USER", "1730447831")

BOT_TOKEN = os.environ.get("BOT_TOKEN")

DB_URI = os.environ.get("DB_URI")

USER_SESSION = os.environ.get("USER_SESSION")

BOT_NAME = os.environ.get("BOT_NAME", "Linker")

ADMIN_USERNAME = os.environ.get("ADMIN_USERNAME", "Ts_bots")

GROUP_USERNAME = os.environ.get("GROUP_USERNAME", "Ts_bots")

VERIFY = {}

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            "autofilterbot.txt",
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

start_uptime = time.time()


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
