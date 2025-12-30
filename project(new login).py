from tkinter import *
from PIL import Image, ImageTk
import tkinter.messagebox as tsmg
from tkinter import filedialog, Toplevel

root = Tk()
root.title("Login Page")
root.geometry("800x700")
root.minsize(800, 700)
bg_all = "gray"
fg_all = "white"
root.configure(bg=bg_all)

bg_color="white"
fg_color="black"

file_path = None


def afterlogin():
    global  stetusbar, strbar, c1, c2, c3, c4, c5, c6, e1, e2, e3

    after = Toplevel(root)
    root.withdraw()
    after.geometry("800x700")
    after.title("food rating")
    after.configure(bg=bg_color)

    f1 = Frame(after, bg="yellow")
    f1.pack(fill=X)
    l1 = Label(f1, font="arial 20 bold", text="🍽 Welcome To My Foody Store", fg="green", bg="yellow")
    l1.pack()

    f2 = Frame(after, bg=bg_color)
    f2.pack(fill=X)

    l2 = Label(f2, text="What You Like To Order:", bg=bg_color, fg=fg_color, font="arial 15 bold")
    l2.pack(side=LEFT, pady=10)

    # Order 1.
    f3 = Frame(after, bg=bg_color)
    f3.pack(fill=X)

    Label(f3, text="1}  The Amazing Biryani:-", bg=bg_color, fg=fg_color, font="arial 13 bold").pack(side=LEFT,
                                                                                                     anchor="w")

    c1 = IntVar()
    adition1 = StringVar()
    cb1 = Checkbutton(f3, bg=bg_color, variable=c1, borderwidth=3)
    cb1.pack(anchor="w")

    f4 = Frame(after, bg=bg_color)
    f4.pack(fill=X)
    Label(f4, text="Some Tips From You:", bg=bg_color, font="arial 10 bold", fg="gray", anchor="w").pack(side=LEFT,
                                                                                                         padx=5)
    e1 = Entry(f4, textvariable=adition1, width=30, bg="gray", fg=bg_color)
    e1.pack(side=LEFT)

    # Order 2.

    f5 = Frame(after, bg=bg_color)
    f5.pack(fill=X)

    Label(f5, text="2}  Bihari Chicken Pulaw :-", bg=bg_color, fg=fg_color, font="arial 13 bold").pack(side=LEFT,
                                                                                                       anchor="w")

    c2 = IntVar()
    adition2 = StringVar()
    cb1 = Checkbutton(f5, bg=bg_color, variable=c2, borderwidth=3)
    cb1.pack(anchor="w")

    f6 = Frame(after, bg=bg_color)
    f6.pack(fill=X)
    Label(f6, text="Some Tips From You:", bg=bg_color, font="arial 10 bold", fg="gray", anchor="w").pack(side=LEFT,
                                                                                                         padx=5)
    e2 = Entry(f6, textvariable=adition2, width=30, bg="gray", fg=bg_color)
    e2.pack(side=LEFT)

    # order Drinks.

    f7 = Frame(after, bg=bg_color)
    f7.pack(fill=X)
    c3 = IntVar()
    c4 = IntVar()
    c5 = IntVar()
    c6 = IntVar()

    l7 = Label(f7, text="3}  Drink's", bg=bg_color, fg=fg_color, font="arial 13 bold")
    l7.pack(anchor="w")

    d1 = Checkbutton(f7, text="Watar ,", bg=bg_color, fg=fg_color, variable=c3)
    d1.pack(side=LEFT)

    d2 = Checkbutton(f7, text="Cola ,", bg=bg_color, fg=fg_color, variable=c4)
    d2.pack(side=LEFT)

    d3 = Checkbutton(f7, text="Pepsi ,", bg=bg_color, fg=fg_color, variable=c5)
    d3.pack(side=LEFT)

    d4 = Checkbutton(f7, text="Lassi ", bg=bg_color, fg=fg_color, variable=c6)
    d4.pack(side=LEFT)

    adition3 = StringVar()
    f8 = Frame(after, bg=bg_color)
    f8.pack(fill=X)
    Label(f8, text="If you Want To add Anything :-", bg=bg_color, fg=fg_color, font="arial 13 bold").pack(side=LEFT)
    e3 = Entry(f8, bg="gray", fg=bg_color, width=30, textvariable=adition3)
    e3.pack(side=LEFT)

    b1 = Label(after, text="Order", borderwidth=10, font="arial 20 bold", relief=SUNKEN, bg="green", fg=bg_color)
    b1.pack(padx=5, pady=5)
    b1.bind("<Button-1>", order)

    menu = Menu(after)
    file_menu = Menu(menu, tearoff=0)

    file_menu.add_command(label="save", command=none)
    file_menu.add_command(label="save as", command=none)
    file_menu.add_separator()
    file_menu.add_command(label="about", command=about)
    menu.add_cascade(label="File", menu=file_menu)
    root.config(menu=menu)

    help_menu = Menu(menu, tearoff=0)
    help_menu.add_command(label="Contect Us", command=contect)
    help_menu.add_command(label="feedback", command=feedback)
    help_menu.add_separator()
    help_menu.add_command(label="help", command=helpbar)
    menu.add_cascade(label="Help", menu=help_menu)
    root.configure(menu=menu)

    stetusbar = StringVar()
    stetusbar.set("ready")

    strbar = Label(after, textvariable=stetusbar, relief=FLAT, bg="red", fg="black", anchor="w")
    strbar.pack(fill=X, side=BOTTOM)


