import time
import sys
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import geckodriver_autoinstaller
from selenium.webdriver.firefox.options import Options
import pyperclip

from userge import userge, Message, config
from pyrogram import enums
from ..download import url_download
from userge.utils import is_url

chrome_options = Options()
chrome_options.add_argument("--headless")
geckodriver_autoinstaller.install() 


@userge.on_cmd("tor", about="download movie")
async def imdb_(message: Message) -> None:
  driver = webdriver.Firefox(options=chrome_options)
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

