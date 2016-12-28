# Moodle Scraper
A scraper for older versions of Moodle.

- Instead of using outdated packages in older version. I am going to use webkit to get a screen capture of the page to retain the nice formatting.
  - currently looking at packages:
    1. `PyQt`
    2. `PySide`
    3. `Ghost`
  - These packages don't really support login right now. Might have to find a work around.
- [Probably low priority] And A pdf file will be created containing all the screenshots of a course.
- Investigate structure of older versions of moodle to get the files `.doc . pdf etc`
- Replace redirect links with actual target.


### Log

#### 11/27

Reading thru the old scraper and investigate on better libs to use. Found `PyQt` , `PySide` and `Ghost`

#### 11/28

Installing moodle on Mac with mama and stuffs. However, `macOS sierra` has incompatibility with `PyQt` or `PySide` packages which are essential for `screen capture` of particular page.

Found a bash tool that works quite well on taking a screen capture. However, needs to deal with login.

Sample Capture results are saved to `webkit2png outputs` folder.

#### 11/29

Trying to restore moodle site with the test data given by Andrew. Failed a few attempts. Trying to reset back. However, now it just hangs on `checking environments`.

Still stuck on  `checking environments` after 5 attempts by following installation guide for version `1.9 2.0 2.1 2.2 2.3 2.4 2.5`

#### 11/30

After various tries with stuffs, settle down to use a combination of `Firefox` and `selenium` to capture the page. Right now it is working however it captures before the page fully loaded for some reason.

Update:

A dummy wait is implemented in this case. It's dumb but it works :)

#### 12/1 ~ 12/5

Researching Moodle's tree structure. 

Something awkward… Chrome and Firefox coredrive didn't capture the whole page.

PhantomJS does but there is something weird with the `send_key` function using PhantomJS. Researching reveals the problem lies in some compatibility issue in PhantomJS. People saying falling back to 1.9.8 should work and the creator says it will be fixed in the next patch.

Safari Driver works at first..then auto fails somehow… probably some security stuff going on with it..

#### 12/6

Trying to fix problems found on 12/5. No luck yet.

#### 12/7

Created the moodle server both locally with `mamp` and on a ubuntu vps. Spend a lot of time fixing a issue with php version. Eventually fixed but have to know how to restore the test site with test data provided by andrew.

#### 12/8~12/9

Still fixing the issues spotted on 12/5. Found a working solution but it's in `Ruby`. Might have to learn ruby to fix this…

Trying to learn how to administrate moodle as well, but still have to deal with the backup restoring issue.

> And the key.txt is removed for security.

#### 12/12

Still having trouble with it. Will discuss with Andrew tmw.

#### 12/13

Rewrite code for better readability and structure. Continue to find a fix for selenium driver issues..

(Try test selenium driver of phantomJS on lower version of phantonJS or try to find chromium driver version 1)

#### 12/14 

Progressing on using phantomJS on a vps; seems to work sometimes..

#### 12/15

Trying another approach with Java's Spring Boot MVC framework. Have some progress on scraping a test site. But generating screenshot is still a quite hard.

#### 12/16

Learn Ruby.

#### 12/17

Reorganize the workflow. Check `scraper_thoughts.md`.

Found an pdf executor inside phatonJS which can parse links perfectly! ~~But somehow the view is mobile view.~~ Setting window size and adjusting pdf output works fine. Only remaining issue is login of phantomJS in OSX `send_key throws errors`. 

#### 12/18

Trying to resolve the `send_key` error. Still fails it throws a different error on ubuntu server instead of which I expect to work.

```python
selenium.common.exceptions.NoSuchElementException: Message: {"errorMessage":"Unable to find element with xpath './/[@id='username']'","request":{"headers":{"Accept":"application/json","Accept-Encoding":"identity","Connection":"close","Content-Length":"104","Content-Type":"application/json;charset=UTF-8","Host":"127.0.0.1:59944","User-Agent":"Python-urllib/2.7"},"httpVersion":"1.1","method":"POST","post":"{\"using\": \"xpath\", \"sessionId\": \"cd1737c0-c5a7-11e6-b842-617fa01ef11c\", \"value\": \".//[@id='username']\"}","url":"/element","urlParsed":{"anchor":"","query":"","file":"element","directory":"/","path":"/element","relative":"/element","port":"","host":"","password":"","user":"","userInfo":"","authority":"","protocol":"","source":"/element","queryKey":{},"chunks":["element"]},"urlOriginal":"/session/cd1737c0-c5a7-11e6-b842-617fa01ef11c/element"}}

Screenshot: available via screen
```

Which didn't show up locally. Possibly gechodriver issue with ubuntu or some \****.

#### 12/18~12/19

Continue trying to fix. No luck.

#### 12/21~12/23

After countless attempts to solve the bug related to the `gechodriver` of `phantomJs`. Nothing works. Right now:

- Either wait for the 2.5 release where the bug will be fixed.
- Try 1.9.8 on `OSX Yosemite`.
- Continue on the crawler main strategies. (Probably will work on this after Xmas!)

#### 12/26 ~ 12/28

Reading documentation and Investigating internal structure of moodle 1.9.8. Also trying out gechodriver with different languages. But the problem still exists. Probably have to wait for new release of PhantomJS.