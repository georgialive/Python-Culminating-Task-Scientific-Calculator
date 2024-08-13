# Name: Georgia Vrana
# Date Submitted: Thursday, May 9th, 2024
# Culminating Task: Scientific Calculator
# Description: This program creates a graphical user interface (GUI) for a scientific calculator
#              using Python's Tkinter library, allowing users to perform a variety of mathematical operations.

#   NOTES:
#       1. The program cannot handle multiple advanced functions at once, so PLEASE CLICK EQUALS inbetween
#          your advanced calculations functions.
#       2. To use the advanced functions, type your number BEFORE you click the function's button.
#       3. The program will not work if you type in a letter or a symbol that is not one of the buttons
#          and you will recieve an error message.

import tkinter as tk  # Import the tkinter library for creating the GUI
import math  # Import the math library for mathematical functions

# Create the main window
root = tk.Tk()
root.title('Scientific Calculator')  # Set the window title
root.configure(bg='#FFEBCD')  # Set the background color of the window
root.resizable(width=False, height=False)  # Make the window not resizable

# Create an entry field for displaying numbers and expressions
ent_field = tk.Entry(root, bg='#D3D3D3', fg='#000080', font=('Arial', 35),
                     borderwidth=5, justify="right")
ent_field.grid(row=0, columnspan=10, padx=5, pady=5,
               sticky='n'+'s'+'e'+'w')
ent_field.insert(0, '0')  # Insert initial value '0' into the entry field

FONT = ('Arial', 20, 'bold')  # Define the font for buttons

