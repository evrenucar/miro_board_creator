![infinite_miro_faster](https://user-images.githubusercontent.com/34896403/151658306-07350e0f-8375-4670-9432-686e6997f435.gif)




# What does it do?
Generates a new miro board with a temp mail adress for you to use in your creative endeavors. At the end the team invite link is copied to your clipboard. With this you can have as many Miro boards as you want!
[Guide to do it manually](https://evrenucar.notion.site/How-to-open-infinite-Miro-boards-51dc9956257e4ce8a0e911064fb31d19)

# Why do you need it?
[Free version of miro](https://miro.com/pricing/) is limited to only one team that belongs to you. And every board you open within that team has to be shared with everyone that has been added to that team. This makes it hard to have private pages. Also the page limit within the team restricts you from opening more than 3 editable boards.
This tool enables you to create a board whenever you desire. And as you will have seperate teams access will be restricted to people who only have the team invite link.


# How does it work?
1. It generates a temporary mail adress with the help of [1secMail API](https://www.1secmail.com/api/)
2. Registers for a new Miro account with the generated mail adress and randomized **username** and **password**. With [Selenium](https://www.selenium.dev/) 
3. Receives **confimation code** and enters it.
4. Clicks setup and does Next Next Next
5. Copies team invite link to your clipboard with [Pyperclip](pyperclip) and terminates the process.

![miro_board_generator full](https://user-images.githubusercontent.com/34896403/151537904-6623d0ca-d08c-4386-a2f1-528e4c2e6542.gif)


# How to use it?
### 1. Clone/Download this repository to a local directory
`gh repo clone evrenucar/miro_board_creator`

### 2. Install depencencies (Python libraries required)
`pip install -r requirements.txt`

### 3. Install Google Chrome & Webdrivers
-Install from official [Google Chrome Website](https://www.google.com/intl/tr_tr/chrome/)

-Download chrome webdrivers https://sites.google.com/chromium.org/driver/

-Extract and place application to `C:\Program Files (x86)` (If you plce it somewhere else write that directory instead of <!--PATH = "C:\Program Files (x86)\chromedriver.exe" --> at line 115 in `selenium_script.py`

### 4. Run `selenium_script.py`
Chromedriver will go through the process of generating a new account and a new board in Miro. At the end the **team invite link** will be copied to your clipboard

### Enjoy!

# Future plans
Want to build it into a web-App and host it for everyone who wants access to unlimited miro boards. 

# Additional Notes
If you have trouble with the code just [PM me](https://www.instagram.com/evren.builds/) and I'd be glad to help

Thanks to user sameera-madushan for https://github.com/sameera-madushan/Mail-Swipe

Selenium Documentation:https://www.selenium.dev/documentation/

# Disclaimer & Warnings:

Use this ONLY for Educational Purposes! By using this code you agree that I'm not responsible for any kind of trouble caused by the code. THIS PROJECT IS NOT AFFILIATED WITH Miro.
