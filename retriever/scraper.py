import os
import sys 
import datetime
import mechanize
import cookielib

b = mechanize.Browser()

# disable the handling of the robots.txt file (sorry)
# (via http://stackoverflow.com/questions/2846105/screen-scraping-getting-around-http-error-403-request-disallowed-by-robots-tx)
b.set_handle_robots(False)

cj = cookielib.LWPCookieJar()
b.set_cookiejar(cj)

def scrape(the_day):
    
    #if len(sys.argv) == 1:
    #    today = datetime.date.today()
    #else:
    #    today = datetime.date(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]))

    r = b.open('http://shop.ilfattoquotidiano.it/abbonati/')
    print b.title()

    b.select_form(name='loginform')
    b.form['log'] = os.environ['IFQSYNC_IFQ_USERNAME']
    b.form['pwd'] = os.environ['IFQSYNC_IFQ_PASSWORD']
    b.submit()
    
    filename = the_day.strftime(os.path.join(os.environ['IFQSYNC_ARCHIVE_PATH'], 'ilfatto-%Y%m%d.pdf'))
    url = the_day.strftime('http://pdf.ilfattoquotidiano.it/openpdf/?n=%Y%m%d')
    
    f = open(filename, 'w')
    
    b.open(url)
    
    f.write(b.response().read())
    f.close()

    print "written to %s" % (filename)

    return filename