class SC_Calculator():
    def __init__(self):
        self.current = ''  # Current input value
        self.inp_value = True  # Flag to check if input is ready for a new value
        self.result = False  # Flag to check if the last operation was a result

    # Method to update the entry field
    def Entry(self, value):
        ent_field.delete(0, 'end')
        ent_field.insert(0, value)

    # Method to enter a number
    def Enter_Num(self, num):
        self.result = False
        firstnum = ent_field.get()
        secondnum = str(num)
        if self.inp_value:
            self.current = secondnum
            self.inp_value = False
        else:
            self.current = firstnum + secondnum
        self.Entry(self.current)

    # Method to handle standard operations like addition, subtraction, etc.
    def Standard_Ops(self, val):
        temp_str = ent_field.get()
        try:
            if val == '=':
                ans = str(eval(temp_str))  # Evaluate the expression
                self.result = True
                self.Entry(ans)
            else:
                self.Entry(temp_str + val)
            self.inp_value = False
        except ValueError:
            self.Entry('Error')
        except SyntaxError:
            self.Entry('Error')

    # Method to clear the entry field
    def Clear_Entry(self):
        self.result = False
        self.current = "0"
        self.Entry(0)
        self.inp_value = True

    # Method to calculate the square root
    def SQ_Root(self):
        try:
            self.current = math.sqrt(float(ent_field.get()))
            self.Entry(self.current)
        except ValueError:
            self.Entry('Error')
        except SyntaxError:
            self.Entry('Error')

    # Method to enter the value of pi
    def Pi(self):
        self.result = False
        self.current = math.pi
        self.Entry(self.current)

    # Method to enter the value of e (Euler's number)
    def E(self):
        self.result = False
        self.current = math.e
        self.Entry(self.current)

    # Method to convert radians to degrees
    def Deg(self):
        try:
            self.result = False
            self.current = math.degrees(float(ent_field.get()))
            self.Entry(self.current)
        except ValueError:
            self.Entry('Error')
        except SyntaxError:
            self.Entry('Error')

    # Method to convert degrees to radians
    def Rad(self):
        try:
            self.result = False
            self.current = math.radians(float(ent_field.get()))
            self.Entry(self.current)
        except ValueError:
            self.Entry('Error')
        except SyntaxError:
            self.Entry('Error')

    # Method to calculate the exponential (e^x)
    def Exp(self):
        try:
            self.result = False
            self.current = math.exp(float(ent_field.get()))
            self.Entry(self.current)
        except ValueError:
            self.Entry('Error')
        except SyntaxError:
            self.Entry('Error')

    # Method to calculate the factorial
    def Fact(self):
        try:
            self.result = False
            self.current = math.factorial(float(ent_field.get()))
            self.Entry(self.current)
        except ValueError:
            self.Entry('Error')
        except SyntaxError:
            self.Entry('Error')

    # Method to calculate the sine of an angle in degrees
    def Sin(self):
        try:
            self.result = False
            self.current = math.sin(math.radians(float(ent_field.get())))
            self.Entry(self.current)
        except ValueError:
            self.Entry('Error')
        except SyntaxError:
            self.Entry('Error')

    # Method to calculate the cosine of an angle in degrees
    def Cos(self):
        try:
            self.result = False
            self.current = math.cos(math.radians(float(ent_field.get())))
            self.Entry(self.current)
        except ValueError:
            self.Entry('Error')
        except SyntaxError:
            self.Entry('Error')

    # Method to calculate the tangent of an angle in degrees
    def Tan(self):
        try:
            self.result = False
            self.current = math.tan(math.radians(float(ent_field.get())))
            self.Entry(self.current)
        except ValueError:
            self.Entry('Error')
        except SyntaxError:
            self.Entry('Error')

    # Method to calculate the hyperbolic sine
    def Sinh(self):
        try:
            self.result = False
            self.current = math.sinh(math.radians(float(ent_field.get())))
            self.Entry(self.current)
        except ValueError:
            self.Entry('Error')
        except SyntaxError:
            self.Entry('Error')

    # Method to calculate the hyperbolic cosine
    def Cosh(self):
        try:
            self.result = False
            self.current = math.cosh(math.radians(float(ent_field.get())))
            self.Entry(self.current)
        except ValueError:
            self.Entry('Error')
        except SyntaxError:
            self.Entry('Error')

    # Method to calculate the hyperbolic tangent
    def Tanh(self):
        try:
            self.result = False
            self.current = math.tanh(math.radians(float(ent_field.get())))
            self.Entry(self.current)
        except ValueError:
            self.Entry('Error')
        except SyntaxError:
            self.Entry('Error')

    # Method to calculate the natural logarithm (base e)
    def Ln(self):
        try:
            self.result = False
            self.current = math.log(float(ent_field.get()))
            self.Entry(self.current)
        except ValueError:
            self.Entry('Error')
        except SyntaxError:
            self.Entry('Error')

    # Method to calculate the base-10 logarithm
    def Log_10(self):
        try:
            self.result = False
            self.current = math.log10(float(ent_field.get()))
            self.Entry(self.current)
        except ValueError:
            self.Entry('Error')
        except SyntaxError:
            self.Entry('Error')

    # Method to calculate the base-2 logarithm
    def Log_2(self):
        try:
            self.result = False
            self.current = math.log2(float(ent_field.get()))
            self.Entry(self.current)
        except ValueError:
            self.Entry('Error')
        except SyntaxError:
            self.Entry('Error')

    # Method to calculate the square of a number
    def Pow_2(self):
        try:
            self.result = False
            self.current = int(ent_field.get())**2
            self.Entry(self.current)
        except ValueError:
            self.Entry('Error')
        except SyntaxError:
            self.Entry('Error')

    # Method to calculate the cube of a number
    def Pow_3(self):
        try:
            self.result = False
            self.current = int(ent_field.get())**3
            self.Entry(self.current)
        except ValueError:
            self.Entry('Error')
        except SyntaxError:
            self.Entry('Error')

    # Method to calculate 10 raised to the power of a number
    def Pow_10_n(self):
        try:
            self.result = False
            self.current = 10**int(ent_field.get())
            self.Entry(self.current)
        except ValueError:
            self.Entry('Error')
        except SyntaxError:
            self.Entry('Error')

    # Method to calculate the reciprocal of a number
    def One_div_x(self):
        try:
            self.result = False
            self.current = 1/(int(ent_field.get()))
            self.Entry(self.current)
        except ValueError:
            self.Entry('Error')
        except SyntaxError:
            self.Entry('Error')

    # Method to calculate the absolute value
    def Abs(self):
        try:
            self.result = False
            self.current = abs(float(ent_field.get()))
            self.Entry(self.current)
        except ValueError:
            self.Entry('Error')
        except SyntaxError:
            self.Entry('Error')

