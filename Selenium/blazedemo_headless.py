import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

# options = webdriver.ChromeOptions()
# options.binary_location = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
# options.add_argument('headless')

class BlazeTest(unittest.TestCase):

	def setUp(self):
		self.ops = webdriver.ChromeOptions()
		# self.ops.binary_location = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
		self.ops.add_argument('headless')
		# self.ops.add_extension('BlazeMeter---The-Load-Testing-Cloud_v2.4.1.crx')
		self.browser = webdriver.Chrome(chrome_options=self.ops)

	def tearDown(self):
		self.browser.close()

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
		for i in range(timeout):
			if base_url == self.browser.current_url:
				web_element.click()
				print 'clicked'
				time.sleep(1)
			else:
				pass

	def test_BlazeDemo(self):
		self.browser.get('http://blazedemo.com')

		### Welcome Page ###

		assert "BlazeDemo" in self.browser.title, 'Welcome Page not loaded.'
		print 'Welcome Page Reached'

		fromPort = Select(self.find_element_by_locator('name', 'fromPort'))
		fromPort.select_by_visible_text('Boston')

		toPort = Select(self.find_element_by_locator('name', 'toPort'))
		toPort.select_by_visible_text('New York')

		submit = self.find_element_by_locator('xpath', '//div[3]/form/div/input[@class="btn btn-primary"]')
		self.wait_for_clickable(submit)


		### Reserve Page ###

		assert 'reserve' in self.browser.current_url, 'Reserve Page not loaded.'
		print 'Reserve Page Reached'

		chooseFlight = self.find_element_by_locator('xpath', '//div[2]/table/tbody/tr[2]/td[1]/input[@class="btn btn-small"]')
		self.wait_for_clickable(chooseFlight)


		### Purchase Page ###

		assert 'purchase' in self.browser.current_url, 'Purchase Page not loaded.'
		print 'Purchase Page Reached'

if __name__ == "__main__":
	unittest.main()
