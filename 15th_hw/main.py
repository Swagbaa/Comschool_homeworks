import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException


BASE_URL = "https://www.saucedemo.com/"
DEFAULT_PASSWORD = "secret_sauce"
WAIT_TIMEOUT = 10


class SauceDemoTests(unittest.TestCase):

    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(options=options)
        self.wait = WebDriverWait(self.driver, WAIT_TIMEOUT)
        self.driver.get(BASE_URL)

    def tearDown(self):
        self.driver.quit()


    def _login(self, username, password=DEFAULT_PASSWORD):
        user_field = self.wait.until(EC.visibility_of_element_located((By.ID, "user-name")))
        pass_field = self.driver.find_element(By.ID, "password")
        login_btn = self.driver.find_element(By.ID, "login-button")

        user_field.clear()
        user_field.send_keys(username)
        pass_field.clear()
        pass_field.send_keys(password)
        login_btn.click()

    def _get_error_message(self):
        try:
            error_el = self.wait.until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-test='error']"))
            )
            return error_el.text
        except TimeoutException:
            return None

    def _is_logged_in(self):
        try:
            self.wait.until(EC.url_contains("inventory.html"))
            return True
        except TimeoutException:
            return False

    def _logout(self):
        self.driver.find_element(By.ID, "react-burger-menu-btn").click()
        logout_link = self.wait.until(EC.element_to_be_clickable((By.ID, "logout_sidebar_link")))
        logout_link.click()

    def _add_first_n_items_to_cart(self, n=2):
        add_buttons = self.wait.until(
            EC.presence_of_all_elements_located(
                (By.CSS_SELECTOR, "button.btn_inventory")
            )
        )
        for btn in add_buttons[:n]:
            btn.click()


    def test_01_locked_out_user_login_blocked(self):
        self._login("locked_out_user")

        error_text = self._get_error_message()
        self.assertIsNotNone(error_text, "მოსალოდნელი იყო error შეტყობინება locked_out_user-ისთვის")
        self.assertIn("locked out", error_text.lower())
        self.assertFalse(self._is_logged_in(), "locked_out_user არ უნდა შედიოდეს სისტემაში")

    def test_02_performance_glitch_user_login_and_logout(self):
        self._login("performance_glitch_user")

        if self._is_logged_in():
            self._logout()
            self.wait.until(EC.visibility_of_element_located((By.ID, "login-button")))
            self.assertTrue(self.driver.find_element(By.ID, "login-button").is_displayed())
        else:
            error_text = self._get_error_message()
            self.assertIsNotNone(error_text, "მოსალოდნელი იყო login წარმატება ან error შეტყობინება")

    def test_03_problem_user_cart_flow(self):
        self._login("problem_user")

        if not self._is_logged_in():
            error_text = self._get_error_message()
            self.assertIsNotNone(error_text, "მოსალოდნელი იყო error შეტყობინება problem_user-ისთვის")
            return

        try:
            self._add_first_n_items_to_cart(2)

            cart_badge = self.wait.until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, ".shopping_cart_badge"))
            )
            self.assertEqual(cart_badge.text, "2")

            remove_buttons = self.driver.find_elements(By.CSS_SELECTOR, "button.btn_secondary.inventory_details_action_button, button[id^='remove']")
            for btn in remove_buttons:
                btn.click()

            badges = self.driver.find_elements(By.CSS_SELECTOR, ".shopping_cart_badge")
            self.assertEqual(len(badges), 0, "კალათა ცარიელი უნდა იყოს პროდუქტების წაშლის შემდეგ")
        except (NoSuchElementException, TimeoutException):
            error_text = self._get_error_message()
            self.assertIsNotNone(error_text, "მოსალოდნელი იყო error, თუ ფლოუ ჩავარდა")
        finally:
            self._logout()

    def test_04_standard_user_full_flow(self):
        self._login("standard_user")

        if not self._is_logged_in():
            error_text = self._get_error_message()
            self.assertIsNotNone(error_text, "მოსალოდნელი იყო error შეტყობინება standard_user-ისთვის")
            return

        self._add_first_n_items_to_cart(2)
        cart_badge = self.wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".shopping_cart_badge"))
        )
        self.assertEqual(cart_badge.text, "2")

        time.sleep(5)
        remove_button = self.driver.find_element(
            By.CSS_SELECTOR, "button[id^='remove']"
        )
        remove_button.click()

        cart_badge = self.wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".shopping_cart_badge"))
        )
        self.assertEqual(cart_badge.text, "1")

        product_link = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".inventory_item_name"))
        )
        product_name = product_link.text
        product_link.click()

        self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "inventory_details_name")))
        self.assertIn(product_name, self.driver.find_element(By.CLASS_NAME, "inventory_details_name").text)

        time.sleep(5)
        self.driver.back()
        self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "inventory_list")))

        sort_dropdown = Select(self.wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "product_sort_container"))
        ))
        sort_dropdown.select_by_value("hilo")

        prices = self.driver.find_elements(By.CLASS_NAME, "inventory_item_price")
        price_values = [float(p.text.replace("$", "")) for p in prices]
        self.assertEqual(price_values, sorted(price_values, reverse=True),
                          "პროდუქტები უნდა იყოს დალაგებული ფასის კლებადობით (High to Low)")

        main_window = self.driver.current_window_handle

        facebook_link = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "a[data-test='social-facebook']"))
        )
        facebook_link.click()
        self._switch_to_new_window_and_back(main_window)

        linkedin_link = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "a[data-test='social-linkedin']"))
        )
        linkedin_link.click()
        self._switch_to_new_window_and_back(main_window)

        self._logout()
        self.wait.until(EC.visibility_of_element_located((By.ID, "login-button")))
        self.assertTrue(self.driver.find_element(By.ID, "login-button").is_displayed())

    def _switch_to_new_window_and_back(self, main_window):
        self.wait.until(EC.number_of_windows_to_be(2))
        for handle in self.driver.window_handles:
            if handle != main_window:
                self.driver.switch_to.window(handle)
                break
        self.driver.close()
        self.driver.switch_to.window(main_window)


if __name__ == "__main__":
    unittest.main(verbosity=2)