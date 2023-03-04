import os
import sys
import time
import urllib

import pydub as pydub
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options
import speech_recognition as sr
from selenium.webdriver.common.proxy import Proxy, ProxyType
import random
import string
import csv
import requests

url = 'https://acq.iemoapi.com/getProxyIp?lb=1&return_type=txt&protocol=http&num=1&tag=adam'

response = requests.get(url)


proxy = response.text
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument(f"--proxy-server={proxy}")
chrome_options.add_argument("--disable-notifications")
chrome_options.add_argument("--disable-popup-blocking")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-translate")
chrome_options.add_argument("--disable-client-side-phishing-detection")
chrome_options.add_argument("--disable-default-apps")
chrome_options.add_argument("--disable-hang-monitor")
chrome_options.add_argument("--disable-prompt-on-repost")
chrome_options.add_argument("--disable-renderer-backgrounding")
chrome_options.add_argument('--disable-logging')
#
driver = webdriver.Chrome()


print("Chrome Driver created.")
driver.maximize_window()

length = 10
random_email_str = ''.join(
    random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=length)).lower()
driver.get("https://www.facebook.com/")

# Origin Based MODAL ByPass
try:
    time.sleep(5)
    if driver.find_element(By.ID, 'cookie_banner_title'):
        driver.find_element(By.XPATH, '/html/body/div[3]/div[2]/div/div/div/div/div[3]/button[2]').click()
except:
    pass

# Open a new window
driver.execute_script("window.open('');")

# Switch to the new window and open new URL
driver.switch_to.window(driver.window_handles[1])
driver.get('https://yopmail.com')

try:
    time.sleep(5)
    # Different Origin Cookie Popup
    if driver.find_element(By.ID, 'cons-dialog'):
        driver.find_element(By.ID, 'accept').click()
except:
    pass

driver.find_element(By.NAME, 'login').send_keys(f'{random_email_str}')
driver.find_element(By.XPATH,
                    '/html/body/div/div[2]/main/div[3]/div/div[1]/div[2]/div/div/form/div/div/div[4]/button/i').click()

# Switching to FB tab
driver.switch_to.window(driver.window_handles[0])

create_acc = driver.find_element(By.XPATH,
                                 '/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[5]/a').click()

WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.NAME, 'websubmit')))

# Fill in the sign-up form
driver.find_element(By.NAME, 'firstname').send_keys("Ali")

driver.find_element(By.NAME, 'lastname').send_keys("Raza")
driver.find_element(By.NAME, 'reg_email__').send_keys(f"{random_email_str}@yopmail.com")
time.sleep(0.1)
driver.find_element(By.NAME, 'reg_email_confirmation__').send_keys(f"{random_email_str}@yopmail.com")

random_pass = ''.join(random.choices(string.ascii_lowercase, k=10))
driver.find_element(By.NAME, 'reg_passwd__').send_keys(f"{random_pass}")

# Select Birthday Field
bday = driver.find_element(By.NAME, 'birthday_day')
select_bday = Select(bday)
select_bday.select_by_value(f"{random.randint(1, 28)}")

# Select Month Field
month = driver.find_element(By.NAME, 'birthday_month')
select_month = Select(month)
select_month.select_by_value(f"{random.randint(1, 12)}")
# Select Year Field
year = driver.find_element(By.NAME, 'birthday_year')
select_year = Select(year)
random_no = random.randint(1980, 2000)
print(random_no)
select_year.select_by_value(f"{random_no}")

# Gender
male = driver.find_element(By.NAME, 'sex').click()

submit_btn = driver.find_element(By.NAME, 'websubmit').click()

WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,
                                                            '/html/body/div/div/div/div/div/div/div/div/div[2]/div/div/div/div[1]/div/div/div[1]/div/div/div/div/div/div/div/div[2]/div/div/div[2]/div/div/div')))

cont_btn = driver.find_element(By.XPATH,
                               '/html/body/div/div/div/div/div/div/div/div/div[2]/div/div/div/div[1]/div/div/div[1]/div/div/div/div/div/div/div/div[2]/div/div/div[2]/div/div/div')

cont_btn.click()

WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.TAG_NAME, 'iframe')))

frames = driver.find_elements(By.TAG_NAME, 'iframe')
driver.switch_to.frame(frames[0])

WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.TAG_NAME, 'iframe')))

innerFrame = driver.find_element(By.TAG_NAME, 'iframe')

driver.switch_to.frame(innerFrame)
print(innerFrame)
time.sleep(5)

driver.find_element(By.CLASS_NAME, 'recaptcha-checkbox-border').click()
time.sleep(5)

