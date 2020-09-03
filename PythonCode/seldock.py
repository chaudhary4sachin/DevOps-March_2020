from selenium import webdriver

# class test_title():

def test_letskode():
    baseurl = "https://learn.letskodeit.com/p/practice"
    driver = webdriver.Chrome(executable_path="/Users/sachinchaudhary/Desktop/Automation/chromedriver")
    driver.get(baseurl)
    driver.maximize_window()
    title = driver.title
    driver.quit()
    print(title)
    assert title == "Practice | Let's Kode It"