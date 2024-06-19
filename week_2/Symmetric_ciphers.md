# HOW AES WORKS
## Challenge 1:
Here we're asked about the mathematical term for one-to-one corresponding function i.e. every element in the co domain is mapped to exactly one element in the domain. So, this is a direct example for bijective function to get the correct word (bijection/bijective) I just made a trail and error.  
So the flag is
>crypto{bijection}
## Challenge 2:
It asks for the name of best known AES attack which has a time complexities of  
  1.**For AES-128**: The attack has a computational complexity of 2<sup>126.1</sup> operations, compared to the 2<sup>128</sup> operations required for a brute-force attack.  
  2.**For AES-192**: The attack has a computational complexity of 2<sup>189.7</sup> operations, compared to the 2<sup>192</sup> operations required for a brute-force attack.  
  3.**For AES-256**: The attack has a computational complexity of 2<sup>254.4</sup> operations, compared to the 2<sup>256</sup> operations required for a brute-force attack.

The name of the attack is our flag:
>crypto{biclique}

## Challenge 3:
The following challenge expect us to write a function to convert state matrix again into bytes :
```
def bytes2matrix(text):
    """ Converts a 16-byte array into a 4x4 matrix.  """
    return [list(text[i:i+4]) for i in range(0, len(text), 4)]

def matrix2bytes(matrix):
    """ Converts a 4x4 matrix into a 16-byte array.  """
    return ''.join(chr(matrix[i][j]) for i in range(4) for j in range(4))

matrix = [
    [99, 114, 121, 112],
    [116, 111, 123, 105],
    [110, 109, 97, 116],
    [114, 105, 120, 125],
]

print(matrix2bytes(matrix))
```
The following script gives us the value of flag
>crypto{inmatrix}
