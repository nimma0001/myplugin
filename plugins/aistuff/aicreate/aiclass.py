import asyncio
import requests
import json
import base64
import subprocess

class nimmadev:
        
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

    
    async def imageres(self, path, factor="4"):
        '''imporve image res'''
        r = requests.get("https://replicate.com/nightmareai/real-esrgan")
        cookie_token = r.cookies.get_dict()["replicate_anonymous_id"]
        url = "https://replicate.com/api/models/nightmareai/real-esrgan/versions/42fed1c4974146d4d2414e2be2c5277c7fcf05fcc3a73abf41610695738c1d7b/predictions"
        try:
            if "http" not in path:
                pixel_drain = subprocess.check_output(['curl', '-g', 'https://pixeldrain.com/api/file/', '--upload-file', path])
                pixel_link = json.loads(pixel_drain.decode().replace('\n', ''))['id'] 
                pixel_link = f"https://pixeldrain.com/api/file/{pixel_link}?download"
            else:
                pixel_link = path
        except FileNotFoundError:
            return False
        payload = json.dumps({
          "inputs": {
            "scale": factor,
            "face_enhance": False,
            "image": pixel_link
          }
        })
        headers = {
          'authority': 'replicate.com',
          'accept': 'application/json',
          'content-type': 'application/json',
          'origin': 'https://replicate.com',
          'Cookie': f'replicate_anonymous_id={cookie_token}'
        }
        try:
            response = requests.request("POST", url, headers=headers, data=payload)
            result = response.json().get("uuid", False)
            if result:
                proc = "non"
                while proc != "succeeded":
                    r = requests.get(f"https://replicate.com/api/models/nightmareai/real-esrgan/versions/42fed1c4974146d4d2414e2be2c5277c7fcf05fcc3a73abf41610695738c1d7b/predictions/{result}")
                    proc = r.json()["prediction"]["status"]
                else:
                    result = r.json()["prediction"]["output"]
        except BaseException as e:
            return str(e)
        
        return result
