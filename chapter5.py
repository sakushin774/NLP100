import codecs
import sys
import xml.etree.ElementTree as et

#ex40
class Morph:
    'surface'
    'base'
    'pos'
    'pos1'

#ex41
class Chunk:
    "morphs"
    "dst"
    "srcs"

tree = et.parse('neko.xml')
root = tree.getroot()

cnt = 0
for stc in root.findall('sentence'):
    mors_in_stc = []
    chk_in_stc = []
    for chk in stc.findall('chunk'):
        mors_in_chk = []
        for tok in chk.findall('tok'):
            feature = tok.get('feature')
            ftrs = feature.split(',')
            m = Morph()
            m.surface = tok.text
            m.base = ftrs[6]
            m.pos = ftrs[0]
            m.pos1 = ftrs[1]
            mors_in_stc.append(m)
            mors_in_chk.append(m)

        c = Chunk()
        c.morphs = mors_in_chk
        c.dst = chk.get("link")
        c.srcs = chk.get("id")
        chk_in_stc.append(c)

    cnt += 1

    if cnt == 3:
        for m in mors_in_stc:
            sys.stdout.buffer.write(m.surface.encode('utf-8'))
        print()

    elif cnt == 8:
        for c in chk_in_stc:
            for m in c.morphs:
                sys.stdout.buffer.write(m.surface.encode('utf-8'))
            sys.stdout.buffer.write('->'.encode('utf-8'))
            for c2 in chk_in_stc:
                if c2.srcs == c.dst:
                    for m2 in c2.morphs:
                        sys.stdout.buffer.write(m2.surface.encode('utf-8'))

            print()
