import time
import undetected_chromedriver as uc
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains


password = "PASSWORDT"
username = "USERNAME"

#watch a tutorial or read something to do this
chrome_driver_path = "Youre driver path"
chrome_user_path = "your user chrome path"
chrome_user_profile = "profile-directory=Profile 1" #user profile you want to use


# Some options
options = Options()
options.binary_location = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
options.add_argument(chrome_user_path)
options.add_argument(chrome_user_profile)
options.add_argument("--start-maximized")  # open Browser in maximized mode
options.add_argument("--no-sandbox")  # bypass OS security model
options.add_argument("--disable-dev-shm-usage")  # overcome limited resource problems
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)


def view_bot():
    driver = uc.Chrome(options=options, executable_path=chrome_driver_path)
    driver.get("https://www.twitch.tv/maxmalle?referrer=raid")
    time.sleep(1)
    try:

        # Opens loginscreen
        login = driver.find_element(By.XPATH, "//*[@id='root']/div/div[2]/nav/div/div[3]/div[3]/div/div[1]/div[1]/button")
        login.click()
        time.sleep(2)

        # Inserts Username
        u_name = driver.find_element(By.XPATH, "//*[@id='login-username']")
        u_name.send_keys(username)
        time.sleep(2)

        # Inserts Password
        pw = driver.find_element(By.XPATH, "//*[@id='password-input']")
        pw.send_keys(password)
        time.sleep(2)

        # pressing login button
        login_button = driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div/div/div/div[1]/div/div/div[3]/form/div/div[3]/button')
        login_button.click()
    except:
        pass

    finally:
        try:
            offline = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div/main/div[1]/div[3]/div/div/div[1]/div[1]/div[1]/div[2]/div/div/div/div/div[2]/div[1]/div[1]/div/div[1]/div/p').text
            print(offline)
            if offline == "OFFLINE":
                driver.close()

        except:
            try:

                # Unmute the twitch
                action = ActionChains(driver)
                action.send_keys("m")
                action.perform()
                chatbox = driver.find_element(By.CSS_SELECTOR, "#live-page-chat > div > div > div > div > div > section > div > div.Layout-sc-nxg1ff-0.fwjUjn.chat-input > div:nth-child(2) > div.InjectLayout-sc-588ddc-0.dzmTIk > div.Layout-sc-nxg1ff-0.dldMvq > div > div > div.InjectLayout-sc-588ddc-0.bNnJEL > div > div > div > div > div > div > span > span > span")

                # Send a "hello" in chat
                chatbox.send_keys("")
                send_chat = ActionChains(driver)
                send_chat.send_keys(Keys.ENTER)
                send_chat.perform()

            finally:

                while True:
                    time.sleep(60)

                    try:
                        #Collect Streamcoins
                        bonus = driver.find_element(By.CSS_SELECTOR, "#live-page-chat > div > div > div > div > div.Layout-sc-nxg1ff-0.ciSpU.stream-chat > section > div > div.Layout-sc-nxg1ff-0.fwjUjn.chat-input > div:nth-child(2) > div.Layout-sc-nxg1ff-0.ejhEzS.chat-input__buttons-container > div.Layout-sc-nxg1ff-0.cwwMDL > div > div > div > div.Layout-sc-nxg1ff-0.Aqzax > div > div > div > button")
                        bonus.click()
                        # print if successful
                        print("success")

                    except:
                        # print if failed
                        print("failed")

                    finally:
                        try:
                            #Checks if Stream is still running
                            driver.find_element(By.XPATH, '//*[@id="live-channel-stream-information"]/div/div/div/div/div[1]/div/div/div/a/div[2]/div/div/div')

                        except:
                            driver.quit()

                        finally:
                            pass


while True:
    view_bot()
    for i in range(1, 11):
        print(f"Try again in {11-i}")
        time.sleep(1)
