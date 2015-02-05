__author__ = 'Aman'
from itertools import starmap, cycle
regrex = ''
for i in range(0,255):
    regrex += chr(i)

def encrypt(message, key):
    def enc(c,k): return chr(((ord(k) + ord(c)) % 256))
    return "".join(starmap(enc, zip(message, cycle(key))))

def decrypt(message, key):
    def dec(c,k): return chr(((ord(c) - ord(k)) % 256))
    return "".join(starmap(dec, zip(message, cycle(key))))

def rotate(l,n):
    return l[n:] + l[:n]

def findcharactertomatch(ch, match):
    character = ''
    for c in regrex:
        if (decrypt(ch,c) == match):
            character = c
    return character

def findkey(keyportion, wordTomatch, file):
    infile = open(file,'rb')
    encr = infile.read()
    keylist = []
    for c in regrex:
        if((decrypt(encr, c)).count(wordTomatch) > 0):
            keylist.append((decrypt(encr, keyportion+c)).index(wordTomatch))
    return keylist

def keylist(key):
    keydata=''
    for x in range(1,256):
        decrypteddata=''
        for byte in key:
            decrypteddata = decrypteddata+chr((ord(byte)-x)%256)
        keydata=keydata+decrypteddata+'\n'
    return keydata

def toguessthekey(file, name):
    newlinepos = findkey('','\n', file)
    infile = open(file,'rb')
    data = infile.read()
    keylist = []
    str = '\n* Hello, '+name
    for i in newlinepos:
        newstr =''
        for pos in range(0, len(str)):
            if findcharactertomatch(data[i+pos], str[pos]) == '':
                break
            else:
                newstr += findcharactertomatch(data[i+pos], str[pos])
        keylist.append(newstr+'\n')
    return keylist

def is_ascii(s):
    return all(ord(c) < 128 for c in s)

def solved(file, name):
    for k in toguessthekey(file, name):
        if is_ascii(k):
            print k
        #here in k 'rewvfjn,mbjfdhrewvfj' we can see that 'rewvfj' is repeted so the actual key len is len('rewvfjn,mbjfdh') which is 14
        lengthofkey = 14
        key = ''
        listofkeychar = list(k)
        if len(listofkeychar) >= lengthofkey:
            for val in range(0,lengthofkey):
                key += listofkeychar[val]
            for i in range(0,len(key)):
                mesg = decrypt(open(file,'rb').read(), ''.join(''.join(rotate(list(key), i)).split('\n')))
                if '* Hello, '+name in mesg:#This line is known to the hacker
                    print 'key = '+''.join(''.join(rotate(list(key), i)).split('\n'))
                    print mesg

def main(file, name):
    fname = name.split(' ')[0]
    lname = name.split(' ')[1]
    solved(file, fname + ' ' + lname)
    solved(file, lname + ' ' + fname)
    solved(file, fname + ' ')
    solved(file, lname + ' ')

main('file2-39059.txt.enc', 'Aman Yadav')
# solvedwithkey('rewvfjn,mbjfdh', 'file2-39059.txt.enc')



