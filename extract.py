import re, json, time, requests
from selenium import webdriver

PATH = "/Users/Soccerboy_Krish/Documents/chromedriver"
driver = webdriver.Chrome(PATH)

def vsco_extract(usernames):
    for username in usernames:
        url = "https://vsco.co/" + username + "/gallery"
        response = requests.get(url).text
        counter = 1
        data = json.loads(
            re.search(r'window\.__PRELOADED_STATE__ = (\{.*\})', response).group(1))
        for image in data['entities']['images'].values():
            link = image['permalink']
            driver.get(link)
            img = driver.find_element_by_css_selector(".disableSave-mobile.css-6dp941")
            time.sleep(1)
            screenshot = img.screenshot_as_png
            with open(username + str(counter) + ".png", "wb") as f:
                f.write(screenshot)
                counter += 1


profiles = ["krishrastogi"]

vsco_extract(profiles)
