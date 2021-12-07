"""
Functions for loading the text files as well as storing list of Book IDs
Functions include: 
        load_books()
        load_logfile()
"""

book_ids=['01','02','03','04','05','06','07','08','09','10','11',
          '12','13','14','15','16','17','18','19','20','21']

def load_books():
    """
    Upload the database onto the Library System
    Data for function is read from from database.txt
    
    """
    global listOfBooks
    listOfBooks =[]
    f=open("database.txt","r")
    for record in f:
        cleanrecord=record.strip()
        bookInfo=cleanrecord.split(":")
        listOfBooks.append(bookInfo)
    print("Books Library Sucessfuly Loaded")
    f.close()
    return listOfBooks

def load_logfile():
    """
    Upload the logfile onto the Library System
    Data for function is read from logile.txt

    """
    global listLogfile
    listLogfile =[]
    g=open("logfile.txt","r")
    for details in g:
        bookDetails=details.strip().split(":")
        listLogfile.append(bookDetails)
    print("Logfile Sucessfuly Loaded")
    g.close()
    return listLogfile


if __name__=="__main__":
    #Testing Loading Textfiles
    print("Testing Load Database and Load Logfile and list of Book IDs")
    database=load_books()
    print(database,"\n")
    logfile=load_logfile()
    print(logfile,"\n")
    print("Book IDs\n",book_ids)
