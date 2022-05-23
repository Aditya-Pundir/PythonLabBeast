import subprocess  # To execute commands in terminal
import speech_recognition as sr
import datetime
import time
import json
import wikipedia
import webbrowser
import pyautogui  # For clicking on the buttons using cursor
import requests
import randfacts
import os
import pyjokes
import shutil
import pywhatkit
import smtplib  # For sending emails
import re  # For getting to and body for sending email
from datetime import date
from colorama import Fore  # To colour the print statements
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_argument("--headless")
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
place = "haridwar"


def sendMail(to, body):
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.ehlo()

        server.login("formal.googl@gmail.com", "coder420")
        subject = "Email sent by Aditya's PA - Jarvis"
        body = body

        msg = f"Subject: {subject}\n\n{body}"
        server.sendmail("formal.googl@gmail.com", to, msg)
        speak("Email sent successfully")
    except Exception as e:
        print(e)
        speak("Couldn't send email")


def speak(audio):
    print(Fore.CYAN+"Jarvis: "+Fore.GREEN + audio + Fore.WHITE)
    subprocess.run(
        f'''PowerShell -Command "Add-Type –AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('{audio}');"''')


def sendWhatsApp(to, body):
    hour = datetime.datetime.now().hour
    minute = datetime.datetime.now().minute
    pywhatkit.sendwhatmsg(to, body, hour, minute+1)
    time.sleep(20)
    pyautogui.hotkey("ctrl", "w")
    os.remove(
        "C:\\Users\\adity\\Documents\\Code-Playground\\PythonLab\\PyWhatKit_DB.txt")


