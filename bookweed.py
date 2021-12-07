"""
Function that involves Weeding Book
Functions include:
        weed_book(listLogfile,date_today)

"""

from database import *
from datetime import datetime

def weed_book(listLogfile,date_today):          #via book circulation method
    """
    Uses date input to see if a book has not been borrowed in over 1000 days
    - Saves whether to remove or keep book into a list
    - Saves list of no. days since last borrow into a list 
    Both to be used in visual reprsentaion
    Data acquired from list 'listLogfile' assigned from database.py and date
    'date_today' from menu.py
    
    """
    d1 = datetime.strptime(date_today, "%d/%m/%Y")
    print("%s | %67s | %s | %s   | %s"%("ID", "Name of Book", "Check Out Date",
                                        "Return Date", "Weed Option"))
    print("-"*125)
    listDates = []
    toremove = []
    for book in listLogfile:
        RemoveTxt = "Remove"
        nRemoveTxt = "Do not Remove"
        last_checkout = book[3]
        d2 = datetime.strptime(last_checkout, "%d/%m/%Y")
        date_diff = abs((d2 - d1).days)
        listDates.append(date_diff)
        if date_diff >= 1000:
            print ("%s | %67s | %s     | %s    | Remove"%(book[0], book[1],
                                                          book[2], book[3],))
            toremove.append(RemoveTxt)
        else:
            print ("%s | %67s | %s     | %s    | Do Not Remove"%(book[0],
                                                                 book[1],
                                                                 book[2],
                                                                 book[3],))
            toremove.append(nRemoveTxt)
    print("⬆ Here is a list of all the books that need to be removed ⬆")
    return listDates, toremove

if __name__=="__main__":
    #Testing Weed Book Function
    print("Testing Weed Book Option")
    input_date="16/12/2020"
    logfile=load_logfile()
    weed_function1,weed_function2=weed_book(logfile,input_date)
    print(weed_function1)
    print(weed_function2)
    

