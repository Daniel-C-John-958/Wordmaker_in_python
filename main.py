from collections import defaultdict
import json
from itertools import groupby
# reading the data from the file
with open('convert.txt') as f:
    data = f.read()
       
# reconstructing the data as a dictionary
js = json.loads(data)

def fun1(x):
    f={'a':0,'b':0,'c':0,'d':0,'e':0
    ,'f':0,'g':0,'h':0,'i':0,'j':0
    ,'k':0,'l':0,'m':0,'n':0,'o':0
    ,'p':0,'q':0,'r':0,'s':0,'t':0
    ,'u':0,'v':0,'w':0,'x':0,'y':0
    ,'z':0}
    for i in x:
        for key ,value in f.items():
            if key==i:

                f.update({i:value+1})
    #print(f)
    string=''
    for key,value in f.items():
        string+=str(value)
    #print('string is ',string)
    return string
 
S = 'ajalfhladjhfjleuoai'
l= fun1(S)
#print(fun1(S))
fin=[]
for key ,value in js.items():
    flag=True
    for i in range(26):
        if int(l[i])>=int(key[i]):
            pass
        else:
            flag=False
            break
            
    if flag:
        fin.append(value)


flatList = []
for element in fin:
    if type(element) is list:
        for item in element:
            flatList.append(item)
    else:
        flatList.append(element)


print('no of words',len(flatList))
print()


d={}
for word in flatList:
    d.setdefault(len(word), []).append(word)

result=[d[n] for n in sorted(d, reverse=True)] 


# [['sight', 'first'], ['love'], ['was'], ['at', 'It']] 
#print(d.values())
for i in result:
    if len(S)==len(i[0]):
        print('Anagrams of this word\t')
        print(i)
        print()
    else:
        print('no of {} letter words: {}\t'.format(len(i[0]),len(i)))
        print(i)
        print()
