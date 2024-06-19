## Challenge 1: 
    The first challengee is just to submit the given key by doing a simple copy paste.
> crypto{y0ur_f1rst_fl4g}  

## Challenge 2:
Now the challenge introduces to python scripting and gives us the code:
    #!/usr/bin/env python3

    import sys
    #import this

    if sys.version_info.major == 2:
        print("You are running Python 2, which is no longer supported. Please update to Python 3.")

    ords = [81, 64, 75, 66, 70, 93, 73, 72, 1, 92, 109, 2, 84, 109, 66, 75, 70, 90, 2, 92, 79]
    print("Here is your flag:")
    print("".join(chr(o ^ 0x32) for o in ords))

>crypto{z3n_0f_pyth0n}

## Challenge 3:
This challenge required us to the local server and send a json file to it so that we recieve thee flag the code for the process is:  

    #!/usr/bin/env python3

        from pwn import * # pip install pwntools
    import json

    HOST = "socket.cryptohack.org"
    PORT = 11112

    r = remote(HOST, PORT)


    def json_recv():
        line = r.readline()
        return json.loads(line.decode())

    def json_send(hsh):
        request = json.dumps(hsh).encode()
        r.sendline(request)


    print(r.readline())
    print(r.readline())
    print(r.readline())
    print(r.readline())

    request = {
        "buy": "flag"
    }
    json_send(request)

    response = json_recv()

    print(response)

> crypto{sh0pp1ng_f0r_fl4g5}

