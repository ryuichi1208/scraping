# coding: UTF-8
import requests
import time
import csv

from bs4 import BeautifulSoup
from urllib.parse import urljoin
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

# config
URL=""
USER=""
PASS=""

CONF_PATH="userinfo.txt"

def read_conf():
    with open(CONF_PATH, 'r') as f:
        reader = csv.reader(f)
        row = next(reader)
        global USER
        USER = row[1]
        row = next(reader)
        global PASS
        PASS = row[1]

# @param flg True:�֥饦�����̤���
def get_driver(flg):
    options = Options()
    options.set_headless(flg)
    driver = webdriver.Chrome()
    driver.get(URL)

    # USERID������
    driver.find_element_by_id("UserId").send_keys(USER)
    # �ѥ���ɤ�����
    element = driver.find_element_by_id("UserPassword")
    element.send_keys(PASS)

    # ������ܥ��󥯥�å�
    element.send_keys(Keys.ENTER)

    # �������ǧ���֤�Ȥ�
    time.sleep(10)

    # �ɥ饤�ФΥ�����
    driver.close()

read_conf()
get_driver(False)

