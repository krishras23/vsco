from selenium import webdriver

PATH = "/Users/Soccerboy_Krish/Documents/chromedriver"
driver = webdriver.Chrome(PATH)

def vsco_extract(usernames):
    for username in usernames:
        counter = 1
        url = "https://vsco.co/" + username 
        driver.get(url)
        images = driver.find_elements_by_css_selector(".disableSave-mobile.css-6dp941")
        for image in images:
            screenshot = image.screenshot_as_png
            with open(username + str(counter) + ".png", "wb") as f:
                f.write(screenshot)
                counter += 1

    driver.close()


profiles = ["krishrastogi"]
vsco_extract(profiles)
