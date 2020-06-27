import re
heroRegex = re.compile(r'Batman|Tina Fey')
mo1 = heroRegex.search('Batman and Tina Fey and Batman')
mo1.group()
print(mo1.group())