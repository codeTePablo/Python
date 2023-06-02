from tkinter import * 

window = Tk()
window.minsize(300, 100)

# label 
label = Label(text="Calculate km to miles :)")
label.grid(column=2, row=0)
# entry cell
input = Entry()
input.grid(column=3,row=1)

def button_cliked():
    """ testing how works the buttom """
    # print("Here")
    # update label
    # label.config(text="Here Label")
    # return data inside input
    print(input.get())
    
def calculate():
    """ calcutate km to miles 
    1 km = 0.6213712 mile 
    """
    number = input.get()
    result = int(number) / 1.609344, "miles"
    # print result in console
    # print(result)
    label.config(text=result)

# Button 
button = Button(text="Click", command=calculate)
button.grid(column=3,row=2)


window.mainloop()
