from selenium import webdriver

# 크롬 브라우저 제어 드라이버 생성
browser = webdriver.Chrome('/Users/foretrouge7/chromedriver')

# 웹 사이트 가져오기
browser.get('https://www.naver.com')

# 로그인 버튼 클릭
browser.find_element_by_xpath('//*[@id="account"]/div/a').click()

# 웹 사이트의 특정 요소에 접근 후 값 전송
browser.implicitly_wait(1)
user_id = input('id > ')
user_pw = input('pw > ')
browser.find_element_by_xpath('//*[@id="id"]').send_keys(user_id)
browser.find_element_by_xpath('//*[@id="pw"]').send_keys(user_id)

# 1초 대기
browser.implicitly_wait(1)
browser.find_element_by_xpath('//*[@id="log.login"]').click()
# 막힘!!!


# 웹 사이트의 특정 요소에 접근 후 동작 제어
browser.implicitly_wait(1)
browser.save_screenshot('naver_login.png')
browser.implicitly_wait(5)
browser.quit()