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
    self.service = Service(executable_path=ChromeDriverManager().install())
    self.driver = webdriver.Chrome(service=self.service)
    self.email = email
    self.password = password


   def signIn(self):
    self.driver.get('https://www.instagram.com/login/')
    emailInput = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'form input')))[0]
    passwordInput = self.driver.find_elements(By.CSS_SELECTOR, 'form input')[1]
    emailInput.send_keys(self.email)
    passwordInput.send_keys(self.password)
    passwordInput.send_keys(Keys.ENTER)
    sleep(10)


   def followWithUsername(self, username):
    self.driver.get('https://www.instagram.com/' + username + '/')
    flw = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'button')))
    for f in flw:
        if f.text == 'Seguir' or f.text == 'Seguir de volta':
            f.click()
            break
    sleep(2)


   def unfollowWithUsername(self, username):
    self.driver.get('https://www.instagram.com/' + username + '/')
    popup = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'button')))[1]
    popup.click()
    unflw_btn = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'button')))
    for f in unflw_btn:
        if f.text == 'Deixar de seguir':
            f.click()
            sleep(2)
            break     


   # em construção 
   def likePost(self):
    post_btn = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'v1Nh3')))
    post_btn.click()


   def closeBrowser(self):
    self.driver.close()


   def __exit__(self):
     self.closeBrowser()


def main():
    print('ola mundo!')
    driver = InstagramBot('', '')
    driver.signIn()
    followers = driver.getUserFollowers('guilhermemazeto')
    print(followers)
    #driver.followWithUsername('guilhermemazeto')
    #driver.likePost()
    #driver.unfollowWithUsername('guilhermemazeto')
    
    driver.closeBrowser()


if __name__ == '__main__':
    main()
