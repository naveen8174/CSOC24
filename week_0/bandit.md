## BANDIT  
The bandit game is all about finding the passwords of a remote system and logging into it with ssh protocal. I use kali linux for this game which is a VM
### `level 0`

This level ends with logging into the remote machine just by the command:   
>ssh bandit0@bandit.labs.overthewire.org -p 2220

where password is bandit0, username is bandit0 and the domain name of the remote machine is bandit.labs.overthewire.org and the port used for connection of ssh is 2220 instead of usual ssh port 22 or 23.

### `level 1`

This level makes use of cat command which is in the readme file of bandit0 user come out using "exit" command and login to bandit1 user of same domain :  
>ssh bandit1@bandit.labs.overthewire.org -p 2220  

with the password in readme file: NH2SXQwcBdpmTEzi3bvBHMM9H66vVXjL  
so that we enter into the remote machine.
now the password is saved in a file named "-" so we use cat command to view it. Instead of directly viewing it we use:  
>cat ./-

i.e. we use actual address of the file as it may read - as the flag.  
we get a password for bandit2 username  
### `level 2`
Now we exit the bandit1 username and login to bandit2, with the command:  
>ssh bandit2@bandit.labs.overthewire.org -p 2220  

here there is a file named "spaces in the filename" so for opening the file we use cat command but filename in "" because while having spaces cat command takes the first part only.  

>command: cat "spaces in the filename" 

now we get the password for the next username bandit3

### `level 3`
Now enter "exit" then logon to the bandit3 username
>ssh bandit3@bandit.labs.overthewire.org -p 2220  

 with the password that i got there I have a directory named **inhere** by going into that directory with the command  
>cd inhere  

there is a hidden file in the directory and can be seen with the command  
>ls -a  

here we use cat command to look into the hidden files  
>cat .hidden  

here we get the password for bandit4.
### `level 4`
Now enter exit in the CLI the logon to bandit4.  
>ssh bandit4@bandit.labs.overthewire.org -p 2220  

