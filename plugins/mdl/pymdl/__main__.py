from userge import userge, Message, config
import PyMDL
from pyrogram import enums
import urllib.request
import os

THUMB_PATH = config.Dynamic.DOWN_PATH + "imdb_thumb.jpg"


@userge.on_cmd("mdl", about="get movie from mdl")
async def first_command(message: Message) -> None:
    """ this thing will be used as command doc string """
    name = message.input_str
    await message.edit(f"Seachring for : {name}")
    data, image = await search_(name)
    if os.path.exists(THUMB_PATH):
        os.remove(THUMB_PATH)
        fb = open(THUMB_PATH,'wb')
        fb.write(urllib.request.urlopen(image).read())
        fb.close()
        await message.client.send_photo(
            chat_id=message.chat.id,
            photo=THUMB_PATH,
            caption=data,
            parse_mode=enums.ParseMode.HTML
        )
        await message.delete()
async def search_(name):
    try:
        data = PyMDL.search(name).get(0)
        url = data.url
        image_link = data.thumbnail
        mov_name = data.title
        genres = data.genre
        mov_rating = data.ratings
        duration = data.duration
        director = data.director
        stars = ", ".join(data.casts)
        year = data.date
        info = data.synopsis
        story_line = (info[:95] + '...') if len(info) > 75 else indo
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
<b>Story Line : </b><em>{story_line}</em>
<b>Available On : 👇👇👇👇 </b>"""
    
        return description, image_link
    except:
        return "Not Found"
