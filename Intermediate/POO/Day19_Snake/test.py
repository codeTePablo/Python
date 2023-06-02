# to write inside file 
with open('save_score.txt', mode="w") as file:
    file.write("here")
file.close()

with open('save_score.txt') as file:
    read_data = file.read()
    print(read_data)
file.close()