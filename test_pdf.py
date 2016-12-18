from selenium import webdriver
def execute(script, args):
    driver.execute('executePhantomScript', {'script': script, 'args' : args })

driver = webdriver.PhantomJS('phantomjs')

# hack while the python interface lags
driver.command_executor._commands['executePhantomScript'] = ('POST', '/session/$sessionId/phantom/execute')

driver.get('http://xxf1995.github.io/')

# set page format
# inside the execution script, webpage is "this"
pageFormat = '''this.paperSize = {format: "A4", orientation: "portrait" };'''
execute(pageFormat, [])

# render current page
render = '''this.render("test.pdf")'''
execute(render, [])