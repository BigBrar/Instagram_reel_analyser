from playwright.sync_api import sync_playwright
import time

cookies = [] #add your instagram cookies....(logged in) (can be extracted using playwright or selenium)

def scroll_to_bottom(page): #function to scroll to the bottom and wait for the page to load
    html = page.content() #store the page's html
    prev_height = page.evaluate("document.body.scrollHeight")#record current page height
    index=0
    while True:
        page.wait_for_load_state('networkidle')#wait for page to load
        # Scroll to the bottom
        page.evaluate("window.scrollTo(100, document.body.scrollHeight)") #scroll a 100px above from the bottom
        # Wait for page to load
        time.sleep(2)
        page.wait_for_load_state('networkidle')#wait for page to load

        html+=page.content()
        # Get the new height
        page.evaluate("window.scrollTo(100, document.body.scrollHeight)")
        time.sleep(2)
        page.wait_for_load_state('networkidle')# time.sleep(6)
        html+=page.content()#collect html again and append

        curr_height = page.evaluate("document.body.scrollHeight")
        if curr_height == prev_height:
            break
        prev_height = curr_height
    return html

def main_func(username):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)

        context = browser.new_context()
        page = context.new_page()
        page.goto('https://instagram.com')
        print(page.title())
        context.add_cookies(cookies)

        page.goto(f'https://www.instagram.com/{username}/reels/')
        page.wait_for_load_state('networkidle')

        print('calling the scroll function...')
        html = scroll_to_bottom(page)
        
        browser.close()
        return html