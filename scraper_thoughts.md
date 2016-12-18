## ScreenShot Section

1. So first it will login into the account and find the page. 


2. And then use some kind of stuff to send credentials and retrieve the Moodle user main page.

3. On the moodle user main page, find the all course page by finding the "view all courses link".

   - Selenium will be slow, is it possible to use urllib2 inside selenium? And use regex to find all the link hrefs to courses. (How to implement clicking next page after all the courses have been accessed? urllib2 login is still weird )

     > Well, I think a better solution will be find the entry/table of all links to courses but it is unlikely to have it on the website. 
     >
     > If we can get all links to each courses that will be way easier.


-    And save each to the list of course links.

-    Then it's just a basic crawler model:

     ```python
        Logic:
           crawl_list = [....]

        def get_uncrawled():
            return crawl_list[0] # op crawl_list.pop()?

        def doOps(url):
            init selenium driver and goes to this url
            login and wait for the page to load
            then take screenshot
            done and returns
            
        def main():
            while True:
              url = get_uncrawled()
              if url:
                  doOps(url)
              else:
                  crawling done
                  sys.exit()
     ```

Issues:

- Chromium/Firefox only takes a portion of the screen.

- PhantomJS has login errors.

- Safari driver works perfect but have weird unexpected random errors.

- The crawled webpage is unlikely to have those hyperlinks right… (Is it really useful tho?)

  > Using special executor inside phantomJS seems to work perfectly!!!

## File Crawling Functions

Haven't tested the old crawler yet. But if it works fine then it's cool I suppose. Could use better strategy tho. Gonna work on this after screenshooting is done!

