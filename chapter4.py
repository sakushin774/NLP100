import sys
import codecs
import matplotlib.pyplot as plt
import numpy as np

#ex30
f = codecs.open('neko.txt.mecab', 'r', 'utf-8')
mor_strs_list = []
mor_list = []
mor_hash = {}
for line in f.readlines():
    if line == 'EOS\n':
        mor_strs_list.append(mor_list)
        mor_list = []
        continue
    div_tab = line.split('\t')
    div_comma = div_tab[1].split(',')
    mor_hash['surface'] = div_tab[0]
    mor_hash['base'] = div_comma[6]
    mor_hash['pos'] = div_comma[0]
    mor_hash['pos1'] = div_comma[1]
    mor_list.append(mor_hash)
    mor_hash = {}
    # for value in mor_hash.values():
    #     sys.stdout.buffer.write(value.encode('utf-8'))
f.close()


#ex31
verb_surfs = []
for ml in mor_strs_list:
    for mh in ml:
        if mh['pos'] == '動詞':
            verb_surfs.append(mh['surface'])
            # sys.stdout.buffer.write(mh['surface'].encode('utf-8'))

#ex32
verb_bases = []
for ml in mor_strs_list:
    for mh in ml:
        if mh['pos'] == '動詞':
            verb_bases.append(mh['base'])
            # sys.stdout.buffer.write(mh['base'].encode('utf-8'))

#ex33
noun_sahens = []
for ml in mor_strs_list:
    for mh in ml:
        if mh['pos'] == '名詞' and mh['pos1'] == 'サ変接続':
            noun_sahens.append(mh)

#ex34
nouns_connected_by_no = []
def noun_no_noun(morlist):
    for ml in mor_strs_list:
        for (i, mh) in enumerate(ml):
            if mh['surface'] == 'の' and i > 0 and i+1 < len(ml) \
              and ml[i-1]['pos'] == '名詞' and ml[i+1]['pos'] == '名詞':
                noun_phrase = ml[i-1]['surface'] + ml[i]['surface'] + ml[i+1]['surface'] + ','
                nouns_connected_by_no.append(noun_phrase.encode('utf-8'))
                sys.stdout.buffer.write(noun_phrase.encode('utf-8'))


#ex35:名詞の連結の抽出
#リストを先頭から見て名詞が続けば最長一致で返す。
#先頭が名詞でなければ空リストを返す。
def get_str_nouns(mslist):
    for ml in mslist:
        bfr = []
        for mh in ml:
            if mh['pos'] == '名詞':
                bfr.append(mh['surface'])
            elif bfr != []:
                print(','.join(bfr))
                bfr = []
# print('ex35')
#get_str_nouns(mor_strs_list)

#ex36:単語の出現頻度を求める
#キー:単語の基本形, 値:単語の出現回数 のハッシュを返す
def get_tf_ranking(mslist):
    tf_hash = {}
    for ml in mslist:
        for mh in ml:
            base = mh['base']
            if base in tf_hash:
                tf_hash[base] += 1
            else:
                tf_hash[base] = 0
    return tf_hash

#出現頻度上位100件を表示
print('ex36')
tf = []
term = []
for k,v in sorted(get_tf_ranking(mor_strs_list).items(), key=lambda x:x[1], reverse=True)[1:100]:
    tf.append(v)
    term.append(k)
    print(k)


#ex37:出現頻度の高い10語を棒グラフで表示
left = np.array(t for t in term)
height = np.array(tf for tf in term)
plt.bar(left=term, height=tf)
