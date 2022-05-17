from selenium import webdriver
import colorama
from colorama import Fore, Back, Style
import pyperclip
import sys


class Oxford_Definition:
    def __init__ (self, lc_link:str):
        print(Fore.RED + 'Chrome headless' + Fore.RESET)
        opt = webdriver.ChromeOptions()
        opt.add_argument("--window-size=1920,1080")
        opt.add_argument("--no-sandbox")
        opt.add_argument("--headless")
        #opt.add_argument("--disable-gpu")
        opt.add_argument("--disable-crash-reporter")
        opt.add_argument("--disable-extensions")
        opt.add_argument("--disable-in-process-stack-traces")
        opt.add_argument("--disable-logging")
        opt.add_argument("--disable-dev-shm-usage")
        opt.add_argument("--log-level=3")
        opt.add_argument("--output=/dev/null")
        self.driver = webdriver.Chrome(options=opt)
        self.driver.get(lc_link)
        self.definition = ''
        try:
            for element in self.driver.find_elements_by_class_name('sense'):
                try: lc_sensetop = element.find_element_by_class_name('sensetop').text
                except: lc_sensetop = ''
                try: lc_def = element.find_element_by_class_name('def').text
                except: lc_def = ''
                self.definition = self.definition + ((chr(10) if len(self.definition)>0 else '') + \
                                    lc_sensetop + (' ' if len(lc_sensetop.strip())>0 and lc_def.strip()!=lc_sensetop.strip() else '') +\
                                    (lc_def if lc_def!=lc_sensetop else ''))
        except: pass

    def __del__(self):
        try: self.driver.quit()
        except: pass

colorama.init()
print(Fore.RESET, Back.RESET)


lc_word = sys.argv[1]
lc_word = lc_word.strip()
if len(lc_word)>0:
    print(Fore.LIGHTWHITE_EX + lc_word + Fore.RESET)
    lc_definitios = Oxford_Definition(r'https://www.oxfordlearnersdictionaries.com/definition/english/' + lc_word).definition.strip().replace(chr(10)+' ', chr(10))
    print(Fore.LIGHTGREEN_EX+lc_definitios+Fore.RESET)
    if len(lc_definitios.strip())>0:
        pyperclip.copy(lc_definitios)
