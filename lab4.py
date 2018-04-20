import bitarray

#calculates frequency of char in text, return dictionary of chars
def charFrequency(text):
    charCount={}

    for i in range(len(text)):
        pom=text[i]

        if(pom not in charCount):
            charCount[pom]=0
        charCount[pom]+=1

    for i in charCount:
        charCount[i]=(charCount[i]/len(text))

    return charCount

def create():
    return 0

#make code (change char to bin in proper way)
def makeCode():
    code = {}
    alf = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','q','p','r','s','t','u','w','x','y','z',' ','v','0','1','2','3','4','5','6','7','8','9']
    for i in alf:
        if(ord(i)>=97  and ord(i)<=122):  #for letters
            code[i] = '{0:b}'.format(ord(i)-87).rjust(6,'0')
        if(ord(i)==32): #for space (space=36 in my code (32 is 'w'))
            code[i] = '{0:b}'.format(36).rjust(6,'0')
        if(ord(i)>=48 and ord(i)<=57):  #for digits  -> 0-ascii 48, 9- ascii 57
            code[i] = '{0:b}'.format(ord(i)-48).rjust(6,'0')
    return code


#encode text to 6-bytes code
def encode(text, code):
    encodedText=[]
    for i in text:
        encodedText.append(code[i])
    return ''.join(encodedText)

#decode 6-byte code to string
def decode(textBitArray, code):
    decodedText=""
    for i in range(0,len(textBitArray)-6,6):
        #print(i)
        tmp=bitarray.bitarray()
        arr=[]
        for t in range(i,i+6):  #tmp is 6 neighboring digith that makes binary
            tmp.append(textBitArray[t])
            arr=tmp.to01()

        strTmp=getKey(code,arr)
        decodedText=decodedText+strTmp
    return decodedText


#returns key of some value
def getKey(dict, val):
    for i in dict:
        print("dict[i] ",dict[i],"val: ",val)
        if(dict[i]==val):
            return i#dict[i]
    return 0

#saves code and encoded text
def save(text, code):
    #textFile = open('./encodedFile.txt', 'wb')
    bits = bitarray.bitarray(text)
    with open('./encodedFile.txt', 'wb') as textFile:
        bits.tofile(textFile)

    codeFile = open('./code.txt', 'a')
    for i in code:
        codeFile.write(i+" "+code[i]+"\n")

'''
    bits = bitarray.bitarray(bin='0000011111')  # just an example

    with open('somefile.bin', 'wb') as fh:
        bits.tofile(fh)
'''
#returns coded text and code from file
def load():
    #text = open('./encodedFile.txt').read()
    text = bitarray.bitarray()
    with open('./encodedFile.txt', 'rb') as fh:
        text.fromfile(fh)


    codeTmp = open('./code.txt').read()
    code={}
    for i in range (0,len(codeTmp)-1,2):
        code[codeTmp[i]]=codeTmp[i+1]

    return text, code


#compare two texts, if the same returns True
def compare(text1, text2):
    if(text1==text2):
        return True
    else:
        return False


def main():
    #do zakodown
    '''
    code=makeCode()
    text = 'ala ma kota a kot ma ale'
    encoded = encode(text, code)
    decoded = decode(encoded, code)
    print("ZAKODOWANE:", encoded)
    print("ODKODOWANE:",decoded)
    print("CZY DOBRZE:", compare(text,decoded))
    '''

    text = 'ala'
    code = makeCode()
    print("CODE: ", code)
    encoded = encode(text, code)
    print("ENCODE: ",encoded)
    save(encoded,code)
    newText, loadedCode = load()
    print("NEW TEXT: ",newText)
    print("LOADED CODE: ", loadedCode)
    decoded=decode(newText,code) #!!!!ZROBIC Z LOADED CODE
    print("DECODED:", decoded)
    print("CZY DOBRZE:", compare(text, decoded))



if __name__ == '__main__':
    main()