def organize(location):

    if location == "desktop":
        dir_path = "C:\\Users\\adity\\Desktop"
        items = os.listdir(dir_path)
        for i in range(len(items)):
            complete_name = os.path.splitext(items[i])

            name = complete_name[0]
            ext = complete_name[1]
            full_name = f"{name}{ext}"
            full_path = dir_path + "\\" + full_name

            if ext == ".jpg" or ext == ".png" or ext == ".jpeg" or ext == ".gif":
                file_exist_index = 1
                file_exists = os.path.isfile(
                    f"{dir_path}\\Filders\\Images\\{full_name}")
                to_break = False

                while file_exists == True:
                    file_exist_index += 1
                    full_name = f"{name}({file_exist_index}){ext}"
                    file_exists = os.path.isfile(
                        f"{dir_path}\\Filders\\Images\\{full_name}")
                    if file_exists == False:
                        if file_exist_index != 1:
                            os.rename(
                                full_path, f"{dir_path}\\{name}({file_exist_index}){ext}")
                        shutil.move(f"{dir_path}\\{name}({file_exist_index}){ext}",
                                    f"{dir_path}\\Filders\\Images", full_name)
                        to_break = True
                if to_break == False:
                    shutil.move(f"{dir_path}\\{full_name}",
                                f"{dir_path}\\Filders\\Images", full_name)

            if ext == ".txt":
                file_exist_index = 1
                file_exists = os.path.isfile(
                    f"{dir_path}\\Filders\\Text-Documents\\{full_name}")
                to_break = False

                while file_exists == True:
                    file_exist_index += 1
                    full_name = f"{name}({file_exist_index}){ext}"
                    file_exists = os.path.isfile(
                        f"{dir_path}\\Filders\\Text-Documents\\{full_name}")
                    if file_exists == False:
                        if file_exist_index != 1:
                            os.rename(
                                full_path, f"{dir_path}\\{full_name}")
                        shutil.move(f"{dir_path}\\{name}({file_exist_index}){ext}",
                                    f"{dir_path}\\Filders\\Text-Documents", full_name)
                        to_break = True
                if to_break == False:
                    shutil.move(f"{dir_path}\\{full_name}",
                                f"{dir_path}\\Filders\\Text-Documents", full_name)

            if ext == ".xlsx":
                file_exist_index = 1
                file_exists = os.path.isfile(
                    f"{dir_path}\\Filders\\Excel-Documents\\{full_name}")
                to_break = False

                while file_exists == True:
                    file_exist_index += 1
                    full_name = f"{name}({file_exist_index}){ext}"
                    file_exists = os.path.isfile(
                        f"{dir_path}\\Filders\\Excel-Documents\\{full_name}")
                    if file_exists == False:
                        if file_exist_index != 1:
                            os.rename(
                                full_path, f"{dir_path}\\{full_name}")
                        shutil.move(f"{dir_path}\\{name}({file_exist_index}){ext}",
                                    f"{dir_path}\\Filders\\Excel-Documents", full_name)
                        to_break = True
                if to_break == False:
                    shutil.move(f"{dir_path}\\{full_name}",
                                f"{dir_path}\\Filders\\Excel-Documents", full_name)

            if ext == ".docx":
                file_exist_index = 1
                file_exists = os.path.isfile(
                    f"{dir_path}\\Filders\\Word-Documents\\{full_name}")
                to_break = False

                while file_exists == True:
                    file_exist_index += 1
                    full_name = f"{name}({file_exist_index}){ext}"
                    file_exists = os.path.isfile(
                        f"{dir_path}\\Filders\\Word-Documents\\{full_name}")
                    if file_exists == False:
                        if file_exist_index != 1:
                            os.rename(
                                full_path, f"{dir_path}\\{full_name}")
                        shutil.move(f"{dir_path}\\{name}({file_exist_index}){ext}",
                                    f"{dir_path}\\Filders\\Word-Documents", full_name)
                        to_break = True
                if to_break == False:
                    shutil.move(f"{dir_path}\\{full_name}",
                                f"{dir_path}\\Filders\\Word-Documents", full_name)

            if ext == ".rtf":
                file_exist_index = 1
                file_exists = os.path.isfile(
                    f"{dir_path}\\Filders\\Rich-Text-Documents\\{full_name}")
                to_break = False

                while file_exists == True:
                    file_exist_index += 1
                    full_name = f"{name}({file_exist_index}){ext}"
                    file_exists = os.path.isfile(
                        f"{dir_path}\\Filders\\Rich-Text-Documents\\{full_name}")
                    if file_exists == False:
                        if file_exist_index != 1:
                            os.rename(
                                full_path, f"{dir_path}\\{full_name}")
                        shutil.move(f"{dir_path}\\{name}({file_exist_index}){ext}",
                                    f"{dir_path}\\Filders\\Rich-Text-Documents", full_name)
                        to_break = True
                if to_break == False:
                    shutil.move(f"{dir_path}\\{full_name}",
                                f"{dir_path}\\Filders\\Rich-Text-Documents", full_name)

            if ext == ".pptx":
                file_exist_index = 1
                file_exists = os.path.isfile(
                    f"{dir_path}\\Filders\\PowerPoint-Presentations\\{full_name}")
                to_break = False

                while file_exists == True:
                    file_exist_index += 1
                    full_name = f"{name}({file_exist_index}){ext}"
                    file_exists = os.path.isfile(
                        f"{dir_path}\\Filders\\PowerPoint-Presentations\\{full_name}")
                    if file_exists == False:
                        if file_exist_index != 1:
                            os.rename(
                                full_path, f"{dir_path}\\{full_name}")
                        shutil.move(f"{dir_path}\\{name}({file_exist_index}){ext}",
                                    f"{dir_path}\\Filders\\PowerPoint-Presentations", full_name)
                        to_break = True
                if to_break == False:
                    shutil.move(f"{dir_path}\\{full_name}",
                                f"{dir_path}\\Filders\\PowerPoint-Presentations", full_name)

            if ext == ".pdf":
                file_exist_index = 1
                file_exists = os.path.isfile(
                    f"{dir_path}\\Filders\\PDF-Documents\\{full_name}")
                to_break = False

                while file_exists == True:
                    file_exist_index += 1
                    full_name = f"{name}({file_exist_index}){ext}"
                    file_exists = os.path.isfile(
                        f"{dir_path}\\Filders\\PDF-Documents\\{full_name}")
                    if file_exists == False:
                        if file_exist_index != 1:
                            os.rename(
                                full_path, f"{dir_path}\\{full_name}")
                        shutil.move(f"{dir_path}\\{name}({file_exist_index}){ext}",
                                    f"{dir_path}\\Filders\\PDF-Documents", full_name)
                        to_break = True
                if to_break == False:
                    shutil.move(f"{dir_path}\\{full_name}",
                                f"{dir_path}\\Filders\\PDF-Documents", full_name)

            if ext == ".mp4":
                file_exist_index = 1
                file_exists = os.path.isfile(
                    f"{dir_path}\\Filders\\Videos\\{full_name}")
                to_break = False

                while file_exists == True:
                    file_exist_index += 1
                    full_name = f"{name}({file_exist_index}){ext}"
                    file_exists = os.path.isfile(
                        f"{dir_path}\\Filders\\Videos\\{full_name}")
                    if file_exists == False:
                        if file_exist_index != 1:
                            os.rename(
                                full_path, f"{dir_path}\\{full_name}")
                        shutil.move(f"{dir_path}\\{name}({file_exist_index}){ext}",
                                    f"{dir_path}\\Filders\\Videos", full_name)
                        to_break = True
                if to_break == False:
                    shutil.move(f"{dir_path}\\{full_name}",
                                f"{dir_path}\\Filders\\Videos", full_name)

            if ext == "" and name != "Filders":
                folder_exist_index = 1
                folder_exists = os.path.isdir(
                    f"{dir_path}\\Filders\\Folders\\{full_name}")
                to_break = False

                while folder_exists == True:
                    folder_exist_index += 1
                    full_name = f"{name}({folder_exist_index}){ext}"
                    folder_exists = os.path.isdir(
                        f"{dir_path}\\Filders\\Folders\\{full_name}")
                    if folder_exists == False:
                        if folder_exist_index != 1:
                            os.rename(
                                full_path, f"{dir_path}\\{full_name}")
                        shutil.move(f"{dir_path}\\{name}({folder_exist_index}){ext}",
                                    f"{dir_path}\\Filders\\Folders", full_name)
                        to_break = True
                if to_break == False:
                    shutil.move(f"{dir_path}\\{full_name}",
                                f"{dir_path}\\Filders\\Folders", full_name)

        speak("Successfully organized the desktop")

    if location == "downloads":
        dir_path = "C:\\Users\\adity\\Downloads"
        items = os.listdir(dir_path)
        for i in range(len(items)):
            complete_name = os.path.splitext(items[i])

            name = complete_name[0]
            ext = complete_name[1]
            full_name = f"{name}{ext}"
            full_path = dir_path + "\\" + full_name

            if ext == ".jpg" or ext == ".png" or ext == ".jpeg" or ext == ".gif":
                file_exist_index = 1
                file_exists = os.path.isfile(
                    f"{dir_path}\\Filders\\Images\\{full_name}")
                to_break = False

                while file_exists == True:
                    file_exist_index += 1
                    full_name = f"{name}({file_exist_index}){ext}"
                    file_exists = os.path.isfile(
                        f"{dir_path}\\Filders\\Images\\{full_name}")
                    if file_exists == False:
                        if file_exist_index != 1:
                            os.rename(
                                full_path, f"{dir_path}\\{name}({file_exist_index}){ext}")
                        shutil.move(f"{dir_path}\\{name}({file_exist_index}){ext}",
                                    f"{dir_path}\\Filders\\Images", full_name)
                        to_break = True
                if to_break == False:
                    shutil.move(f"{dir_path}\\{full_name}",
                                f"{dir_path}\\Filders\\Images", full_name)

            if ext == ".txt":
                file_exist_index = 1
                file_exists = os.path.isfile(
                    f"{dir_path}\\Filders\\Text-Documents\\{full_name}")
                to_break = False

                while file_exists == True:
                    file_exist_index += 1
                    full_name = f"{name}({file_exist_index}){ext}"
                    file_exists = os.path.isfile(
                        f"{dir_path}\\Filders\\Text-Documents\\{full_name}")
                    if file_exists == False:
                        if file_exist_index != 1:
                            os.rename(
                                full_path, f"{dir_path}\\{full_name}")
                        shutil.move(f"{dir_path}\\{name}({file_exist_index}){ext}",
                                    f"{dir_path}\\Filders\\Text-Documents", full_name)
                        to_break = True
                if to_break == False:
                    shutil.move(f"{dir_path}\\{full_name}",
                                f"{dir_path}\\Filders\\Text-Documents", full_name)

            if ext == ".xlsx":
                file_exist_index = 1
                file_exists = os.path.isfile(
                    f"{dir_path}\\Filders\\Excel-Documents\\{full_name}")
                to_break = False

                while file_exists == True:
                    file_exist_index += 1
                    full_name = f"{name}({file_exist_index}){ext}"
                    file_exists = os.path.isfile(
                        f"{dir_path}\\Filders\\Excel-Documents\\{full_name}")
                    if file_exists == False:
                        if file_exist_index != 1:
                            os.rename(
                                full_path, f"{dir_path}\\{full_name}")
                        shutil.move(f"{dir_path}\\{name}({file_exist_index}){ext}",
                                    f"{dir_path}\\Filders\\Excel-Documents", full_name)
                        to_break = True
                if to_break == False:
                    shutil.move(f"{dir_path}\\{full_name}",
                                f"{dir_path}\\Filders\\Excel-Documents", full_name)

            if ext == ".docx":
                file_exist_index = 1
                file_exists = os.path.isfile(
                    f"{dir_path}\\Filders\\Word-Documents\\{full_name}")
                to_break = False

                while file_exists == True:
                    file_exist_index += 1
                    full_name = f"{name}({file_exist_index}){ext}"
                    file_exists = os.path.isfile(
                        f"{dir_path}\\Filders\\Word-Documents\\{full_name}")
                    if file_exists == False:
                        if file_exist_index != 1:
                            os.rename(
                                full_path, f"{dir_path}\\{full_name}")
                        shutil.move(f"{dir_path}\\{name}({file_exist_index}){ext}",
                                    f"{dir_path}\\Filders\\Word-Documents", full_name)
                        to_break = True
                if to_break == False:
                    shutil.move(f"{dir_path}\\{full_name}",
                                f"{dir_path}\\Filders\\Word-Documents", full_name)

            if ext == ".rtf":
                file_exist_index = 1
                file_exists = os.path.isfile(
                    f"{dir_path}\\Filders\\Rich-Text-Documents\\{full_name}")
                to_break = False

                while file_exists == True:
                    file_exist_index += 1
                    full_name = f"{name}({file_exist_index}){ext}"
                    file_exists = os.path.isfile(
                        f"{dir_path}\\Filders\\Rich-Text-Documents\\{full_name}")
                    if file_exists == False:
                        if file_exist_index != 1:
                            os.rename(
                                full_path, f"{dir_path}\\{full_name}")
                        shutil.move(f"{dir_path}\\{name}({file_exist_index}){ext}",
                                    f"{dir_path}\\Filders\\Rich-Text-Documents", full_name)
                        to_break = True
                if to_break == False:
                    shutil.move(f"{dir_path}\\{full_name}",
                                f"{dir_path}\\Filders\\Rich-Text-Documents", full_name)

            if ext == ".pptx":
                file_exist_index = 1
                file_exists = os.path.isfile(
                    f"{dir_path}\\Filders\\PowerPoint-Presentations\\{full_name}")
                to_break = False

                while file_exists == True:
                    file_exist_index += 1
                    full_name = f"{name}({file_exist_index}){ext}"
                    file_exists = os.path.isfile(
                        f"{dir_path}\\Filders\\PowerPoint-Presentations\\{full_name}")
                    if file_exists == False:
                        if file_exist_index != 1:
                            os.rename(
                                full_path, f"{dir_path}\\{full_name}")
                        shutil.move(f"{dir_path}\\{name}({file_exist_index}){ext}",
                                    f"{dir_path}\\Filders\\PowerPoint-Presentations", full_name)
                        to_break = True
                if to_break == False:
                    shutil.move(f"{dir_path}\\{full_name}",
                                f"{dir_path}\\Filders\\PowerPoint-Presentations", full_name)

            if ext == ".pdf":
                file_exist_index = 1
                file_exists = os.path.isfile(
                    f"{dir_path}\\Filders\\PDF-Documents\\{full_name}")
                to_break = False

                while file_exists == True:
                    file_exist_index += 1
                    full_name = f"{name}({file_exist_index}){ext}"
                    file_exists = os.path.isfile(
                        f"{dir_path}\\Filders\\PDF-Documents\\{full_name}")
                    if file_exists == False:
                        if file_exist_index != 1:
                            os.rename(
                                full_path, f"{dir_path}\\{full_name}")
                        shutil.move(f"{dir_path}\\{name}({file_exist_index}){ext}",
                                    f"{dir_path}\\Filders\\PDF-Documents", full_name)
                        to_break = True
                if to_break == False:
                    shutil.move(f"{dir_path}\\{full_name}",
                                f"{dir_path}\\Filders\\PDF-Documents", full_name)

            if ext == ".mp4":
                file_exist_index = 1
                file_exists = os.path.isfile(
                    f"{dir_path}\\Filders\\Videos\\{full_name}")
                to_break = False

                while file_exists == True:
                    file_exist_index += 1
                    full_name = f"{name}({file_exist_index}){ext}"
                    file_exists = os.path.isfile(
                        f"{dir_path}\\Filders\\Videos\\{full_name}")
                    if file_exists == False:
                        if file_exist_index != 1:
                            os.rename(
                                full_path, f"{dir_path}\\{full_name}")
                        shutil.move(f"{dir_path}\\{name}({file_exist_index}){ext}",
                                    f"{dir_path}\\Filders\\Videos", full_name)
                        to_break = True
                if to_break == False:
                    shutil.move(f"{dir_path}\\{full_name}",
                                f"{dir_path}\\Filders\\Videos", full_name)

            if ext == "" and name != "Filders":
                folder_exist_index = 1
                folder_exists = os.path.isdir(
                    f"{dir_path}\\Filders\\Folders\\{full_name}")
                to_break = False

                while folder_exists == True:
                    folder_exist_index += 1
                    full_name = f"{name}({folder_exist_index}){ext}"
                    folder_exists = os.path.isdir(
                        f"{dir_path}\\Filders\\Folders\\{full_name}")
                    if folder_exists == False:
                        if folder_exist_index != 1:
                            os.rename(
                                full_path, f"{dir_path}\\{full_name}")
                        shutil.move(f"{dir_path}\\{name}({folder_exist_index}){ext}",
                                    f"{dir_path}\\Filders\\Folders", full_name)
                        to_break = True
                if to_break == False:
                    shutil.move(f"{dir_path}\\{full_name}",
                                f"{dir_path}\\Filders\\Folders", full_name)

        speak("Successfully organized the downloads")


