

with open("file.txt", "r") as file:
    content = file.read()
    totalLetters = len(content)
with open("file.txt", "r") as file:
    word = file.readlines()
    
print(f"totalWords :{len(word)} , totalletters :{totalLetters}")

    

count = 0 
with open("file.txt","r") as file:
    for i in file:
        count+=1
print("total lines",count)



    
    
   


    

    
    

    
    

   

    
   




    

 


