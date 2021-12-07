#-----------------------------LIRARY SYTSTEM-----------------------------------#
""""
Make GUI interface to work along side the Python shell that will show the list
of titles for each book

"""
print("*----------------Welcome to The Library System----------------*")
print("Hint: Reminder to load Books onto system before use!!!")

from tkinter import *
from booksearch import *
from bookcheckout import *
from bookreturn import *
from bookweed import *
from database import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib.pyplot as plt


listOfBooks=[]
listLogfile=[]
listDates=[]
toremove=[]

#Load Data and Exit Functions
def exit_system():
    """
    Exit TKinter Window
    
    """
    textbox_lbl9 = "Goodbye!!!"
    text1.configure(text=textbox_lbl9)
    print("Thank you, Have a nice day!!")
    window.destroy()
    
def load_system():
    """
    Load books from database into the system

    """
    global listOfBooks
    global listLogfile
    listOfBooks=load_books()
    listLogfile=load_logfile()
    textbox_lbl2 = "Books"+" Loaded!!!"
    text1.configure(text=textbox_lbl2)
    textbox_lbl10 = "⬆SELECT"+" OPTION⬆"
    text.configure(text=textbox_lbl10)

#Confirm Username and Date Functions
def login_username():
    """
    Uses Entry box to print a welcome message in the window

    """
    msg_username=str(username1.get())
    msg_label['text'] = "Welcome",msg_username

def confirm_date():
    """
    Uses Entry box to print a date that was confirmed

    """
    msg_date=str(date1.get())
    msg_label2['text'] = "Date","is",msg_date

#Print Data Options    
def printing_books():
    """
    Calls the list_books() function to print books in backend and print books in
    window
    
    """
    list_books(listOfBooks)
    i=0
    textbox1.delete(0,END)
    for book_detail in listOfBooks:
        textbox1.insert(i,book_detail[0]+" : "+book_detail[5])
        i+=1
    textbox_lbl3 = "Books"+" Printed!!!"
    text1.configure(text=textbox_lbl3)

def printing_logfile():
    """
    Calls the print_logfile() function to print logfile in backend and print 
    logfile in window
    
    """
    print_logfile(listLogfile)
    i=0
    textbox1.delete(0,END)
    for book_detail in listLogfile:
        textbox1.insert(i,book_detail[0]+" : "+book_detail[2]+" : "+book_detail[3])
        i+=1
    textbox_lbl4 = "Logfile"+" Printed!!!"
    text1.configure(text=textbox_lbl4)

#Search Book Functions
def b_search():
    """
    Calls the search_book() function to search book in database and print result
    in backend and window
    
    """
    bookSearch = s_book.get()
    search_book(listOfBooks,bookSearch)
    s_textbox(bookSearch,listOfBooks)

def s_textbox(bookSearch,listOfBooks):
    """
    Uses call from b_search() to print the books found in the listbox
    
    
    """
    textbox_lbl1 = "⬇Books"+" Found⬇"
    text.configure(text=textbox_lbl1)
    textbox_lbl6 = "Library System!!"
    text1.configure(text=textbox_lbl6)
    i=0
    textbox1.delete(0,END)
    search = bookSearch.lower()
    for book_detail in listOfBooks:
        if search in book_detail[2].lower():
            textbox1.insert(i,book_detail[0]+":"+book_detail[5])
            i+=1
    SearchResult = "Searched database for '"+bookSearch+"'. Check Backend for list of matched Titles"
    printResult['text'] = str(SearchResult)
    
#Check Out Function
def checking_out():
    """
    Calls check_out_between() function to check out book 

    """
    date_today = date1.get()
    b_id = c_book.get()
    m_id = c_book2.get()
    CheckOutResult = check_out_between(listOfBooks,listLogfile,date_today,book_ids,b_id,m_id)
    printResult['text'] = str(CheckOutResult)
    textbox_lbl6 = "Library System!!"
    text1.configure(text=textbox_lbl6)

#Return Book Function
def book_return():
    """
    Calls return_book function to return

    """
    date_today = date1.get()
    book_id = r_book.get()
    BookReturnResult = return_book(book_ids,listOfBooks,listLogfile,date_today,book_id)
    printResult['text'] = str(BookReturnResult)
    textbox_lbl7 = "Library System!!"
    text1.configure(text=textbox_lbl7)

