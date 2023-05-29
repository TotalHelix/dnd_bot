from splinter import Browser

browser = Browser()
browser.visit("https://character.ai")
searchBox = browser.find_by_name("q")
searchBox.fill("test")

button = browser.find_by_name("btnK")
button.click()
