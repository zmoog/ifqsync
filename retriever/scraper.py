import os
import sys
import datetime
import mechanize
import cookielib

import settings

browser = mechanize.Browser()

# disable the handling of the robots.txt file (sorry)
# (via http://stackoverflow.com/questions/2846105/screen-scraping-getting-around-http-error-403-request-disallowed-by-robots-tx)
browser.set_handle_robots(False)

cj = cookielib.LWPCookieJar()
browser.set_cookiejar(cj)

def scrape(target_day):

    response = browser.open('http://shop.ilfattoquotidiano.it/abbonati/')
    print 'title: ', browser.title()

    browser.select_form(name='loginform')
    browser.form['log'] = settings.IFQ_USERNAME
    browser.form['pwd'] = settings.IFQ_PASSWORD
    browser.submit()

    filename = target_day.strftime(os.path.join(settings.TMP_PATH, 'ilfatto-%Y%m%d.pdf'))
    url = target_day.strftime('http://pdf.ilfattoquotidiano.it/openpdf/?n=%Y%m%d')

    browser.open(url)

    response = browser.response()
    headers = response.info()

    print headers

    content_type = headers['Content-Type']
    if "application/pdf" != content_type:
        print "Response type 'application/pdf' was expected, but '%s' was found." % (content_type)
	return


    pdf_file = open(filename, 'w')
    pdf_file.write(response.read())
    pdf_file.flush()
    pdf_file.close()

    return filename