def tellJoke():
    joke = pyjokes.get_joke().replace("'", "")
    speak(joke)


def wish():
    hour = datetime.datetime.now().hour
    data = json.loads(requests.get(
        "https://api.openweathermap.org/data/2.5/weather?appid=d850f7f52bf19300a9eb4b0aa6b80f0d&q=haridwar&units=metric").text)
    condition = data["weather"][0]["main"]
    temperature = data["main"]["temp"]
    current_location = "haridwar"
    if hour >= 0 and hour < 12:
        speak(
            f"Good Morning Sir! Its {condition} with {temperature} degrees celsius in {current_location}")
    elif hour >= 12 and hour < 17:
        speak(
            f"Good Afternoon Sir! Its {condition} with {temperature} degrees celsius in {current_location}")
    elif hour >= 17 and hour < 24:
        speak(
            f"Good Evening Sir! Its {condition} with {temperature} degrees celsius in {current_location}")


def takeCommand():
    recog = sr.Recognizer()
    with sr.Microphone() as src:
        print(Fore.LIGHTMAGENTA_EX+"Listening...")
        recog.pause_threshold = 1
        audio = recog.listen(src)

    try:
        print("Recognizing...")
        query = recog.recognize_google(audio, language="en-in")
        print(query)
    except Exception as e:
        print(e)
        return "None"

    return query


