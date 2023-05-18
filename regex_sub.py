import re

urls = '''
http://www.google.com
https://coreyms.com
http://youtube.com
https://www.nasa.gov
'''
pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')

# matches = pattern.finditer(urls)
#
# for match in matches:
#     print(match)
#     print(match.group(0))
subbed_urls = pattern.sub(r'\2\3',urls)
print(subbed_urls)