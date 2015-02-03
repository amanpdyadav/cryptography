__author__ = 'Aman'
#Creates and returns an array of numbers, the index corresponds to the ascii number and the value is the frequency in the text
def countcharacter():
    infile = open('file3-39059.txt.enc','rb')
    data = infile.read()
    letterFrequencyIndata = [0]*256
    for ascii in data:
        letterFrequencyIndata[ord(ascii)] += 1
    index = 0
    occuringstring=''
    for i in letterFrequencyIndata:
        occuringstring = occuringstring + chr(index) +" occurs " +str(i)+" times"+'\n'
        index = index +1
    #Count the frequency of a character and write it to a text file
    outfile = open('FrequecyCount.txt','wb')
    outfile.write(occuringstring)
    return letterFrequencyIndata

def change_letters(letterFrequencyIndata):
    #Frequency table for the english table considering space to have the highest frequency
    frequencylist = []
    for c in ' etaoinsrhdlucmwfywgpbvkxqjzASERBTMLNPOIDCHGKFJUW.!Y*@V-ZQX_$,?;&`\)': #' etaoinsrhdlucmwfywgpbvkxqjz'
        frequencylist.append(c)

    infile = open('file3-39059.txt.enc','rb')
    decryptedarray = ['']*256
    data = infile.read();
    for i in range(len(frequencylist)):
        m = letterFrequencyIndata.index(max(letterFrequencyIndata))
        decryptedarray[m]=frequencylist[i]
        letterFrequencyIndata[m]= -1

    key=''
    keysymbol = ''
    for c in decryptedarray:
        if(len(c)>0):
            key=key+str(ord(c))+'\n'
        else:
            key=key+str(-1)+'\n'
        keysymbol += c +'\n'

    keysymbolfile = open('keysymbol.txt','wb')
    keysymbolfile.write(keysymbol)

    keyfile=open('keyfile.txt','wb')
    keyfile.write(key)

    decryptedmessage=''
    for ascii in data:
        decryptedmessage += decryptedarray[ord(ascii)]

    outfile = open('message.txt','wb')
    outfile.write(decryptedmessage)

    print decryptedmessage
change_letters(countcharacter())

