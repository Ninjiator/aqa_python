
#LEGEND
# X. Item_for_search - Name_of_Page
# //path



# 1. Sign in button - Main Page
# //button[@class = 'header_signin']
# button.header_signin

# 2. Guest log in button - Main Page
# //button[@class = 'header-link -guest']
# button.header-link.-guest

# 3. Contacts button - Main Page
# //button[@appscrollto = 'contactsSection']
# button[appscrollto="contactsSection"]

# 4. About Button - Main Page
# //button[@appscrollto = 'aboutSection']
# button[appscrollto="aboutSection"]

# 5. Home Button - Main Page
# //a[@class = 'btn header-link -active']
# a.btn.header-link.-active

# 6. Sign up button - Main Page
# //button[@class = 'hero-descriptor_btn btn btn-primary']
# button.hero-descriptor_btn.btn.btn-primary

# 7. Facebook link - Main Page
#  //a[contains(@class, 'socials_link') and @href='https://www.facebook.com/Hillel.IT.School']
# a.socials_link[href*="facebook.com"]

# 8. Telegram link - Main Page
# //a[contains(@class, 'socials_link') and @href="https://t.me/ithillel_kyiv"]
# a.socials_link[href*="t.me"]

# 9. YouTube link - Main Page
# //a[contains(@class, 'socials_link') and @href="https://www.youtube.com/user/HillelITSchool?sub_confirmation=1"]
# a.socials_link[href*="youtube.com"]

# 10. Instagram link - Main Page
# //a[contains(@class, 'socials_link') and @href="https://www.instagram.com/hillel_itschool/"]
# a.socials_link[href*="instagram.com"]

# 11. LinkedIn link - Main Page
# //a[contains(@class, 'socials_link') and @href="https://www.linkedin.com/school/ithillel/"]
# a.socials_link[href*="linkedin.com"]

# 12. ithillel.ua link - Main Page
# //a[@class = 'contacts_link display-4']
# a.contacts_link.display-4

# 13. support@ithillel.ua - Main Page
# //a[@class = 'contacts_link h4']
# a.contacts_link.h4

# 14. Play Button in YouTube video - Main Page
# //button[@class = 'ytp-large-play-button ytp-button ytp-large-play-button-red-bg']
# button.ytp-large-play-button.ytp-button.ytp-large-play-button-red-bg

# 15. Repost Button in YouTube video - Main Page
# //button[@class = 'ytp-button ytp-share-button ytp-show-share-title ytp-share-button-visible']
# button.ytp-share-button.ytp-button

# 16. Watch later Button in YouTube video - Main Page
# //button[@class = 'ytp-watch-later-button ytp-button ytp-show-watch-later-title']
# button.ytp-watch-later-button.ytp-button

# 17. hillel auto - Main Page
# //a[@class = 'header_logo']
# a.header_logo

# 18. Add car - Guest log in Page
# //button[@class = 'btn btn-primary']
# button.btn.btn-primary

# 19. Fuel Expenses - Guest log in Page
# //a[@class = 'btn btn-white btn-sidebar sidebar_btn -active']
# a.btn.btn-white.btn-sidebar.sidebar_btn.-active

# 20. Instructions - Guest log in Page
# //a[contains(@class, 'btn btn-white btn-sidebar sidebar_btn') and @href="/panel/instructions"]
# a.btn-sidebar[href="/panel/instructions"]

# 21. Log out - Guest log in Page
# //a[@class = 'btn btn-link text-danger btn-sidebar sidebar_btn']
# a.btn-link.text-danger.btn-sidebar

# 22. Name field - Registration pop up window
# //input[@id='signupName']
# #signupName

# 23. Last name field - Registration pop up window
# //input[@id='signupLastName']
# #signupLastName

# 24. Email - Registration pop up window
# //input[@id='signupEmail']
# #signupEmail

# 25. signupPassword - Registration pop up window
# //input[@id='signupPassword']
# #signupPassword