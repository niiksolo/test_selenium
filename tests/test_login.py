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




    

