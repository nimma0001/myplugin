from userge import userge, Message, config
from pyrogram import enums
from pathlib import Path
from .aiclass import nimmadev
    
@userge.on_cmd("t2i", about={
    'header': "make image from text takes 1-2 min",
    'usage': "t2i gorilla on bike"})
async def t2i(message: Message) -> None:
    text = message.input_str
    await message.edit(
                        "wait 1-2 min genrating image",
                        disable_web_page_preview=True
                        )
    ai_app = nimmadev()
    response = await ai_app.text2img(text)
    if isinstance(response, list):
      for link in response:
        await message.client.send_document(
                                            chat_id=message.chat.id,
                                            document=f"https://img.craiyon.com/{link}"
                                          )
    elif isinstance(response, str):
        await message.edit(
                          response,
                          disable_web_page_preview=True
                          )
        
    else:
      await message.edit(
                        "Error Try Agin Later",
                        disable_web_page_preview=True
                        )
      
@userge.on_cmd("t2p", about={
    'header': "make paragraph from text twakes 10-40 sec",
    'usage': "t2p gorilla on bike"})
async def t2p(message: Message) -> None:
    text = message.input_str
    await message.edit(
                        "wait 10-40 sec genrating text",
                        disable_web_page_preview=True
                        )
    ai_app = nimmadev()
    response = await ai_app.text2para(text)
    if isinstance(response, list):
      for text in response:
        await message.client.send_message(
                                            chat_id=message.chat.id,
                                            text=f"{text}"
                                          )
    elif isinstance(response, str):
        await message.edit(
                          response,
                          disable_web_page_preview=True
                          )
        
    else:
      await message.edit(
                        "Too Small",
                        disable_web_page_preview=True
                        )
      
      
@userge.on_cmd("upscale", about={
    'header': "upscale the image takes 40-120 sec",
    'usage': "upscaled image_path"})
async def t2p(message: Message) -> None:
    image = message.filtered_input_str
    await message.edit(
                    "wait 1-2 min upscaling the image",
                    disable_web_page_preview=True
                    )
    ai_app = nimmadev()
    image_path = str(Path().cwd() / image)
    path_ = str(Path().cwd() / "upscaled.jpg")
    response = await ai_app.imageres(image_path)
    if isinstance(response, bytes):
      with open("upscaled.jpg", "wb") as p:
        p.write(response)
      await message.client.send_document(
                                          chat_id=message.chat.id,
                                          document=path_
                                        )
      
    elif isinstance(response, str):
      await message.edit(
                        response,
                        disable_web_page_preview=True
                        )
      
    else:
      await message.edit(
                        "File Not Found",
                        disable_web_page_preview=True
                        )
      
