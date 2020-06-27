import pyperclip , re

phoneRegex = re.compile(r'''(
    (\d{4}|\(\d{4}\))? #区号三位
    (\s|-|\.)? #分隔符
    (\d{3}) 
    (\s|-|\.)
    (\d{4})
    (\s*(ext|x|ext\.)\s(\d{2,5}))?
    )''', re.VERBOSE)

# create email regex
emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+
    @
    [a-zA-Z0-9.-]+
    (\.[a-zA-Z]{2,4})
)''', re.VERBOSE)

text = str(pyperclip.paste())

matches = []
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)
for groups in emailRegex.findall(text):
    matches.append(groups[0])

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('\n'.join(matches))
else:
    print('没有找到电话和邮箱')
