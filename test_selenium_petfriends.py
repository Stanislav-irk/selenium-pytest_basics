import time

from selenium.webdriver.common.by import By

base_url = "https://petfriends.skillfactory.ru"


def test_petfriends(web_browser):
    web_browser.get(base_url)

    time.sleep(5)

    btn_newuser = web_browser.find_element(By.XPATH, "//button[@onclick=\"document.location='/new_user';\"]")
    btn_newuser.click()

    btn_exist_acc = web_browser.find_element(By.LINK_TEXT, u"У меня уже есть аккаунт")
    btn_exist_acc.click()

    field_email = web_browser.find_element(By.ID, "email")
    field_email.clear()
    field_email.send_keys("stanislav-irk@bk.ru")

    # То же самое для поля с паролем
    field_pass = web_browser.find_element(By.ID, "pass")
    field_pass.clear()
    field_pass.send_keys("Taisia-28.11")

    # Ищем кнопку "Войти" и нажимаем на нее
    btn_submit = web_browser.find_element(By.XPATH, "//button[@type='submit']")
    btn_submit.click()

    time.sleep(10)  # небольшая задержка, чисто ради эксперимента

    if web_browser.current_url == f'{base_url}/all_pets':
        # Если мы на странице отображения моих питомцев, то сделать скриншот
        web_browser.save_screenshot('result_petfriends.png')
    else:
        raise Exception("login error")
