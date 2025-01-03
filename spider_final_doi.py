import os
import random
import traceback
from urllib import request
import requests
from fake_useragent import UserAgent
from urllib.parse import quote
from bs4 import BeautifulSoup
from selenium import webdriver
import re
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import time
from selenium.webdriver.common.keys import Keys
import pyautogui
from selenium.webdriver.common.by import By

output_text = ""

def create_folder(folder_path):
    try:
        # 使用 makedirs 创建文件夹，如果不存在则创建
        os.makedirs(folder_path)
        print(f"文件夹 '{folder_path}' 创建成功")
    except OSError as e:
        raise TypeError(f"创建文件夹 '{folder_path}' 失败: {e}")


def LinkDownload(url, big_theme, small_theme, flag):
    base_url = 'https://sci-hub.st/'
    User_Agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:121.0) Gecko/20100101 Firefox/121.0'
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Pragma": "no-cache",
        "Referer": "no-cache",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "cross-site",
        "Sec-Fetch-User": "?1",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": User_Agent,
        "sec-ch-ua": "\"Microsoft Edge\";v=\"117\", \"Not;A=Brand\";v=\"8\", \"Chromium\";v=\"117\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\""
    }
    req = request.Request(base_url + url, headers=headers)
    html = request.urlopen(req, timeout=10000)
    # print('\n响应结果是：', html)
    print('访问的地址是：', html.url)
    soup = BeautifulSoup(html.read().decode(), features='lxml')
    link = soup.find_all(name='embed', attrs={"src": re.compile(r'(.*pdf.*)')})
    print(link)
    pdf_URL = link[-1].get('src')
    # try:
    #     soup = BeautifulSoup(html.read().decode(), features='lxml')
    #     link = soup.find_all(name='embed', attrs={"src": re.compile(r'(.+\.pdf)')})
    #     pdf_URL = link[-1].get('src')
    # except:
    #     print("解析失败！")
    #     return 0
    try:
        if "sci-hub" in pdf_URL:
            pdf_URL = "https:" + pdf_URL
        else:
            pdf_URL = "https://sci-hub.st" + pdf_URL
        print('PDF的地址是：', pdf_URL)
        PdfDownload(pdf_URL, big_theme, small_theme, flag)

    except:
        print("该文章为空")


def LinkDownload0(url, big_theme, flag):
    # 设置下载路径
    download_path = f"D:\study\Final Design\Python_code\Metagpt1_paper\data\{big_theme}"# 绝对路径，不能用相对路径
    #print(download_path)
    # 创建Firefox选项
    options = Options()
    # 创建Firefox配置文件
    profile = webdriver.FirefoxProfile()
    profile.set_preference("browser.download.folderList", 2)
    profile.set_preference("browser.download.dir", download_path)
    profile.set_preference("browser.download.manager.showWhenStarting", False)
    profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/pdf")
    # 将Firefox配置文件设置为选项的属性
    options.profile = profile
    # 创建Firefox WebDriver实例并应用选项
    driver = webdriver.Firefox(options=options)
    try:
        driver.get("https://www.sci-hub.ren/" + url)
        # time.sleep(10)
        driver.implicitly_wait(15)
        # 切换到iframe框架
        source = driver.page_source
        soup = BeautifulSoup(source, features='lxml')
        links0 = []
        for link in soup.find_all(id='pdf', attrs={"src": re.compile(r'pdf')}):
            links0.append(link.get('src'))
        # 找到下载按钮并点击
        driver.get(links0[0])
        download_button = driver.find_element(By.ID, "download")
        download_button.click()
        time.sleep(5)
        # driver.implicitly_wait(30)
        # download_button.send_keys(Keys.ENTER)
        pyautogui.hotkey("enter")  # enter键
        time.sleep(5)
        # download_button.send_keys(Keys.ENTER)
        print(f"file {url} download successful")
    except:
        # traceback.print_exc()

        print(f"file {url} download error")

    # 关闭浏览器
    driver.quit()