and enter the password. Now move to the inhere directory it is given that password is in human readable file so we use file command to know the type of file without actually entering into it we can also check all files at once using wildcard "*".  
> file ./*  

now we can observe that -file07 is human readable so we use cat command as used previously:
> cat ./-file07 

*note*: '.' represents current directory  
 here we get the password.
### `level 5`
now exit from bandit4 and get login to bandit5:  
>ssh bandit4@bandit.labs.overthewire.org -p 2220  

and enter the password. now there are few constraints to the file  
*  size is 1033 bytes
*  it should not be executable
*  human readable

for this I use find command in which options of it allows me to do tasks like filtering for size and non execution and at last if there are multiple files we may use grep text command using pipe character  
>find -type f -size 1033c ! -executable  

this will gives out only one file in maybehere07 folder of file .file2 this can be seen using  
>cat ./inhere/maybehere07/.file2  

here we'll get password for next level bandit6 .
### `level 6`
now exit the bandit5 and logon to bandit6:  
>ssh bandit4@bandit.labs.overthewire.org -p 2220  

and enter the password. Now the conditions are 
*  user bandit7
*  group bandit6
*  size 33 bytes  

we again use find command but now there is a likely chance of getting permission denied errors as we operating from the root so we redirect all stderr(2) to file /dev/null which always discards what ever written to it and we get the required file.
> find -user bandit7 -group bandit6 -size 33c 2>/dev/null  

we get a file and seeing the file through cat command.  
now we get the password.
### `level 7`
now exit the user and login to bandit7 with  
>ssh bandit7@bandit.labs.overthewire.org -p 2220  

and enter the password. Now we need to get the password that is next to the word millionth in data.txt which is a very huge file. so we use grep commands for it. 
>cat data.txt | grep millionth  

there we get the password for the next username 
### `level 8`
now exit the user and logon to bandit8 with
>ssh bandit8@bandit.labs.overthewire.org -p 2220  

and enter the password there. The next password is of unique occurance so we use command uniq for it but we have to sort it before for the function uniq to work.

>command: sort data.txt | uniq -u  

here we'll get the next password.

### `level 9`
now exit the previous user and log in to bandit9
>ssh bandit9@bandit.labs.overthewire.org -p 2220  

now enter the password. Here the password is hidden in a binary file so we use a command called as <mark>strings</mark> so we only get ascii text later we filter it with grep commands to get the text after multiple "=" symbols.  
>strings data.txt | grep "=="  

this gives the new password.
### `level 10`
now exit the old username and login to bandit10
>ssh bandit10@bandit.labs.overthewire.org -p 2220  

now enter the password for entering in as bandit10. Now  we have a file data.txt in the home directory which is encoded differently other than utf-8 encoding i.e. in base64 encoding so we have to decode it for this we have a command base64 and with option -d refers to decoding of the file.
>base64 -d data.txt  

from here we'll get the password.
### `level 11`
now exit the user and log in to bandit11 
>ssh bandit11@bandit.labs.overthewire.org -p 2220  

now enter the password for entering in as bandit11. here it is like a ciphher encoding for this we have to rotate the message by 13 characters so we use <mark>tr</mark> command .   
>cat data.txt | tr 'a-zA-Z' 'n-zm-aN-ZM-A'  

from this we get password.
### `level 12`
now exit the user and log in to bandit11 
>ssh bandit12@bandit.labs.overthewire.org -p 2220  

now enter the password to get in as bandit12.  
here files are encoded or compressed into different file formats we can get to know about the specific file format either by hexdum format or simply by the command <mark>file</mark> .  
before everything we have to make a directory in /tmp folder where files files are deleted automatically for every day with some random name so that no other dir of /tmp has the same name.
1.  firstly it is hexdum file so we revert it by using the command
> xxd -r data.txt  

now we check the type of file with:
>file data.txt

2.  we get the file as gzip file so change it's name to data2.gz now decode the file using gzip command.
> gzip -d data2.txt  

3.  here u'll get a file <mark>data2</mark> now check file type for data2 it is bzip2 now change it's name to bzip3.bz and apply the command  
>bzip2 -d bzip3.bz  

4.  now the file is again gzip make data3 file as data4.gz and decode  
> gzip -d data4.gz

5.  now u have a file that is tape archived so we have to extract the file using the command
>tar -xf data4

6.  now with ls command we see another file named data5.bin this data is also tape archived and have to be extracted 
>tar -xf data5.bin

7.  now we get a file named data6.bin which compressed by using bzip2 format so we have to rename it to data6.gz and then decode it using
>bzip2 -d data6.bz

8.  now we get file bzip which is tape archived again now we use  
>tar -xf data6  

9.  we now have a file data8.bin which is finally gzip extracted so we have to rename it to data8.gz  
and then decode it
> gzip -d data8.gz

we have data8 which is ASCII file having the password.  
### `level 13`
now exit the user and log in to bandit12 
>ssh bandit13@bandit.labs.overthewire.org -p 2220  

now enter the password to get in as bandit13. Until now we loggged in to remote systems using ssh protocol and now we'll do so with private key which is available in home directory 
### `level 14`
stay in bandit 13 and write the following command
>ssh -i sshkey.private bandit14@bandit.labs.overthewire.org -p 2220  

there in the folder /etc/bandit_pass/bandit14 we have the password for the next password we have to connect to localhost using the port 30000 for this we use
>nc localhost 30000

now enter the password of bandit14 to get bandit15 password.
### `level 15`
now exit the user and log in to bandit14 
>ssh bandit15@bandit.labs.overthewire.org -p 2220  

now enter the password to get in as bandit15. For next password we have to connect to localhost using ssl encryption for that we use openssl command and with simple client i.e. for s_client overthe port
>openssl s_client -connect localhost:30001

now we have to enter the password of bandit15 then we get password of bandit16.  
### `level 16`
now exit the user and log in to bandit15 
>ssh bandit16@bandit.labs.overthewire.org -p 2220  

now enter the password to get in as bandit16.now there are several conditions to meet firstly finding the port that can listen and speak for that we use <mark>nmap</mark>.
>nmap -sV -p 31000-32000

here we get the services and versions of the ports in the range 31000-32000. we find 31790 as the port with ssl encryption and unknown service and some other port with ssl encryption but echo service which indeed not necessary so we go with the port 31790 now we have to connect to local host.
>openssl s_client -connect localhost:31790

but now we get a private key and we write it to a file and keep all permissions to users and no permissions to other.
### `level 17`
now we get into the bandit17:
>ssh -i private.key bandit17@bandit.labs.overthewire.org port -2220

here we will have two files one is password.old,password.new we need to find out the only changed line in password.new this is done by 
>diff password.new password.old

in this we get different lines on both sides and take the password on left side.
### `level 18`
here we cannot login into the server but we can read the files with the command:
>ssh bandit18@bandit.labs.overthewire.org -p 2200 cat readme

here we get password for bandit19

### `level 19`
here we can login into the server with  username bandit20 with the command:
>ssh bandit19@bandit.labs.overthewire.org -p 2200  

here there is a code in the home directory of bandit19 named as ./bandit20-do which is used for executing any command using the permissions of bandit20 user. as all passwords are present in /etc/bandit_pass we see the password of bandit20 in bandit20 file with only bandit20 user nly to access it.
>./bandit20-do cat /etc/bandit_pass/bandit20

here we get the password of bandit20
### `level 20`
now exit the user and log in to bandit19 
>ssh bandit120@bandit.labs.overthewire.org -p 2220  

now enter the password to get in as bandit20. Here there is again a setuid whose work is to connect to the localhost with the port as argument and reads the message in connection if it is password of bandit20 it'll give password of bandit21.

for this first we should have a port that should listen (that is open and ready for connections and input the password through the new port):
>echo $*password_bandit20* | nc -l -p 5555 &

here option -l for listening and -p 5555 for the port 5555 to listen through and & for makinng the process in background.

now use the setuid suconnect with port 5555 as the argument
>./suconnect 5555

this will give the password of bandit21
### `level 21`
now exit the user and log in to bandit20 
>ssh bandit21@bandit.labs.overthewire.org -p 2220  

now enter the password to get in as bandit21. as given in the question there is a file in /etc/cron.d which is crontab here we get a file on the name of cronjob_bandit22 where there are cron commands to start a code in usr/bin in at the time of reboot and also for every minute and return what ever output or error recieved to /dev/null which discards the output upon entry. now seeing the cronjob_bandit22 we have a file in /tmp/ folder which is resetting itself for everyday by looking into that file we get password of bandit22 user as given in the code
>cat /etc/bandit_pass/bandit22 > /tmp/t7O.....

here we get the password
### `level 22`
now exit the user and log in to bandit21 
>ssh bandit22@bandit.labs.overthewire.org -p 2220  

now enter the password to get in as bandit22.here similar to previos level there is a cron file naming cronjob_bandit23 in which there is again a scripted file named as cronjob_bandit23.sh in /usr/bin dir so i saw the script there which converts the message "I am user bandit23"  into it's hash value and taken it's first field out of md5 hash value and uses this name as a file name in /tmp folder in which stores password of bandit23 user. hence we get the password from the file in /tmp/$hashoOfTheMessage.
hence we get the password here.
### `level 23`
now exit the user and log in to bandit22 
>ssh bandit23@bandit.labs.overthewire.org -p 2220  

now enter the password to get in as bandit23.here just like previous assignments we have a code in usr/bin which repeats at every minute and the code reads as
```  
myname=$(whoami)

cd /var/spool/$myname
echo "Executing and deleting all scripts in /var/spool/$myname:"
for i in * .*;
do
    if [ "$i" != "." -a "$i" != ".." ];
    then
        echo "Handling $i"
        owner="$(stat --format "%U" ./$i)"
        if [ "${owner}" = "bandit23" ]; then
            timeout -s 9 60 ./$i
        fi
        rm -f ./$i
    fi
done
```
here every file in  /var/spool/$myname gets deleted if it belongs to the username of bandit23 then it'll be executed as bandit24 and then deleted so we make a script in tmp directory which returns the password in another file of tmp directory after one minute.

>#!/bin/bash  
cat /etc/bandit_pass/bandit24 > /tmp/tmp.ljEyl6kv1M/password

now by checking into the file we'll get bandit24 password.
### `level 24`
now exit the user and log in to bandit23 
>ssh bandit24@bandit.labs.overthewire.org -p 2220  

now enter the password to get in as bandit24. here when connected to localhost using port 30002 it asks for the password and security pin for the we tends to check all four digit numbers i.e. all 10000 possibilities and for that we use a simple shell script for brute forcing. 
```
#!/bin/bash

for i in {0000..9999}
do
echo UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ $i >> values.txt
done

cat values.txt | nc localhost 30002 > password.txt
```
but i split the code into two parts for two 5000 loops and checked each time at last in password file there are 9999 error messages and one passsword for that we remove errors using grep command
>grep -v Wrong password.txt


here we get the password for bandit25
### `level 25`
now exit the user and log in to bandit24 
>ssh bandit25@bandit.labs.overthewire.org -p 2220  

now enter the password to get in as bandit25.here it says the shell is not /bin/bash by default but it is some other to find it we have to see /etc/passwd file and at last field we have the shell of the specific user so we have the shell as /bin/showtext if we go through the showtext file we have an assignment of environmental variable and having shown text.txt file with more option and then exit 0 line which makes us logout every time we login to bandit26 with the key in home directory unlike cat command for more command if the file is larger than window size it is shown in pages but text.txt file being small it is shown all at once.
### `level 26`
 The onle way to get into the bandit26 user is by changing the shell to /bin/bash so we have to access the cli in bandit26 this can be done by vi editor which can be accessed through commands in <mark>more</mark> but for that the screen size shouldbe smaller so minimize it now run the command

>ssh -i bandit26.private bandit26@localhost -p 2220

now type **v** to go into vi editor where we can run commands now for getting a shell we have to write
>:shell

to change shell we use
>:set shell=/bin/bash

so now we get into bandit26 where we have setuid for user bandit27 so we get password of bandit27 with accessing the bandit27 file in /etc/bandit_pass there we get the password for bandit27
### `level 27`
now exit the user and log in to bandit26 
>ssh bandit27@bandit.labs.overthewire.org -p 2220  

now enter the password to get in as bandit27. the password of the file should be stored in some git repository it seems so we'll clone the repository to port 2220 in some /tmp subdirectory.
>git clone ssh://bandit27-git@localhost:2220/home/bandit27-git/repo

here wee can find a sub-directory repo in which there is a readme file which contains the password of the bandit28.
### `level 28`
now exit the user and log in to bandit27 
>ssh bandit28@bandit.labs.overthewire.org -p 2220  

now enter the password to get in as bandit28. here again we have to enter into a git repository so we go to /tmp directory and makes a clonne there.
>git clone ssh://bandit27-git@localhost:2220/home/bandit27-git/repo

there in readme we can observe that password is written to be XXXXXXX , there is a chance that there is password in that place before and now it is changed. git can remember changes by storing them into a log so we usee the command
>git log


in this log we see a specific fixture contains fixture of data leak so we see the modification by
>git show $*modification_id*

here we can get the actual password of the data.

### `level 29`
now exit the user and log in to bandit28 
>ssh bandit29@bandit.labs.overthewire.org -p 2220  

now enter the password to get in as bandit29.  
here there is nothing in the password section of README.md so we'll check it in other braches so that may others have the password so we'll go by trail and error and then check in other readme files with
>git branch -a 

i get all the branches and with
>git checkout $*newbranch*

we can navigate into new branch.
here in dev branch i got the password for bandit 30
### `level 30`
now exit the user and log in to bandit29 
>ssh bandit30@bandit.labs.overthewire.org -p 2220  

now enter the password to get in as bandit30.
now there is nothing in readme and no other branches and like chilli to the wound there is no git log.  
the file being empty there is a chance that password may be added and them the commit was deleted so let's check tags if the change is tagged it being the only option 
>git tag

there is only tag nammed secret so with
>git show secret

we get the password
### `level 31`
now exit the user and log in to bandit30 
>ssh bandit31@bandit.labs.overthewire.org -p 2220  

now enter the password to get in as bandit31.in readme file it asks us to push the file key.txt by haaving a message "May I come in?" by making the file with
>echo May I come in? >key.txt

now add the change and the commit it.
>git add -f key.txt  
git commit -m 'type something random'

without -f it throws an error message asking to keep a -f option.

now push the change
>git push origin main

we'll have a message now which tells us password for bandit32
### `level 32`
now exit the user and log in to bandit31 
>ssh bandit32@bandit.labs.overthewire.org -p 2220  

now enter the password to get in as bandit32.now this terminal isn't a bash one entering anything to the shell results in throwing out error if it is a lowercase and get executed if it is uppercase so we ca run local or global variables only here we can write 
>$0

as it gives the name of the current bash shell and it gives out a shell whose user is bandit33 so wee can get password from
>cat etc/bandit_pass/bandit33

we get password for bandit 33 which is the last level for bandit game.