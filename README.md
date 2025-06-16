# Instagram_reel_analyser
Find the most popular video of your favourite creator based on like, comment and views. Uses Python Playwright.

# Requirements - 
*playwright
*flask
*bs4

# How to Install - 
- create a virtual env in project folder
- activate the virtual env
- "pip install playwright"
- "pip install flask"
- "pip install bs4"
- "playwright install chromium"
- Don't forget to add your instagram login cookies to main.py

# How to run - 
- after installing activate the created virtual env and run "flask run"

Now after this the app will start getting hosted at localhost:5000 ..


# Usage - 
Simple to use, just go to the running flask app (localhost:5000) and enter the username whose reels you wanna analyse, and then enter or submit. Now it will open chromium and start opening instagram. If you don't have set the cookies ofcourse it will show an exception. Then after scrolling to the bottom of the desired user's reels tab it will return the dictionary data on the page....

# Screenshots -
Entering username
![Screenshot](https://raw.githubusercontent.com/BigBrar/Instagram_reel_analyser/main/Screenshot%202024-06-15%20072421.png)
# Output
![Screenshot](https://raw.githubusercontent.com/BigBrar/Instagram_reel_analyser/main/Screenshot%202024-06-15%20072941.png)
