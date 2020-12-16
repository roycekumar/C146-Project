from tkinter import *
root=Tk()
root.title("Fibonacci")
root.geometry("400x400")
label_series=Label(root)
label_sum=Label(root)
my_input=Entry(root)
def Fibonacci():
    num=int(my_input.get())
    total=0
    first_no=0
    second_no=1
    sum=0
    total=sum
    counter=1
    label_series['text']="Fibonacci Series: "
    while(counter<=num):
        label_series['text']+=str(sum)+" "
        counter=counter+1
        first_no=second_no
        second_no=sum
        total+=sum
        sum=first_no+second_no
        label_sum['text']="Fibonacci Sum : "+str(total)
btn=Button(root,text="Show Fibonacci Series",command=Fibonacci,bg='#000088',fg='white')
my_input.pack()
btn.pack()                                                                                                    
label_series.pack()
label_sum.pack()
root.mainloop() 