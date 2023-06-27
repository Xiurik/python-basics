from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
import time as t


SRV = Service("./msedgedriver.exe")
OPTS = Options()
OPTS.add_argument("start-maximized")

edge = webdriver.Edge(service=SRV, options=OPTS)
edge.get("https://demo.seleniumeasy.com/basic-first-form-demo.html")
t.sleep(2)

# Take Screenshot of Warning
# edge.save_screenshot("automation/images/WarningCertificate.png")

# Click the Advanced button
advanced = edge.find_element(By.ID, "details-button")
advanced.click()

# Click the Proceed link
advUrl = edge.find_element(By.ID, "proceed-link")
advUrl.click()

edge.implicitly_wait(2)
user_message = edge.find_element(By.ID, "user-message")
user_message.clear()
user_message.send_keys("I AM EXTRA COOOOL")

t.sleep(2)
show_message_button = edge.find_element(By.CLASS_NAME, "btn-primary")
show_message_button.click()

output_message = edge.find_element(By.ID, "display")
assert "I AM EXTRA COOOOL" in output_message.text

# Closes after 6 seconds.
t.sleep(6)
edge.quit()