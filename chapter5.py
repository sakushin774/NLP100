import codecs
import sys
import xml.etree.ElementTree as et

class Morph:
    'surface'
    'base'
    'pos'
    'pos1'


tree = et.parse('neko.xml')
root = tree.getroot()
#ex40
cnt = 0
for stc in root.findall('sentence'):
    morph_list = []
    for chk in stc.findall('chunk'):
        for tok in chk.findall('tok'):
            feature = tok.get('feature')
            ftrs = feature.split(',')
            m = Morph()
            m.surface = tok.text
            m.base = ftrs[6]
            m.pos = ftrs[0]
            m.pos1 = ftrs[1]
            morph_list.append(m)
    cnt += 1
    if cnt == 3:
        for m in morph_list:
            sys.stdout.buffer.write(m.surface.encode('utf-8'))
