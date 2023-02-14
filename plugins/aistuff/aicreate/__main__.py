from userge import userge, Message, config
from pyrogram import enums
import asyncio
import requests
import json
import base64

class nimmadev:
    
    def __init__(self):
        pass
        
    async def text2img(self, text):
        '''convert text to img takes text as string'''
        url = "https://api.craiyon.com/draw"

        payload = json.dumps({
          "prompt": f"{text}",
          "version": "35s5hfwn9n78gb06",
          "token": None
        })
        headers = {
          'accept': 'application/json',
          'accept-language': 'en-GB,en;q=0.9,en-US;q=0.8',
          'content-type': 'application/json',
          'origin': 'https://www.craiyon.com',
          'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1660.12'
        }
        try:
            response = requests.request("POST", url, headers=headers, data=payload)
        except BaseException as e:
            return e
        return response.json().get("images", False)
    
    async def text2para(self, text):
        '''genrate text content based on text'''
        url = "https://backend.zyro.com/v1/ai/generate_texts"
        if len(text) < 4:
            return False
        payload = json.dumps({
          "prompt": f"{text}",
          "length": 130,
          "temperature": 0.9,
          "top_k": 90
        })
        headers = {
          'accept': 'application/json, text/plain, */*',
          'content-type': 'application/json'
        }
        try:
            response = requests.request("POST", url, headers=headers, data=payload)
        except BaseException as e:
            return e
            
        return response.json()["texts"]

    
    async def imageres(self, path):
        '''imporve image res'''
        url = "https://upscaler.zyro.com/v1/ai/image-upscaler"
        try:
            file = open(path, 'rb')
        except FileNotFoundError:
            return False
        file_read = file.read()
        file_encode = base64.encodebytes(file_read).decode()
        headers = {
                  'authority': 'upscaler.zyro.com',
                  'accept': '*/*',
                  'accept-language': 'en-GB,en;q=0.9,en-US;q=0.8',
                  'access-control-request-headers': 'content-type',
                  'access-control-request-method': 'POST',
                  'origin': 'https://zyro.com',
                  'referer': 'https://zyro.com/',
                  'sec-fetch-dest': 'empty',
                  'sec-fetch-mode': 'cors',
                  'sec-fetch-site': 'same-site',
                  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1660.12',
                  'Content-Type': 'application/json'
                }
        payload = json.dumps({
                              "image_data": f"data:image/jpeg;base64,{file_encode}"})
        try:
            response =  requests.request("POST", url, headers=headers, data=payload)
            result = response.json().get("upscaled", None).encode()
        except BaseException as e:
            return e
            
        return base64.decodebytes(result)
    
    
@userge.on_cmd("t2i", about={
    'header': "make image from text",
    'usage': "t2i gorilla on bike"})
async def t2i(message: Message) -> None:
    text = message.input_str
    ai_app = nimmadev()
    response = ai_app.text2img(text)
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
    'header': "make paragraph from text",
    'usage': "t2p gorilla on bike"})
async def t2p(message: Message) -> None:
    text = message.input_str
    ai_app = nimmadev()
    response = ai_app.text2para(text)
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
    'header': "upscale the image",
    'usage': "upscaled image_path"})
async def t2p(message: Message) -> None:
    image = message.input_str
    ai_app = nimmadev()
    response = ai_app.imageres(image)
    if isinstance(response, bytes):
      await message.client.send_document(
                                          chat_id=message.chat.id,
                                          document=response
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
      
