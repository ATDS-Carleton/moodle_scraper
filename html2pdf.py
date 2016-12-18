import pdfcrowd

try:
    # create an API client instance
    client = pdfcrowd.Client("xiax", "e7f96eea2888944a76f8126febbe3ebd")

    # convert a web page and store the generated PDF into a pdf variable
    pdf = client.convertURI('http://xxf1995.github.io')

    # # convert an HTML string and save the result to a file
    # output_file = open('html.pdf', 'wb')
    # html="<head></head><body>My HTML Layout</body>"
    # client.convertHtml(html, output_file)
    # output_file.close()
    #
    # # convert an HTML file
    # output_file = open('file.pdf', 'wb')
    # client.convertFile('/path/to/MyLayout.html', output_file)
    # output_file.close()
    output_file = open('html.pdf', 'wb')
    output_file.write(pdf)
    output_file.close()

except pdfcrowd.Error, why:
    print 'Failed:', why