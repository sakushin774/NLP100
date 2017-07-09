import CaboCha
import sys
import codecs

c = CaboCha.Parser()
f_read = codecs.open('neko.txt', 'r', 'utf-8')
f_write = open('neko.txt.cabocha', 'w')

for s in f_read.readlines():
    # sys.stdout.buffer.write(c.parseToString(s).encode('utf-8'))
    # f_write.buffer.write(c.parseToString(s).encode('utf-8'))

    tree =  c.parse(s)
    f_write.buffer.write(tree.toString(CaboCha.FORMAT_TREE).encode('utf-8'))
    f_write.buffer.write(tree.toString(CaboCha.FORMAT_LATTICE).encode('utf-8'))


f_read.close()
f_write.close()
