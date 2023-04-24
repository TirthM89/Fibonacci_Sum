from tkinter import *
root = Tk()
root.title("Fibonacci")
root.geometry("400x400")

label_series = Label(root, text = "Fibonacci Series ")
enter = Entry(root)
label_sum = Label(root)

def Fibonacci():
    num = int(enter.get())
    fn = 0
    sn = 1
    sum = 0
    counter = 1
    while(counter <= num):
        label_series["text"]+=str(sum)+" "
        counter = counter+1
        fn = sn
        sn = sum
        sum = fn+sn

    label_sum["text"]="The sum is "+str(sum)
    
btn = Button(root, text = "Show Fibonacci Series", command = Fibonacci)

enter.pack()
btn.pack()
label_series.pack()
label_sum.pack()

root.mainloop()