from Member import * 
from Sort import *
from Functions import *
from Queue import * 

# Data Structure to store member details 
# Dict: {ID (PK): Member Object, ID: Member Object, ...}
db = {}
emp_queue = Queue()

# Test data
def populateData():
    memList = []
    newMemA = Member("M002", "steve", "steve@mail.com", "C", 2000)
    memList.append(newMemA)
    newMemA = Member("M007", "strange", "strange@mail.com", "A", 6000)
    memList.append(newMemA)
    newMemA = Member("M001", "peter", "peter@mail.com", "C", 1000)
    memList.append(newMemA)
    newMemA = Member("M005", "tony", "tony@mail.com", "A", 6500)
    memList.append(newMemA)
    newMemA = Member("M004", "banner", "banner@mail.com", "B", 3500)
    memList.append(newMemA)
    newMemA = Member("M006", "clark", "clark@mail.com", "B", 5000)
    memList.append(newMemA)
    newMemA = Member("M003", "bruce", "bruce@mail.com", "B", 3000)
    memList.append(newMemA)
    print("Data populated!\n")
    return memList

# Program 
recordNum = 1
loop = True
while loop:
    print("""
    Loyalty/Membership System 
    
    Main Page:
    -----------------------------------
    (1). Add a new member
    (2). Display all members' records 
    (3). Sort Members by points (DESC)
    (4). Sort Members by Tier (ASC)
    (5). Sort Members by Member ID (ASC)
    (6). Sort Members by Tier, followed by Points (ASC)
    (7). Enter Member's Request
    (8). Set Number of Records per row to display    
    (9). Populate Data (Reset Database)
    (0). Quit
    -----------------------------------
    """)
    option = int(input("Choose an option [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]: "))
    if option == 1:      # Add new member 
        db = AddMem(db)  

    elif option == 2:   
        recurFunction(recordNum, db)

    elif option == 3:    # Bubble Sort (Desc)
        db = bubbleSort(db)    # Original DB is reassigned to the sorted db that is returned by bubbleSort() func      
        # Display Sorted Member Info
        recurFunction(recordNum, db)

    elif option == 4:    # Selection Sort (Asc)
        db = selectionSort(db)  # Original DB is reassigned to the sorted db that is returned by bubbleSort() func      
        # Display Sorted Member Info
        recurFunction(recordNum, db)

    elif option == 5:   # Insertion Sort (ASC)
        db = insertionSort(db)  # Original DB is reassigned to the sorted db that is returned by insertionSort() func
        # Display Sorted Member Info
        recurFunction(recordNum, db)

    elif option == 6:   # Merge Sort by Tier, followed by points 
        sortResult = mergeSort(db)   
        # Re-Initialise db so that display is Merge Sorted 
        db = {}
        for i in sortResult:
            db[i.getId()] = i

        # Display Sorted Member Info
        print("\nMerge Sorted")
        recurFunction(recordNum, sortResult)   
               
        
    elif option == 7:    # Member Request Page 
        requestPage(db, emp_queue)

    elif option == 8:   # Set number of records per row to display
        recordNum = int(input("Please enter the number of records to display per row: "))
        recurFunction(recordNum, db)

    elif option == 9:   # Set Test Data / Reset DB 
        db = {}
        member_list = populateData()
        for i in member_list:   # Adds every member into database with ID as key and Member object as value 
            db[i.getId()] = i 
    else:
        loop = False