# Create buttons for the number pad (1-9)
numberpad = "789456123"  # Define the layout of the number pad
i = 0  # Index for iterating through numberpad
button = []  # List to store button objects
for j in range(2, 5):  # Loop through rows 2 to 4
    for k in range(3):  # Loop through columns 0 to 2
        button.append(tk.Button(root, text=numberpad[i], font=FONT,
                                fg="#000000", width=6, height=2,
                                highlightbackground='#ADD8E6', highlightthickness=2))
        button[i].grid(row=j, column=k, sticky='n' +
                       's'+'e' + 'w', padx=3, pady=3)
        button[i]["command"] = lambda x=numberpad[i]: sc_app.Enter_Num(x)
        i += 1

# Create button for Clear Entry (CE)
btn_CE = tk.Button(root, text='CE', command=lambda: sc_app.Clear_Entry(),
                   font=FONT, height=2, fg="#000000",
                   highlightbackground='#ADD8E6', highlightthickness=2)
btn_CE.grid(row=1, column=0, columnspan=2,
            sticky='n'+'s'+'e'+'w', padx=3, pady=3)

# Create button for square root (√)
btn_sqr = tk.Button(root, text='\u221A', command=lambda: sc_app.SQ_Root(),
                    font=FONT, width=6, height=2, fg="#000000",
                    highlightbackground='#ADD8E6', highlightthickness=2)
btn_sqr.grid(row=1, column=2, sticky='n'+'s'+'e'+'w', padx=3, pady=3)

# Create button for number 0
btn_0 = tk.Button(root, text='0', command=lambda: sc_app.Enter_Num('0'),
                  font=FONT, width=6, height=2, fg="#000000",
                  highlightbackground='#ADD8E6', highlightthickness=2)
btn_0.grid(row=5, column=0, columnspan=2,
           sticky='n'+'s'+'e'+'w', padx=3, pady=3)

# Create button for decimal point (.)
btn_point = tk.Button(root, text='.', command=lambda: sc_app.Standard_Ops('.'),
                      font=FONT, width=6, height=2, fg="#000000",
                      highlightbackground='#ADD8E6', highlightthickness=2)
btn_point.grid(row=5, column=2, sticky='n'+'s'+'e'+'w', padx=3, pady=3)

# Create button for equal (=)
btn_equal = tk.Button(root, text='=', command=lambda: sc_app.Standard_Ops('='),
                      font=FONT, width=6, height=2, fg="#000000",
                      highlightbackground='#ADD8E6', highlightthickness=2)
btn_equal.grid(row=5, column=3, sticky='n'+'s'+'e'+'w', padx=3, pady=3)

# Create button for addition (+)
btn_add = tk.Button(root, text='+', command=lambda: sc_app.Standard_Ops('+'),
                    font=FONT, width=6, height=2, fg="#000000",
                    highlightbackground='#ADD8E6', highlightthickness=2)
btn_add.grid(row=1, column=3, sticky='n'+'s'+'e'+'w', padx=3, pady=3)

# Create button for subtraction (-)
btn_sub = tk.Button(root, text='-', command=lambda: sc_app.Standard_Ops('-'),
                    font=FONT, width=6, height=2, fg="#000000",
                    highlightbackground='#ADD8E6', highlightthickness=2)
btn_sub.grid(row=2, column=3, sticky='n'+'s'+'e'+'w', padx=3, pady=3)

# Create button for multiplication (*)
btn_mul = tk.Button(root, text='*', command=lambda: sc_app.Standard_Ops('*'),
                    font=FONT, width=6, height=2, fg="#000000",
                    highlightbackground='#ADD8E6', highlightthickness=2)
btn_mul.grid(row=3, column=3, sticky='n'+'s'+'e'+'w', padx=3, pady=3)

