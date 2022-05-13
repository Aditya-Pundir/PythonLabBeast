from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import subprocess

options = webdriver.ChromeOptions()
options.add_argument("--headless")
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)


def get_local():
    driver.get("http://192.168.0.1/index.html")
    time.sleep(5)
    bandwidth_control = driver.find_element(By.ID, "net-control")
    bandwidth_control.click()
    time.sleep(5)
    devices = driver.find_elements(By.CLASS_NAME, "deviceName")
    print("-------------------------------------------------------------------------")
    for i in range(len(devices)):
        devices[i] = devices[i].get_attribute("innerHTML")
        print(devices[i])
    return devices


devices = []


def new():
    global devices
    devices = get_local()


new()
while True:
    devices_New = get_local()
    print("\nDevices:", len(devices))
    print("Devices New:", len(devices_New))
    devices_New = get_local()
    print("\nDevices:", len(devices))
    print("Devices New:", len(devices_New))
    if len(devices_New) != len(devices):
        for i in range(len(devices_New)):
            try:
                if devices.index(devices_New[i]) == -1:
                    print(devices_New[i] +
                          ". Something is wrong that you don't know")
                    break
            except ValueError:
                print("\n", devices_New[i]+" just came into the network")
                subprocess.run(
                    f'''PowerShell -Command "Add-Type –AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('{devices_New[i]} just came into the network');"''')
                pass
        new()
