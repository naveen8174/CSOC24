# Challenge 2:
The given text is
>01000011 01010011 01001111 01000011 00110010 33 7b 6a 75 35 37 5f ZDFmZjNyM243XzNuYw== 60 144 61 156 66 65 137 154 60 154 175

first part is binary: CSOC2  
second part is hexal numbers: 3{ jU57_  
third part is base64: and tells: d1ff3r3n7_3nc  
fourth part is octal: 1n65_lol}

flag is :
> CSOC23{jU57_d1ff3r3n7_3nc1n65_lol}

# Challenge 1:
The source.enc file is the base64 encoding of a script which translates to  
```
with open('flag.txt', 'r') as f:
   flag = f.read()

s = ''.join(format(ord(i), '02x') for i in flag)
e = ""

for i in range(0,len(s),4):
   e += format(int(s[i:i+2],16)^int(s[i:i+4],16), '02x')

with open('output.txt', 'w') as f:
   f.write(e)
```
This code converts data into hexa form and for every 4 bytes it removed the last two bytes and returned the data:
>C�O�2�{H4�y&b�5�6�_kn _'0B?B

we get this by decoding the output.txt  
first word should be CSOC23{^4^y^b^5^6^_^n^ _^0^?}  
where '^' can be any value.
