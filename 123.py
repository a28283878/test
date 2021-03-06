#!/usr/bin/env python3

from tkinter import *                   #python GUI

#Initial Permutation (IP)       64
IP = [58,50,42,34,26,18,10, 2,
      60,52,44,36,28,20,12, 4,
      62,54,46,38,30,22,14, 6,
      64,56,48,40,32,24,16, 8,
      57,49,41,33,25,17, 9, 1,
      59,51,43,35,27,19,11, 3,
      61,53,45,37,29,21,13, 5,
      63,55,47,39,31,23,15, 7]

#Final Permutation (IP**-1)     64
FP = [40,  8, 48, 16, 56, 24, 64, 32,
      39,  7, 47, 15, 55, 23, 63, 31,
      38,  6, 46, 14, 54, 22, 62, 30,
      37,  5, 45, 13, 53, 21, 61, 29,
      36,  4, 44, 12, 52, 20, 60, 28,
      35,  3, 43, 11, 51, 19, 59, 27,
      34,  2, 42, 10, 50, 18, 58, 26,
      33,  1, 41,  9, 49, 17, 57, 25]

#F_Function expansion           32 to 48
expansion = [32, 1, 2, 3, 4, 5,
              4, 5, 6, 7, 8, 9,
              8, 9,10,11,12,13,
             12,13,14,15,16,17,
             16,17,18,19,20,21,
             20,21,22,23,24,25,
             24,25,26,27,28,29,
             28,29,30,31,32, 1]

#F_Function permutation         32
permutation = [16, 7,20,21,29,12,28,17,
                1,15,23,26, 5,18,31,10,
                2, 8,24,14,32,27, 3, 9,
               19,13,30, 6,22,11, 4,25]

#Substitution Box               [3][16]
S1=[14,  4, 13,  1,  2, 15, 11,  8,  3, 10,  6, 12,  5,  9,  0,  7,
     0, 15,  7,  4, 14,  2, 13,  1, 10,  6, 12, 11,  9,  5,  3,  8,
     4,  1, 14,  8, 13,  6,  2, 11, 15, 12,  9,  7,  3, 10,  5,  0,
    15, 12,  8,  2,  4,  9,  1,  7,  5, 11,  3, 14, 10,  0,  6, 13]

S2=[15,  1,  8, 14,  6, 11,  3,  4,  9,  7,  2, 13, 12,  0,  5, 10,
     3, 13,  4,  7, 15,  2,  8, 14, 12,  0,  1, 10,  6,  9, 11,  5,
     0, 14,  7, 11, 10,  4, 13,  1,  5,  8, 12,  6,  9,  3,  2, 15,
    13,  8, 10,  1,  3, 15,  4,  2, 11,  6,  7, 12,  0,  5, 14,  9]

S3=[10,  0,  9, 14,  6,  3, 15,  5,  1, 13, 12,  7, 11,  4,  2,  8,
    13,  7,  0,  9,  3,  4,  6, 10,  2,  8,  5, 14, 12, 11, 15,  1,
    13,  6,  4,  9,  8, 15,  3,  0, 11,  1,  2, 12,  5, 10, 14,  7,
     1, 10, 13,  0,  6,  9,  8,  7,  4, 15, 14,  3, 11,  5,  2, 12]

S4=[ 7, 13, 14,  3,  0,  6,  9, 10,  1,  2,  8,  5, 11, 12,  4, 15,
    13,  8, 11,  5,  6, 15,  0,  3,  4,  7,  2, 12,  1, 10, 14,  9,
    10,  6,  9,  0, 12, 11,  7, 13, 15,  1,  3, 14,  5,  2,  8,  4,
     3, 15,  0,  6, 10,  1, 13,  8,  9,  4,  5, 11, 12,  7,  2, 14]

