
from tkinter import *
import math


win = Tk()
win.title("Scientific Calculator by Sam")
win.configure(background="black")
win.resizable(width=False, height=False)
win.geometry("930x568+0+0")

calc = Frame(win)
calc.grid()

#=== Class & methods===========

class Calc():
    def __init__(self):
        self.current = ""
        self.total = 0
        self.val_input = True
        self.check_sum = False
        self.op = ""
        self.result = False

    def display(self, value):
        entered.delete(0, END)
        entered.insert(0, value)


    def num_entry(self, num):
        self.result = False
        first_num = entered.get()
        second_num = str(num)
        if self.val_input:
            self.current = second_num
            self.val_input= False
        else:
            if second_num == ".":
                if second_num in first_num:
                    return
            self.current= first_num+second_num
        self.display(self.current)

    def Equal(self):
        self.result = True
        try:
          self.current = float(self.current)
          if self.check_sum == True :
               self.validate()
          else:
             self.total = float(entered.get())
        except (SyntaxError,ZeroDivisionError,ValueError):
            self.current=str('error')
            self.display(self.current)


    def validate(self):
        if self.op == "multi":
            self.total *= self.current
        elif self.op == "divide":
            self.total /= self.current
        elif self.op == "add":
            self.total += self.current
        elif self.op == "sub":
            self.total -= self.current
        elif self.op == "pow":
            self.total **= self.current
        self.val_input = True
        self.check_sum = False
        self.display(self.total)

    def operation(self, op):
        self.current = float(self.current)
        if self.check_sum:
            self.validate()
        elif not self.result:
            self.total = self.current
            self.val_input = True
        self.check_sum = True
        self.op = op
        self.result = False

    def clear_ent(self):
        self.result = False
        self.current = "0"
        self.display(0)
        self.val_input = True

    def Clear(self):
        self.clear_ent()
        self.total = 0

    def Sign(self):
        self.result = False
        self.current = -(float(entered.get()))
        self.display(self.current)

    def Power(self):
        self.result = False
        self.current = math.pow(float(entered.get()), float(entered.get()))
        self.display(self.current)

    def pi(self):
        self.result = False
        self.current = math.pi
        self.display(self.current)

    def e(self):
        self.result = False
        self.current = math.e
        self.display(self.current)

    def factoriel(self):
        self.result = False
        self.current = math.factorial(int(entered.get()))
        self.display(self.current)
        self.display(self.ERROR)


    def sq(self):
        self.result = False
        self.current = math.sqrt(float(entered.get()))
        self.display(self.current)

    def Square(self):
        self.result = False
        self.current = ((float(entered.get()))*(float(entered.get())))
        self.display(self.current)


    def exp(self):
        self.result = False
        self.current = math.exp(float(entered.get()))
        self.display(self.current)


    def inverse(self):
        self.result = False
        self.current = 1/float(entered.get())
        self.display(self.current)



#trigonometry methods

    def degrees(self):
        self.result = False
        self.current = math.degrees(float(entered.get()))
        self.display(self.current)

    def rad(self):
        self.result = False
        self.current = math.radians(float(entered.get()))
        self.display(self.current)


    def cos(self):
        self.result = False
        self.current = math.cos(math.radians(float(entered.get())))
        self.display(self.current)

    def sin(self):
        self.result = False
        self.current = math.sin(math.radians(float(entered.get())))
        self.display(self.current)

    def tan(self):
        self.result = False
        self.current = math.tan(math.radians(float(entered.get())))
        self.display(self.current)


    def atan(self):
        self.result = False
        self.current = math.atan(math.radians(float(entered.get())))
        self.display(self.current)


    def asin(self):
        self.result = False
        self.current = math.asin(float(entered.get()))
        self.display(self.current)

    def acos(self):
        self.result = False
        self.current = math.acos(float(entered.get()))
        self.display(self.current)



#logarithimic methods

    def log(self):
        self.result = False
        self.current = math.log(float(entered.get()))
        self.display(self.current)

    def log10(self):
        self.result = False
        self.current = math.log10(float(entered.get()))
        self.display(self.current)

#other bases conversion

    def bin(self):
        self.result = False
        self.current = format(int(entered.get()),'b')
        self.display(self.current)


    def oct(self):
        self.result = False
        self.current = oct(int(entered.get()))
        self.display(self.current)



    def hex(self):
        self.result = False
        self.current = hex(int(entered.get()))
        self.display(self.current)



added_value=Calc()

entered=Entry(calc, font=("arial",20,"bold"), bg="white", bd=30, width=29,  justify=RIGHT)
entered.grid(columnspan=10, pady=1)
entered.insert(0,"0")

numberpad = "789456123"
i = 0
btn = []
for j in range(2,5):
    for k in range(3):
        btn.append(Button(calc, width=6, height=2, font=("arial", 20, "bold"), bd=4, text=numberpad[i]))
        btn[i].grid(row=j, column=k, pady=1)
        btn[i]["command"] = lambda x=numberpad[i] : added_value.num_entry(x)
        i += 1


#======== Buttons================#

btnClear = Button(calc, text=chr(67), width=6, height=2, font=("arial", 20, "bold"),
                  bd=4, bg="#cb1eff", command=added_value.clear_ent).grid(row=1, column=0, pady=1)

btnClearA = Button(calc, text=chr(67) + chr(69), width=6, height=2, font=("arial", 20, "bold"),
                     bd=4, bg="grey", command=added_value.Clear)\
    .grid(row=1, column=1, pady=1)

btnsq= Button(calc, text="√", width=6, height=2, font=("arial", 20, "bold"),
              bd=4, bg="grey", command=added_value.sq).grid(row=1, column=2, pady=1)