try:
    driver.find_element(By.CLASS_NAME,'recaptcha-checkbox-checkmark')
    driver.switch_to.default_content()
    driver.find_element(By.XPATH,'/html/body/div/div/div/div/div/div/div/div/div[2]/div/div/div/div[1]/div/div/div[1]/div/div/div/div/div/div/div/div[3]/div/div/div/div').click()
except:

    driver.switch_to.default_content()
    driver.switch_to.frame(driver.find_element(By.TAG_NAME, 'iframe'))
    driver.switch_to.frame(driver.find_element(By.XPATH, '/html/body/div[3]/div[4]/iframe'))
    driver.find_element(By.XPATH, '/html/body/div/div/div[3]/div[2]/div[1]/div[1]/div[2]/button').click()
    time.sleep(3)
    driver.find_element(By.XPATH, '/html/body/div/div/div[3]/div/button').click()
    time.sleep(2)


    # get the mp3 audio file
    src = driver.find_element(By.ID, "audio-source").get_attribute("src")
    path_to_mp3 = os.path.normpath(os.path.join(os.getcwd(), "sample.mp3"))
    path_to_wav = os.path.normpath(os.path.join(os.getcwd(), "sample.wav"))

    # download the mp3 audio file from the source
    urllib.request.urlretrieve(src, path_to_mp3)
    try:
        sound = pydub.AudioSegment.from_mp3(path_to_mp3)
        sound.export(path_to_wav, format="wav")
        sample_audio = sr.AudioFile(path_to_wav)
    except:
        sys.exit(
            "[ERR] Please run program as administrator or download ffmpeg manually, "
            "https://blog.gregzaal.com/how-to-install-ffmpeg-on-windows/"
        )
    time.sleep(2)

    r = sr.Recognizer()
    with sample_audio as source:
        audio = r.record(source)

    try:
        key = r.recognize_google(audio)
        print(f"[INFO] Recaptcha Passcode: {key}")
        driver.find_element(By.ID, "audio-response").send_keys(key.lower())
        driver.find_element(By.ID, "audio-response").send_keys(Keys.ENTER)


    except sr.UnknownValueError:
        print("Speech recognition could not understand audio")
        driver.quit()

    time.sleep(2)

    driver.switch_to.default_content()
    driver.find_element(By.XPATH,
                        '/html/body/div/div/div/div/div/div/div/div/div[2]/div/div/div/div[1]/div/div/div[1]/div/div/div/div/div/div/div/div[3]/div/div/div').click()
    driver.switch_to.default_content()

    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,
                                                                '/html/body/div/div/div/div/div/div/div/div/div[2]/div/div/div/div[1]/div/div/div[1]/div/div/div/div/div/div/div/div[3]/div/div[1]/span/div')))
time.sleep(10)
# RESEND CODE
driver.find_element(By.XPATH,
                    '/html/body/div/div/div/div/div/div/div/div/div[2]/div/div/div/div[1]/div/div/div[1]/div/div/div/div/div/div/div/div[3]/div/div[1]/span/div').click()

# Switch to YOPMAIL
driver.switch_to.window(driver.window_handles[1])

# Refresh Mail Page
time.sleep(10)
driver.find_element(By.XPATH, '/html/body/div[1]/div/main/div[2]/div[1]/div/div[1]/div[6]/button').click()
time.sleep(10)
# Get Code from Side bar
driver.switch_to.default_content()
driver.switch_to.frame(driver.find_element(By.XPATH, '/html/body/div[1]/div/main/div[2]/div[1]/div/div[3]/iframe[1]'))
code = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/button/div[2]')
code = code.text.split()
code = code[0]
# Switch to FB
driver.switch_to.window(driver.window_handles[0])
driver.find_element(By.XPATH,
                    '/html/body/div/div/div/div/div/div/div/div/div[2]/div/div/div/div[1]/div/div/div[1]/div/div/div/div/div/div/div/div[2]/div/label/div/div/input').send_keys(
    f'{code}')
driver.find_element(By.XPATH,
                    '/html/body/div/div/div/div/div/div/div/div/div[2]/div/div/div/div[1]/div/div/div[1]/div/div/div/div/div/div/div/div[4]/div/div[2]/div[1]').click()

print(random_email_str)
cookie = driver.get_cookies()

row = [cookie, f'{random_email_str}@yopmail.com', random_pass]

# name of csv file
filename = "account_logins.csv"

# writing to csv file
with open(filename, 'w') as csvfile:
    # creating a csv writer object
    csvwriter = csv.writer(csvfile)
    # writing the data rows
    csvwriter.writerows(row)

time.sleep(1800)

driver.quit()
