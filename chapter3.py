import sys
import codecs
import json
import re
import urllib.parse
import urllib.request


#ex20
print('ex20:')
f = codecs.open('jawiki-country.json', 'r', 'utf-8')
for str_json in f.readlines():
    dict_json = json.loads(str_json)
    if dict_json['title'] == 'イギリス':
        sys.stdout.buffer.write(dict_json['text'].encode('utf-8'))
        britain_f = open('Britain.txt', 'w')
        britain_f.buffer.write(dict_json['text'].encode('utf-8'))
        britain_f.close()
f.close()
print('\n')



#ex21
print('ex21:')
britain_f = codecs.open('Britain.txt', 'r', 'utf-8')
for line in britain_f.readlines():
    if re.compile('\[\[Category:.*\]\]').search(line):
        sys.stdout.buffer.write(line.encode('utf-8'))
britain_f.close()
print('\n')

#ex22
print('ex22:')
britain_f = codecs.open('Britain.txt', 'r', 'utf-8')
for line in britain_f.readlines():
    if re.compile('\[\[Category:.*\]\]').search(line):
        category = re.sub(string=line, pattern='\[\[Category:|\]\]', repl='')
        sys.stdout.buffer.write(category.encode('utf-8'))
britain_f.close()
print('\n')


#ex23
print('ex23:')
britain_f = codecs.open('Britain.txt', 'r', 'utf-8')
for line in britain_f.readlines():
    if re.compile('==.*==').match(line):
        level = line.count('=') // 2 - 1
        section = re.sub('=', '', line).replace(' ', '')
        section_level = re.sub('\n', ': ' + str(level) + '\n', section)
        sys.stdout.buffer.write(section_level.encode('utf-8'))
britain_f.close()
print('\n')


#ex24
print('ex24:')
britain_f = codecs.open('Britain.txt', 'r', 'utf-8')
for line in britain_f.readlines():
    if re.compile('\[\[File:.*\]\]').search(line):
        media = re.sub('\[\[File:|\|.*', '', line)
        sys.stdout.buffer.write(media.encode('utf-8'))
britain_f.close()
print('\n')


#ex25-28
print('ex25:')
britain_f = codecs.open('Britain.txt', 'r', 'utf-8')
is_in_basic_inf = False
basic_inf_hash = {}
basic_inf_file = open('basic_inf.txt', 'w')
for line in britain_f.readlines():
    if re.compile('{{基礎情報').match(line):
        is_in_basic_inf = True
    elif re.compile('}}').match(line):
        is_in_basic_inf = False
    elif re.compile('\|.*').match(line) and is_in_basic_inf:
        key = re.sub('\||=.*', '', line).strip()
        value = re.sub('\'', '', line)
        value = re.sub('<.*>', '', value)
        value = re.sub('\|.*=', '', value)
        if re.search('\[\[ファイル:.*\]\]', value):
            ptn_f = re.compile('\[\[ファイル:(.*)\|(.*)\|(.*)\]\]')
            files = re.finditer(ptn_f, value)
            for f in files:
                value = f.groups()[0]
        ptn_in_link1 = re.compile('\[\[(.*)\|(.*)\]\]')
        if re.search(ptn_in_link1, value):
            links = re.finditer(ptn_in_link1, value)
            for l in links:
                value = l.groups()[1]
        ptn_in_link2 = re.compile('\[\[(.*)\]\]')
        if re.search(ptn_in_link2, value):
            links = re.finditer(ptn_in_link2, value)
            for l in links:
                value = l.groups()[0]
        value = value.strip()
        basic_inf_hash[key] = value
        basic_inf_file.buffer.write((key +': '+ value + '\n').encode('utf-8'))
basic_inf_file.close()
britain_f.close()
print('\n')

#ex29
nat_flag_ref = basic_inf_hash['国旗画像']
print(nat_flag_ref)
nat_flag_url = 'https://www.mediawiki.org/w/api.php?' \
             + 'action=query' \
             + '&titles=File:' + urllib.parse.quote(nat_flag_ref) \
             + '&format=json' \
             + '&prop=imageinfo' \
             + '&iiprop=url'

request = urllib.request.Request(nat_flag_url)
connection = urllib.request.urlopen(request)
data = json.loads(connection.read())
# print(data['query']['pages'].items())
url = data['query']['pages'].popitem()[1]['imageinfo'][0]['url']
print(url)