S5=[ 2, 12,  4,  1,  7, 10, 11,  6,  8,  5,  3, 15, 13,  0, 14,  9,
    14, 11,  2, 12,  4,  7, 13,  1,  5,  0, 15, 10,  3,  9,  8,  6,
     4,  2,  1, 11, 10, 13,  7,  8, 15,  9, 12,  5,  6,  3,  0, 14,
    11,  8, 12,  7,  1, 14,  2, 13,  6, 15,  0,  9, 10,  4,  5,  3]

S6=[12,  1, 10, 15,  9,  2,  6,  8,  0, 13,  3,  4, 14,  7,  5, 11,
    10, 15,  4,  2,  7, 12,  9,  5,  6,  1, 13, 14,  0, 11,  3,  8,
     9, 14, 15,  5,  2,  8, 12,  3,  7,  0,  4, 10,  1, 13, 11,  6,
     4,  3,  2, 12,  9,  5, 15, 10, 11, 14,  1,  7,  6,  0,  8, 13]

S7=[ 4, 11,  2, 14, 15,  0,  8, 13,  3, 12,  9,  7,  5, 10,  6,  1,
    13,  0, 11,  7,  4,  9,  1, 10, 14,  3,  5, 12,  2, 15,  8,  6,
     1,  4, 11, 13, 12,  3,  7, 14, 10, 15,  6,  8,  0,  5,  9,  2,
     6, 11, 13,  8,  1,  4, 10,  7,  9,  5,  0, 15, 14,  2,  3, 12]

S8=[13,  2,  8,  4,  6, 15, 11,  1, 10,  9,  3, 14,  5,  0, 12,  7,
     1, 15, 13,  8, 10,  3,  7,  4, 12,  5,  6, 11,  0, 14,  9,  2,
     7, 11,  4,  1,  9, 12, 14,  2,  0,  6, 10, 13, 15,  3,  5,  8,
     2,  1, 14,  7,  4, 10,  8, 13, 15, 12,  9,  0,  3,  5,  6, 11]

S_BOX = [S1,S2,S3,S4,S5,S6,S7,S8]


#Permuted Choice 1 (PC-1)           64 to 56
PC_1=[57, 49, 41, 33, 25, 17,  9,
       1, 58, 50, 42, 34, 26, 18,
      10,  2, 59, 51, 43, 35, 27,
      19, 11,  3, 60, 52, 44, 36,
      63, 55, 47, 39, 31, 23, 15,
       7, 62, 54, 46, 38, 30, 22,
      14,  6, 61, 53, 45, 37, 29,
      21, 13,  5, 28, 20, 12,  4]

#Permuted Choice 2 (PC-2)           56 to 48
PC_2 =[14, 17, 11, 24,  1,  5,
        3, 28, 15,  6, 21, 10,
       23, 19, 12,  4, 26,  8,
       16,  7, 27, 20, 13,  2,
       41, 52, 31, 37, 47, 55,
       30, 40, 51, 45, 33, 48,
       44, 49, 39, 56, 34, 53,
       46, 42, 50, 36, 29, 32]

def xor_func(arrayA,arrayB):                # xor two binary array or string
    result=""
    for i in range(len(arrayA)):
        result+=str(int(arrayA[i])^int(arrayB[i]))
    return result

def shift(array,mode,n):                    #shift right or left n bit
    if mode=="r":
        n=-n
    return array[n:]+array[:n]

def product(data,key,n,mode):               #product cipher
    result=""
    if mode==1:
        for i in range(n):
            result+=data[key[i]-1]
    else:
        for i in range(1,n+1):
            result+=data[key.index(i)]
    return result

def key_schedule(key):                      #schedule 16 times key
    r_t=[1,1,2,2,2,2,2,2,1,2,2,2,2,2,2,1]
    f_key = product(key,PC_1,56,1)
    result=[None for i in range(16)]
    L=f_key[:28]
    R=f_key[28:]
    for i in range(16):
        L=shift(L,"l",r_t[i])
        R=shift(R,"l",r_t[i])
        result[i]=product(L+R,PC_2,48,1)

    return result


