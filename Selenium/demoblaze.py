import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
# from selenium.webdriver.support.ui import Select
import time

class BlazeTest(unittest.TestCase):

	def setUp(self):
		self.ops = webdriver.ChromeOptions()
		self.browser = webdriver.Chrome("/Users/daper01/Documents/WebDriver/chromedriver")

	# def tearDown(self):
	# 	self.browser.close()

	def find_element_by_locator(self, locator = '', locatee = ''):
		if locator == 'id':
			return self.browser.find_element_by_id(locatee)
		elif locator == 'name':
			return self.browser.find_element_by_name(locatee)
		elif locator == 'class name':
			return self.browser.find_element_by_class_name(locatee)
		elif locator == 'xpath':
			return self.browser.find_element_by_xpath(locatee)
		elif locator == 'type':
			return self.browser.findelement_by_type(locatee)

	
	def wait_for_clickable(self, web_element, timeout = 10):
		base_url = self.browser.current_url
		if web_element != None:
			for i in range(timeout):
				if base_url == self.browser.current_url:
					web_element.click()
					print 'tried clicking ' + str(i + 1) + ' time/s'
					time.sleep(1)
				else:
					break
		else:
			print "item link not found on " + self.browser.current_url


	def wait_for_available(self, locator = '', locatee = '', timeout = 5):
		
		for i in range(timeout):
			try:
				return self.find_element_by_locator(locator,locatee)
				break
			except:
				print "failed to find " + str(i + 1) + " time/s."
				time.sleep(1)


	def test_DemoBlaze(self):
		### Index ###
		self.browser.get('https://www.demoblaze.com')
		
		### Item Page ###
		item_link = self.wait_for_available("xpath", "//*[@id='tbodyid']/div[1]/div/div/h4/a")
		self.wait_for_clickable(item_link)

		add_cart_button = self.wait_for_available("xpath", "//*[@id='tbodyid']/div[2]/div/a")
		self.wait_for_clickable(add_cart_button)
		# try:
		# 	self.wait_for_clickable(add_cart_button)
		# 	time.sleep(10)
		# 	Alert(self.browser).dismiss()
		# except selenium.common.exceptions.UnexpectedAlertPresentException:
		# 	print "dunno"
		alert = self.browser.switch_to_alert()
		print "found alert"
		alert.accept()
		# print "accepted alert"
		# time.sleep(10)



		# //*[@id="tbodyid"]/div[1]/div/a/img
		

if __name__ == "__main__":
	unittest.main()
