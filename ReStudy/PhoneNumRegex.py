import re

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('my number is 415-555-4242')
print('Phone number found:' + mo.group(1))
