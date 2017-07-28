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
    "morphs"    #形態素のリスト
    "dst"       #係り先文節のインデックス番号
    "srcs"      #係り元文節のインデックス番号

tree = et.parse('neko.xml')
root = tree.getroot()

cnt = 0
# Chunkオブジェクトのリストのリスト
chk_in_stcs = []
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

        #Chunkオブジェクトを生成
        c = Chunk()
        c.morphs = mors_in_chk
        c.dst = chk.get("link")
        c.srcs = chk.get("id")
        chk_in_stc.append(c)

    chk_in_stcs.append(chk_in_stc)
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

#形態素のリストを受け取って,記号を除いたテキストを返す関数
def get_mor_text(morphs):
    result = ""
    for m in morphs:
        if m.pos != "記号":
            result = result + m.surface
    return result

#ex42
#係り元の文節と係り先の文節のテキストをタブ気切りで抽出する
def get_dst_srcs(chk_in_stcs):
    res = ""
    for stc in chk_in_stcs:
        dic = []
        # 各文節のテキストを索引付けする
        for chk in stc:
            dst_id = chk.dst
            dic.append(get_mor_text(chk.morphs))

        # 係り元と係り先の文節のテキストを抽出
        for chk in stc:
            dst_id = int(chk.dst)
            src_id = int(chk.srcs)
            res = res + dic[src_id] + "\t" + dic[dst_id] + "\n"

        res = res + "\n"
    return res

sys.stdout.buffer.write(get_dst_srcs(chk_in_stcs).encode('utf-8'))
