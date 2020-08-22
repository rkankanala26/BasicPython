#methods no inputs, no outputs

def sayBookname():
    print("Book Name")
    
# call the method
sayBookname() 

#Method with one input and no ouptuts
def sayBookname(name):
    print(f"Book Name {name}")
    
#call method
sayBookname('Ramanayam')

#Method with no inputs and one output

def getBook():
    return "Ramayanam"

# call the method

message = getBook()
print(message)

#Method with one input and one output

def getBook(name):
    return f"Ramayanam {name}"
    
# call the method
message = getBook('Ramayanam')
print (message)

#Method with multiple inputs and one output
def getBook(name, message):
    return f"Ramayanam {name}, you said{message}"
#call the method
message = getBook ('Ramayanam', ' How is it?')
print(message)


    

     




