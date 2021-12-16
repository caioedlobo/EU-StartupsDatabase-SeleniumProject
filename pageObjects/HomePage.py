class HomePage:
    def __init__(self, driver):
        self.driver = driver

    country = "(//ul[@class='wpbdp-categories cf wpbdp-categories-medium']//li//a)"
    countries_list = "//ul[@class='wpbdp-categories cf wpbdp-categories-medium']//li"

    def CountryPage(self, index):
        country_link = self.driver.find_element_by_xpath(self.country + "[" + str(index) + "]").get_attribute('href')
        return self.driver.get(country_link)

    def getCountryListSize(self):
        return len(self.driver.find_elements_by_xpath(self.countries_list))
