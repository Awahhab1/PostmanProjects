__author__ = 'abdul.wahhab'

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import Config, logging
import ReadData

import xlrd
import datetime
global driver , date_time_stamp,adunit_id
import unittest, time
class PortalTestData(unittest.TestCase):
    # Define prerequisite required to execute the test cases
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome("C:/Python27/selenium/webdriver/chromedriver.exe")
        cls.driver.implicitly_wait(30)
        cls.base_url = Config.base_url
        global driver
        driver = cls.driver
        driver.get(cls.base_url + "/")
        driver.maximize_window()
        driver.find_element_by_id("email").clear()
        driver.find_element_by_id("email").send_keys(Config.user_name)
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys(Config.password)
        driver.find_element_by_xpath("//input[@value='LOG IN']").click()

    def test_create_order(self):


        global date_time_stamp
        date_time_stamp = time.strftime('%Y-%m-%d  %H:%M:%S')
        logging.basicConfig(filename='Log.log', level=logging.DEBUG)
        table= ReadData.read_order_file()

        for x in range(len(table)):
            listVal1 = table[x][0]
            listVal2 = table[x][1]
            listVal3 = table[x][2]

            logging.info("Start of logging 'test_create_order' Test case "+ " | " + " System Date " + " " + date_time_stamp)
            global driver

            driver.find_element_by_link_text("Advertisers").click()

            driver.find_element_by_css_selector("button.btn.btn-success").click()
            driver.find_element_by_id("order_name").clear()
            driver.find_element_by_id("order_name").send_keys(table[x][0])
            driver.find_element_by_id("advertiser").clear()
            driver.find_element_by_id("advertiser").send_keys(table[x][1])
            driver.find_element_by_id("description").clear()
            driver.find_element_by_id("description").send_keys(table[x][2])
            driver.find_element_by_id("enabled").click()
            driver.find_element_by_css_selector("button.btn.btn-primary").click()
            time.sleep(1)
            self.assertTrue(self.is_element_present(By.LINK_TEXT, table[x][0]))
            logging.info("Order created successfully")
            logging.info("End of logging 'test_create_order' Test case "+ " | " + " System Date " + " " + date_time_stamp)
    def test_create_campaign_network(self):
        global date_time_stamp
        date_time_stamp = time.strftime('%Y-%m-%d  %H:%M:%S')
        logging.basicConfig(filename='Log.log', level=logging.DEBUG)

        campaign_record=ReadData.read_campaign_file()
        for x in range(len(campaign_record)):
            #listVal1 = campaign_record[x][0]
            logging.info("Start of logging 'test_create_campaign_network' Test case "+ " | " + " System Date " + " " + date_time_stamp)
            global driver
            driver.find_element_by_link_text(campaign_record[x][12]).click()
            driver.find_element_by_css_selector("button.btn.btn-success").click()
            driver.find_element_by_id("name").clear()
            driver.find_element_by_id("name").send_keys(campaign_record[x][0])
            driver.find_element_by_id("description").clear()
            driver.find_element_by_id("description").send_keys(campaign_record[x][1])
            Select(driver.find_element_by_id("id_campaign_type")).select_by_visible_text(campaign_record[x][2])
            Select(driver.find_element_by_id("id_priority")).select_by_visible_text(str(int(campaign_record[x][3])))
            time.sleep(1)
            Select(driver.find_element_by_id("network_id")).select_by_visible_text(campaign_record[x][4])
            time.sleep(1)
            Select(driver.find_element_by_id("network_dimension_id")).select_by_visible_text(campaign_record[x][5])

            driver.find_element_by_id("id_budget").clear()
            driver.find_element_by_id("id_budget").send_keys(str(int(campaign_record[x][6])))
            Select(driver.find_element_by_id("budget_type")).select_by_visible_text(campaign_record[x][7])
            driver.find_element_by_id("id_rate").clear()
            driver.find_element_by_id("id_rate").send_keys(str(int(campaign_record[x][8])))
            Select(driver.find_element_by_id("id_price_model")).select_by_visible_text(campaign_record[x][9])
            driver.find_element_by_id("id_dvs_all").click()

            driver.find_element_by_id("startDate").click()
            driver.find_element_by_id("startDate").clear()
            #start_date = datetime.datetime.strptime(campaign_record[x][10],'%m-%d-%y  %H:%M')
            driver.find_element_by_id("startDate").send_keys(campaign_record[x][10])
            driver.find_element_by_xpath("//form[@id='campaign_form']/fieldset/div[13]/div").click()
            #driver.find_element_by_id("endDate").click()
            driver.find_element_by_id("endDate").clear()
            #end_date = datetime.datetime.strptime(campaign_record[x][11],'%m/%d/%y  %H:%M')
            driver.find_element_by_id("endDate").send_keys(campaign_record[x][11])
            driver.find_element_by_xpath("//form[@id='campaign_form']/fieldset/div[14]/div").click()
            driver.find_element_by_id("is_approved").click()
            driver.find_element_by_id("enabled").click()
            driver.find_element_by_css_selector("button.btn.btn-primary").click()
            time.sleep(1)
            driver.find_element_by_id("save_form").click()
            time.sleep(1)
            self.assertTrue(self.is_element_present(By.LINK_TEXT, campaign_record[x][0]))
            logging.info("Network campaign created successfully")
            logging.info("End of logging 'test_create_campaign_Network' Test case "+ " | " + " System Date " + " " + date_time_stamp)
            driver.find_element_by_link_text("Advertisers").click()
    def test_create_application(self):
        global date_time_stamp
        date_time_stamp = time.strftime('%Y-%m-%d  %H:%M:%S')
        logging.basicConfig(filename='Log.log', level=logging.DEBUG)
        application_record=ReadData.read_application_file()
        for x in range(len(application_record)):
            logging.info("Start of logging 'test_create_application' Test case "+ " | " + " System Date " + " " + date_time_stamp)

            driver.find_element_by_link_text("Publisher").click()
            driver.find_element_by_css_selector("button.btn.btn-success").click()
            driver.find_element_by_id("name").clear()
            driver.find_element_by_id("name").send_keys(application_record[x][0])
            Select(driver.find_element_by_id("platform")).select_by_visible_text(application_record[x][1])
            driver.find_element_by_id("appStoreURL").clear()
            driver.find_element_by_id("appStoreURL").send_keys(application_record[x][2])
            driver.find_element_by_id("packageName").clear()
            driver.find_element_by_id("packageName").send_keys(application_record[x][3])

            driver.find_element_by_id("enabled1").click()
            driver.find_element_by_id("privacyPolicy1").click()
            driver.find_element_by_id("paid1").click()
            driver.find_element_by_css_selector("button.btn.btn-primary").click()
            time.sleep(1)
            self.assertTrue(self.is_element_present(By.LINK_TEXT, application_record[x][0]))
            logging.info("End of logging 'test_create_application' Test case "+ " | " + " System Date " + " " + date_time_stamp)
    # Helper Function
    def is_element_present(self, how, what):

        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    def test_create_adunit(self):
        global date_time_stamp
        date_time_stamp = time.strftime('%Y-%m-%d  %H:%M:%S')
        logging.basicConfig(filename='Log.log', level=logging.DEBUG)
        adunit_record=ReadData.read_adunit_file()
        for x in range(len(adunit_record)):
            logging.info("Start of logging 'test_create_adunit' Test case "+ " | " + " System Date " + " " + date_time_stamp)

            driver.find_element_by_link_text(adunit_record[x][4]).click()
            driver.find_element_by_css_selector("button.btn.btn-success").click()
            driver.find_element_by_id("name").clear()
            driver.find_element_by_id("name").send_keys(adunit_record[x][0])
            driver.find_element_by_id("description").clear()
            driver.find_element_by_id("description").send_keys(adunit_record[x][1])
            Select(driver.find_element_by_id("adType")).select_by_visible_text(adunit_record[x][2])
            Select(driver.find_element_by_id("format")).select_by_visible_text(adunit_record[x][3])
            driver.find_element_by_id("enabled1").click()
            driver.find_element_by_css_selector("button.btn.btn-primary").click()
            time.sleep(1)
            self.assertTrue(self.is_element_present(By.LINK_TEXT, adunit_record[x][0]))
            driver.find_element_by_link_text("Publisher").click()
            logging.info("End of logging 'test_create_adunit' Test case "+ " | " + " System Date " + " " + date_time_stamp)

    # Test case to target particular campaign with particular adunit
    def test_targeting(self):
        adunit_ids=list()
        global date_time_stamp
        date_time_stamp = time.strftime('%Y-%m-%d  %H:%M:%S')
        logging.basicConfig(filename='Log.log', level=logging.DEBUG)
        targeting_record=ReadData.read_targeting_file()
        for x in range(len(targeting_record)):
            logging.info("Start of logging 'test_targeting' Test case "+ " | " + " System Date " + " " + date_time_stamp)
            driver.find_element_by_link_text("Advertisers").click()
            driver.find_element_by_link_text(targeting_record[x][0]).click()
            driver.find_element_by_link_text(targeting_record[x][1]).click()
            driver.find_element_by_css_selector("button.btn.btn-success").click()
            time.sleep(3)
            driver.find_element_by_id("filter").clear()
            driver.find_element_by_id("filter").send_keys(targeting_record[x][3])
            time.sleep(1)
            adunit= targeting_record[x][3]
            driver.find_element_by_xpath("//td[contains(text(),'" + adunit + "')]/following-sibling::td/input[@type='checkbox']").click()
            time.sleep(10)
            adunit_no=driver.find_element_by_xpath("//td[contains(text(),'" + adunit + "')]/following-sibling::td[contains(text(),'-')]")

            adunit_id=adunit_no.text
            ReadData.write_adunits_ids(adunit_id)




    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()