def PdfDownload0(pdf_url, big_theme, flag):
    # 设置下载路径
    download_path = f"D:\study\Final Design\Python_code\Metagpt1_paper\data\{big_theme}"# 绝对路径，不能用相对路径
    #print(download_path)
    # 创建Firefox选项
    options = Options()
    # 创建Firefox配置文件
    profile = webdriver.FirefoxProfile()
    profile.set_preference("browser.download.folderList", 2)
    profile.set_preference("browser.download.dir", download_path)
    profile.set_preference("browser.download.manager.showWhenStarting", False)
    profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/pdf")
    # 将Firefox配置文件设置为选项的属性
    options.profile = profile
    # 创建Firefox WebDriver实例并应用选项
    driver = webdriver.Firefox(options=options)
    try:
        driver.get(pdf_url)
        # time.sleep(10)
        driver.implicitly_wait(15)
        # 切换到iframe框架
        # 找到下载按钮并点击
        download_button = driver.find_element(By.ID, "download")
        download_button.click()
        time.sleep(5)
        pyautogui.hotkey("enter")  # enter键
        # download_button.send_keys(Keys.ENTER)
        # driver.implicitly_wait(30)
        # download_button.send_keys(Keys.ENTER)
        time.sleep(5)
        # download_button.send_keys(Keys.ENTER)
        print(f"file {pdf_url} download successful")
    except:
        print(f"file {pdf_url} download error")
    # 关闭浏览器
    driver.quit()


def PdfDownload(pdf_url, big_theme, small_theme, flag):
    User_Agent = UserAgent.firefox
    #User_Agent= 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.2210.91'
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Pragma": "no-cache",
        "Referer": "no-cache",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "cross-site",
        "Sec-Fetch-User": "?1",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": User_Agent,
        "sec-ch-ua": "\"Microsoft Edge\";v=\"117\", \"Not;A=Brand\";v=\"8\", \"Chromium\";v=\"117\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\""
    }
    proxies = {
        'https': 'https://127.0.0.1:33210',
        'http': 'http://127.0.0.1:33210'
    }
    opener = request.build_opener(request.ProxyHandler(proxies))
    request.install_opener(opener)
    # time.sleep(random.random() * 5)
    # req = request.Request(pdf_url, headers=headers)
    # html = request.urlopen(req, timeout=10000)
    # with open(f'data\{big_theme}\{small_theme}\{small_theme}_{flag}.pdf', 'wb') as f:
    #     f.write(html.read())
    # print(f"file {pdf_url} has been downloaded")
    try:
        time.sleep(random.random() * 5)
        req = request.Request(pdf_url, headers=headers)
        html = request.urlopen(req, timeout=10000)
        with open(f'data\{big_theme}\{small_theme}_{flag}.pdf', 'wb') as f:
            f.write(html.read())
        print(f"file {pdf_url} has been downloaded")
        time.sleep(random.random() * 5)
    except:
        print(f"file {pdf_url} download error")

def list_files_only(directory_path):  # 读取文件列表
    if os.path.isdir(directory_path):
        file_list = [
            f
            for f in os.listdir(directory_path)
            if os.path.isfile(os.path.join(directory_path, f))
        ]
        file_list = [file for file in file_list if ".pdf" in file]
        return file_list
    else:
        return f"{directory_path} is not a directory"

def crawler(big_theme, small_theme, flag_c):
    global output_text
    flag0 = 1
    try:
        create_folder(f"data\{big_theme}")
    except:
        pass
    flag1 = len(list_files_only(fr"data\{big_theme}"))/flag_c
    output_text += f"当前小标题文献有{flag1}篇 \n"
    if big_theme in small_theme:
        title = small_theme
    else:
        title = f'{small_theme} of {big_theme}'
        title = small_theme
    while flag1 <= 10 :
        driver = webdriver.Firefox()
        try:#改成自动生成关键词
            # 打开Firefox浏览器
            # 停留三秒
            driver.get("https://www.connectedpapers.com/search?q="
                       + quote(title) + f"&p={flag0}")

            time.sleep(10)
            driver.implicitly_wait(15)
            source = driver.page_source
            soup = BeautifulSoup(source, features='lxml')
            links = {"link": [], "pdf": []}
            for link in soup.find_all(name='a', attrs={"href": re.compile(r'pdf')}):
                links["pdf"].append(link.get('href'))
            for link in soup.find_all(name='a', attrs={"href": re.compile(r'doi')}):
                if link.get('href') not in links["pdf"]:
                    links["link"].append(link.get('href'))
            text = links["pdf"]
            output_text += f"{text} \n"
            text = links["link"]
            output_text += f"{text} \n"
            driver.quit()
            try:
                create_folder(f"data\{big_theme}")
            except:
                pass
            flag = 0
            for link in links["link"]:
                LinkDownload0(link, big_theme, flag)
                flag += 1
            for pdf in links["pdf"]:
                PdfDownload0(pdf, big_theme, flag)
                flag += 1
            flag0 += 1
            flag1 = len(list_files_only(f"data\{big_theme}"))/flag_c
        except:
            driver.quit()


#
# if __name__ == '__main__':
#     #
#     crawler("medical", "introduction")
#     # PdfDownload('https://arxiv.org/pdf/2002.00708.pdf', "microfluidics", "materials", 1)
#     # PdfDownload0("https://arxiv.org/pdf/1910.10045.pdf","exam","exam",1)