btnadd = Button(calc, text="+", width=6, height=2, font=("arial", 20, "bold"),
                bd=4, bg="grey", command=lambda: added_value.operation("add")).grid(row=1, column=3, pady=1)

btnsub = Button(calc, text="-", width=6, height=2, font=("arial", 20, "bold"),
                bd=4, bg="grey", command=lambda: added_value.operation("sub")).grid(row=2, column=3, pady=1)

btnmul = Button(calc, text="*", width=6, height=2, font=("arial", 20, "bold"),
                bd=4, bg="grey", command=lambda: added_value.operation("multi")).grid(row=3, column=3, pady=1)

btndiv = Button(calc, text=chr(247), width=6, height=2, font=("arial", 20, "bold"),
                bd=4, bg="grey", command=lambda: added_value.operation("divide")).grid(row=4, column=3, pady=1)

btnDot = Button(calc, text=".", width=6, height=2, font=("arial", 20, "bold"),
                bd=4, bg="grey", command=lambda: added_value.num_entry(".")).grid(row=5, column=0, pady=1)

btn0 = Button(calc, text="0", width=6, height=2, font=("arial", 20, "bold"),
              bd=4, command=lambda: added_value.num_entry(0)).grid(row=5, column=1, pady=1)

btnsign = Button(calc, text=chr(177), width=6, height=2, font=("arial", 20, "bold"),
                 bd=4, bg="grey", command=added_value.Sign).grid(row=5, column=2, pady=1)

btneq = Button(calc, text="=", width=6, height=2, font=("arial", 20, "bold"),
               bd=4, bg="grey", command=added_value.Equal).grid(row=5, column=3, pady=1)


btnPi = Button(calc, text="π", width=6, height=2, font=("arial", 20, "bold"),
               bd=4, bg="grey", command=added_value.pi).grid(row=1, column=4, pady=1)

btnsin = Button(calc, text="sin", width=6, height=2, font=("arial", 20,"bold"),
                bd=4, bg="grey", command=added_value.sin).grid(row=1, column=5, pady=1)

btncos= Button(calc, text="cos", width=6, height=2, font=("arial", 20, "bold"),
               bd=4, bg="grey", command=added_value.cos).grid(row=1, column=6, pady=1)

btntan = Button(calc, text="tan", width=6, height=2, font=("arial", 20, "bold"),
                bd=4, bg="grey", command=added_value.tan).grid(row=1, column=7, pady=1)


#-----------------------------------------------------------------------------------------------------

btnSquare = Button(calc, text="x^2", width=6, height=2, font=("arial", 20, "bold"),
                bd=4, bg="grey", command=added_value.Square).grid(row=2, column=4, pady=1)

btnasin= Button(calc, text="asin", width=6, height=2, font=("arial", 20, "bold"),
                 bd=4, bg="white", command=added_value.asin).grid(row=2, column=5, pady=1)

btnacos= Button(calc, text="acos", width=6, height=2, font=("arial", 20, "bold"),
                bd=4, bg="white", command=added_value.acos).grid(row=2, column=6, pady=1)

btnatan = Button(calc, text="atan", width=6, height=2, font=("arial", 20, "bold"),
                 bd=4, bg="white", command=added_value.atan).grid(row=2, column=7, pady=1)
#-----------------------------------------------------------------------------------------------------------------------
btnlog = Button(calc, text="ln", width=6, height=2, font=("arial", 20, "bold"),
                bd=4, bg="grey", command=added_value.log).grid(row=4, column=4, pady=1)

btnexp = Button(calc, text="e^x", width=6, height=2, font=("arial", 20, "bold"),
                bd=4, bg="white", command=added_value.exp).grid(row=4, column=5, pady=1)

btnFactoriel = Button(calc, text="x!", width=6, height=2, font=("arial", 20, "bold"),
                bd=4, bg="white", command=added_value.factoriel).grid(row=4, column=7, pady=1)

btne= Button(calc, text="e", width=6, height=2, font=("arial", 20, "bold"),
             bd=4, bg="white", command=added_value.e).grid(row=4, column=6, pady=1)
#-----------------------------------------------------------------------------------------------------------------------

btnPower = Button(calc, text="^", width=6, height=2, font=("arial", 20, "bold"),
                 bd=4, bg="grey", command=lambda: added_value.operation("pow")).grid(row=3, column=4, pady=1)

btndeg = Button(calc, text="deg", width=6, height=2, font=("arial", 20, "bold"),
                bd=4, bg="white", command=added_value.degrees).grid(row=3, column=5, pady=1)

btnRadians = Button(calc, text="rad", width=6, height=2, font=("arial", 20, "bold"),
                  bd=4, bg="white", command=added_value.rad).grid(row=3, column=6, pady=1)

btnInverse= Button(calc, text="1/x", width=6, height=2, font=("arial", 20, "bold"),
                 bd=4, bg="white", command=added_value.inverse).grid(row=3, column=7, pady=1)
#-----------------------------------------------------------------------------------------------------------------------

btnlog10 = Button(calc, text="log10", width=6, height=2, font=("arial", 20, "bold"),
                  bd=4, bg="grey", command=added_value.log10).grid(row=5, column=4, pady=1)

btnhex = Button(calc, text="hex", width=6, height=2, font=("arial", 20, "bold"),
                  bd=4, bg="grey", command=added_value.hex).grid(row=5, column=7, pady=1)

btnoct = Button(calc, text="oct", width=6, height=2, font=("arial", 20, "bold"),
                   bd=4, bg="grey", command=added_value.oct).grid(row=5, column=6, pady=1)

btnbin= Button(calc, text="bin", width=6, height=2, font=("arial", 20, "bold"),
                  bd=4, bg="grey", command=added_value.bin).grid(row=5, column=5, pady=1)


win.mainloop()