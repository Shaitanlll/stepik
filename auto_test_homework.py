from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest
import math

@pytest.mark.parametrize('liter', ["236895","236896","236897","236898","236899","236903","236904","236905"])
class TestAbs():
    def test_abs1(self,liter):
        self.browser = webdriver.Chrome()
        self.browser.get(f"https://stepik.org/lesson/{liter}/step/1")
        # https://stepik.org/lesson/236895/step/1
        # https://stepik.org/lesson/236899/step/1
        self.browser.implicitly_wait(10)
        button = self.browser.find_element(By.CSS_SELECTOR, "a#ember33")
        button.click()
        input1 = self.browser.find_element(By.CSS_SELECTOR, 'input[name="login"]')
        input1.send_keys("shaitan.2024@mail.ru")
        input2 = self.browser.find_element(By.CSS_SELECTOR, 'input[name="password"]')
        input2.send_keys("IslamVorokov01")
        button = self.browser.find_element(By.CSS_SELECTOR, 'button[class="sign-form__btn button_with-loader "]')
        button.click()
        time.sleep(3)
        input3 = self.browser.find_element(
        By.XPATH, "//textarea[@placeholder='Напишите ваш ответ здесь...']")
        if input3.get_property("disabled"):
            feedback = self.browser.find_element(
                By.XPATH, "//p[@class='smart-hints__hint']").text
            assert "Correct!" == feedback
        else:
            input3.send_keys(math.log(int(time.time())))
            # input4 = self.browser.find_element(By.CSS_SELECTOR, "input[class='form-control second']")
            # input4.send_keys("89996669966")
            # input5 = self.browser.find_element(By.CSS_SELECTOR, "input[class='form-control second']")
            # input5.send_keys("Russia")
            button = self.browser.find_element(By.CSS_SELECTOR, "button.submit-submission")
            button.click()
            feedback = self.browser.find_element(
                By.XPATH, "//p[@class='smart-hints__hint']").text
            self.browser.quit()
            assert "Correct!" == feedback

if __name__ == "__main__":
    pytest.main()
