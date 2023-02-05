from userge import userge, Message, config
from imdb import Cinemagoer
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

  
  
  
  
async def search_(name):
    imdb = Cinemagoer()
    try:
        if "tt" in name:
          data = imdb.get_movie(name[2:]).data
        else:
          data = imdb.search_movie(name)
        url = data.url
        image_link = data.thumbnail
        mov_name = data.get("title")
        genres = ", ".join(bb.get("genres"))
        mov_rating = data.get("rating")
        duration = data.get("runtimes")
        director = data.get("director")[0].data.get("name")
        cast = ([x.get("name") for x in bb.get("cast")][:4]) if len([x.get("name") for x in bb.get("cast")]) > 5 else [x.get("name") for x in bb.get("cast")]
        stars = ", ".join(cast)
        year = data.get("original air date")
        info = data.get("plot outline")
        story_line = (info[:95] + '...') if len(info) > 75 else info
     
    
    except:
        return "Not Found"
