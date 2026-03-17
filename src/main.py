import time 
import os
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By 
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class SearchOpticals:
    
    def __init__(self):
        self.os = os 
        self.time = time
        self.logging = logging
        self.webdriver = webdriver
        self.By = By
        self.ChromeDriverManager = ChromeDriverManager
        self.Service = Service
        self.Wait = Wait
        self.EC = EC
        self.driver = None
        
        
    def start_driver(self):
        try:
            options = self.webdriver.ChromeOptions()
            options.add_argument("--disable-gpu")
            options.add_argument("--window-size=1920,1080")
            service = self.Service(self.ChromeDriverManager().install())
            driver = self.webdriver.Chrome(service=service, options=options)
            driver.get("https://www.google.com/maps")
            print("Driver started successfully.")
            
            return driver
            
        except Exception as e:
            self.logging.error(f"Error starting the driver: {e}")
            
    def safe_wait(self, driver,  condition, timeout=20, action_desc="accion"):
        try:
            return  self.Wait(driver, timeout).until(condition)
        except Exception as e:
            self.logging.error(f"Error waiting for {action_desc}: {e}")
        return None
    
    def search_opticals(self, driver):
        try:
            search_box = self.safe_wait(driver, self.EC.element_to_be_clickable((self.By.ID, "ucc-1")), action_desc="search box")  #Get the search box element
            if search_box:
                search_box.send_keys("OPTICAS CALI" + Keys.ENTER) #Send the string value and press enter
                print("Search for 'OPTICAS CALI' executed successfully.")
            else:
                    self.logging.error("Search box not found.")
        except Exception as e:
            self.logging.error(f"Error searching for opticals: {e}") 
            
            
    def main(self):
            driver = self.start_driver()
            self.search_opticals(driver)
            time.sleep(5)  
            driver.quit()
            
if __name__ == "__main__":
    search_opticals = SearchOpticals()
    search_opticals.main()