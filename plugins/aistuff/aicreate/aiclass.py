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
            return str(e)
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
            return str(e)
            
        return response.json()["texts"]

    
    async def imageres(self, path):
        '''imporve image res'''
        url = "https://upscaler.zyro.com/v1/ai/image-upscaler"
        try:
            file = open(path, "rb").read()
        except FileNotFoundError:
            return False
        file_encode = base64.encodebytes(file).decode()
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
            return str(e)
            
        return base64.decodebytes(result)
    
