from selenium import webdriver

# 크롬 브라우저 제어 드라이버 생성
browser = webdriver.Chrome('/Users/foretrouge7/chromedriver')

# 웹 사이트 가져오기
browser.get('https://www.naver.com')

# 웹 사이트의 특정 요소에 접근 후 값 전송
browser.find_element_by_xpath('//*[@id="query"]').send_keys('아이유')

# 3초 대기
browser.implicitly_wait(1)

# 웹 사이트의 특정 요소에 접근 후 동작 제어
browser.find_element_by_xpath('//*[@id="search_btn"]').click()
browser.implicitly_wait(1)

browser.save_screenshot('website.png')
browser.implicitly_wait(1)
browser.quit()