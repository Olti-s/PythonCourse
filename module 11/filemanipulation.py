lines=["Hello world\n","Welcome to Python\n"]
with open("example.txt","w") as file: #we open the file with permissions to wtire
    file.writelines(lines) # we write on multiple lines