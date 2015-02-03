__author__ = 'Aman'

def decrytion():
#For decryption
    print ("Decrypting Caesar ASCII")
    str = raw_input("Enter your input file: ")
    infile = open(str,'rb')
    data = infile.read()
    for x in range(1,256):
        decrypteddata=''
        for byte in data:
            decrypteddata = decrypteddata+chr((ord(byte)-x)%256)
        if '\n' in decrypteddata:
            print "found key! : ",  x,"\n"
            outfile = open('CaesarDecrypted.rtf','wb')
            outfile.write(decrypteddata)
            print "----------------------------DECRYPTED MESSAGE-----------------------------------"
            print decrypteddata
            print "--------------------------------------------------------------------------------"
            break
decrytion()

def encryption():
    #For trying encryption
    print ("Encrypting Caesar ASCII")
    str = raw_input("Enter your input file: ")
    x = int(raw_input("Enter the key: "))
    infile = open(str,'rb')
    data = infile.read()
    encrypteddata = ''
    for byte in data:
        encrypteddata = encrypteddata+chr((ord(byte)+x)%256)

    outfile = open('e'+str,'wb')
    outfile.write(encrypteddata)
    print encrypteddata




# x = int(raw_input("Enter the key: "))
# infile = open('a.rtf.enc','rb')
# data = infile.read()
# while(True):
#     decrypteddata = ''
#     for byte in data:
#         decrypteddata = decrypteddata+chr((ord(byte)-x) % 256)
#     print 'key = ', x
#     print '<-----------------Decrepted data------------------------------->'
#     print decrypteddata
#     x = int(raw_input("Enter the key: "))
#leave empty to break while loop