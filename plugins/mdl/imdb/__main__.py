from userge import userge, Message, config
from imdb import cinemagoer
from pyrogram import enums
import os
from pathlib import Path
from pySmartDL import SmartDL

THUMB_PATH = str(Path().cwd())

@userge.on_cmd("imdb", about="get movie from imdb")
