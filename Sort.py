# Bubble Sort
def bubbleSort(db):
    bubble_list = []    # Empty List for sorting 
    for key in db:
        bubble_list.append(db[key])     # Add all member objects into the bubble sorting list 
    n = len(db)
    for i in range(n-1, 0, -1):
        for j in range(i):
            if bubble_list[j+1].getPoints() > bubble_list[j].getPoints():   # When second member has more points than first member
                # Three point switching
                tmp = bubble_list[j+1]  # Second member is put into a temporary holder
                bubble_list[j+1] = bubble_list[j]   # First member is assigned to Second Member's position
                bubble_list[j] = tmp    # Second member is assigned to First Member's position
        # Print Pass Items
        print(f"""
Pass: {n-i}
---------------------------------""")
        for k in bubble_list:   
            print(f"ID: {k.getId()}, Points: {k.getPoints()}")

    # Reset the db into a empty dictionary
    db = {}     
    for i in bubble_list:   
        db[i.getId()] = i   # Set ID as Key and Member object as Value

    return db   # Sorted db
                        

# Selection Sort
def selectionSort(db):
    selection_list = []     # Empty List for sorting 
    for key in db:
        selection_list.append(db[key])      # Add all member objects into the selection sorting list 
    n = len(db) 
    for i in range(n-1):
        smallNdx = i    # Assign the current pass as the smallest index 
        for j in range(i+1, n):
            if selection_list[j].getTier() < selection_list[smallNdx].getTier():
                smallNdx = j
        if smallNdx != i:
            tmp = selection_list[i]
            selection_list[i] = selection_list[smallNdx]
            selection_list[smallNdx] = tmp
        # Print Pass Items
        print(f"""
Pass: {i+1}
---------------------------------""")
        for k in selection_list:
            print(f"ID: {k.getId()}, Tier: {k.getTier()}")
                
    db = {}     # Reset the db into a empty dictionary
    for i in selection_list:
        db[i.getId()] = i      # Set ID as Key and Member object as Value

    return db   # Sorted db

# Insertion Sort 
def insertionSort(db):
    insertionList = []
    n = len(db)
    for key in db:
        insertionList.append(db[key])
    for i in range(1, n):
        target = insertionList[i]   # Set the target employee object to move 
        value = insertionList[i].getId()    # Comparison item: Member ID
        pos = i
        while pos > 0 and value < insertionList[pos-1].getId():  # Compare against every 
            insertionList[pos] = insertionList[pos-1]   # Employee object changes places if condition is met 
            pos -= 1    # position number is reduced by one 
        insertionList[pos] = target   # Update the list if changes were made, if not target stays at the same position   

        print(f"""
Pass: {i}
---------------------------------""")
        for k in insertionList:
            print(f"ID: {k.getId()}")

    db = {}     # Reset the db into a empty dictionary
    for i in insertionList:
        db[i.getId()] = i    # Set ID as Key and Member object as Value

    return db   # Sorted db


def mergeSort(db):   # Intake list of Member Objects
    if type(db) == dict: 
        mergeList = []
        for key in db:
            mergeList.append(db[key])
    else:
        mergeList = db
    if len(mergeList) <= 1:
        return mergeList
    else:
        mid = len(mergeList) // 2                           # Find midpoint to split list
        leftHalf = mergeSort(mergeList[:mid])               # Recursively call mergeSort for
        rightHalf = mergeSort(mergeList[mid:])              # each half list that was split
        newList = mergeSortedLists(leftHalf, rightHalf)     # join both lists after being sorted 

        # Further sorting based on points 
        for i in range(1, len(newList)):
            if newList[i].getTier() == newList[i-1].getTier():  # If the tiers are the same
                if newList[i].getPoints() < newList[i-1].getPoints():   # compare member points, switch places 
                    temp = newList[i-1]                                   # between member with lesser points and 
                    newList[i-1] = newList[i]                           # member with more points
                    newList[i] = temp                                 # Uses three point switching

        # Displaying Passes / New Lists
        print("""
New List:
------------------------""")
        for mem in newList:
            print(f"ID: {mem.getId()}, Tier: {mem.getTier()}")
        print("------------------------")

    return newList

def mergeSortedLists(left, right):
    i = 0
    j = 0
    newList = []
    while i < len(left) and j < len(right):
        if left[i].getTier() < right[j].getTier():
           newList.append(left[i])
           i += 1
        elif left[i].getTier() == right[j].getTier() and left[i].getPoints() < right[i].getPoints():
            newList.append(left[i])
            i += 1 
        else:
           newList.append(right[j])
           j += 1 

    while i < len(left):
        newList.append(left[i])
        i += 1

    while j < len(right):
        newList.append(right[j])
        j += 1

    return newList