def none():
    pass


def feedback():
    msg = tsmg.askquestion("Feedback",
                           "This GUI is Only Made For Practice \n And Fun If You Like this Please Click On Yes Button")
    if msg == "yes":
        tsmg.showinfo("thanks", "Thanks For Give Your Best Feedback")
    else:
        tsmg.showinfo("Sorry", "Sorry For Your Inconvenience \n We will Reach You Soon")


def contect():
    tsmg.showinfo("contect Us", "Our Email:- nomail@nomail.com \n our phone no.:- 1234567890 \n \n timeing:-8am to 6pm")


def about():
    tsmg.showinfo("about", "THis Gui Made Only For Traning And Fun So Please Dont Take Serious")


def helpbar():
    tsmg.showinfo("Help", "Sorry For Your Inconvenience \n We will Reach You Soon")


def order(event):
    # Check if ALL values are zero/empty
    if (c1.get() == 0 and c2.get() == 0 and c3.get() == 0 and c4.get() == 0
        and c5.get() == 0 and c6.get() == 0
        and e1.get() == "" and e2.get() == "" and e3.get() == ""):

        tsmg.showwarning("order", "⚠️ You didn’t select any item!")
        print("No order placed")
        return

    else:
        tsmg.showinfo("order", "Thanks To Order From My Store")
        print(
            f"the amazing biryani:-{c1.get()}, some tips for biryani:-{e1.get()}, "
            f"bihari chiken pulaw:-{c2.get()}, some tips for chiken pulaw:-{e2.get()},\n "
            f"water: {c3.get()}, cola: {c4.get()}, pepsi: {c5.get()}, lassi: {c6.get()}, "
            f"if customer want something else:-{e3.get()}"
        )

        with open("/Users/apple/Desktop/aamir/coding/python/Testing And Learning/login.txt", "a") as f:
            f.write(
                f"the amazing biryani:-{c1.get()}, some tips for biryani:-{e1.get()}, "
                f"bihari chiken pulaw:-{c2.get()}, some tips for chiken pulaw:-{e2.get()}, \n"
                f"water: {c3.get()}, cola: {c4.get()}, pepsi: {c5.get()}, lassi: {c6.get()}, "
                f"if customer want something else:-{e3.get()}\n\n"
            )

        # Update status bar
        stetusbar.set("updating...")
        strbar.update()
        import time
        time.sleep(2)
        stetusbar.set("ready")





def save(event):
    print(f"login id: {var1.get()} , password:{var2.get()}")
    with open("login.txt", "a") as f:
        # FIX: removed wrong {","} in f-string
        f.write(f"\n Login ID: {var1.get()} , Password: {var2.get()}\n")

    if var1.get() == "user1212" and var2.get() == "pass1212":
        afterlogin()
    else:
        tsmg.showinfo("error", "invalid login id or password")


def savefile():
    global file_path
    if file_path:  # if we already saved before
        with open(file_path, "w") as f:
            f.write(f"Login ID: {var1.get()}\nPassword: {var2.get()}")
        tsmg.showinfo("Saved", f"File saved: {file_path}")
    else:
        saveas()  # if not saved yet, behave like Save As


