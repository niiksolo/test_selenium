import pytest
import selenium
from pages.page_login import LoginPage
import allure



@pytest.mark.parametrize("login, password",
[
    ("NikSolo", "12345677"),
    (123123123, 123131312),
    ('!@#!$!#', '!@$@!$!'),
    ('іаіаівфіаб', 'акуперцу')
])

def test_login(driver,login, password):
    page = LoginPage(driver)
    with allure.step("Открываем страницу логина"):
        page.open()
    with allure.step("Вводим имя пользователя"):
        page.enter_username(login)
    with allure.step("Вводим пароль"):
        page.enter_password(password)
    with allure.step("Нажимаем кнопку входа"):
        page.login_click()
    with allure.step("Проверяем сообщение об ошибке"):
        alert_text = page.get_alert_text()
        assert "invalid" in alert_text

    #def test_login(driver):
    # wait = WebDriverWait(driver, 10, 1)
    # driver.get(URL)
    # LOGIN = driver.find_element(*LOGIN_LOCATOR).send_keys('NikSolo')
    #
    # PASSWORD = driver.find_element(*PASS_LOCATOR)
    # PASSWORD.send_keys('12345677')
    #
    # BUTTON = driver.find_element(*BUTTON_LOCATOR).click()
    # ALERT = wait.until(EC.visibility_of_element_located(ALERT_LOCATOR))
    # assert "invalid" in ALERT.text


    

