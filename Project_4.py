#Question Statement
"""Creating a Caesar Cipher: an encryption technique.
a key is set which helps shift the alphabets of the text for encryption,
which is turn will be used to decrypt the text message."""

d=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
final=""

def encrypt(sentence, key):
    # print("en ans")
    for each in sentence:
        if each in d:
            pos=d.index(each)
            res=d[pos+key]
    print(final+res)


def decrypt(sentence,key):
    # print('dc ans')
    for each in sentence:
        if each in d:
            pos=d.index(each)
            res=d[pos-key]
    print(final+res)


repeat="y"
while repeat=="y":
    ans=input("Type 'encrypt' for performing encryption and 'decrypt' for performing decryption: \n")
    sen=input("Type your message: \n")
    k=int(input("Type the shift number"))
    
    if ans== "encrypt":
        encrypt(sen,k)
                
    elif ans =="decrypt":
        decrypt(sen,k)
    
    repeat=input("Type 'y' if you wanna go again, otherwise type 'n'. ")