def saveas():
    global file_path
    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if file_path:  # only if user selected a file
        with open(file_path, "w") as f:
            f.write(f"Login ID: {var1.get()}\nPassword: {var2.get()}")
        tsmg.showinfo("Saved", f"File saved as: {file_path}")


def support():
    tsmg.showinfo("Contect As", "Our Mail Id:- newlogin@nomail.com \n "
                                "\n Our Contect Number:- 1234567890")


def feedback():
    msg = tsmg.askquestion("How Was This GUI", "This GUI Is Grate")
    if msg == "yes":
        tsmg.showinfo("Thanks", "Thanks To Give As Good Feedback")
    else:
        tsmg.showinfo("Sorry", "We Will Improved Our GUI")


def popscale(scale, popup):
    var = scale.get()
    if var <= 3:
        tsmg.showinfo("Sorry", "We will try to improve 😊")
    else:
        tsmg.showinfo("Thanks", "Thanks for your great rating ❤️")
    popup.destroy()


def pop():
    popup = Toplevel(root)
    popup.geometry("300x300")
    popup.minsize(300, 300)
    popup.maxsize(300, 300)
    popup.title("rate Your Experiace")
    popup.configure(bg=bg_all)
    poplabel = Label(popup, text="plase rate your experience in 1 to 5",
                     fg=fg_all, relief="solid", font="arial 15 bold", bg="royalblue")
    poplabel.pack(fill="x")

    my_slide = Scale(popup, from_=1, to=5, orient=HORIZONTAL, tickinterval=1,
                     bg="purple", fg=fg_all, relief="raised", borderwidth=5)
    my_slide.pack(fill="x")

    poplabel2 = Label(popup, text="Submit", font="arial 20 bold", bg="green",
                      fg="black", borderwidth=6, relief="sunken")
    poplabel2.pack(padx=10, pady=10)
    poplabel2.bind("<Button-1>", lambda e: popscale(my_slide, popup))


menu_bar = Menu(root)
menu1 = Menu(menu_bar, tearoff=0)
menu2 = Menu(menu_bar, tearoff=0)

menu1.add_command(label="Save", command=savefile)
menu1.add_command(label="Save As", command=saveas)
menu1.add_separator()
menu1.add_command(label="Exit", command=quit)

menu2.add_command(label="Support", command=support)
menu2.add_command(label="feedback", command=feedback)
menu2.add_separator()
menu2.add_command(label="Eperiance", command=pop)
menu_bar.add_cascade(label="File", menu=menu1)
menu_bar.add_cascade(label="Help", menu=menu2)

root.config(menu=menu_bar)

# Load and resize JPG image using Pillow
try:
    image = Image.open("/Users/apple/Desktop/aamir/coding/python/Testing And Learning/1.jpg")
    resized = image.resize((350, 700))
    p1 = ImageTk.PhotoImage(resized)
    b1 = Label(root, image=p1)
    b1.pack(side="left")
except:
    b1 = Label(root, text="Image Not Found", bg="black", fg="white", width=40, height=40)
    b1.pack(side="left")

# Frame for login widget
frame1 = Frame(root, bg=bg_all)
frame1.pack(side="left", padx=30, pady=100)

# Login ID label
l1 = Label(frame1, text="Login ID:", font="arial 20 bold", bg=bg_all, fg=fg_all)
l1.pack(anchor="w", pady=10)

# Entry box (optional but needed for input)
var1 = StringVar()
var2 = StringVar()
entry1 = Entry(frame1, font="arial 16", width=25, textvariable=var1)
entry1.pack(anchor="w", pady=5)

l2 = Label(frame1, text="Password:", font="arial 20 bold", bg=bg_all, fg=fg_all)
l2.pack(anchor="w", pady=10)

# FIX: hide password with show="*"
entry2 = Entry(frame1, font="arial 16", width=25, textvariable=var2, show="*")
entry2.pack(anchor="w", pady=5)

def show_password():
    if entry2.cget("show") == "":
        entry2.config(show="*")   # hide password
    else:
        entry2.config(show="")    # show password

show_pass = Checkbutton(frame1, text="Show Password", bg=bg_all, fg=fg_all,
                        command=show_password)
show_pass.pack(anchor="w")


button_label = Label(frame1, text="Login", bg="purple", fg=fg_all, borderwidth=6, relief="raised")
button_label.pack(anchor="w", pady=10)
button_label.bind("<Button-1>", save)

root.mainloop()