def F_func(data,k):                         #f-function
    temp = product(data,expansion,48,1)
    temp = xor_func(temp,k)
    result="" 
    for i in range(8):
        S=temp[i*6:(i+1)*6] 
        row = int(S[::5],2)
        column = int(S[1:-1],2)
        t = S_BOX[i][row*16+column]
        result+=bin(t)[2:].zfill(4)
    result = product(result,permutation,32,1)
    return result


#############################################################################
def DES(data,key):
    result = product(data,IP,64,1)    #inital permutation
    keyarray=key_schedule(key)
    #print(keyarray)
    for i in range(16):
        L=result[:32]
        R=result[32:]
        # if i == 0:
        #   print(L+R)
        #   print(F_func(R,keyarray[0]))
        #   print(xor_func(L,F_func(R,keyarray[0])))
        result=R
        result+=xor_func(L,F_func(R,keyarray[i]))
        #print(result)
    result = result[32:] + result[:32]
    result = product(result,FP,64,1)    #final permutation

    return result
# 000011110100000111011001000100000000000010000100
# 000011110100000111011001000100000000000010000100   
# 000111110100100110011001000000000010000010000001
# 000111110100000110011001000000000010000010000001
def de_DES(data,key):
    result = product(data,FP,64,2)
    result = result[32:] + result[:32]
    keyarray = key_schedule(key)
    for i in range(16):
        L=result[:32]
        R=result[32:]
        result=xor_func(R,F_func(L,keyarray[15-i]))
        result+=L

    result = product(result,IP,64,2)

    return result
#############################################################################


#####    GUI   #####
def encodeMethod():
    plaintext="1111101011111010111110101111101011111010111110101111101011111010"
    key="1010111110101111101011111010111110101111101011111010111110101111"
    result = DES(plaintext,key)
    print(result)
    #c_text.set(result)
    #result_value["text"]=result
    #1011000000011010000100001011101010111100100110100000001111011010

def decodeMethod():
    cipher="1011110111100001101101110001110110100010001111010110111011000011"
    key="1010111110101111101011111010111110101111101011111010111110101111"
    result = de_DES(cipher,key)
    print(result)
    # p_text.set(result)
    # result_value["text"]=result

encodeMethod()
decodeMethod()
# root = Tk()
# root.title("DES")

# plain_label  = Label(root,width=10,height=5,text="Plaintext : ")
# plain_label.grid(row=0,column=0)
# key_label  = Label(root,width=10,height=5,text="Key : ")
# key_label.grid(row=1,column=0)
# cipher_label = Label(root,width=10,height=5,text="Cipher : ")
# cipher_label.grid(row=2,column=0)

# p_text=StringVar()
# plain_entry = Entry(root,width=70,font=("Purisa", 10),textvariable=p_text)
# plain_entry.focus_set()
# plain_entry.grid(row=0,column=1,columnspan=6,padx=(10,40))
# key_entry =Entry(root,width=70,font=("Purisa",10))
# key_entry.grid(row=1,column=1,columnspan=6,padx=(10,40))
# c_text=StringVar()
# cipher_entry =Entry(root,width=70,font=("Purisa",10),textvariable=c_text)
# cipher_entry.grid(row=2,column=1,columnspan=6,padx=(10,40))

# result_label = Label(root,width=10,height=5,text="result : ")
# result_label.grid(row=3,column=0)
# result_value = Label(root,width=70,height=5,text="")
# result_value.grid(row=3,column=1,columnspan=8,padx=(10,40))

# Encode_button = Button(root,text="DES encode",command=encodeMethod)
# Encode_button.grid(row=5,column=4,pady=(20,40))
# Decode_button = Button(root,text="DES decode",command=decodeMethod)
# Decode_button.grid(row=5,column=5,pady=(20,40))


# root.mainloop()