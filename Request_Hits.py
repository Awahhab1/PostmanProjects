__author__ = 'abdul.wahhab'


import Config
import unittest
import requests
global response ,date_time_stamp
import logging
import time
import ReadData
import Portal_Test_Data_Creation
class TestCases(unittest.TestCase):

    # Test case to send request for AD serving
    def test_rest_request(self):
        # Logging info to Log file
        global date_time_stamp
        date_time_stamp = time.strftime('%Y-%m-%d  %H:%M:%S')
        logging.basicConfig(filename='Log.log', level=logging.DEBUG)
        logging.info("Start of logging 'test_rest_request' Test case "+ " | " + " System Date " + " " + date_time_stamp)
        url=self.UpdateURL()
        URL = url
        Headers= Config.header

        while(Config.request_count!=0):
            global response
            response = requests.get(URL, headers=Headers)

            Response_Status= response.status_code
            self.assertEqual(Response_Status,200)

            Config.request_count-=1
        logging.info("End of logging 'test_rest_request' Test case "+ " | " + " System Date " + " " + date_time_stamp)
        # Test case to send click request in AD serving flow
    def test_click_request(self):
        global date_time_stamp
        date_time_stamp = time.strftime('%Y-%m-%d  %H:%M:%S')
        logging.basicConfig(filename='Log.log', level=logging.DEBUG)
        logging.info("Start of logging 'test_click_request' Test case "+ " | " + " System Date " + " " + date_time_stamp)

        Headers= Config.header

        campaign_id_list=list()
        global response
        click_URL= response.headers.get('X-Clickthrough')
        mylist = click_URL.split("&")[4]
        global campaign_id
        campaign_id = mylist.split("=")[1]
        print(campaign_id)
        ReadData.write_campaign_ids(campaign_id)
        while(Config.click_count!=0):
            Click_response = requests.get(click_URL, headers=Headers)
            self.assertEqual(Click_response.status_code,200)

            Config.click_count-=1
        logging.info("Test Case 'test_click_request' executed successfully "+ " | " + " System Date " + " " + date_time_stamp)
        logging.info("End of logging 'test_click_request' Test case "+ " | " + " System Date " + " " + date_time_stamp)
    # Test case to send ompression  request in AD serving flow
    def test_impression_request(self):
        global date_time_stamp
        date_time_stamp = time.strftime('%Y-%m-%d  %H:%M:%S')
        logging.basicConfig(filename='Log.log', level=logging.DEBUG)
        logging.info("Start of logging 'test_impression_request' Test case "+ " | " + " System Date " + " " + date_time_stamp)


        global response
        Impression_URL =  response.headers.get('X-Imptracker')
        Headers= Config.header
        while(Config.impression_count!=0):
            impression_response = requests.get(Impression_URL, headers=Headers)

            self.assertEqual(impression_response.status_code,200)

            Config.impression_count-=1
        logging.info("Test Case 'test_impression_request' executed successfully "+ " | " + " System Date " + " " + date_time_stamp)
        logging.info("End of logging 'test_impression_request' Test case "+ " | " + " System Date " + " " + date_time_stamp)

    # Helper function to update the adunit ID in URL
    def UpdateURL(self):
        URL=Config.Url
        adunit_id=(ReadData.read_adunit_ids())
        update_url = (URL.format(adunit_id[0][0]))
        #print(update_url)
        return update_url