# 关闭浏览器
import os
import random
import traceback
from urllib import request
import requests
from fake_useragent import UserAgent
from urllib.parse import quote
from bs4 import BeautifulSoup
from selenium import webdriver
import re
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import time
from selenium.webdriver.common.keys import Keys
import pyautogui
from selenium.webdriver.common.by import By


def create_folder(folder_path):
    try:
        # 使用 makedirs 创建文件夹，如果不存在则创建
        os.makedirs(folder_path)
        print(f"文件夹 '{folder_path}' 创建成功")
    except OSError as e:
        print(f"创建文件夹 '{folder_path}' 失败: {e}")


def LinkDownload(url, big_theme, small_theme, flag):
    base_url = 'https://sci-hub.st/'
    User_Agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:121.0) Gecko/20100101 Firefox/121.0'
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Pragma": "no-cache",
        "Referer": "no-cache",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "cross-site",
        "Sec-Fetch-User": "?1",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": User_Agent,
        "sec-ch-ua": "\"Microsoft Edge\";v=\"117\", \"Not;A=Brand\";v=\"8\", \"Chromium\";v=\"117\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\""
    }
    req = request.Request(base_url + url, headers=headers)
    html = request.urlopen(req, timeout=10000)
    # print('\n响应结果是：', html)
    print('访问的地址是：', html.url)
    soup = BeautifulSoup(html.read().decode(), features='lxml')
    link = soup.find_all(name='embed', attrs={"src": re.compile(r'(.*pdf.*)')})
    print(link)
    pdf_URL = link[-1].get('src')
    # try:
    #     soup = BeautifulSoup(html.read().decode(), features='lxml')
    #     link = soup.find_all(name='embed', attrs={"src": re.compile(r'(.+\.pdf)')})
    #     pdf_URL = link[-1].get('src')
    # except:
    #     print("解析失败！")
    #     return 0
    try:
        if "sci-hub" in pdf_URL:
            pdf_URL = "https:" + pdf_URL
        else:
            pdf_URL = "https://sci-hub.st" + pdf_URL
        print('PDF的地址是：', pdf_URL)
        PdfDownload(pdf_URL, big_theme, small_theme, flag)

    except:
        print("该文章为空")


def LinkDownload0(url, big_theme, flag):
    # 设置下载路径
    download_path = f"D:\study\Final Design\Python_code\Metagpt1_paper\data\{big_theme}"# 绝对路径，不能用相对路径
    #print(download_path)
    # 创建Firefox选项
    options = Options()
    # 创建Firefox配置文件
    profile = webdriver.FirefoxProfile()
    profile.set_preference("browser.download.folderList", 2)
    profile.set_preference("browser.download.dir", download_path)
    profile.set_preference("browser.download.manager.showWhenStarting", False)
    profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/pdf")
    # 将Firefox配置文件设置为选项的属性
    options.profile = profile
    # 创建Firefox WebDriver实例并应用选项
    driver = webdriver.Firefox(options=options)
    try:
        driver.get("https://www.sci-hub.ren/" + url)
        # time.sleep(10)
        driver.implicitly_wait(15)
        # 切换到iframe框架
        source = driver.page_source
        soup = BeautifulSoup(source, features='lxml')
        links0 = []
        for link in soup.find_all(id='pdf', attrs={"src": re.compile(r'pdf')}):
            links0.append(link.get('src'))
        # 找到下载按钮并点击
        driver.get(links0[0])
        download_button = driver.find_element(By.ID, "download")
        download_button.click()
        time.sleep(5)
        # driver.implicitly_wait(30)
        # download_button.send_keys(Keys.ENTER)
        pyautogui.hotkey("enter")  # enter键
        time.sleep(5)
        # download_button.send_keys(Keys.ENTER)
        print(f"file {url} download successful")
    except:
        # traceback.print_exc()

        print(f"file {url} download error")

    # 关闭浏览器
    driver.quit()


