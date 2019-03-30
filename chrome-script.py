from selenium import webdriver
chromepath = '/home/jatin/Downloads/chromedriver'
driver = webdriver.Chrome(chromepath)
driver.maximize_window()
driver.get('https://www.amway.com')
