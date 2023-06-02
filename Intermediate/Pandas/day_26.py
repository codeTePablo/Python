# # list comprehension 
# import math
# import random as rd
import pandas as pd

# number = [1,2,3]

# # new item = n+1
# # item = n 
# new_number = [n+1 for n in number]
# print(new_number)

# name = "Pablo"
# new_name = [letter for letter in name]
# print(new_name)

# range_list = [num * 2 for num in range(1,10)]
# print(range_list)

# names = ["Jose", "Pablo", "Sanchez", "Sanchezz"]
# short_names = [name for name in names if len(name) > 3]
# short_names_low = [name.lower() for name in names if len(name) > 3]
# print(short_names)
# print(short_names_low)

# numbers = [1,1,2,3,5,8,13,21,34,55]
# squared_numbers = [n for n in numbers if n % 2 ==0]
# print(squared_numbers)

# # using disctionary

# dictionary_ = [{"name":"Pablo"}]

# #new_key:new_value for names
# score = {student:rd.randint(1,100) for student in names}
# print(score)

# passing = {student:score for (student,score) in score.items() if score >= 60}
# print(passing)

# # generate like this but more simplify
# # students_score = {
# #     "Jose": rd.randint,
# #     "Pablo": rd.randint,
# #     "Sanchez": rd.randint,
# #     "Sanchezz": rd.randint
# # }

# sentence = "I Show Speed loves Cristiano"
# result = {word:len(word) for word in sentence.split()}
# print(result)

data = pd.read_csv("alphabet.csv")

dictionary = {row.letter:row.code for (index, row) in data.iterrows()} 
print(dictionary)

word = input(" ").upper()
out_list = [dictionary[letter] for letter in word]
print(out_list)