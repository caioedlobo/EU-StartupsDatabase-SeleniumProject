import time
from pageObjects.CountryPage import CountryPage
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestStartupDatabase(BaseClass):
    startup_list = []
    def test_startupDatabase(self):
        index = 1
        initial = 2
        homepage = HomePage(self.driver)
        countrypage = CountryPage(self.driver)
        index_max = homepage.getCountryListSize()
        try:
            homepage.CountryPage(index)

        except:
            time.sleep(8)
            homepage.CountryPage(index)

        self.setExcel()
        while(index_max >= index):

            pagesize = countrypage.getPageQuantity()

            for i in range(1, pagesize + 1):
                try:
                    countrypage.getCompanyName(i).click()

                except:
                    self.driver.refresh()
                    countrypage.getCompanyName(i).click()

                startup_list = countrypage.getCompanyListPage()

                self.setExcelSheet(initial, startup_list)
                try:
                    self.driver.back()
                except:
                    time.sleep(2)
                    self.driver.back()
                initial += 1
                startup_list.clear()


            try:
                countrypage.getNextPage().click()

            except:
                index += 1
                self.getBaseURL()
                homepage.CountryPage(index)
