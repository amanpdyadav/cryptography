__author__ = 'Aman'
def Listofchar():
    infile = open('file2-39059.txt.enc','rb')
    data = infile.read()

    dataarray=[]
    matchlistpercent = []
    for byte in data:
        dataarray.append(ord(byte))

    for i in range(1, len(dataarray)):
        count =0.0
        for j in range(1, i):
           count += matchlist(dataarray, rotate(dataarray,j))
        num = ("%0.3f" %  (count/i))
        matchlistpercent.append(str(num)+'000'+str(i))
    print keylengthlist(sortinglist(matchlistpercent))
    print sortinglist(matchlistpercent)

def sortinglist(list):
    numbers = map(float, list)
    output = []
    while numbers:
        smallest = min(numbers)
        index = numbers.index(smallest)
        output.append(numbers.pop(index))
    return output[::-1]

def keylengthlist(list):
    key=[]
    for i in range(0, 15):
        length=((str(list[i]).split('.'))[1])
        num=''
        for j in range(3, len(length)):
            num += str(length[j])
        key.append(int(num))
    return key

def matchlist(first, second):
    counter = 0
    for i in range(1, len(first)):
        if(first[i-1] == second[i-1]):
            counter += 1
    return counter

def rotate(l,n):
    return l[n:] + l[:n]

Listofchar()


