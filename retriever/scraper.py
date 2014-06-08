import os
import sys
import datetime
import mechanize
import cookielib

browser = mechanize.Browser()

# disable the handling of the robots.txt file (sorry)
# (via http://stackoverflow.com/questions/2846105/screen-scraping-getting-around-http-error-403-request-disallowed-by-robots-tx)
browser.set_handle_robots(False)

cj = cookielib.LWPCookieJar()
browser.set_cookiejar(cj)

def scrape(target_day):

    #if len(sys.argv) == 1:
    #    today = datetime.date.today()
    #else:
    #    today = datetime.date(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]))

    response = browser.open('http://shop.ilfattoquotidiano.it/abbonati/')
    print browser.title()

    browser.select_form(name='loginform')
    browser.form['log'] = os.environ['IFQSYNC_IFQ_USERNAME']
    browser.form['pwd'] = os.environ['IFQSYNC_IFQ_PASSWORD']
    browser.submit()

    filename = target_day.strftime(os.path.join(os.environ['IFQSYNC_ARCHIVE_PATH'], 'ilfatto-%Y%m%d.pdf'))
    url = target_day.strftime('http://pdf.ilfattoquotidiano.it/openpdf/?n=%Y%m%d')

    pdf_file = open(filename, 'w')

    browser.open(url)

    pdf_file.write(browser.response().read())
    pdf_file.close()
    pdf_file.flush()

    print "written to %s" % (filename)

    return filename
