from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def go_to_site(self, url):
        return self.driver.get(url)

    def get_current_url(self):
        return self.driver.current_url

    def send_keys(self, locator, value):
        return self.driver.find_element(*locator).send_keys(value)

    def get_current_text(self, locator):
        return self.driver.find_element(*locator).text

    def find_element_located(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator), message=f'Not found {locator}')

    def find_elements_located(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator), message=f'Not found {locator}')

    def find_clickable_element(self, locator, time=30):
        return WebDriverWait(self.driver, time).until(EC.element_to_be_clickable(locator), message=f'Not found {locator}')

    def find_visible_element_located(self, locator, time=30):
        return WebDriverWait(self.driver, time).until(EC.visibility_of_element_located(locator), message=f'Not found {locator}')

    def find_invisible_element_located(self, locator, time=30):
        return WebDriverWait(self.driver, time).until(EC.invisibility_of_element_located(locator), message=f'Not found {locator}')

    def drag_and_drop_on_element(self, locator_one, locator_two):
        draggable = self.driver.find_element(*locator_one)
        droppable = self.driver.find_element(*locator_two)
        action_chains = ActionChains(self.driver)
        action_chains.drag_and_drop(draggable, droppable).perform()
