from selenium import webdriver
import os, time, sys, getopt, pdfcrowd


def screenShot(browser, saveName):
	# browser.execute_script("document.body.style.zoom=(top.window.screen.height-70)/Math.max(document.body.scrollHeight, document.body.offsetHeight, document.documentElement.clientHeight, document.documentElement.scrollHeight, document.documentElement.offsetHeight);")	time.sleep(5)
	browser.save_screenshot(saveName)
	browser.quit()

def html2pdf(html):
	client = pdfcrowd.Client("xiax", "e7f96eea2888944a76f8126febbe3ebd")
	# convert an HTML string and save the result to a file
	output_file = open('html.pdf', 'wb')
	client.convertHtml(html, output_file)
	output_file.close()

def main(argv):
	chromedriver = "./chromedriver"
	os.environ["webdriver.chrome.driver"] = chromedriver
	crawl_url = "http://xxf1995.github.io/"

	try:
		opts, args = getopt.getopt(argv, "hd:", ["driver="])
	except getopt.GetoptError:
		print "Error: test_screenShot.py -d <choose driver>"
		sys.exit(2)

	for opt, arg in opts:
		if opt == "-h":
			print "test_screenShot.py -d <driver_name>"
			print '''
Choose from the following:
s for Safari
c for Chrome
p for PhantomJS
			'''
			sys.exit()
		elif opt in ("-d", "--driver"):
			if arg == "s":
				browser = webdriver.Safari()
				saveName = "test_Safari.png"
			elif arg == "c":
				browser = webdriver.Chrome(chromedriver)
				saveName = "test_Chrome.png"
			elif arg == "p":
				browser = webdriver.PhantomJS()
				saveName = "test_PhantomJS.png"
			else:
				print "invalid driver"
				sys.exit()

	browser.get(crawl_url)
	time.sleep(5)
	source = browser.page_source
	html2pdf(source)
	screenShot(browser, saveName)

if __name__ == '__main__':
	main(sys.argv[1:])