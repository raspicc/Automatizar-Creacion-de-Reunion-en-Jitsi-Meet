from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.chrome.options import Options
from localizarPermitir import start_permitir

options = Options()
options.add_argument("--disable-extensions")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=options)
driver.get("https://meet.jit.si/")

name_meet = driver.find_element(by="xpath", value="//*[@id='enter_room_field']")
name_meet.send_keys("Labmatnano")
name_meet.send_keys(Keys.ENTER)

time.sleep(5)
start_permitir()



time.sleep(3)
name_user = driver.find_element(by="xpath", value="//*[@id='videoconference_page']/div[4]/div[1]/div/div/div[1]/div[1]/div/input")
name_user.send_keys("Creador de la Reunión")
name_user.send_keys(Keys.ENTER)


input("Presione cualquier tecla para cerrar el navegador...")
while True:
    pass
