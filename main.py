from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait 



class InstagramBot():
   def __init__(self, email, password):
    self.driveProfile = webdriver.ChromeOptions()
    self.driveProfile.add_experimental_option('prefs', {'intl.accept_languages': 'en,en_US'})
    self.service = Service(executable_path=ChromeDriverManager().install())
    self.driver = webdriver.Chrome(service=self.service)
    self.email = email
    self.password = password


   def signIn(self):
    self.driver.get('https://www.instagram.com/login/')
    sleep(2)
    emailInput = self.driver.find_elements(By.CSS_SELECTOR, 'form input')[0]
    passwordInput = self.driver.find_elements(By.CSS_SELECTOR, 'form input')[1]
    emailInput.send_keys(self.email)
    passwordInput.send_keys(self.password)
    passwordInput.send_keys(Keys.ENTER)
    sleep(10)


   def followWithUsername(self, username):
    self.driver.get('https://www.instagram.com/' + username + '/')
    sleep(5)
    flw_btn = self.driver.find_elements(By.CSS_SELECTOR, 'button')
    for f in flw_btn:
        if f.text == 'Seguir':
            f.click()
            break     
    sleep(2)


   def unfollowWithUsername(self, username):
    self.driver.get('https://www.instagram.com/' + username + '/')
    sleep(5)
    popup = self.driver.find_elements(By.CLASS_NAME, 'button')



   #def getUserFollowers():

   def closeBrowser(self):
    self.driver.close()


   #def __exit__():

def main():
    print('ola mundo!')
    driver = InstagramBot('', '')
    driver.signIn()
    #driver.followWithUsername('guilhermemazeto')
    driver.unfollowWithUsername('guilhermemazeto')
    driver.closeBrowser()

if __name__ == '__main__':
    main()