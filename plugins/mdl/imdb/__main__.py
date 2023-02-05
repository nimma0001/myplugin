from userge import userge, Message, config
from imdb import cinemagoer
from pyrogram import enums
import os
from pathlib import Path
from pySmartDL import SmartDL

THUMB_PATH = str(Path().cwd())

@userge.on_cmd("imdb", about="get movie from imdb")
async def imdb_(message: Message) -> None:
  """takes name and search with imdb"""
  name = message.input_str
  await message.edit(f"Seachring for : {name}")
