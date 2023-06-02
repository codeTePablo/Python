import random as rn
def for_loop():
    ls = ["nam1, nam2, nam3"]
    new = []
    for i in ls:
        print(i)

def average():
    student_heights = input("insert students data: ").split(",")

    # print data in list 
    # convert str to int
    a = len(student_heights)
    for n in range(0, a):
        student_heights[n] = int(student_heights[n])
    print(student_heights)

    # sum the total data in list 
    total_height = 0
    for height in student_heights:
        total_height += height
    print(total_height)

    # len list students_heights
    number_students = 0
    for students in student_heights:
        number_students += 1

    avg = round(total_height/number_students, 2)
    print(avg)        

def hight_score():
    student_score = input("insert students data: ").split(",")
    a = len(student_score)
    for n in range(0, a):
        student_score[n] = int(student_score[n])
    print(student_score)

    # check all list and load the first and continue += 
    # if score > high continue or pass
    hight_score = 0
    for score in student_score:
        if score > hight_score:
            hight_score = score
    print(score) 
    print(f"the high score is : {hight_score}")

def sum_even():

    even = 0
    for n in range(2, 101,2):
        even += n      
    print(even)



def password_generator():
    ls_up = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R',
    'S','T','U','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','q','l','m',
    'o','p','q','r','s','t','u','w','x','y','z']
    symbols = ['!','@','#','$','%','^','*']
    numbers = ['0','1','2','3','4','5','6','7','8','9']

    print("Password Generator")
    user_choise_letter = int(input("how many letter would u like in u password?"))
    user_choise_symbols = int(input("how many symbols would u like in u password?"))
    user_choise_number = int(input("how many number would u like in u password?"))

    # Eazy level 
    # fghf^&23
    # password = ""
    # for n in range(1, user_choise_letter + 1):
    #     password += rn.choice(ls_up)

    # for n in range(1, user_choise_symbols + 1):
    #     password += rn.choice(symbols)
    
    # for n in range(1, user_choise_number + 1):
    #     password += rn.choice(numbers)

    # print(password)

    # Hard level 
    # g^2jk8&
    password_list = []
    for n in range(1, user_choise_letter + 1):
        password_list += (rn.choice(ls_up))

    for n in range(1, user_choise_symbols + 1):
        password_list += (rn.choice(symbols))
    
    for n in range(1, user_choise_number + 1):
        password_list += (rn.choice(numbers))

    rn.shuffle(password_list)

    password = ""
    for char in password_list:
        password += char
    print(password)
    


if __name__ == '__main__':
    # for_loop()
    # average()
    # hight_score()
    # sum_even()
    password_generator()