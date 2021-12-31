from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

name = "Benjamin Bliss"
email = "bbliss@uoguelph.ca"
phone = "2262350542"
PATH = "C:\\Program Files (x86)\\chromedriver.exe"
ser = Service(PATH)
driver = webdriver.Chrome(service=ser)
#driver.maximize_window()
driver.get("https://uoguelph.eu.qualtrics.com/jfe/form/SV_4Ntfm8k1oXAPssm")

try:
    yes = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "QID3-1-label"))
    )
    yes.click()

    driver.find_element(By.ID, "NextButton").click()
except():
    print("'page 1' quit")
    driver.quit()

try:
    link = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Ontario COVID-19 Self-Assessment Tool"))
    )
    driver.find_element(By.ID, "NextButton").click()

except():
    print("'page 2' quit")
    driver.quit()

try:
    student = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "QID9-1-label"))
    )
    student.click()
    driver.find_element(By.ID, "NextButton").click()

except():
    print("'page 3' quit")
    driver.quit()

try:
    yes = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "QID11-1-label"))
    )
    yes.click()
    driver.find_element(By.ID, "NextButton").click()

except():
    print("'page 4' quit")
    driver.quit()

try:
    myself = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "QID12-1-label"))
    )
    myself.click()
    driver.find_element(By.ID, "NextButton").click()

except():
    print("'page 5' quit")
    driver.quit()

try:
    nameBox = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "QR~QID5"))
    )
    driver.find_element(By.ID, "QR~QID5").send_keys(name)
    driver.find_element(By.ID, "QR~QID7").send_keys(email)
    driver.find_element(By.ID, "QR~QID8").send_keys(phone)
    driver.find_element(By.ID, "NextButton").click()

except():
    print("'page 6' quit")
    driver.quit()

try:
    symptoms = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "QID23-2-label"))
    )
    symptoms.click()
    driver.find_element(By.ID, "NextButton").click()

except():
    print("'page 7' quit")
    driver.quit()

driver.quit()

