"""
Functions involving Checking Out a Book
Functions include:
        check_out_between(listOfBooks,listLogfile,date_today,book_ids,b_id,m_id)
        check_out(b_id,m_id,listOfBooks,listLogfile,date_today)

"""
from database import *
from datetime import datetime

def check_out_between(listOfBooks,listLogfile,date_today,book_ids,b_id,m_id):
    """
    Checks if input for Book ID and Memebr ID is valid
    Data acquired from lists 'listLogfile', 'listOfBooks' and 'book_ids'
    assigned from database.py, with Book ID 'b_id' and Member ID 'm_id'
    inputs from menu.py

    """
    if (len(m_id)!=4 or not m_id.isnumeric()) and b_id not in book_ids:
        result1 = "Invalid Book ID and Member ID, please try again"
        print(result1)
        return result1
    elif len(m_id)!=4 or not m_id.isnumeric():
        result2 = "Invalid Member ID, please try again"
        print(result2)
        return result2
    elif b_id in book_ids:
        r2 = check_out(b_id,m_id,listOfBooks,listLogfile,date_today)
        return r2
    elif not b_id in book_ids:
        result3 = "This book does not exist. Please Try again"
        print(result3)
        return result3

def check_out(b_id,m_id,listOfBooks,listLogfile,date_today):
    """
    Check out book from user input of Book ID and Member ID
    Using call from check_out_between()
    Data acquired from lists 'listLogfile', 'listOfBooks' and 'book_ids'
    assigned from database.py, with Book ID 'b_id' and Member ID 'm_id' inputs
    from menu.py
    
    """
    for book_detail in listOfBooks:
        if book_detail[0] == b_id:
            if not book_detail[5] == '0000':
                result4 = "Book is already being borrowed"
                print(result4)
                return result4
            else:
                book_detail[5]= m_id
                r1 = update_check_out(b_id,m_id,listLogfile,date_today)
                return r1

def update_check_out(b_id,m_id,listLogfile,date_today):
    """
    Updates the Check out date and Return date of Logfile for the book borrowed
    Using call from check_out()
    Data acquired from lists 'listLogfile' and 'listOfBooks' assigned from
    database.py, with book id 'b_id' and 'm_id' inputs from menu.py
    
    """
    for detail in listLogfile:
        if detail[0] == b_id:
            detail[2] = date_today
            detail[3] = "11/01/2021"
            result5a = "Successfully Checked Out '"+detail[1]
            result5 = result5a +"' and Updated Logfile"
            print(result5)
            return result5

if __name__=="__main__":
    #Testing Book Checkout Option
    print("Testing Book Checkout Option")
    input_book="01"
    input_member="1234"
    input_date="16/12/2020"
    logfile=load_logfile()
    database=load_books()
    check_out_between(database,logfile,input_date,book_ids,input_book,
                      input_member)
