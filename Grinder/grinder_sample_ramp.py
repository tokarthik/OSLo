import random
from net.grinder.script import Test
from net.grinder.script.Grinder import grinder
from net.grinder.plugin.http import HTTPRequest
from net.grinder.common import GrinderException
 
tests = [
    "User Group 1",
    "User Group 2"
]
 
SERVER  = "http://blazedemo.com"
URIs_1  = ['/', '/vacation.html']
URIs_2  = ['/', '/reserve.php', '/confirmation.php', '/purchase.php']

class TestRunner:
    def rampUpSleeper(self):
        if grinder.runNumber != 0: return
        tprops = grinder.properties.getPropertySubset('taurus.')
        inc = tprops.getDouble('ramp_up', 0)/tprops.getInt('concurrency', 1)
        sleep_time = int(1000 * grinder.threadNumber * inc)
        grinder.sleep(sleep_time, 0)
        if sleep_time: grinder.logger.info('slept for %sms' % sleep_time)
        else: grinder.logger.info('No sleep needed')

    def __call__(self):
        self.rampUpSleeper()

        for testName in tests:

            if testName == "User Group 1":
                URI = random.choice(URIs_1)
                testID = 0
            else:
                URI = random.choice(URIs_2)
                testID = 1

            grinder.statistics.delayReports = 1
            requestString = "%s%s" % (SERVER, URI)
            request = HTTPRequest()
            request = Test(testID, testName).wrap(request)
            result = request.GET(requestString)