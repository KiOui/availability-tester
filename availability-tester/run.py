#!/usr/bin/env python

import time
from rainbowwrapper import RainbowWrapper
from HTTPUpTest import HTTPUpTest

SITES = [("sitename", "site_url"), ("another site name", "another_site_url")]
BRIGHTNESS = 0.01

if __name__ == "main":

	testers = []
	pings = []
	r = RainbowWrapper(0, BRIGHTNESS)


	for i in range(0, len(SITES)):
	    name, url = SITES[i]
	    h = HTTPUpTest(name, url, i, r)
	    testers = testers + [h]

	while True:
	    retvalue = True
	    for test in testers:
	        retvalue = test.test_once()
	        if not retvalue:
	            break
	    time.sleep(30)

