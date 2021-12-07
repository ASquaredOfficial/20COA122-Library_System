"""
Functions involving Searching and Printing Books
Functions include:
        search_book(listOfBooks,bookSearch)
        list_books(listOfBooks)
        print_logfile(listLogfile)

"""
from database import *
listOfBooks=[]
listLogfile=[]

def search_book(listOfBooks,bookSearch):
    """
    Checks if the name of the book is inside database
    Careful since this function is Case sensitive
    Data acquired from list 'listLogfile' assigned from database.py and date
    'bookSearch' from menu.py
    
    """
    print("%s | %13s | %60s | %22s | %s | %s"%("ID","ISBN", "Name of Book",
                                               "Author","Purchase Date",
                                               "Member ID"))
    print("-"*134)
    search = bookSearch.lower()
    for book_detail in listOfBooks:
        if search in book_detail[2].lower():
            print ("%s | %13s | %60s | %22s | %s    | %s"%(book_detail[0],
                                                           book_detail[1], 
                                                           book_detail[2],
                                                           book_detail[3],
                                                           book_detail[4],
                                                           book_detail[5]))
    print(bookSearch," has been Searched!!")


def list_books(listOfBooks):
    """
    Prints list of books from database
    Data acquired from list 'listOfBooks' assigned from database.py 
    
    """
    print("%s | %13s | %60s | %22s | %s | %s"%("ID","ISBN", "Name of Book",
                                               "Author","Purchase Date",
                                               "Member ID"))
    print("-"*134)
    for book_detail in listOfBooks:
        print ("%s | %13s | %60s | %22s | %s    | %s"%(book_detail[0],
                                                       book_detail[1],
                                                       book_detail[2],
                                                       book_detail[3],
                                                       book_detail[4],
                                                       book_detail[5]))
    print("⬆ All Books in the Library have been Printed ⬆")

    
def print_logfile(listLogfile):
    """
    Prints logfile from database
    Data acquired from list 'listLogfile' assigned from database.py
    
    """
    print("%s | %67s | %s | %s "%("ID","Name of Book", "Check Out Date",
                                  "Return Date"))
    print("-"*106)
    for book in listLogfile:
        print ("%s | %67s | %s     | %s    "%(book[0], book[1],
                                              book[2], book[3]))
    print("⬆ Logfile has been Printed ⬆")


if __name__=="__main__":
    #Testing Search Option and Printing Books and Logifle
    print("Testing Print Logfile, Print Book Library and Search Option")
    database=load_books()
    logfile=load_logfile()
    printList1=print_logfile(logfile)
    printList2=list_books(database)
    inputSearch= "1"
    search_book(database,inputSearch)



    
