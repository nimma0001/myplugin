import time
import sys
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller
import pyperclip

from userge import userge, Message, config
from pyrogram import enums
from ..download import url_download
from userge.utils import is_url


chromedriver_autoinstaller.install() 
driver = webdriver.Chrome()

@@userge.on_cmd("tor", about="download movie")
async def imdb_(message: Message) -> None:
  driver= webdriver.Chrome()
  driver.get(message.input_str)
  load_button = driver.find_element(By.CLASS_NAME, 'btn.my-btn-link.zip').click()
  await asyncio.sleep(3)
  copy_button = driver.find_element(By.CLASS_NAME, 'btn.copy-btn.btn-primary').click()
  url = pyperclip.paste()
  if is_url(url):
    try:
      path_, _ = await url_download(message, url)
    except ProcessCanceled:
            await message.canceled()
            return
    except Exception as e_e:  # pylint: disable=broad-except
        await message.err(str(e_e))
        return
    await message.replay(str(path_))

