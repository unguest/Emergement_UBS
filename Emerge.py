from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import NoSuchElementException
import time
from dotenv import load_dotenv
import os
import logging

logging.basicConfig(
    filename='emergement.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filemode='a'
)

load_dotenv()
USERNAME = os.getenv("MoodleUs", "USER")
PASSWORD = os.getenv("MoodlePa", "PASS")
SHADOW = os.getenv("MoodleSh", "False").lower() == "true"
STATUT = os.getenv("MoodleSt")

logging.info("Ouverture du navigateur Selenium.")

options = Options()
if SHADOW:
    options.add_argument('-headless')
service = Service(executable_path=f"{os.getcwd()}/geckodriver")
driver = webdriver.Firefox(options=options, service=service)

driver.get("https://moodle.univ-ubs.fr/")
time.sleep(0.5)

select_element = driver.find_element(By.ID, "idp")
dropdown = Select(select_element)
dropdown.select_by_visible_text("Université Bretagne Sud - UBS")

select_button = driver.find_element(By.XPATH, "//button[@type='submit' and contains(@class, 'btn-primary')]")
select_button.click()
time.sleep(1)

username_input = driver.find_element(By.ID, "username")
username_input.send_keys(USERNAME)

password_input = driver.find_element(By.ID, "password")
password_input.send_keys(PASSWORD)

login_button = driver.find_element(By.XPATH, "//span[text()='SE CONNECTER']/parent::button")
login_button.click()

try:
    error_message = driver.find_element(By.XPATH, "//*[contains(text(), 'Mauvais identifiant / mot de passe')]")
    print("[-] Mauvais Identifiant ou Mot de passe")
    logging.info("Mauvais Identifiant ou Mot de passe")
    if USERNAME == 'USER':
        print("[-] Créez le fichier .env pour y stocker vos identifiants (https://github.com/MTlyx/Emergement_UBS)")
    driver.quit()
    quit()
except NoSuchElementException:
    logging.warning("Connection réussi")
    print("[*] Connection réussi")

time.sleep(1)

course_url = "https://moodle.univ-ubs.fr/course/view.php?id=10731"
driver.get(course_url)

time.sleep(0.5)

attendance_url = "https://moodle.univ-ubs.fr/mod/attendance/view.php?id=433339"
driver.get(attendance_url)

time.sleep(0.5)

try:
    link_element = driver.find_element(By.XPATH, "//a[contains(text(), 'Envoyer le statut de présence')]")
    link_href = link_element.get_attribute("href")
    driver.get(link_href)
except NoSuchElementException:
    logging.warning("Impossible d'envoyer le statut, statut non présent encore")
    print("[*] Impossible d'envoyer le statut, statut non présent encore")
    driver.quit()
    quit()

time.sleep(1)

present_radio_button = driver.find_element(By.XPATH, f"//input[@type='radio' and @name='status'][following-sibling::span[text()='{STATUT}']]")
present_radio_button.click()

save_button = driver.find_element(By.XPATH, "//input[@type='submit' and @id='id_submitbutton']")
save_button.click()

logging.info("Statut envoyé avec succès")
print("[*] Statut envoyé avec succès")

time.sleep(4)
driver.quit()