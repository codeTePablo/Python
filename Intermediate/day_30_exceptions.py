try:
    # somethiong that might cause an exception 
    file = open("a_file.txt")
    a_dictionary = {"key": "value"}
    print(a_dictionary["key"]) # this don't print if file until has create
except FileNotFoundError: 
    # do this if there was an exception
    # genereate file 
    file = open("a_file.txt", "w")
    file.write("Generate file")
except KeyError as error_message:
    # if have an arror 
    print(f"The key {error_message} doesn't exist")
else:
    # for this if there were no exceptions
    content = file.read()
    print(content)
finally:
    # fo this no matter waht happens
    file.close()

fruits = ["banana", "strowberry", "apple"]

def fruit(index):
    try:
        banana = fruits[index]
    except IndexError:
        print("fruit pie")
    else:
        print(fruit + "pies")
