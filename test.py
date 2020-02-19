import os
import time
from selenium import webdriver

targetUrl = os.environ['TARGET_URL']
windowCount = os.environ['WINDOW_MAX_COUNT']
tabCount = os.environ['TAB_MAX_COUNT_PER_WINDOW']
sleepTime = os.environ['SLEEP_TIME_SEC']

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
for windowIndex in range(int(windowCount)):
    driver = webdriver.Chrome(options=options)
    driver.get(targetUrl)
    print(str(windowIndex + 1) + ' : 1', flush=True)
    for tabIndex in range(int(tabCount)-1):
        driver.execute_script("window.open('" + targetUrl + "');")
        print(str(windowIndex+1) + ' : ' + str(tabIndex+2), flush=True)
        time.sleep(float(sleepTime))

print('done', flush=True)
time.sleep(50000000)
