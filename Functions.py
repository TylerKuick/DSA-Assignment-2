from Member import *
from Queue import *

def displayMem(db):
    if type(db) == tuple:
        for i in db[1]: 
            print(i)
    else:
        for key in db:
            member = db[key]
            print(f"""-----------------------------------
ID: {member.getId()}
Name: {member.getName()}
Email: {member.getEmail()}
Tier: {member.getTier().upper()}
Points: {member.getPoints()}
-----------------------------------
            """)  

def AddMem(db):
    tiers = ["A", "B", "C"]
    # Prompt users for ID
    # Validation: ID length is 4, ID start with "M", ID not in db 
    memID = input("Enter member's ID: ")
    while (len(memID) != 4) or (memID.startswith("M") == False) or (memID in db):   # Loop prompt if validation fails
        if memID in db:
            print("Member ID invalid: ID already exists in database!")  
        else:
            print("Please enter a valid ID with the format M000")
        memID = input("Enter member's ID: ")      

    memName = input("Enter member's name: ")
    memEmail = input("Enter member's email: ")
    
    # Prompt users for Tier, if tier is not a valid tier, prompt again
    memTier = input("Enter member's tier [A, B, C]: ").upper()
    while (memTier not in tiers): 
        print("Please enter a valid tier (A, B, or C)")
        memTier = input("Enter member's tier [A, B, C]: ").upper()
    memPoints = int(input("Enter member's points: "))

    # Add new member into the db 
    new_member = Member(memID, memName, memEmail, memTier, memPoints)
    db[new_member.getId()] = new_member

    return db
    
        
def requestPage(db, queue): # Display request page 
    while True:
        print("""
        Member's Request Page: 
        1. Enter Member's Request
        2. View Number of Request
        3. Service next in Queue
        0. Return to Main Menu
        """)
        option = int(input("Please Select One: "))
        if option == 1:
            addRequest(db, queue)
        elif option == 2:
            print(f"Number of Request: {queue.__len__()}")
        elif option == 3:
            serviceRequest(db, queue)
        elif option == 0:
            return False
        

def addRequest(db, queue):      # Add request into the queue
    inputID = input("Enter Member ID: ")
    while inputID not in db:    # Check if input member id is in the db / valid
        print("Invalid Member Id. Please try again")
        inputID = input("Enter Member ID: ")
    inputReq = input("Enter Member's Request: ")
    newReq = MemRequest(inputID, inputReq)      # Initialise MemRequest object with input id and request
    # Queue request 
    queue.enqueue(newReq)
    print("Member's request added successfully!")


def serviceRequest(db, queue):      # Dequeue first request in the queue
    cur_req = queue.dequeue()   # Get first MemRequest object in the queue 
    memID = cur_req.getMemID()  # Get member id of the request 
    req = cur_req.getRequest()  # Get request detail 
    member = db[memID]          # Get relevant member information from db to display
    print(f"""
        Display Member's Request: 
        -------------------------------
        Member ID: {memID}
        Name: {member.getName()}
        Email: {member.getEmail()}
        Tier: {member.getTier()}
        Points: {member.getPoints()}
        -------------------------------
        Request: {req}
        -------------------------------

        Remaining Request: {queue.__len__()}
    """)

def recurFunction(recordNum, db):
    if type(db) == dict: 
        tempDb = []
        for key in db:
            tempDb.append(db[key])
    else:
        tempDb = db
    if len(tempDb) == 0: 
        return 
    else:
        rowList = []
        while len(rowList) < recordNum and len(tempDb) != 0:
            rowList.append(tempDb.pop(0))
        memStr = ""
        nameStr = ""
        emailStr = ""
        tierStr = ""
        pointStr = ""
        for j in rowList:
            memStr += f"Member ID: {j.getId()}\t\t\t"
            nameStr += f"Name: {j.getName()}\t\t\t"
            emailStr += f"Email: {j.getEmail()}\t\t"
            tierStr += f"Tier: {j.getTier()}\t\t\t\t"
            pointStr += f"Points: {j.getPoints()}\t\t\t"
        print(f"\n{memStr}\n{nameStr}\n{emailStr}\n{tierStr}\n{pointStr}\n")
        recurFunction(recordNum, tempDb)
        