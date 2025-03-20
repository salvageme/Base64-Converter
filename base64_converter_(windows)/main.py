import pickle
import os


def encode():
    os.system('cls')
    print(r'''    ______   _   __   ______   ____     ____     ______
   / ____/  / | / /  / ____/  / __ \   / __ \   / ____/
  / __/    /  |/ /  / /      / / / /  / / / /  / __/   
 / /___   / /|  /  / /___   / /_/ /  / /_/ /  / /___   
/_____/  /_/ |_/   \____/   \____/  /_____/  /_____/   
                                                       ''')

    x=input("Enter text to be encoded: ")
    print('')
    asc1=''
    val=''

    for i in range(0,len(x)):
        n=ord(x[i])
        b=str(bin(n)[2:])
        if len(b)<8:
            w=8-len(b)
            b=('0'*w)+b
        asc1+=b

    print(asc1)
    if len(asc1)%6!=0:
        asc=asc1+'0'*(6-len(asc1)%6)
        print(asc)
    else:
        asc=asc1
    
    for i in range(0,len(asc),6):
        bas=asc[i:i+6]
        f=open("binary.dat",'rb')
        try:
            while True:
                r=pickle.load(f)
                y=r[1]
                if len(y)<6:
                    y='0'*(6-len(y))+y    
                if y==bas:
                    val+=r[0]

        except EOFError:
            f.close()

    if len(asc1)%6==4:
        val=val+'='
    if len(asc1)%6==2:
        val=val+'=='
    
    os.system('cls')
    print("The encoded text is:")
    print('')
    print(val)
    print('')
    input('Press Enter to continue.')
    os.system('cls')



def decode():
    os.system('cls')
    print(r'''    ____     ______   ______   ____     ____     ______
   / __ \   / ____/  / ____/  / __ \   / __ \   / ____/
  / / / /  / __/    / /      / / / /  / / / /  / __/   
 / /_/ /  / /___   / /___   / /_/ /  / /_/ /  / /___   
/_____/  /_____/   \____/   \____/  /_____/  /_____/   
                                                       ''')

    x=input("Paste the Base64 code here: ")
    print('')
    l=[]
    bas=''
    val=''

    for i in range(len(x)):
        if x[i]=='=':
            continue
        else:
            l.append(x[i])
    
    for i in l:
        f=open("binary.dat",'rb')
        try:
            while True:
                r=pickle.load(f)
                if i==r[0]:
                    b=r[1]
                    bas=bas+b
                    break
                else:
                    continue
    
        except EOFError:
            f.close()

    if len(bas)%8!=0:       
        bas=bas.rstrip('0')

    for i in range(0,len(bas),8):
        asc=bas[i:i+8]
        asc1=int(asc,2)
        val+=chr(asc1)

    os.system('cls')
    print("The decoded text is:")
    print('')
    print(val)
    print('')
    input('Press Enter to continue.')
    os.system('cls')



### MAIN ###
while True:
    print(r'''        ____  ___   _____ ______     _____ __ __       ______                           __           
       / __ )/   | / ___// ____/    / ___// // /      / ____/___  ____ _   _____  _____/ /____  _____
      / __  / /| | \__ \/ __/      / __ \/ // /_     / /   / __ \/ __ \ | / / _ \/ ___/ __/ _ \/ ___/
     / /_/ / ___ |___/ / /___     / /_/ /__  __/    / /___/ /_/ / / / / |/ /  __/ /  / /_/  __/ /    
    /_____/_/  |_/____/_____/     \____/  /_/       \____/\____/_/ /_/|___/\___/_/   \__/\___/_/ ''')
    print("Welcome!")
    print("What would you like to do?")
    print('1. Encode')
    print('2. Decode')
    print('3. Exit')
    a=input('(1/2/3): ')

    if a=='1':
        encode()
    elif a=='2':
        decode()
    elif a=='3':
        os.system('cls')        
        print('Exiting...')
        break
    else:
        print("Invalid option!")
        input('Press Enter to continue.')
        os.system('cls')

#