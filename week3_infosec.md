# WEB GAUNTLET
This is a sql injection question with five rounds where we have to login as admin.  
and from the other linnk we get the hint as `or` so it is sufficient to login as `admin` and for password we use  
either:   

>admin' --  
#anything in password

i.e. commenting out the next parts

for second layer the filters says
>or and like = --

so I used other commenting techniques now like `;#` ,`/*`,`*/`
>admin' ; #

for round3 it is like:
>or and = like > < -  
innerHTML: "Round3:   or and = like \&gt; \&lt; --\<br>"

noww that it seems like any spaces during the injection will be failed and any commenting containing spaces will be failed.  
so we can use the commands in username like
>admin'#

for round4 it is given as the word admin is not allowed so we have to use the input admin in any other form.
so I used the words like  
>ad'||'min';#


for round5 it is said that we should not use union `kudos` we didn't even used it until now so same applies here:
>ad'||'min';#

now in filter.php we have the flag
>picoCTF{y0u_m4d3_1t_cab35b843fdd6bd889f76566c6279114}

# WEB GAUNTLET 2
now the filters are like level5 of lasr round
>Filters: or and true false union like = > < ; -- /* */ admin

now we can not terminate the sql directly as `;` is filtered so we have to use some other way to terminate the query or assign a true value at the password.  
so I used 
>a'||'dmin  
1' IS NOT '0

so I got the flag as
>picoCTF{0n3_m0r3_t1m3_b55c7a5682db6cb0192b28772d4f4131}
# WEB GAUNTLET 3
our previous work even applies here so we use same credentials now.
>a'||'dmin  
1' IS NOT '0

but for some reason I didn't get the flag by refreshing filter.php so I changed the url index.php as filter.php.

so the flag is
>picoCTF{k3ep_1t_sh0rt_eb90a623e2c581bcd3127d9d60a4dead}

# Irish name Repo
here using the link in the challenge I have directed to a webpage in which I found a option of admin login so I entered in to it where it asked for credentials so I have decided to go with sql injection as admin
>username: admin  
password : ' OR 1=1

so I got the flag in a webpage. 
>picoCTF{s0m3_SQL_c218b685}

# Irish name Repo 2
now I'm on to the same website but the login site is filtered so we have to try some other technique if our older one doesn't work  
unfortunately our old technique went wrong so I've tried the one used in our previous challenges.
>admin';#  
#any_random_password

so I got the flag
>picoCTF{m0R3_SQL_plz_fa983901}

# Irish name Repo 3
Now it just asks for the passwords only. while attempting to do so I got an error from the server so I've learned that updating the `debug` in the html code of the inspect page to 1(true) leads to normal behaviour as earlier and throw errors if we're wrong.  
I also recognised that it follows rot13 cipher and for other characters no cipher is followed so now our commands become
> ' BE 1=1--

so now I got the flag
>picoCTF{3v3n_m0r3_SQL_06a9db19}

# JaWT scratchpad
as the name suggested it uses many things like jwt which are json objects used to transfer data so when we entered the link we are asked to enter any name except admin so by doing so with john we'll find some cookie there so I found this wonderful jwt [editor](https://jwt.io/)
```
basically in jwt we have three fields seperated by '.' and first two fields are base64 encoded and last field is sha256 hashed 
```
so we changed second field to admin and then to keep the cookie to be authentic we have to crack the last field and for doing so we'll use this famous tool `john` with the command
>john token.txt --format=HMAC-SHA256 --wordlist=/usr/share/wordlists/rockyou.txt

so I got the key to be `ilovepico` and giving it as input we get the contents of the cookie
>eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoiYWRtaW4ifQ.gtqDl4jVDvNbEe_JYEZTN19Vx6X9NNZtRVbKPBkhO-s

by copying the contents in the cookie and reloading the page i got the key
>picoCTF{jawt_was_just_what_you_thought_1ca14548}

# Secret
for this I was asked to launch a instance where I found a webpage the hint says folders folders folders which means to search the web server for correct file so I inspected the webpage in headers I got a file named `secret` and in that page I found a file named `hidden` at there I found `supperhidden` there in the code the flag is hidden in the html file but not in the webpage and I found the flag to be
>picoCTF{succ3ss_@h3n1c@10n_790d2615}

# who are you
For this challenge we are greatly dependent on the tool burpsuite which modifies the http headers and change our requests    
![this video](who_are_you.mp4) explains the work we've done and the header tags are searched through the internet.
so I got the flag to be
>picoCTF{http_h34d3rs_v3ry_c0Ol_much_w0w_f56f58a5} 
we need some knowledge on http headers for which the document is provided while entering the link 
1.  It asks us to only use PicoBrowser for that we have to change `User-Agent` to PicoBrowser
2.  now that it asks we have to login to the page from pico site only so we use Referer we set it to http://mercury.picoctf.net:1270/
3.  now it asks for date which only perates on year 2018 so we used `date: 1 Jun 2018`
4.  now we're asked not to be tracked so `DNT` as true or 1
5.  now again it asks for a sweden ip address for the client `X-Forwarded-For` and any swedish IP address
6.  now change the language label to `sv` from `eng-Us`
There you get the flag.

# Intro to burp 
even for this challenge as the name suggests we use burpsuite and we open the browser(chromium) in my case and then intecept(in proxy) it we use any random credential earlier and then it asks for 2 factor auth for an otp we give a random number to it and go to the intercept page now at last we find otp=....... so we clear that row and go to the browser so we observe our flag
>picoCTF{#0TP_Bypvss_SuCc3$S_e1eb16ed}
