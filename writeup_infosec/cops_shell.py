import cops
File=input("enter the file to be compiled: ")
with open(File,"rb") as f:
    lines=f.readlines()
    lines=compile.run()
