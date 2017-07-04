import sys
import re
import random

def print_ary(str, ary):
    print(str + ",".join(ary))


#ex0
str0 = "stressed"
rev_str = str0[::-1]
print("ex0:" + rev_str)



#ex1
str1 = "パタトクカシーー"
ex1 = ""
for i in range(0, len(str1), 2):
    ex1 = ex1 + str1[i]
sys.stdout.buffer.write(("ex1:" + ex1 + "\n").encode("utf-8"))



#ex2
ptcar = "パトカー"
taxi = "タクシー"
ex2 = ""
for i in range(0, min(len(ptcar), len(taxi))):
    ex2 = ex2 + ptcar[i] + taxi[i]
sys.stdout.buffer.write(("ex2:" + ex2 + "\n").encode("utf-8"))



#ex3
str3 = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
terms3 = re.sub("[^a-zA-Z ]", "", str3).split(" ")
ex3 = []
for t in terms3:
    ex3.append(str(len(t)))
print("ex3:" + ",".join(ex3))

## ex3の題意を勘違いして作った
## aからzまでのアルファベットの出現回数を数える
## 大文字小文字は区別しない
# for i in range(0, 26):
#     ex3.append(str(str3.count(chr(ord("a") + i)) + str3.count(chr(ord("A") + i))));
# ex3 = ",".join(ex3)
# print("ex3:" + ex3)



#ex4
str4 = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
terms4 = re.sub("[^a-zA-Z ]", "", str4).split(" ")
ex4 = {}
pos4 = 1
for t in terms4:
    if pos4 in [1, 5, 6, 7, 8, 9, 15, 16, 19]:
        ex4 [t[0]] = pos4
    else:
        ex4 [t[0:2]] = pos4
    pos4 += 1
print("ex4:" + ",".join(ex4))



#ex5
def term_n_gram(n, str):
    terms = str.split(" ")
    ary = []
    for i in range(0, len(terms)-n+1):
        n_gram_term = ""
        for j in range(0, n):
            n_gram_term += terms[i+j] + "-"
        n_gram_term = n_gram_term[:-1]
        ary.append(n_gram_term)
    return list(set(ary)) #重複を削除

print("ex5:" + ",".join(term_n_gram(2, "I am an NLPer")))

def char_n_gram(n, str):
    ary = []
    str = re.sub(" ", "", str)
    for i in range(0, len(str)-n+1):
        n_gram_chr = ""
        for j in range(0, n):
            n_gram_chr += str[i+j]
        ary.append(n_gram_chr)
    return list(set(ary)) #重複を削除

print("ex5:" + ",".join(char_n_gram(2, "I am an NLPer")))



#ex6
print(",".join(char_n_gram(2, "paraparaparadise")))
def union_intersection_difference(list1, list2):
    union = list1 + list2
    intersection = []
    for i in list1:
        if i in list2:
            intersection.append(i)
    difference = union
    for i in intersection:
        difference.remove(i)
    print ("ex6:")
    print_ary("union:", union)
    print_ary("intersection:", intersection)
    print_ary("difference:", difference)

x = char_n_gram(2,"paraparaparadise")
y = char_n_gram(2, "paragraph")
union_intersection_difference(x, y)

print("\"se\" is in X: " + str("se" in x))
print("\"se\" is in Y: " + str("se" in y))



#ex7
def x_jino_y_ha_z(x, y, z):
    return str(x) + "時の" + str(y) + "は" + str(z)
print("ex7:")
sys.stdout.buffer.write(x_jino_y_ha_z(12, "気温", 22.4).encode("utf-8"))
print("")



#ex8
def cipher(str):
    i = 0
    for c in str:
        if re.compile("[a-z]").match(c):
            str = str[:i] + chr(219 - ord(c)) + str[i+1:]
        i += 1
    return str
print(cipher("sakushin774@gmail.com"))
print(cipher(cipher("sakushin774@gmail.com")))



test = [1, 2, 3, 4, 5]
random.shuffle(test)

#ex9
def typoglycemia(str):
    terms = str.split(" ")
    i = 0
    for t in terms:
        if len(t) >4:
            l = list(t[1:-1])
            random.shuffle(l)
            terms[i] = t[0] + "".join(l) + t[-1]
        i += 1
    return " ".join(terms)
print("ex9: " + typoglycemia("I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."))
