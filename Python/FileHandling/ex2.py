
with open("file.txt","w") as file:
    file.write("hello Word")
    
with open ("file.txt","r")as file:
    content = file.read()
    print(content)