# Create button for division (/)
btn_div = tk.Button(root, text='/', command=lambda: sc_app.Standard_Ops('/'),
                    font=FONT, width=6, height=2, fg="#000000",
                    highlightbackground='#ADD8E6', highlightthickness=2)
btn_div.grid(row=4, column=3, sticky='n'+'s'+'e'+'w', padx=3, pady=3)

# Create button for pi (π)
btn_pi = tk.Button(root, text='\u03C0', command=lambda: sc_app.Pi(),
                   font=FONT, width=5, height=2, fg="#000000",
                   highlightbackground='#ADD8E6', highlightthickness=2)
btn_pi.grid(row=1, column=4, sticky='n'+'s'+'e'+'w', padx=3, pady=3)

# Create button for Euler's number (e)
btn_e = tk.Button(root, text='e', command=lambda: sc_app.E(),
                  font=FONT, width=5, height=2, fg="#000000",
                  highlightbackground='#ADD8E6', highlightthickness=2)
btn_e.grid(row=1, column=5, sticky='n'+'s'+'e'+'w', padx=3, pady=3)

# Create button for degrees (Deg)
btn_deg = tk.Button(root, text='Deg', command=lambda: sc_app.Deg(),
                    font=FONT, width=5, height=2, fg="#000000",
                    highlightbackground='#ADD8E6', highlightthickness=2)
btn_deg.grid(row=1, column=6, sticky='n'+'s'+'e'+'w', padx=3, pady=3)

# Create button for exponent (Exp)
btn_exp = tk.Button(root, text='Exp', command=lambda: sc_app.Exp(),
                    font=FONT, width=5, height=2, fg="#000000",
                    highlightbackground='#ADD8E6', highlightthickness=2)
btn_exp.grid(row=2, column=4, sticky='n'+'s'+'e'+'w', padx=3, pady=3)

# Create button for factorial (x!)
btn_fact = tk.Button(root, text='x!', command=lambda: sc_app.Fact(),
                     font=FONT, width=5, height=2, fg="#000000",
                     highlightbackground='#ADD8E6', highlightthickness=2)
btn_fact.grid(row=2, column=5, sticky='n'+'s'+'e'+'w', padx=3, pady=3)

# Create button for radians (Rad)
btn_rad = tk.Button(root, text='Rad', command=lambda: sc_app.Rad(),
                    font=FONT, width=5, height=2, fg="#000000",
                    highlightbackground='#ADD8E6', highlightthickness=2)
btn_rad.grid(row=2, column=6, sticky='n'+'s'+'e'+'w', padx=3, pady=3)

# Create button for sine (sin)
btn_sin = tk.Button(root, text='sin', command=lambda: sc_app.Sin(),
                    font=FONT, width=5, height=2, fg="#000000",
                    highlightbackground='#ADD8E6', highlightthickness=2)
btn_sin.grid(row=3, column=4, sticky='n'+'s'+'e'+'w', padx=3, pady=3)

# Create button for cosine (cos)
btn_cos = tk.Button(root, text='cos', command=lambda: sc_app.Cos(),
                    font=FONT, width=5, height=2, fg="#000000",
                    highlightbackground='#ADD8E6', highlightthickness=2)
btn_cos.grid(row=3, column=5, sticky='n'+'s'+'e'+'w', padx=3, pady=3)

# Create button for tangent (tan)
btn_tan = tk.Button(root, text='tan', command=lambda: sc_app.Tan(),
                    font=FONT, width=5, height=2, fg="#000000",
                    highlightbackground='#ADD8E6', highlightthickness=2)
btn_tan.grid(row=3, column=6, sticky='n'+'s'+'e'+'w', padx=3, pady=3)

# Create button for hyperbolic sine (sinh)
btn_sinh = tk.Button(root, text='sinh', command=lambda: sc_app.Sinh(),
                     font=FONT, width=5, height=2, fg="#000000",
                     highlightbackground='#ADD8E6', highlightthickness=2)
btn_sinh.grid(row=4, column=4, sticky='n'+'s'+'e'+'w', padx=3, pady=3)

