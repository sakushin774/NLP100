import re

test = '[[abc]]aiueo[[def]]'
ptn = '\[\[(.*)\]\]((.*)\[\[(.*)\]\])*'
terms = re.finditer(ptn, test)
for t in terms:
    print(t.groups()[0])
