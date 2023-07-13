from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time
from dotenv import load_dotenv
import requests
import os

load_dotenv()

SHEETLY_URL = os.getenv("SHEETLY_URL")
BEAR = os.getenv("BEAR")

sheetly_headers = {
    "Authorization": BEAR,
}

chrome_drive_path = r"C:\Users\Zach\Desktop\chromedriver_win32\chromedriver.exe"

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options, service=Service(executable_path=chrome_drive_path, log_path="NUL"))

driver.get(
    "https://bloodmallet.com/chart/death_knight/frost/trinkets/castingpatchwerk")
all_trinkets = {}
character_trinkets = {}

accept_cookies = driver.find_element(By.CSS_SELECTOR, 'button[class="btn btn-primary"]')
accept_cookies.click()
time.sleep(2)
trinkets = driver.find_elements(By.CSS_SELECTOR, 'span[opacity="1"]')  # Finds the trinket names
time.sleep(1)
trinket_values = driver.find_elements(By.CSS_SELECTOR, 'text[data-z-index="1"]')  # Finds the trinket value at max level
time.sleep(1)
total_trinkets = len(trinkets)

for n in range(len(trinkets)):
    trinket_starting = total_trinkets + n
    character_trinkets[n] = {
        "Trinket Name": trinkets[n].text,
        "Trinket Value": trinket_values[trinket_starting].text,
    }

test_json = {
    "trinket": {
        "class": f"Deathknight",
        "toptrinket1": f"{character_trinkets[0]['Trinket Name']}",
        "value1": f"{character_trinkets[0]['Trinket Value']}",
        "toptrinket2": f"{character_trinkets[1]['Trinket Name']}",
        "value2": f"{character_trinkets[1]['Trinket Value']}",
        "toptrinket3": f"{character_trinkets[2]['Trinket Name']}",
        "value3": f"{character_trinkets[2]['Trinket Value']}",
        "toptrinket4": f"{character_trinkets[3]['Trinket Name']}",
        "value4": f"{character_trinkets[3]['Trinket Value']}",
        "toptrinket5": f"{character_trinkets[4]['Trinket Name']}",
        "value5": f"{character_trinkets[4]['Trinket Value']}",
        "toptrinket6": f"{character_trinkets[5]['Trinket Name']}",
        "value6": f"{character_trinkets[5]['Trinket Value']}",
        "toptrinket7": f"{character_trinkets[6]['Trinket Name']}",
        "value7": f"{character_trinkets[6]['Trinket Value']}",
        "toptrinket8": f"{character_trinkets[7]['Trinket Name']}",
        "value8": f"{character_trinkets[7]['Trinket Value']}",
    }
}

test_dk_json = {
    "trinket": {
        "deathknight": f"{character_trinkets[0]['Trinket Name']}",
        "dkvalue": f"{character_trinkets[0]['Trinket Value']}",
    }
}
print(f"{character_trinkets[0]['Trinket Name']}")
print((f"{character_trinkets[0]['Trinket Value']} {type(character_trinkets[0]['Trinket Value'])}"))


time.sleep(2)
response = requests.post(url=SHEETLY_URL, json=test_json, headers=sheetly_headers)
response.raise_for_status()
# print(character_trinkets)
print(response.text)