# Create button for hyperbolic cosine (cosh)
btn_cosh = tk.Button(root, text='cosh', command=lambda: sc_app.Cosh(),
                     font=FONT, width=5, height=2, fg="#000000",
                     highlightbackground='#ADD8E6', highlightthickness=2)
btn_cosh.grid(row=4, column=5, sticky='n'+'s'+'e'+'w', padx=3, pady=3)

# Create button for hyperbolic tangent (tanh)
btn_tanh = tk.Button(root, text='tanh', command=lambda: sc_app.Tanh(),
                     font=FONT, width=5, height=2, fg="#000000",
                     highlightbackground='#ADD8E6', highlightthickness=2)
btn_tanh.grid(row=4, column=6, sticky='n'+'s'+'e'+'w', padx=3, pady=3)

# Create button for natural logarithm (ln)
btn_ln = tk.Button(root, text='ln', command=lambda: sc_app.Ln(),
                   font=FONT, width=5, height=2, fg="#000000",
                   highlightbackground='#ADD8E6', highlightthickness=2)
btn_ln.grid(row=5, column=4, sticky='n'+'s'+'e'+'w', padx=3, pady=3)

# Create button for base-2 logarithm (log2)
btn_log2 = tk.Button(root, text='log2', command=lambda: sc_app.Log_2(),
                     font=FONT, width=5, height=2, fg="#000000",
                     highlightbackground='#ADD8E6', highlightthickness=2)
btn_log2.grid(row=5, column=5, sticky='n'+'s'+'e'+'w', padx=3, pady=3)

# Create button for base-10 logarithm (log10)
btn_log10 = tk.Button(root, text='log10', command=lambda: sc_app.Log_10(),
                      font=FONT, width=5, height=2, fg="#000000",
                      highlightbackground='#ADD8E6', highlightthickness=2)
btn_log10.grid(row=5, column=6, sticky='n'+'s'+'e'+'w', padx=3, pady=3)

# Create button for x squared (x²)
btn_x_pow2 = tk.Button(root, text='x\u00B2', command=lambda: sc_app.Pow_2(),
                       font=FONT, width=5, height=2, fg="#000000",
                       highlightbackground='#ADD8E6', highlightthickness=2)
btn_x_pow2.grid(row=1, column=7, sticky='n'+'s'+'e'+'w', padx=3, pady=3)

# Create button for x cubed (x³)
btn_x_pow3 = tk.Button(root, text='x\u00B3', command=lambda: sc_app.Pow_3(),
                       font=FONT, width=5, height=2, fg="#000000",
                       highlightbackground='#ADD8E6', highlightthickness=2)
btn_x_pow3.grid(row=2, column=7, sticky='n'+'s'+'e'+'w', padx=3, pady=3)

# Create button for 10 raised to the power of x (10ⁿ)
btn_10_pow_n = tk.Button(root, text='10\u207F', command=lambda: sc_app.Pow_10_n(),
                         font=FONT, width=5, height=2, fg="#000000",
                         highlightbackground='#ADD8E6', highlightthickness=2)
btn_10_pow_n.grid(row=3, column=7, sticky='n'+'s'+'e'+'w', padx=3, pady=3)

# Create button for reciprocal (1/x)
btn_1div_by_x = tk.Button(root, text='1/x', command=lambda: sc_app.One_div_x(),
                          font=FONT, width=5, height=2, fg="#000000",
                          highlightbackground='#ADD8E6', highlightthickness=2)
btn_1div_by_x.grid(row=4, column=7, sticky='n'+'s'+'e'+'w', padx=3, pady=3)

# Create button for absolute value (Abs)
btn_abs = tk.Button(root, text='Abs', command=lambda: sc_app.Abs(),
                    font=FONT, width=5, height=2, fg="#000000",
                    highlightbackground='#ADD8E6', highlightthickness=2)
btn_abs.grid(row=5, column=7, sticky='n'+'s'+'e'+'w', padx=3, pady=3)

# Main loop to run the application
if __name__ == '__main__':
    sc_app = SC_Calculator()  # Create an instance of the SC_Calculator class
    root.mainloop()  # Run the main loop of the application
