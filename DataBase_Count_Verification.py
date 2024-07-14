__author__ = 'abdul.wahhab'

import pymysql
import Config
import Request_Hits
import unittest
import ReadData
import time
import logging
global db,current_time ,Current_Date ,date_time_stamp
from datetime import datetime, timedelta

class TestCases(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        try:
            global db
            db = pymysql.connect(host=Config.Host,    # your host, usually localhost
                     user=Config.User,         # your username
                     passwd=Config.Password,  # your password
                     db=Config.DB)

        except Exception as e:

             print ('Error in connecting to data Base')
# Test case to check the Response count from the database
    def test_response_from_db(self):
        global date_time_stamp
        date_time_stamp = time.strftime('%Y-%m-%d  %H:%M:%S')
        logging.basicConfig(filename='Log.log', level=logging.DEBUG)
        logging.info("Start of logging 'test_response_from_db' Test case "+ " | " + " System Date " + " " + date_time_stamp)


        campaign_id=self.read_campaign()
        dbcursor= db.cursor()
        dbcursor.execute("SELECT responses FROM campaigns WHERE campaigns.campaign_id=%s",campaign_id)
        record= dbcursor.fetchone()

        self.assertEqual(record[0],Config.response_count)
        logging.info("Test Case 'test_response_from_db' executed successfully "+ " | " + " System Date " + " " + date_time_stamp)
        logging.info("End of logging 'test_response_from_db' Test case "+ " | " + " System Date " + " " + date_time_stamp)

# Test case to check the Impressions count from the database
    def test_impressions_from_db(self):
        global date_time_stamp
        date_time_stamp = time.strftime('%Y-%m-%d  %H:%M:%S')
        logging.basicConfig(filename='Log.log', level=logging.DEBUG)
        logging.info("Start of logging 'test_impressions_from_db' Test case "+ " | " + " System Date " + " " + date_time_stamp)


        campaign_id=self.read_campaign()
        dbcursor= db.cursor()
        dbcursor.execute("select impressions from campaigns where campaigns.campaign_id=%s",campaign_id)
        record= dbcursor.fetchone()

        self.assertEqual(record[0],Config.impression_count)
        logging.info("Test Case 'test_impressions_from_db' executed successfully "+ " | " + " System Date " + " " + date_time_stamp)
        logging.info("End of logging 'test_impressions_from_db' Test case "+ " | " + " System Date " + " " + date_time_stamp)
# Test case to check the Clicks count from the database
    def test_clicks_from_db(self):
        global date_time_stamp
        date_time_stamp = time.strftime('%Y-%m-%d  %H:%M:%S')
        logging.basicConfig(filename='Log.log', level=logging.DEBUG)
        logging.info("Start of logging 'test_clicks_from_db' Test case "+ " | " + " System Date " + " " + date_time_stamp)
        campaign_id=self.read_campaign()
        dbcursor= db.cursor()
        dbcursor.execute("select clicks from campaigns where campaigns.campaign_id=%s",campaign_id)
        record= dbcursor.fetchone()
        self.assertEqual(record[0],Config.click_count)
        logging.info("Test Case 'test_clicks_from_db' executed successfully "+ " | " + " System Date " + " " + date_time_stamp)
        logging.info("End of logging 'test_clicks_from_db' Test case "+ " | " + " System Date " + " " + date_time_stamp)

    def read_campaign(self):
        campaign_id_list=(ReadData.read_campaign_ids())
        #print(Campaign_id_list[0][0])
        return campaign_id_list[0][0]

    @classmethod
    def tearDownClass(cls):
        global db
        db.close()