if __name__ == "__main__":
    try:
        wish()
        awake = True
        while True:
            query = takeCommand().lower()

            # Logic for executing the tasks based on query:
            if "hey jarvis" in query and awake == True:
                query = query.replace("hey jarvis ", "")

            if "how are you" in query and awake == True:
                speak("I am fine Sir, thanks for asking")

            if "organise " in query and awake == True:
                location = query.replace("organise ", "")
                organize(location)

            if "wikipedia" in query and awake == True:
                speak("Searching wikipedia...")
                query = query.replace(" wikipedia", "")
                try:
                    results = wikipedia.summary(query, sentences=2)
                    speak(results)
                except:
                    speak("Unable to understand!")

            if "good morning" in query and awake == True:
                hour = datetime.datetime.now().hour
                if hour >= 0 and hour < 12:
                    weatherDetails = requests.get(
                        "http://api.openweathermap.org/data/2.5/weather?appid=d850f7f52bf19300a9eb4b0aa6b80f0d&q=haridwar&units=metric").json()
                    temperature = weatherDetails["main"]["temp"]

                    speak(
                        f"Good Morning Sir, its {temperature} degrees celsius outside")
                else:
                    strtime = time.strftime("%H hours and %M minutes")
                    speak(f"It's {strtime}, so technically it's not morning")

            if "good afternoon" in query or "goodmorning" in query and awake == True:
                hour = datetime.datetime.now().hour
                if hour >= 12 and hour < 18:
                    weatherDetails = requests.get(
                        "http://api.openweathermap.org/data/2.5/weather?appid=d850f7f52bf19300a9eb4b0aa6b80f0d&q=haridwar&units=metric").json()
                    temperature = weatherDetails["main"]["temp"]

                    speak(
                        f"Good Afternoon Sir, its {temperature} degrees celsius outside")
                else:
                    strtime = time.strftime("%H hours and %M minutes")
                    speak(f"It's {strtime}, so technically it's not afternoon")

            if "good evening" in query or "goodevening" in query and awake == True:
                hour = datetime.datetime.now().hour
                if hour >= 17 and hour < 19:
                    weatherDetails = requests.get(
                        "http://api.openweathermap.org/data/2.5/weather?appid=d850f7f52bf19300a9eb4b0aa6b80f0d&q=haridwar&units=metric").json()
                    temperature = weatherDetails["main"]["temp"]

                    speak(
                        f"Good Evening Sir, its {temperature} degrees celsius outside")
                else:
                    strtime = time.strftime("%H hours and %M minutes")
                    speak(f"It's {strtime}, so technically it's not evening")

            if "good night" in query or "goodnight" in query and awake == True:
                hour = datetime.datetime.now().hour
                if hour >= 19 and hour < 24:
                    weatherDetails = requests.get(
                        "http://api.openweathermap.org/data/2.5/weather?appid=d850f7f52bf19300a9eb4b0aa6b80f0d&q=haridwar&units=metric").json()
                    temperature = weatherDetails["main"]["temp"]

                    speak(
                        f"Good Night Sir, its {temperature} degrees celsius outside, have sweet dreams")
                else:
                    strtime = time.strftime("%H hours and %M minutes")
                    speak(f"It's {strtime}, so technically it's not night")

            if "the temperature" in query and awake == True:
                data = json.loads(requests.get(
                    "https://api.openweathermap.org/data/2.5/weather?appid=d850f7f52bf19300a9eb4b0aa6b80f0d&q=haridwar&units=metric").text)
                temperature = data["main"]["temp"]
                speak(
                    f"Its {temperature} degrees celsius today in haridwar")

            if "weather condition" in query and awake == True:
                data = json.loads(requests.get(
                    "https://api.openweathermap.org/data/2.5/weather?appid=d850f7f52bf19300a9eb4b0aa6b80f0d&q=haridwar&units=metric").text)
                condition = data["weather"][0]["main"]

                speak(
                    f"Its {condition} outside")

            if "the time" in query and awake == True:
                strtime = time.strftime("%H hours and %M minutes")
                speak(strtime)

            if "the day" in query and awake == True:
                if datetime.datetime.today().weekday() == 0:
                    speak("Monday")
                elif datetime.datetime.today().weekday() == 1:
                    speak("Tuesday")
                elif datetime.datetime.today().weekday() == 2:
                    speak("Wednesday")
                elif datetime.datetime.today().weekday() == 3:
                    speak("Thursday")
                elif datetime.datetime.today().weekday() == 4:
                    speak("Friday")
                elif datetime.datetime.today().weekday() == 5:
                    speak("Saturday")
                elif datetime.datetime.today().weekday() == 6:
                    speak("Sunday")

            if "the date" in query and awake == True:
                d = str(date.today())
                d = d.split("-")
                d.reverse()
                if d[1] == "01":
                    month = "january"
                elif d[1] == "02":
                    month = "february"
                elif d[1] == "03":
                    month = "march"
                elif d[1] == "04":
                    month = "april"
                elif d[1] == "05":
                    month = "may"
                elif d[1] == "06":
                    month = "june"
                elif d[1] == "07":
                    month = "july"
                elif d[1] == "08":
                    month = "august"
                elif d[1] == "09":
                    month = "september"
                elif d[1] == "10":
                    month = "october"
                elif d[1] == "11":
                    month = "november"
                elif d[1] == "12":
                    month = "december"
                d[1] = month
                dateStr = ""
                for i in range(len(d)):
                    dateStr += f" {d[i]}"
                speak(dateStr)

            if "hello jarvis" in query and awake == True:
                speak("Hi Sir")

            if "are you mad" in query and awake == True:
                speak("I can never be as mad as Spider Man")

            if "open google" in query and awake == True:
                webbrowser.open("https://google.com")

            if "open news monkey" in query and awake == True:
                webbrowser.open("https://newsmonkey.world")

            if "open email" in query and awake == True:
                webbrowser.open("https://mail.google.com/mail/u/0/#inbox")

            if "open flipkart" in query and awake == True:
                webbrowser.open("https://flipkart.com")

            if "open amazon" in query and awake == True:
                webbrowser.open("https://amazon.in")

            if "open youtube" in query and awake == True:
                webbrowser.open("https://youtube.com")

            if "open wikipedia" in query and awake == True:
                webbrowser.open("https://wikipedia.com")

            if "open spotify" in query and awake == True:
                webbrowser.open("https://open.spotify.com")

            if "search google for" in query and awake == True:
                search = query.replace("search google for ", "")
                webbrowser.open(
                    f"https://google.com/search?q={search}")

            if "search youtube for" in query and awake == True:
                search = query.replace("search youtube for ", "")
                # webbrowser.open(
                #     f"https://youtube.com/results?search_query={search}")
                # time.sleep(10)
                # pyautogui.click(720, 260)
                # time.sleep(5)
                # pyautogui.press("f")

                pywhatkit.playonyt(search)
                time.sleep(5)

            if "send email to" in query and awake == True:
                # Name:
                # In "(.*)", I added "?" to only grab the first time name occurs:
                name = re.search("send email to (.*?) that", query)
                to = name.group(1)

                # Body:
                bod = re.search(" that (.*?)", query)
                body = bod.group(1)

                if "myself" in to:
                    sendMail("adityapundir2k@gmail.com", body)

                if "dad" in to:
                    sendMail("devendrak248@gmail.com", body)

                if "sister" in to:
                    sendMail("vandana.er1994@gmail.com", body)

                if "brother" in to:
                    sendMail("avneesh.er1991@gmail.com", body)

                if "mom" in to:
                    sendMail("pundirsunita7@gmail.com", body)

                if "sister-in-law" in to:
                    sendMail("anshikatanwar4@gmail.com", body)

            if "send whatsapp message to" in query and awake == True:
                # Name:
                # In "(.*)", I added "?" to only grab the first time name occurs:
                name = re.search("send whatsapp message to (.*?) that", query)
                to = name.group(1)

                # Body:
                bod = re.search(" that (.*)", query)
                body = bod.group(1)

                if "dad" in to:
                    sendWhatsApp("+919319464278", body)

                if "sister" in to:
                    sendWhatsApp("+917417114870", body)

                if "brother" in to:
                    sendWhatsApp("+919899101602", body)

                if "mother" in to:
                    sendWhatsApp("+918909090032", body)

                if "sister-in-law" in to:
                    sendWhatsApp("+919873788317", body)

            if "tell me a joke" in query or "tell me another joke" in query and awake == True:
                tellJoke()

            if "tell me a fact" in query or "tell me another fact" in query and awake == True:
                fact = randfacts.get_fact()
                speak(fact)

            if "live" in query and awake == True:
                pywhatkit.playonyt(query)
                time.sleep(10)
                pyautogui.press("tab")
                pyautogui.press("tab")
                pyautogui.press("tab")
                pyautogui.press("tab")
                pyautogui.press("tab")
                pyautogui.press("tab")
                pyautogui.press("tab")
                pyautogui.press("tab")
                pyautogui.press("tab")
                pyautogui.press("tab")
                pyautogui.press("tab")
                pyautogui.press("tab")
                pyautogui.press("enter")
                time.sleep(5)
                pyautogui.press("tab")
                pyautogui.press("tab")
                pyautogui.press("tab")
                pyautogui.press("tab")
                pyautogui.press("tab")
                pyautogui.press("tab")
                pyautogui.press("tab")
                pyautogui.press("enter")

            if "open stackoverflow" in query and awake == True:
                webbrowser.open("https://stackoverflow.com")

            if "it's music time" in query and awake == True:
                speak("Playing your liked songs on spotify")
                webbrowser.open("https://open.spotify.com/collection/tracks")
                time.sleep(15)
                pyautogui.press("tab")
                pyautogui.press("tab")
                pyautogui.press("tab")
                pyautogui.press("tab")
                pyautogui.press("tab")
                pyautogui.press("tab")
                pyautogui.press("tab")
                pyautogui.press("tab")
                pyautogui.press("tab")
                pyautogui.press("tab")
                pyautogui.press("tab")
                pyautogui.press("tab")
                pyautogui.press("tab")
                pyautogui.press("tab")
                pyautogui.press("tab")
                pyautogui.press("tab")
                pyautogui.press("tab")
                pyautogui.press("tab")
                pyautogui.press("tab")
                pyautogui.press("tab")
                pyautogui.press("tab")
                pyautogui.press("tab")
                pyautogui.press("tab")
                pyautogui.press("tab")
                pyautogui.press("tab")
                pyautogui.press("tab")
                pyautogui.press("tab")
                pyautogui.press("tab")
                pyautogui.press("tab")
                pyautogui.press("tab")
                pyautogui.press("enter")

            if "tell" and "stories" in query and awake == True:
                query = query.replace("tell ", "")
                query += " for kids"
                query = query.replace(" ", "+")
                pywhatkit.playonyt(query)
                time.sleep(10)
                pyautogui.press("f")

            if "play" in query and awake == True:

                query = query.replace("play ", "")
                speak("playing " + query)
                pywhatkit.playonyt(query)
                time.sleep(10)
                pyautogui.press("f")

            if "thanks" in query or "thank you" in query and awake == True:
                speak("Mention not Sir")

            if "sleep jarvis" in query or "go to sleep jarvis" in query or "go to bed jarvis" in query and awake == True:
                speak("As you wish Sir!")
                awake = False

            if "wake up jarvis" in query and awake == False:
                speak("Jarvis ready in your service Sir!")
                awake = True

    except Exception as e:
        print(e)
