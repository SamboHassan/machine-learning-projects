# #!/usr/bin/python
# """
# runs on the server, reads form input, prints HTML;
# url=http://server-name/cgi-bin/tutor3.py
# """
# import cgi
# import html

# form = cgi.FieldStorage()  # parse form data
# print("Content-type: text/html\n\n")  # plus blank line

# html = """
# <TITLE>tutor3.py</TITLE>
# <H1>Greetings</H1>
# <HR>
# <P>%s</P>
# <HR>"""
# if not "user" in form:
#     print(html % "Who are you?")
# else:
#     print(html % ("Hello, %s." % html.escape(form["user"].value)))


#!C:\Python311\python.exe
"""
runs on the server, reads form input, prints HTML
url=http://localhost:8000/cgi-bin/tutor3.py
"""
import cgi
import html

form = cgi.FieldStorage()

# Print required headers + blank line
print("Content-Type: text/html\n")

html_template = """
<TITLE>tutor3.py</TITLE>
<H1>Greetings</H1>
<HR>
<P>%s</P>
<HR>"""

if "user" not in form:
    print(html_template % "Who are you?")
else:
    user_input = html.escape(form["user"].value)
    print(html_template % ("Hello, %s." % user_input))
