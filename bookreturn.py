"""
Functions involving returning a book
Functions include:
        return_book(book_ids,listOfBooks,listLogfile,date_today,book_id)
        return_book_logfile(book_id,listLogfile,date_today)
                
"""
from database import *
from datetime import datetime

def return_book(book_ids,listOfBooks,listLogfile,date_today,book_id):                                                                                  
    """
    Returns a book if the input is valid and the book is not already available
    Data acquired from lists 'listLogfile', 'listOfBooks' and 'book_ids' assigned from
    database.py, with date 'date_today' and 'book_id' inputs from menu.py
    
    """
    if book_id not in book_ids:
        string1 = "Invalid ID has been input"
        print(string1)
        return string1
    else:
        for line in listOfBooks:
            if book_id == line[0] and line[5] == '0000' :                                           
                string2 = "Book is already available"
                print(string2)
                return string2
            elif book_id == line[0] and line[5] != '0000':
                line[5] = '0000'
                string4 = return_book_logfile(book_id,listLogfile,date_today)
                return string4
                
def return_book_logfile(book_id,listLogfile,date_today):        
    """
    Updates Logfile after Book has been retuned
    Using a call from return_book()
    Data acquired from list 'listLogfile' assigned from database.py, with date
    'date_today' and 'book_id' inputs from menu.py
    
    """
    for line in listLogfile:
        if book_id == line[0]:
            line[3] = date_today
            string3 = "'"+line[1]+"' has been returned!!!"
            print(string3)
            return string3

if __name__=="__main__":
    #Testing Return Book Option
    print("Testing Book Return Option")
    input_book="04"
    input_date="16/12/2020"
    logfile=load_logfile()
    database=load_books()
    function_return=return_book(book_ids,database,logfile,input_date,
                                input_book)


