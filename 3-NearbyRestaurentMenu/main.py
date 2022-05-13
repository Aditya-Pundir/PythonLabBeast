import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)


def get_zomato_restaurant_menu(name, swiggy_price_average):
    driver.get("https://www.zomato.com")
    select_menu = driver.find_element(
        By.XPATH, '//*[@id="root"]/div/div[3]/div[2]/div[2]/div/div[1]/i[2]')
    select_menu.click()
    time.sleep(5)
    detect_location = driver.find_element(By.CLASS_NAME, "sc-hizQCF")
    detect_location.click()

    time.sleep(10)
    search_bar = driver.find_element(By.CLASS_NAME, "sc-dTLGrV")
    search_bar.click()
    search_bar.send_keys(name)
    time.sleep(5)
    try:
        restaurant_first = driver.find_element(By.CLASS_NAME, "sc-1kx5g6g-3")
        restaurant_first.click()
        time.sleep(10)
        # items = driver.find_elements(By.CLASS_NAME, "sc-1s0saks-15")
        prices = driver.find_elements(By.CLASS_NAME, "sc-17hyc2s-1")
        price_sum = 0
        price_qty = 0

        for i in range(len(prices)):
            prices[i] = str(prices[i].text).replace("₹", "")
            price_qty += 1
            price_sum += float(prices[i])
        print(name +
              "'s average price on Zomato: {:.2f}".format(price_sum/price_qty))
        return (price_sum/price_qty)
    except:
        print(f"There's something wrong with {name} on zomato")


def get_swiggy_menu(restaurant, url):
    driver.get(url)
    items = driver.find_elements(By.CLASS_NAME, "styles_itemNameText__3bcKX")
    prices = driver.find_elements(By.CLASS_NAME, "rupee")
    price_sum = 0
    price_qty = 0
    for i in range(len(items)):
        print(items[i].text+" --> ₹"+prices[i].text)
        price_sum += float(prices[i].text)
        price_qty += 1
    prices_average = price_sum/price_qty
    zomato_average = get_zomato_restaurant_menu(restaurant, prices_average)
    print(restaurant +
          "'s average price on Swiggy: {:.2f}".format(price_sum/price_qty))
    if type(zomato_average) != str:
        difference = zomato_average - prices_average
        if difference < 0:
            difference = str(difference).replace("-", "")
            print(
                f"{restaurant} sells ₹{difference} more on swiggy than he sells his items on zomato")
        else:
            difference = str(difference)
            print(
                f"{restaurant} sells ₹{difference} more on zomato than he sells his items on swiggy")
    driver.quit()


def get_swiggy_restaurants():
    driver.get(
        "https://www.swiggy.com/restaurants/")
    swiggy_locate = driver.find_element(By.CLASS_NAME, "_1fiQt")
    swiggy_locate.click()

    time.sleep(5)
    restaurant_links = driver.find_elements(By.CLASS_NAME, "_1j_Yo")
    restaurants = driver.find_elements(By.CLASS_NAME, "nA6kb")
    print("Enter:")
    for i in range(len(restaurants)):
        print(f"\t{i} for {str(restaurants[i].text)}")

    choice = int(input("here:"))
    print(f"Showing menu of {restaurants[choice].text}:")
    get_swiggy_menu(restaurants[choice].text,
                    restaurant_links[choice].get_attribute("href"))


get_swiggy_restaurants()
