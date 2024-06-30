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
even for this challenge as the name suggests we use burpsuite and we open the browser(chromium) in my case and then intecept(in proxy) it we use any random credential earlier and then it asks for 2 factor auth for an otp we give a random number to it and go to the intercept page now at last we find `otp=.......` so we clear that row and go to the browser so we observe our flag
>picoCTF{#0TP_Bypvss_SuCc3$S_e1eb16ed}

# Client-Side-Again
now we go through the source code and found that the javascript code is obfuscated and can be deobfuscated by the tools like [this](https://obf-io.deobfuscate.io/). Now we understand the code
```
var _0x5a46 = ['f49bf}', '_again_e', 'this', "Password Verified", "Incorrect password", 'getElementById', 'value', 'substring', 'picoCTF{', 'not_this'];
(function (_0x4bd822, _0x2bd6f7) {
  var _0xb4bdb3 = function (_0x1d68f6) {
    while (--_0x1d68f6) {
      _0x4bd822.push(_0x4bd822.shift());
    }
  };
  _0xb4bdb3(++_0x2bd6f7);
})(_0x5a46, 0x1b3);
var _0x4b5b = function (_0x2d8f05, _0x4b81bb) {
  _0x2d8f05 = _0x2d8f05 - 0x0;
  var _0x4d74cb = _0x5a46[_0x2d8f05];
  return _0x4d74cb;
};
function verify() {
  checkpass = document[_0x4b5b('0x0')]('pass')[_0x4b5b('0x1')];
  split = 0x4;
  if (checkpass[_0x4b5b('0x2')](0x0, split * 0x2) == _0x4b5b('0x3')) {
    if (checkpass[_0x4b5b('0x2')](0x7, 0x9) == '{n') {
      if (checkpass[_0x4b5b('0x2')](split * 0x2, split * 0x2 * 0x2) == _0x4b5b('0x4')) {
        if (checkpass[_0x4b5b('0x2')](0x3, 0x6) == 'oCT') {
          if (checkpass[_0x4b5b('0x2')](split * 0x3 * 0x2, split * 0x4 * 0x2) == _0x4b5b('0x5')) {
            if (checkpass.substring(0x6, 0xb) == 'F{not') {
              if (checkpass[_0x4b5b('0x2')](split * 0x2 * 0x2, split * 0x3 * 0x2) == _0x4b5b('0x6')) {
                if (checkpass[_0x4b5b('0x2')](0xc, 0x10) == _0x4b5b('0x7')) {
                  alert(_0x4b5b('0x8'));
                }
              }
            }
          }
        }
      }
    }
  } else {
    alert(_0x4b5b('0x9'));
  }
}
```
here it says 
1.  7 - {
2.  8 - n
3.  3-o,4-C,5-T
4.  6-F,9-o,10-t
so it is picoCTF{not_this_again_f49bf} as we can say it by the relative position of the variable \_0x4b5b with checkpass\_
>picoCTF{not_this_again_f49bf}
# JavaScript kiddie-1
by inspecting the following webpage we get 
```
<html><head>    
		<script src="jquery-3.3.1.min.js"></script>
		<script>
			var bytes = [];
			$.get("bytes", function(resp) {
				bytes = Array.from(resp.split(" "), x => Number(x));
			});

			function assemble_png(u_in){
				var LEN = 16;
				var key = "0000000000000000";
				var shifter;
				if(u_in.length == LEN){
					key = u_in;
				}
				var result = [];
				for(var i = 0; i < LEN; i++){
					shifter =key.charCodeAt(i) - 48;
					for(var j = 0; j < (bytes.length / LEN); j ++){
						result[(j * LEN) + i] = bytes[(((j + shifter) * LEN) % bytes.length) + i]
					}
				}
				while(result[result.length-1] == 0){
					result = result.slice(0,result.length-1);
				}
				document.getElementById("Area").src = "data:image/png;base64," + btoa(String.fromCharCode.apply(null, new Uint8Array(result)));
				return false;
			}
		</script>
	</head>
	<body>

		<center>
			<form action="#" onsubmit="assemble_png(document.getElementById('user_in').value)">
				<input type="text" id="user_in">
				<input type="submit" value="Submit">
			</form>
			<img id="Area" src="">
		</center>

	


</body></html>
```
The code basically takes the image from bytes and shifts the image rows using the key given in by us and returns a broken image we can fix this issue with a logic that `it is a png file` and has same header for all 
```
89 50 4E 47 0D 0A 1A 0A
```
so we shift our rows accordingly and next 4 bytes are the length of IHDR portion and other 4 bytes are "IHDR" string itself so we can say first 16 numbers shoulld be same for every array   
we start with test key "0000000000000000".  
so on appending *bytes* on the end we get the modified bytes  
```
87 130 78 188 0 84 26 157 143 239 249 82 248 212 239 82 195 80 1 207 13 6 1 0 119 243 73 193 78 36 133 108 85 0 0 14 0 186 68 0 0 222 0 243 0 24 174 163 126 0 133 252 137 177 121 10 0 0 0 237 73 63 0 100 96 20 3 224 59 171 16 114 0 0 0 69 0 68 68 147 137 179 110 112 74 121 238 65 1 0 156 0 155 0 95 120 0 233 226 40 78 194 248 44 84 0 208 13 41 72 138 59 164 98 71 0 209 0 99 176 97 120 202 0 135 192 54 101 64 252 81 71 205 10 243 133 30 22 125 237 3 93 90 42 73 221 25 114 243 0 116 22 4 3 59 75 188 119 169 221 161 184 178 2 73 73 231 45 14 99 102 153 166 178 206 54 127 84 240 191 220 10 163 81 64 206 128 132 102 197 72 127 239 253 78 93 8 22 239 207 146 111 143 239 27 243 28 0 173 159 196 48 247 28 84 98 63 52 171 214 214 26 233 254 65 106 111 59 73 255 148 111 103 91 20 206 222 70 252 199 161 124 245 188 102 81 159 119 174 51 190 243 55 243 156 249 124 125 2 143 191 27 119 139 126 88 18 247 171 227 72 66 54 251 0 80 171 146 113 173 4 79 211 216 214 122 119 115 225 45 24 54 44 76 43 253 5 235 104 248 96 8 229 200 75 64 233 217 23 87 40 254 187 107 181 200 181 233 181 81 231 171 165 82 254 196 239 51 43 114 170 73 249 50 114 201 138 64 11 203 155 192 249 226 35 188 156 223 40 217 67 75 100 45 93 102 169 13 34 197 80 175 210 128 137 201 167 45 140 82 171 56 212 17 126 113 139 229 127 223 181 15 0 116 221 186 219 230 56 233 31 15 249 74 119 152 44 41 226 60 35 253 172 97 32 137 233 165 35 181 104 80 217 56 186 205 212 15 64 81 230 230 153 62 251 251 47 151 141 108 32 25 65 11 253 119 201 147 243 11 31 247 233 54 126 217 136 141 191 226 137 213 131 239 100 145 151 150 119 124 159 203 190 63 18 170 210 175 122 223 223 114 124 59 93 245 177 100 15 57 63 239 165 144 13 149 32 198 39 52 53 113 97 91 186 76 91 74 207 133 208 0 245 241 245 73 122 193 223 159 82 175 241 159 231 205 24 92 75 11 247 77 55 170 7 95 127 143 96 207 242 142 153 226 242 93 163 110 185 26 188 4 178 102 159 97 53 58 186 172 239 6 78 215 65 156 90 150 112 205 73 76 149 163 159 242 45 147 16 210 49 254 82 126 200 30 62 190 230 2 86 171 181 197 185 132 170 153 82 191 154 235 147 55 57 92 252 48 207 118 191 170 253 53 127 94 143 122 230 254 154 151 186 55 160 132 126 57 183 217 129 181 95 255 35 223 50 70 77 107 100 203 17 61 163 17 227 147 182 184 79 126 239 28 115 159 254 111 90 250 14 206 185 137 187 141 231 211 241 249 39 99 131 95 210 50 147 241 95 127 103 239 113 165 223 164 245 35 231 132 166 220 241 207 67 178 148 29 156 94 194 74 222 110 0 243 107 158 173 214 210 249 84 66 107 40 0 203 138 164 0 241 9 109 147 207 85 29 204 0
```
so the only thing we have to do now is make sure that first 16 bytes are 
```
89 50 4E 47 0D 0A 1A 0A 00 00 00 0D 49 48 44 52
```
so now split the array and find the difference between the first line and the required byte in each line.
now I came with the following python script
```
bytes_ = "87 130 78 188 0 84 26 157 143 239 249 82 248 212 239 82 195 80 1 207 13 6 1 0 119 243 73 193 78 36 133 108 85 0 0 14 0 186 68 0 0 222 0 243 0 24 174 163 126 0 133 252 137 177 121 10 0 0 0 237 73 63 0 100 96 20 3 224 59 171 16 114 0 0 0 69 0 68 68 147 137 179 110 112 74 121 238 65 1 0 156 0 155 0 95 120 0 233 226 40 78 194 248 44 84 0 208 13 41 72 138 59 164 98 71 0 209 0 99 176 97 120 202 0 135 192 54 101 64 252 81 71 205 10 243 133 30 22 125 237 3 93 90 42 73 221 25 114 243 0 116 22 4 3 59 75 188 119 169 221 161 184 178 2 73 73 231 45 14 99 102 153 166 178 206 54 127 84 240 191 220 10 163 81 64 206 128 132 102 197 72 127 239 253 78 93 8 22 239 207 146 111 143 239 27 243 28 0 173 159 196 48 247 28 84 98 63 52 171 214 214 26 233 254 65 106 111 59 73 255 148 111 103 91 20 206 222 70 252 199 161 124 245 188 102 81 159 119 174 51 190 243 55 243 156 249 124 125 2 143 191 27 119 139 126 88 18 247 171 227 72 66 54 251 0 80 171 146 113 173 4 79 211 216 214 122 119 115 225 45 24 54 44 76 43 253 5 235 104 248 96 8 229 200 75 64 233 217 23 87 40 254 187 107 181 200 181 233 181 81 231 171 165 82 254 196 239 51 43 114 170 73 249 50 114 201 138 64 11 203 155 192 249 226 35 188 156 223 40 217 67 75 100 45 93 102 169 13 34 197 80 175 210 128 137 201 167 45 140 82 171 56 212 17 126 113 139 229 127 223 181 15 0 116 221 186 219 230 56 233 31 15 249 74 119 152 44 41 226 60 35 253 172 97 32 137 233 165 35 181 104 80 217 56 186 205 212 15 64 81 230 230 153 62 251 251 47 151 141 108 32 25 65 11 253 119 201 147 243 11 31 247 233 54 126 217 136 141 191 226 137 213 131 239 100 145 151 150 119 124 159 203 190 63 18 170 210 175 122 223 223 114 124 59 93 245 177 100 15 57 63 239 165 144 13 149 32 198 39 52 53 113 97 91 186 76 91 74 207 133 208 0 245 241 245 73 122 193 223 159 82 175 241 159 231 205 24 92 75 11 247 77 55 170 7 95 127 143 96 207 242 142 153 226 242 93 163 110 185 26 188 4 178 102 159 97 53 58 186 172 239 6 78 215 65 156 90 150 112 205 73 76 149 163 159 242 45 147 16 210 49 254 82 126 200 30 62 190 230 2 86 171 181 197 185 132 170 153 82 191 154 235 147 55 57 92 252 48 207 118 191 170 253 53 127 94 143 122 230 254 154 151 186 55 160 132 126 57 183 217 129 181 95 255 35 223 50 70 77 107 100 203 17 61 163 17 227 147 182 184 79 126 239 28 115 159 254 111 90 250 14 206 185 137 187 141 231 211 241 249 39 99 131 95 210 50 147 241 95 127 103 239 113 165 223 164 245 35 231 132 166 220 241 207 67 178 148 29 156 94 194 74 222 110 0 243 107 158 173 214 210 249 84 66 107 40 0 203 138 164 0 241 9 109 147 207 85 29 204 0"
byte_list = bytes_.split(" ")
hex_list=[hex(int(x)) for x in byte_list]
png = ["0x89", "0x50", "0x4e", "0x47", "0xd", "0xa", "0x1a", "0xa", "0x0", "0x0", "0x0" ,"0xd", "0x49", "0x48", "0x44", "0x52"]

broken=[]
for i in range(16):
    broken.append([])
key = []
LEN = len(hex_list)
for i in range(LEN):
    broken[i%16].append(hex_list[i])

for i in range(16):
    key.append(broken[i].index(png[i]))
key = [str(x) for x in key]
print("".join(key))
```
we get it as `5108180323263640`  
but we have same fields in 8,9,10 index at [2,3,4],[3,4,5,6],[2,3,4]  
there are a total of 36 possibilities  
so let's check them all using burpsuite
we should bruteforce all these possibilities now
and the key was found to be `5108180345363640`
and I got the qr code:
![image](qrcode.png)  


then I used this [tool](https://qrcoderaptor.com/)  
and got the flag to be
>picoCTF{066cad9e69c5c7e5d2784185c0feb30b}
# Javascript Kiddie 2
```
228 80 39 113 0 148 0 143 252 172 225 6 220 243 68 255 63 0 164 243 13 127 26 30 158 48 174 68 6 119 95 128 200 0 191 28 0 107 1 69 243 234 78 13 176 66 110 174 27 16 188 71 135 228 68 235 100 192 219 0 235 72 229 231 56 148 150 114 141 247 101 254 172 69 171 237 90 192 73 117 43 154 78 2 150 254 129 252 124 0 255 71 174 77 152 91 137 13 1 95 69 59 180 0 164 0 78 233 73 171 255 245 0 197 0 0 133 0 243 10 255 120 0 85 0 153 129 195 164 223 70 170 205 10 48 114 73 28 0 243 154 253 15 130 48 32 220 62 37 0 35 65 0 216 156 170 129 59 90 82 112 104 153 12 45 73 221 105 1 147 32 98 68 221 137 108 66 208 191 111 29 45 30 190 84 239 166 159 118 77 151 164 140 250 34 210 24 45 211 223 164 197 74 30 206 132 127 102 111 36 153 144 9 75 10 206 89 102 188 212 103 191 71 20 156 126 73 179 227 131 33 69 226 223 96 88 214 252 91 248 142 219 199 161 196 98 96 0 59 125 205 3 74 206 60 30 69 210 115 144 166 73 249 122 128 229 153 237 231 205 252 122 71 0 143 190 70 255 103 200 65 136 172 166 227 56 55 178 248 255 245 247 24 170 253 165 156 130 31 95 61 57 148 55 159 255 31 96 26 195 185 96 129 252 233 36 36 92 146 111 113 180 242 210 175 208 29 63 102 246 172 154 248 191 12 248 22 153 140 180 61 151 111 0 138 113 101 89 73 125 184 15 12 8 65 144 72 239 249 63 168 110 239 198 158 57 79 235 35 165 197 248 51 223 107 7 132 217 126 255 169 201 223 33 206 181 158 1 166 55 247 219 91 91 14 248 115 149 105 93 117 130 242 84 226 148 83 84 232 117 181 155 51 31 4 180 252 237 161 195 206 164 175 75 19 245 194 65 186 239 62 253 211 111 130 154 24 254 201 214 194 254 105 173 174 5 159 173 8 180 114 23 202 53 39 243 173 87 59 95 61 69 64 219 122 143 62 8 136 51 98 146 128 67 241 126 216 166 166 234 242 191 207 157 242 53 254 39 78 197 215 197 26 33 176 36 193 113 151 211 131 57 158 179 86 113 139 116 59 100 7 189 164 45 200 251 122 12 223 253 179 103 74 228 254 89 155 83 5 173 32 230 126 201 199 199 86 91 126 114 62 105 91 132 183 188 243 193 77 217 243 167 201 190 123 71 196 110 117 115 76 58 103 61 190 114 58 130 232 110 171 147 243 73 157 202 30 235 240 239 174 224 172 149 53 141 170 206 34 55 212 227 229 152 130 217 221 155 221 102 48 87 109 62 235 107 150 58 64 18 142 4 187 24 70 133 180 175 223 13 22 191 126 255 188 198 73 119 40 156 95 111 160 79 155 223 234 138 98 7 145 127 26 141 174 207 179 31 191 122 251 233 191 79 174 130 160 190 232 244 231 191 225 105 222 159 253 46 37 155 3 212 182 239 250 149 102 196 245 107 225 95 126 186 126 233 226 147 189 51 197 30 206 77 239 128 184 176 255 106 236 145 96 160
```
now that key length is 32 but we only consider odd places so we filler elements like 0 first we find the value of key using the previous script.
```
bytes_ = "228 80 39 113 0 148 0 143 252 172 225 6 220 243 68 255 63 0 164 243 13 127 26 30 158 48 174 68 6 119 95 128 200 0 191 28 0 107 1 69 243 234 78 13 176 66 110 174 27 16 188 71 135 228 68 235 100 192 219 0 235 72 229 231 56 148 150 114 141 247 101 254 172 69 171 237 90 192 73 117 43 154 78 2 150 254 129 252 124 0 255 71 174 77 152 91 137 13 1 95 69 59 180 0 164 0 78 233 73 171 255 245 0 197 0 0 133 0 243 10 255 120 0 85 0 153 129 195 164 223 70 170 205 10 48 114 73 28 0 243 154 253 15 130 48 32 220 62 37 0 35 65 0 216 156 170 129 59 90 82 112 104 153 12 45 73 221 105 1 147 32 98 68 221 137 108 66 208 191 111 29 45 30 190 84 239 166 159 118 77 151 164 140 250 34 210 24 45 211 223 164 197 74 30 206 132 127 102 111 36 153 144 9 75 10 206 89 102 188 212 103 191 71 20 156 126 73 179 227 131 33 69 226 223 96 88 214 252 91 248 142 219 199 161 196 98 96 0 59 125 205 3 74 206 60 30 69 210 115 144 166 73 249 122 128 229 153 237 231 205 252 122 71 0 143 190 70 255 103 200 65 136 172 166 227 56 55 178 248 255 245 247 24 170 253 165 156 130 31 95 61 57 148 55 159 255 31 96 26 195 185 96 129 252 233 36 36 92 146 111 113 180 242 210 175 208 29 63 102 246 172 154 248 191 12 248 22 153 140 180 61 151 111 0 138 113 101 89 73 125 184 15 12 8 65 144 72 239 249 63 168 110 239 198 158 57 79 235 35 165 197 248 51 223 107 7 132 217 126 255 169 201 223 33 206 181 158 1 166 55 247 219 91 91 14 248 115 149 105 93 117 130 242 84 226 148 83 84 232 117 181 155 51 31 4 180 252 237 161 195 206 164 175 75 19 245 194 65 186 239 62 253 211 111 130 154 24 254 201 214 194 254 105 173 174 5 159 173 8 180 114 23 202 53 39 243 173 87 59 95 61 69 64 219 122 143 62 8 136 51 98 146 128 67 241 126 216 166 166 234 242 191 207 157 242 53 254 39 78 197 215 197 26 33 176 36 193 113 151 211 131 57 158 179 86 113 139 116 59 100 7 189 164 45 200 251 122 12 223 253 179 103 74 228 254 89 155 83 5 173 32 230 126 201 199 199 86 91 126 114 62 105 91 132 183 188 243 193 77 217 243 167 201 190 123 71 196 110 117 115 76 58 103 61 190 114 58 130 232 110 171 147 243 73 157 202 30 235 240 239 174 224 172 149 53 141 170 206 34 55 212 227 229 152 130 217 221 155 221 102 48 87 109 62 235 107 150 58 64 18 142 4 187 24 70 133 180 175 223 13 22 191 126 255 188 198 73 119 40 156 95 111 160 79 155 223 234 138 98 7 145 127 26 141 174 207 179 31 191 122 251 233 191 79 174 130 160 190 232 244 231 191 225 105 222 159 253 46 37 155 3 212 182 239 250 149 102 196 245 107 225 95 126 186 126 233 226 147 189 51 197 30 206 77 239 128 184 176 255 106 236 145 96 160"
byte_list = bytes_.split(" ")
hex_list=[hex(int(x)) for x in byte_list]
png = ["0x89", "0x50", "0x4e", "0x47", "0xd", "0xa", "0x1a", "0xa", "0x0", "0x0", "0x0" ,"0xd", "0x49", "0x48", "0x44", "0x52"]

broken=[]
for i in range(16):
    broken.append([])
key = []
LEN = len(hex_list)
for i in range(LEN):
    broken[i%16].append(hex_list[i])
prob = []
for i in range(16):
    key.append(broken[i].index(png[i]))
for i in range(16):
    prob.append(broken[i][:10].count(png[i]))
    
print(prob)
print(png[9])
print(broken[10])
key = [str(x) for x in key]
print("".join(key))

```
so I got the key to be 6053181795726309 and 9,10 position have two possibilities [5,6],[7,8].  
so on manual trail the key is found to be 6053181795726309.  
![image](qrcode_2.png)  
and the flag is
>picoCTF{59d5db659865190a07120652e6c77f84}

