with open("example.txt","w",encoding="utf-8") as f:   #w means write mode,it covers the original content
    f.write("hello world I/O!\n")
    f.write("This is second line.\n")

with open("example.txt","r",encoding="utf-8") as f:  
    content=f.read()
    print("read from file:")  
    print(content)

with open("example.txt","r",encoding="utf-8") as f: # this means read line by line
    print("read line by line:")
    for line in f:
        print("line one content:",line.strip())

with open("example.txt","a",encoding="utf-8") as f:   #a means append mode ,it will not cover the original content
                  f.write("this is appended line.\n")


a_list=["apple","banana","cherry"]
with open("fruits.txt","w",encoding="utf-8") as f:
       for line in a_list:
              f.write(line+"\n")

with open("fruits.txt","r",encoding="utf-8") as f:
       print(f.read())