def PdfDownload0(pdf_url, big_theme, flag):
    # 设置下载路径
    download_path = f"D:\study\Final Design\Python_code\Metagpt1_paper\data\{big_theme}"# 绝对路径，不能用相对路径
    #print(download_path)
    # 创建Firefox选项
    options = Options()
    # 创建Firefox配置文件
    profile = webdriver.FirefoxProfile()
    profile.set_preference("browser.download.folderList", 2)
    profile.set_preference("browser.download.dir", download_path)
    profile.set_preference("browser.download.manager.showWhenStarting", False)
    profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/pdf")
    # 将Firefox配置文件设置为选项的属性
    options.profile = profile
    # 创建Firefox WebDriver实例并应用选项
    driver = webdriver.Firefox(options=options)
    try:
        driver.get(pdf_url)
        # time.sleep(10)
        driver.implicitly_wait(15)
        # 切换到iframe框架
        # 找到下载按钮并点击
        download_button = driver.find_element(By.ID, "download")
        download_button.click()
        time.sleep(5)
        pyautogui.hotkey("enter")  # enter键
        # download_button.send_keys(Keys.ENTER)
        # driver.implicitly_wait(30)
        # download_button.send_keys(Keys.ENTER)
        time.sleep(5)
        # download_button.send_keys(Keys.ENTER)
        print(f"file {pdf_url} download successful")
    except:
        print(f"file {pdf_url} download error")
    # 关闭浏览器
    driver.quit()


def PdfDownload(pdf_url, big_theme, small_theme, flag):
    User_Agent = UserAgent.firefox
    #User_Agent= 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.2210.91'
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Pragma": "no-cache",
        "Referer": "no-cache",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "cross-site",
        "Sec-Fetch-User": "?1",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": User_Agent,
        "sec-ch-ua": "\"Microsoft Edge\";v=\"117\", \"Not;A=Brand\";v=\"8\", \"Chromium\";v=\"117\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\""
    }
    proxies = {
        'https': 'https://127.0.0.1:33210',
        'http': 'http://127.0.0.1:33210'
    }
    opener = request.build_opener(request.ProxyHandler(proxies))
    request.install_opener(opener)
    # time.sleep(random.random() * 5)
    # req = request.Request(pdf_url, headers=headers)
    # html = request.urlopen(req, timeout=10000)
    # with open(f'data\{big_theme}\{small_theme}\{small_theme}_{flag}.pdf', 'wb') as f:
    #     f.write(html.read())
    # print(f"file {pdf_url} has been downloaded")
    try:
        time.sleep(random.random() * 5)
        req = request.Request(pdf_url, headers=headers)
        html = request.urlopen(req, timeout=10000)
        with open(f'data\{big_theme}\{small_theme}_{flag}.pdf', 'wb') as f:
            f.write(html.read())
        print(f"file {pdf_url} has been downloaded")
        time.sleep(random.random() * 5)
    except:
        print(f"file {pdf_url} download error")

def list_files_only(directory_path):  # 读取文件列表
    if os.path.isdir(directory_path):
        file_list = [
            f
            for f in os.listdir(directory_path)
            if os.path.isfile(os.path.join(directory_path, f))
        ]
        file_list = [file for file in file_list if ".pdf" in file]
        return file_list
    else:
        return f"{directory_path} is not a directory"

def crawler(big_theme, small_theme, flag_c):
    flag0 = 1
    create_folder(f"data/{big_theme}")
    flag1 = len(list_files_only(fr"data\{big_theme}"))/flag_c
    print(f"当前小标题文献有{flag1}篇")
    while flag1 <= 10 :
        driver = webdriver.Firefox()
        try:#改成自动生成关键词
            # 打开Firefox浏览器
            if big_theme in small_theme:

                title = small_theme
            else:
                title = f'{small_theme} of {big_theme}'
                title = small_theme
            # 停留三秒
            driver.get("https://www.connectedpapers.com/search?q="
                       + quote(title) + f"&p={flag0}")

            time.sleep(10)
            driver.implicitly_wait(15)
            source = driver.page_source
            soup = BeautifulSoup(source, features='lxml')
            links = {"link": [], "pdf": []}
            for link in soup.find_all(name='a', attrs={"href": re.compile(r'pdf')}):
                links["pdf"].append(link.get('href'))
            for link in soup.find_all(name='a', attrs={"href": re.compile(r'doi')}):
                if link.get('href') not in links["pdf"]:
                    links["link"].append(link.get('href'))
            print(links["pdf"])
            print(links["link"])
            driver.quit()
            create_folder(f"data/{big_theme}")
            flag = 0
            for link in links["link"]:
                LinkDownload0(link, big_theme, flag)
                flag += 1
            for pdf in links["pdf"]:
                PdfDownload0(pdf, big_theme, flag)
                flag += 1
            flag0 += 1
            flag1 = len(list_files_only(f"data\{big_theme}"))
        except:
            driver.quit()

# 已删除small_theme
#
# if __name__ == '__main__':
#     #
#     crawler("medical", "introduction")
#     # PdfDownload('https://arxiv.org/pdf/2002.00708.pdf', "microfluidics", "materials", 1)
#     # PdfDownload0("https://arxiv.org/pdf/1910.10045.pdf","exam","exam",1)

# 关闭浏览器
