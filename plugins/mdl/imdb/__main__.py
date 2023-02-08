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
    data, image = await search_(name)
    #os.remove(THUMB_PATH)
    if not image:
        await message.edit(
        data,
        disable_web_page_preview=True,
        parse_mode=enums.ParseMode.HTML
    )
    else:
        try:
            id = SmartDL(image, THUMB_PATH, progress_bar=False)
            id.start()
            await message.client.send_photo(
            chat_id=message.chat.id,
            photo=id.get_dest(),
            caption=data,
            parse_mode=enums.ParseMode.HTML
        )
            await message.delete()
            os.remove(id.get_dest())
        except:
            await message.edit(
        description,
        disable_web_page_preview=True,
        parse_mode=enums.ParseMode.HTML
    )
  
  
  
  
async def search_(name):
    imdb = Cinemagoer()
    try:
        if "tt" in name:
            data = imdb.get_movie(name[2:]).data
        else:
            id = imdb.search_movie(name)[0].movieID
            data = imdb.get_movie(id).data
        url = "https://www.imdb.com/title/tt" + data.get("imdbID")
        image_link = data.get("cover url").split("V1")[0] + "V1_720.jpg"
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
        description = f"""
<b>Title</b><a href='{image_link}'>🎬</a>: <code>{mov_name}</code>
<b>>Genres: </b><code>{genres}</code>
<b>Rating⭐: </b><code>{mov_rating}</code>
<b>Language: Hindi</b>
<b>Duration⏳: </b><code>{duration}</code>
<b>Director📽: </b><code>{director}</code>
<b>Stars🎭: </b><code>{stars}</code>
<b>Release Year📅: </b><code>{year}</code>
<b>Resolution : 480,720,1080</b>
<b>IMDB :</b> {url}
<b>Story Line : </b><em>{story_line}</em>"""
    
        return description, image_link
    
    except:
        return "Not Found", False
