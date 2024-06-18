# Forensics
## Challenge 1 :
### information
the hint says: Files can always be changed in a secret way. Can you find the flag? cat.jpg
so I first went into the exiftool command to go through the metadata there i found two strings of different encoding and I found a field of saying encoding type saying **huffman** encoding.  
So i downloaded hurl command to decode the license term in huffman encoding so i get the flag.  
>picoCTF{the_m3tadata_1s_modified}

## Challenge 2 :
### matryoshka dolls
The description says: Matryoshka dolls are a set of wooden dolls of decreasing size placed one inside another. What's the final one? Image: this  
here the dolls in doll may claims the files hidden in the file so we use binwalker tool for finding the hidden files so we get so hidden files for 3 times consecutively and then a text file having the flag
>picoCTF{e3f378fe6c1ea7f6bc5ac2c3d6801c1f}
## challenge 3:
### Tunn3l v1s10n
hint: We found this file. Recover the flag.  
this specific challenge needs us go through the hexadump format of the file which is corrupted by with the message **bad0** so i studied the format of header and dib header of the given version and corrected the bytes using hexeditor where the missing bytes actually represents the size of the header file and the dib header part hence we get the image. BUT on looking into the image we can see that image is not completely given but the dimensions in the header file should be changed so i first changed width of the file but the image got distorted but on changing length i got the flag.
>picoCTF{qu1t_a_v13w_2020}

## Challenge 4:
### MAcroHard WeakEdge
Here i got some ppts which can not be opened directly so I searched for exiftools but found nothing interesting and then went on finding huge no.of files with binwalker and there i extracted the zip files later I went into the ppts directory as I have an empty file on one side and a with xml contents and a image with nothing unusual on other so i decided to choose dive into ppts subdirectory and there I found slides and slideLayouts which can not be opened as they are the slides of the file finally i peeped into a subdirectory naming slideMaster where I found the file named ***hidden*** which is an usual text file but on decoding by assuming it to be base64 I got the flag.
>flag: picoCTF{D1d_u_kn0w_ppts_r_z1p5}

## Challenge 5:
### Enhance!:
now we have nothing in the picture like in binwalk or exiftools we just have a pice of code so the only option for us is to go through the code on doing so we observe this at the last parrt of the code:
```
{ 3 n h 4 n </tspan><tspan
         sodipodi:role="line"
         x="107.43014"
         y="132.11588"
         style="font-size:0.00352781px;line-height:1.25;fill:#ffffff;stroke-width:0.26458332;"
         id="tspan3752">c 3 d _ a a b 7 2 9 d d }
```
here we find flag here at starting and ending of the code.
>picoCTF{3nh4nc3d_aab729dd}
## Challenge 6:
### advanced-potion-making:
I have got a file *advanced-potion-making* on doing a useless stuff of binwalk and exiftools I've decided to go through the xxd command and It was found to be corrupted png file so I changed the signature and fixed the ihdr length and finally I got an image which is stegnographed using the [website](https://incoherency.co.uk/image-steganography/#unhide) 
and found the flag finally.
>picoCTF{w1z4rdry}

## Challenge 7:
### File type
description:This file was found among some files marked confidential but my pdf reader cannot read it, maybe yours can.
You can download the file from here.  
from exiftools i identified the file to be a script and with file command we get it as shell archive. we decode it by installing sharutils and then run the shell script so we get a file out in the directory which is archive i.e. flag.ar we decode it by.
>ar -x flag.ar

we find file typr again which is cpio now we name it as flag.cpio
>cpio -iv < flag.cpio

now that file is bzip2
>bzip2 -d flag

we find a flag.out which is gzip
> gz -d flag.gz

now again the file is lunzip
>lunzip -d flag

now again it is lz4 
>lz4 -d flag

here it is lzma file
> lzma -d flag.xz

here again it is lzop file
> lzop -d flag -oflag.a

it is lzip file
>lzip -d flag.a

fianlly there is an xz compressed file 
>unxz -d flag.a

we get a hexdump file we retrace it by
>xxd -p -r flag
```
picoCTF{f1len@m3_m@n1pul@t10n_f0r_0b2cur17y_79b01c26}
```
## Challenge 8:
### findme
for this an image is downloaded and going throungh the binwalk command 
>binwalk -e flag.png

there we get a file in the directory named secret in which there is an image called as flag.png
>picoCTF{Hiddinng_An_imag3_within_@n_ima9e_ad9f6587}

