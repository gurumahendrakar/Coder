import re 
import requests

# text_ = '''>>> url = "http://olympus.realpython.org/profiles/poseidon"
#             >>> page = urlopen(url)

#             url = "http:+olympus.realpython.org/profiles/poseidon"
#             >>> html = page.read().decode("utf-8")
#             >>> start_index = html.find("<title>") + len("<title>")
#             >>> end_index = html.find("</title>")
#             >>> title = html[start_index:end_index]
#             >>> title
#             '\n<head>\n<title >Profile: Poseidon

# '''
# compile = re.compile('[a-z]+:(//|-|\+)+[a-z]+\.[a-z]+\.[a-z]+',re.IGNORECASE)
# search = compile.finditer(text_)

# for x in search:
#     print(x)


# & 
# or
# not
# xor 

import webbrowser


opening = webbrowser.Chrome('google').open('https://docs.python.org/3/library/threading.html#condition-objects')


