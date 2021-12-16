from selenium.webdriver.common.by import By


class CountryPage:
    def __init__(self, driver):
        self.driver = driver

    country = (By.XPATH, "//h2[@class='category-name']")

    company_link = "(//div[@class='listing-title']//a)"

    company_name = "(//div[@class='wpbdp-field-display wpbdp-field wpbdp-field-value field-display field-value " \
                   "wpbdp-field-business_name wpbdp-field-title wpbdp-field-type-textfield " \
                   "wpbdp-field-association-title  ']//div) "

    category = "(//div[@class='wpbdp-field-display wpbdp-field wpbdp-field-value field-display field-value " \
               "wpbdp-field-category wpbdp-field-category wpbdp-field-type-select wpbdp-field-association-category  " \
               "']//div//a) "

    basedin = "(//div[@class='wpbdp-field-display wpbdp-field wpbdp-field-value field-display field-value " \
              "wpbdp-field-based_in wpbdp-field-meta wpbdp-field-type-textfield wpbdp-field-association-meta  ']//div) "

    tag = "(//div[@class='wpbdp-field-display wpbdp-field wpbdp-field-value field-display field-value " \
          "wpbdp-field-tags wpbdp-field-meta wpbdp-field-type-textfield wpbdp-field-association-meta  ']//div) "

    founded = "(//div[@class='wpbdp-field-display wpbdp-field wpbdp-field-value field-display field-value " \
              "wpbdp-field-founded wpbdp-field-meta wpbdp-field-type-select wpbdp-field-association-meta  ']//div) "

    description = "(//div[@class='wpbdp-field-display wpbdp-field wpbdp-field-value field-display field-value " \
                  "wpbdp-field-business_description wpbdp-field-meta wpbdp-field-type-textarea " \
                  "wpbdp-field-association-meta  ']//div) "

    nextPage = "//span[@class='next']"

    def getPageQuantity(self):
        length = self.driver.find_elements_by_xpath(self.company_link)
        return len(length)

    def getCountryName(self):
        return self.driver.find_element(*CountryPage.country)

    def getCompanyName(self, index):
        return self.driver.find_element_by_xpath(self.company_link + "[" + str(index) + "]")


    def getNextPage(self):
        return self.driver.find_element_by_xpath(self.nextPage)

    def getCompanyListPage(self):
        pagelist = []
        try:
            pagelist.append(self.driver.find_element_by_xpath(self.company_name).text)
        except:
            pagelist.append("")

        try:
            pagelist.append(self.driver.find_element_by_xpath(self.category).text)
        except:
            pagelist.append("")

        try:
            pagelist.append(self.driver.find_element_by_xpath(self.basedin).text)
        except:
            pagelist.append("")

        try:
            pagelist.append(self.driver.find_element_by_xpath(self.tag).text)
        except:
            pagelist.append("")

        try:
            pagelist.append(self.driver.find_element_by_xpath(self.founded).text)
        except:
            pagelist.append("")

        try:
            pagelist.append(self.driver.find_element_by_xpath(self.description).text)
        except:
            pagelist.append("")


        return pagelist