## Challenge 9:
### MSB  
given that the image should we decoded with MSB so i used this [link](https://stegonline.georgeom.net/upload) so from here i got a huge amount of data so that i used grep command for finding the flag
>picoCTF{15_y0ur_que57_qu1x071c_0r_h3r01c_24d55bee}

## Challenge 10:
### extensions
It is obvious now that some thing wrong with extensions then i went through xxd of the file which is so obvious to be png hence i renamed the extension to png then I got an image showing the flag
>picoCTF{now_you_know_about_extensions}

# OSINT
## Challenge 1:
### Sakura room:
Here the task 0 is just to enter let's go now in task 1  
description: 

>The OSINT Dojo recently found themselves the victim of a cyber attack. It seems that there is no major damage, and there does not appear to be any other significant indicators of compromise on any of our systems. However during forensic analysis our admins found an image left behind by the cybercriminals. Perhaps it contains some clues that could allow us to determine who the attackers were?  
We've copied the image left by the attacker, you can view it in your browser [HERE](https://raw.githubusercontent.com/OsintDojo/public/3f178408909bc1aae7ea2f51126984a8813b0901/sakurapwnedletter.svg).


now we just click the link and right click on the image and click view source there we can find the the inscape-export filename there we find the name to be  
>inkscape:export-filename="/home/SakuraSnowAngelAiko/Desktop/pwnedletter.png"

hence username is ***SakuraSnowAngelAiko***  
Now we move to task 2:  
>description:
It appears that our attacker made a fatal mistake in their operational security. They seem to have reused their username across other social media platforms as well. This should make it far easier for us to gather additional information on them by locating their other social media accounts.  
Most digital platforms have some sort of username field. Many people become attached to their usernames, and may therefore use it across a number of platforms, making it easy to find other accounts owned by the same person when the username is unique enough. This can be especially helpful on platforms such as on job hunting sites where a user is more likely to provide real information about themselves, such as their full name or location information.  
**Instruction**:  
A quick search on a reputable search engine can help find matching usernames on other platforms, and there are also a large number of specialty tools that exist for that very same purpose. Keep in mind, that sometimes a platform will not show up in either the search engine results or in the specialized username searches due to false negatives. In some cases you need to manually check the site yourself to be 100% positive if the account exists or not. In order to answer the following questions, use the attacker's username found in Task 2 to expand the OSINT investigation onto other platforms in order to gather additional identifying information on the attacker. Be wary of any false positives!  

so now I used a tool called sherlock in my kali and found out that there are accounts on this name on reddit,github, ... but all are false positives except github so I went into git I found a repo being forked by many people so I cloned it as it says PGP and later I learned that PGP is something like ssh i.e. encryption system so i got pgp key (public) so I used gpg command to connect as doing so I got email of the account 
>SakuraSnowAngel83@protonmail.com

with this I got mail id . Now I started looking for her fool name so I searched the name directly in th chrome I found a twitter handel named sakuraloveraiko as obviously the middlename is random where I found a name called as AIKO ABE  
now it is task 4:
>description:  
It seems the cybercriminal is aware that we are on to them. As we were investigating into their Github account we observed indicators that the account owner had already begun editing and deleting information in order to throw us off their trail. It is likely that they were removing this information because it contained some sort of data that would add to our investigation. Perhaps there is a way to retrieve the original information that they provided?   
On some platforms, the edited or removed content may be unrecoverable unless the page was cached or archived on another platform. However, other platforms may possess built-in functionality to view the history of edits, deletions, or insertions. When available this audit history allows investigators to locate information that was once included, possibly by mistake or oversight, and then removed by the user. Such content is often quite valuable in the course of an investigation. In order to answer the below questions, you will need to perform a deeper dive into the attacker's Github account for any additional information that may have been altered or removed. You will then utilize this information to trace some of the attacker's cryptocurrency transactions.  

For this I went into the github repository so I found two repos with suspicios name one is bitcoin and other is ETH. I went into ETH being recently updated there it contains a single file with single line which is 
>0xa102397dbeeBeFD8cD2F73A89122fCdB53abB6ef.Aiko:pswd@eu1.ethermine.org:4444

which is the account address by searching it directly into google we find it as an crypto wallet where all transanctions are visible in ethereum. and there are also other tranction using tether using Ethermine pool.  
Now it is Task4:  
>Just as we thought, the cybercriminal is fully aware that we are gathering information about them after their attack. They were even so brazen as to message the OSINT Dojo on Twitter and taunt us for our efforts. The Twitter account which they used appears to use a different username than what we were previously tracking, maybe there is some additional information we can locate to get an idea of where they are heading to next?  
We've taken a screenshot of the message sent to us by the attacker, you can view it in your browser here.   
Although many users share their username across different platforms, it isn't uncommon for users to also have alternative accounts that they keep entirely separate, such as for investigations, trolling, or just as a way to separate their personal and public lives. These alternative accounts might contain information not seen in their other accounts, and should also be investigated thoroughly. In order to answer the following questions, you will need to view the screenshot of the message sent by the attacker to the OSINT Dojo on Twitter and use it to locate additional information on the attacker's Twitter account. You will then need to follow the leads from the Twitter account to the Dark Web and other platforms in order to discover additional information.


There we asked about attackers official twitter handle  
>sakuraloveraiko  

we found this out from our previous search results themselves.  
WE have to go through the **DARK PASTE** website for the wifi ssid and passwords as seen in the twitter handels post for this we either have to use browsers like duckduckgo and the deep paste server may be on and off for many times but the answer might be.
>deepv2w7p33xa4pwxzwi2ps4j62gfxpyp44ezjbmpttxz3owlsp4ljid.onion/show.php?md5=

as of seen from the screenshot as the deep paste server is closed now.  
for bssid i used a website from osint framework named as WiGLE. and searched for bssid using ssid and finally got the bssid.
>84:af:ec:34:fc:f8

now task6:
now that i installed a reveye tool to scan images by the chronological order of posting images it was found out to be the initial post is made i.e. before gng to take flight is from washington which contains the washington monument but later we have a post at longue which is at handae tokyo there after i saw a free city wifi naming to the city **Hirosaki** most probably his final home town so I decided to look into the japan map in between tokyo to hirosaki and I found the region mentioned in the twitter post and found the name of the lake to be **lake inawashiro**  
## Challenge 2:
Exercise006  
here I reviewed the image using reveye osint tool that i collected from osint framework and i inspected it and the photo is found to be fake as the photo also present in many articles published before 19 jan 2023 hence   
***NO***  

## Challenge 3:
exercise004  
Task briefing:
This is a photo of a resort located on an island.  
1.   What is the name of the resort?  
2.   What are the coordinates of the island?  
3.   In which cardinal direction was the camera facing when   the photo was taken?

by doing a quick search in google with reveye It was found out to be **Oan resort**.  
and then the coordinates are found after searching to be:7º 21' 45" N, 151º 45' 22" L  
now with google earth we can see direction as northwest.
## challenge 4:
exercise003  
In April 2017 Mohamed Abdullahi Farmaajo, the then president of Somalia, visited Turkey. A news agency published a photo where he was seen shaking hands with Recep Tayyip Erdoğan, the country’s president. The article did not disclose where the photo was taken. Your task is to find out the name and coordinates of the location seen below.

so as usual i used reveye again and now it says ankara presidential palace so I went to google map for finding out the cordinates.
>The coordinates for the Presidential Complex in Ankara, Turkey are 39.9308°N latitude and 32.7989°E longitude  

## Challenge 5:
exercise014  
The video below was recorded during an earthquake.
Please find the answer to the following questions:

1.  What was the magnitude of this earthquake?
2.  What are the coordinates of where the camera was likely located in order to record this scene?  

now that i searced the screenshot of the image in google lens and clicked on **find source** and found the youtubbe videos saying  
Moldova earthquake  
Cutremur chisinau  
which says the name os the place is **Moldova chisinau** wheree cutremur is a word meant for earthquake.
>latitude 47.00556 and longitude 28.8575

## Challenge 6:
exercise026  
The image below shows the contents of a zip file. Inside you will find a 31-second video recorded during a train ride, and four photos of undisclosed locations. They were all taken by the same individual in February 2024. Despite having no useful metadata, they still contain enough information to track down this person’s movements.
Your task is to determine:

1. At which train stations did the person board and alight?

  
and Image_2597 is from chosu bazar complex,central market of Tashkent.

Here I found the hoardings in uzbek and with image_2626it is clear that from lens it is a Navruz park, Tashkent, Uzbekistan.  

now the image_2658 is from a street named as saray District, Tashkent, Uzbekistan that I found from samasung galaxy hoarding in the picture.  
Now he took train from tashkent as seen from the file names of the photos and left the tashkent on early morning as the photo in image_2658 shows sunrise.   

from [here](https://www.advantour.com/uzbekistan/trains/timetable.htm) I got the time table of the trains and the sunrise time is around 7:20 AM so we look for trains at 7:30 AM from Tashkent. We get direction of travel from the video. that is south to Tashkent there are samarkhand, Navoi, Bhukara. so ig it's enough to search for bridges to match the place of destination. Hopefully bridges in bukhara aren't so big so we ca move to navoi even the only bridge in navoi is not so similar so it must be samarkhand and finally found the bridge to be siyab bridge