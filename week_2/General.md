# Encoding.md

## Challenge 1:
Here we have given a list of numbers and we get ouur flag with them so I used the following code  

    list = [99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]  
    print("".join(chr(i) for i in list))  

so I got the flag as:
>crypto{ASCII_pr1nt4bl3}

## Challenge 2:
now I have given a hex string for decoding it i use the following python code:

    hex_s= '63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d'
    hex_split=[hex[i:i+2] for i in range(0,len(hex),2)]
    print("".join(chr(int(j,16)) for j in hex_split))

and the output gives :
>crypto{You_will_be_working_with_hex_strings_a_lot}

## challenge 3:
for the next challenge we have decode the strings into bytes and then we have to encode it again to base64 format.  

    >>>import base64
    >>>string=bytes.fromhex("72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf")
    >>> base_=base64.b64encode(string)
    >>> print(base_)

we got the following flag then:
> crypto/Base+64+Encoding+is+Web+Safe/

## challenge 4:
Here the long number should be encoded into hexa format so that we can get the flag.

    from Crypto import *
    num=11515195063862318899931685488813747395775516287289682636499965282714637259206269
    numhex=long_to_bytes(num)
    print(numhex)

The flag is found to be:
>crypto{3nc0d1n6_4ll_7h3_w4y_d0wn}

# XOR

## challenge 1:
It is given that we should xor the string "label" with the integer 13 so we get a string that should be our flag.

    import pwn
    print(pwn.xor(13,'label'))
so I got the flag as:
> crypto{aloha}

## challenge 2:

```
KEY1=a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313
KEY2 ^ KEY1 = 37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e
KEY2 ^ KEY3 = c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1
FLAG ^ KEY1 ^ KEY3 ^ KEY2 = 04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf
```

Here we know 
> Identity: A ⊕ 0 = A  
Self-Inverse: A ⊕ A = 0

so if we xor FLAG ^ KEY1 ^ KEY3 ^ KEY2 with KEY2 ^ KEY3  we get  
FLAG ^ KEY1 ^ KEY3 ^ 0 ^ KEY3  
=> FLAG ^ KEY1 
NOW AGAIN  xoring the result with key1 gives the the flag.
```
from Crypto import *

x1=bytes.fromhex("04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf")
x2=bytes.fromhex("c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1")

import pwn

x3=xor(x1,x2)
x3=pwn.xor(x1,x2)
x4=bytes.fromhex("a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313")
x5=pwn.xor(x3,x4)

print(x5.decode("utf-8"))
```

so we get the flag as:
>crypto{x0r_i5_ass0c1at1v3}

Here we converted each number into bytes and then we xored it and then decoded into "utf-8"
 encoding.  
## challenge 3:
For this we don't know the number that it should be xored with so we just bruteforced it with the following script:
```
import pwn

lists=[]
a=bytes.fromhex("73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d")

for i in range(256):
	x=pwn.xor(a,i)
	if x.find("crypto")!=-1:
		print(x)
		break
	lists.append(pwn.xor(a,i))

```
it is listed so we can also find the bit it should be xored with by using .index() method.

so the flag is:
>crypto{0x10_15_my_f4v0ur173_by7e}

## Challenge 4:
Here the password to the key is unknown but we can crack it with a bit of logic:  
xor(a,b)=c  
then, xor(c,a)=b as  
xor(a,a)=0,    
xor(b,0)=b
so we know that the flag is in the form of crypto{*}
sow I used the following script:
```
import pwn

a=bytes.fromhex("0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104")
print(pwn.xor(a,b"crypto{000000}"))
```
so with the output I realized that the key is :
>myXORkey

so the flag is found to be:
>crypto{1f_y0u_Kn0w_En0uGH_y0u_Kn0w_1t_4ll}

# Mathematics
## challenge 1:
here we have to write a code for finding gcd of two numbers:
```
def gcd(a,b):
	
	if a%b == 0 :
		return b
	else:
		return gcd(b,a%b)
print(gcd(66528,52920))
```
so I got the number as:
>1512

## challenge 2:
Here we are asked the code for extended gcd coefficients.  
before that we discuss few things :  
1.  gcd of a number with 0 is the number itself.
This forms the base case for our code.
2.  for the second iteration of gcd(a,b)  
it goes as gcd(b,a%b) here  
```
gcd(a,b)=gcd(b,a%b)  
gcd(a,b)=x\*a + y\*b  
gcd(b,a%b)=x1\*b + y1\*(a%b)  
anyhow, a%b = a - a//b\*b  
=x1\*b + y1\*(a-a//b\*b)  
=y1\*a +  (x1-a//b\*y1)\*b  
by comparing coefficients  
x=y1  
y=x1-a//b\*y1
```
and the code goes as:
```
def extended_gcd(a, b):
# assuming b > a
    if a == 0:
        return 0, 1
    x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return x, y
```
The values are
>(10245, -8404)
smallest number is -8404




## Challenge 3:
Here we just got introduced to modulo functions which are basically finding the remainder so I just used '%' operator.
```
11 ≡ x mod 6
8146798528947 ≡ y mod 17
```
in the first case it is so obvious i.e. <mark>5</mark>  
but in second case I took the help of python and found the answer to be <mark>4</mark>.
hence flag is ***4***.
## Challenge 4:
```
Fermat's Little Theorem :  
This says that for a prime number p when raised with any integer a less than p then
a^p - a is divisible by p.
```
Here it is given for  
273246787654<sup>65536</sup> mod 65537 where it is equals to  1.  
because  
273246787654<sup>65537</sup>= 273246787654 (mod 65537)  
now dividing 273246787654 on both sides we get 1 as the value on right and 273246787654<sup>65536</sup> on left.  
Hence answer is ***1***.

## Challenge 5
given
```
A finite field Fp is the set of integers {0,1,...,p-1}, and under both addition and multiplication there is an inverse element b for every element a in the set, such that a + b = 0 and a * b = 1
```
and also we are asked to find multiplicative inverse of 3 in F<sub>13</sub>. We were asked to look into little theorem for it.  
first we write:  
>a<sup>p-1</sup>=1 (mod p)  
a . a<sup>p-2</sup>=1(mod p)  
hence for any integer a, a<sup>p-2</sup>=1(mod p) is the inverse for that field here  
3<sup>11</sup> mod 13.  
we have 3<sup>3</sup>=1(mod 13) so  
3<sup>9</sup>=1(mod 13)  
multiplying 3<sup>2</sup> on both sides.  
>>3<sup>11</sup>=9(mod 13)


or use the following script:  
```
def mod_inverse(a, p):
        return pow(a, p-2, p)

a = 3
p = 13

inverse = mod_inverse(a, p)

print(f"The multiplicative inverse of {a} modulo {p} is {inverse}")
```