#Weed Books Functions
def book_weed():
    """
    Calls weed_book() function and creates graph for visual representation

    """
    global listDates
    global toremove
    date_today = date1.get()
    listDates,toremove=weed_book(listLogfile,date_today)
    w_textbox(toremove, book_ids)
    #tkinter canvas
    x=book_ids
    y=[1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,
       1000,1000,1000,1000,1000,1000,1000,1000]
    plt.plot(x,y,'r--',label='Weed Threshold')
    plt.legend(loc='upper right')
    plt.title("Books to Weed")
    plt.xlabel("Book IDs")
    plt.ylabel("No. of Days not Borrowed")
    ax1=fig.add_subplot(1,1,1)
    ax1.bar(book_ids,listDates)
    canvas.draw()
    plt.savefig('l.png')

def w_textbox(toremove, book_ids):
    """
    Uses call from book_weed() function to print the Book ID and whether or
    not to remove the book in the backend and window
    
    """
    textbox_lbl2 = "⬇Book"+" Reccomendations⬇"
    text.configure(text=textbox_lbl2)
    textbox1.delete(0,END)
    for i in range(0,21):
        textbox1.insert(i,book_ids[i]+" : "+str(toremove[i]))
    WeedResult = "Check Backend for Titles of books to remove"
    printResult['text'] = str(WeedResult)




################################################################################
#______________________________________________________________________________#
#---------------------------------WINDOW STUFF---------------------------------#
################################################################################

window = Tk()
window.title("*------------------Welcome to The Library System---------------*")
window.geometry("1110x680")
text1 = Label(window, text="Library System!!")
text1.grid(column=3,row=2)

#Load Data and Exit Options
btnLoad=Button(window,text="Load Books",width=22, command=load_system)
btnExit=Button(window,text="Exit",width=22,command=exit_system)
btnLoad.grid(column=0,row=2)
btnExit.grid(column=0,row=8)

#Listbox Visuals
text = Label(window, text="⬆Load Books⬆")
text.grid(column=0,row=9)
textline = Label(window, text="--------------------------------")
textline.grid(column=0,row=10)
textbox1=Listbox(window)
textbox1.grid(column=0,row=12,ipadx=20,ipady=120)

#Print Data Options
btnPrintBooks1=Button(window,text="Print Books",
                      command=printing_books)
btnPrintBooks2=Button(window,text="Print Logfile",width=12,
                      command=printing_logfile)
btnPrintBooks1.grid(column=1,row=2)
btnPrintBooks2.grid(column=2,row=2)

#Username Confirmation
l_username=Label(window,text="Enter your username:")
l_username.grid(column=0,row=0)
username1 = Entry(window, width=11)
username1.grid(column=1,row=0)
btnLogin=Button(window,text="Login",width=12,
                command=login_username)
btnLogin.grid(column=2,row=0)
msg_label = Label(window, text="")
msg_label.grid(column=3,row=0)

#Date Confirmation
lbl_a=Label(window,text="Enter Date:")
lbl_a.grid(column=0,row=1)
date1 = Entry(window, width=11)
date1.grid(column=1,row=1)
btnLogin=Button(window,text="Confirm Date",width=12,
                command=confirm_date)
btnLogin.grid(column=2,row=1)
msg_label2 = Label(window, text="")
msg_label2.grid(column=3,row=1)

#Search Book Option
btnSearchBooks=Button(window,text="Search Book",width=22,
                      command=b_search)
btnSearchBooks.grid(column=0,row=3)
EnterBookLbl = Label(window, text="Enter Book")
EnterBookLbl.grid(column=1,row=3)
s_book = Entry(window, width=15)
s_book.grid(column=2,row=3)

#Check Out Option
btnCheckOut=Button(window,text="Check Out",width=22,
                   command=checking_out)
btnCheckOut.grid(column=0,row=4)
EnterBookID = Label(window, text="Book ID")
EnterBookID.grid(column=1,row=4)
MemberID = Label(window, text="Member ID")
MemberID.grid(column=1,row=5)
c_book = Entry(window, width=15)
c_book.grid(column=2,row=4)
c_book2 = Entry(window, width=15)
c_book2.grid(column=2,row=5)
printResult = Label(window, text="")
printResult.grid(column=11,row=0)

#Return Book Option
btnReturnBook=Button(window,text="Return Book",width=22,
                    command=book_return)
btnReturnBook.grid(column=0,row=6)
ReturnBookID = Label(window, text="Book ID")
ReturnBookID.grid(column=1,row=6)
r_book = Entry(window, width=15)
r_book.grid(column=2,row=6)

#Weed Books Option
btnWeedBooks=Button(window,text="Weed Library Books",width=22,
                    command=book_weed)
btnWeedBooks.grid(column=0,row=7)
fig=plt.figure(figsize=(7,4))
canvas = FigureCanvasTkAgg(fig, master=window)
canvas.get_tk_widget().grid(column=11, row=12)
fig.patch.set_facecolor('#f0f0f0')


window.mainloop()
