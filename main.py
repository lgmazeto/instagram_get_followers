from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class InstagramBot():
   def __init__(self):
    self.service = Service(executable_path=ChromeDriverManager().install())
    self.driver = webdriver.Chrome(service=self.service)

   def signIn(self):
    self.driver.get('https://google.com')

   #def followWithUsername():

   #def unfollowWithUsername():

   #def getUserFollowers():

   #def closeBrowser():

   #def __exit__():

def main():
    print('ola mundo!')
    driver = InstagramBot()
    driver.signIn()

if __name__ == '__main__':
    main()