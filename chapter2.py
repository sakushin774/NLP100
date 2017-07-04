#coding:utf-8

import codecs
import sys
import math
f = codecs.open('hightemp.txt', 'r', 'utf-8')

raw = 0
replaced_tab = []
col1 = []
col2 = []
for line in f.readlines():
    raw += 1    #ex10
    replaced_tab.append(line.replace('\t', ' ').encode('utf-8'))    #ex11
    col1.append((line.split('\t')[0] + '\n').encode('utf-8'))   #ex12
    col2.append((line.split('\t')[1] + '\n').encode('utf-8'))   #ex12

print('ex10: ' + str(raw))
f.close()
new_f = open('new_hightemp.txt', 'w')
new_f.buffer.writelines(replaced_tab)
new_f.close()
col1_f = open('col1.txt', 'w')
col1_f.buffer.writelines(col1)
col1_f.close()
col2_f = open('col2.txt', 'w')
col2_f.buffer.writelines(col2)
col2_f.close()

#ex13
col1_f = codecs.open('col1.txt', 'r', 'utf-8')
col2_f = codecs.open('col2.txt', 'r', 'utf-8')
merge = []
merge_f = open('merge.txt', 'w')
for line1 in col1_f.readlines():
    line2 = col2_f.readline()
    merge.append((line1.replace('\n', '') + '\t' + line2).encode('utf-8'))
merge_f.buffer.writelines(merge)
col1_f.close()
col2_f.close()
merge_f.close()


#ex14
f = codecs.open('hightemp.txt', 'r', 'utf-8')
print('ex14:')
ex14_n = int(sys.stdin.readline())
for i in range(ex14_n):
    line = f.readline()
    sys.stdout.buffer.write(line.encode('utf-8'))
f.close()


#ex15
f = codecs.open('hightemp.txt', 'r', 'utf-8')
print('ex15:')
ex15_n = int(sys.stdin.readline())
i = 0
for line in f.readlines():
    if i in range(raw - ex15_n, raw):
        sys.stdout.buffer.write(line.encode('utf-8'))
    i += 1
f.close()


# ex16
f = codecs.open('hightemp.txt', 'r', 'utf-8')
print('ex:16')
ex16_n = int(sys.stdin.readline())
raw_block = math.ceil(raw / ex16_n)
divide = []
i = 0
for line in f.readlines():
    if i % raw_block == 0 and i != 0:
        divide.append('\n'.encode('utf-8'))
    divide.append(line.encode('utf-8'))
    i += 1
divide_f = open('divide.txt', 'w')
divide_f.buffer.writelines(divide)
f.close()
divide_f.close()


#ex17
print('ex17:')
f = codecs.open('hightemp.txt', 'r', 'utf-8')
chars = []
for line in f.readlines():
    col = line.split('\t')[0]
    for c in col:
        if not(c in chars):
            chars.append(c)
sys.stdout.buffer.write((','.join(chars) + '\n').encode('utf-8'))
f.close()


# ex18
print('ex18:')
f = codecs.open('hightemp.txt', 'r', 'utf-8')
hash_ex18 = {}
for line in f.readlines():
    hash_ex18[line] = line.split('\t')[2]
for key, value in sorted(hash_ex18.items(), key = lambda x: x[1]):
    sys.stdout.buffer.write(key.encode('utf-8'))
f.close()

# ex19
print('ex19:')
f = codecs.open('hightemp.txt', 'r', 'utf-8')
hash_ex19 = {}
for line in f.readlines():
    col = line.split('\t')[0]
    for c in col:
        if c in hash_ex19:
            hash_ex19[c] += 1
        else:
            hash_ex19[c] = 1
for key, value in sorted(hash_ex19.items(), key = lambda x: -x[1]):
    sys.stdout.buffer.write((key).encode('utf-8'))
print('')
f.close()
