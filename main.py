
from pymongo import MongoClient
from dotenv import load_dotenv
from os import getenv

load_dotenv()


uri = getenv("MONGO_URI")

# Create a new client and connect to the server
client = MongoClient(uri)

# db = client.list_database_names()

# print(db)

db = client[getenv("DB_NAME")]
# print(db.list_collection_names())
coll = db[getenv("DB_COLLECTION")]



def getData():
    allData = []
    try:
        for data in coll.find():
            allData.append([data['_id'],data['title'],data['status'],data['due_date']])
            # print(data)
    except:
        print('')

    return allData

    
def printData(dataSet):
    for index,data in enumerate(dataSet):
        # print(f"{index}. {data['title']} | Status {data['status']} | Time{data}") 
        print(f"[{index+1}] {data[1]:<30} | Status: {data[2]:<10} | \033[92mTime: {data[3]}\033[0m")


def addData():
    title = ''
    date = ''

    while True:
        title = input("Enter todo title: ")
        if title == '':
            print("Invalid Input!!")
            continue
        elif title == 'q':
            quitProgram()
        else:
            break

    while True:
        date = input("Enter due date : ")

        if title == '' or date == '':
            print("Invalid Input!!")
            continue
        elif title == 'q' or date == 'q':
            quitProgram()
        else:
            coll.insert_one({
                'title':title,
                'due_date': date,
                'status':"Pending"
            })
            break

def deleteTodo(collection,todoData):
    # delete todo
    while True:
        usrInpt = input("\033[93mEnter Sl No.: \033[0m")
        if usrInpt == 'q':
            quitProgram()
        elif usrInpt.isnumeric():
            humanizeToProgramizeIndex = int( usrInpt) -1
            idOfDeletingTodo = todoData[humanizeToProgramizeIndex][0]
            # print(idOfDeletingTodo)
            collection.delete_one({'_id':idOfDeletingTodo})
            break
        else:
            print("Invalid Input!! ")
            


def quitProgram():
    print("\033[91mQuiting...\033[0m")
    exit() 

def statusTodo(todoData):
    idOfTodo = ''
    while True:
        usrInpt = input("\033[93mEnter Todo Sl No: \033[0m")
        if usrInpt.lower() == 'q':
            quitProgram()
        elif usrInpt.isnumeric() and int(usrInpt) <= len(todoData):
            idOfTodo = todoData[int(usrInpt)-1][0]
            break
        elif usrInpt == '':
            print('Invalid Input!!')
            continue
        else:
            print('Invalid Input!!')
            pass

    while True:
        userInpStatus = input("('c' for Comkpleted), ('p' for Progress), ('b' for Blocked): ")
        currentStatus = ''
        if userInpStatus.lower() == 'q':
            # currentStatus = "\033[0mPending\033[0m"
            quitProgram()
        elif userInpStatus.lower() == 'c':
            currentStatus = "\033[92mCompleted\033[0m"
        elif userInpStatus.lower() == 'p':
            currentStatus = "\033[93mIn Progress\033[0m"
        elif userInpStatus.lower() == 'b':
            currentStatus = "\033[91mBlocked\033[0m"
        elif userInpStatus == '':
            print('Invalid Input!!')
            continue
        else:
            print('Invalid Input!!')
            continue
        # i am here8
        if currentStatus != '':
            coll.update_one({"_id":idOfTodo},{"$set":{"status":currentStatus}})
            break


def editTodo (coll,todoData):
    while True:
        usrInpt = input("Enter todo sl no: ")
        if usrInpt == '':
            print("Invalid Input!!")
            continue
        elif usrInpt.lower() == 'q':
            quitProgram()
        elif usrInpt.isnumeric() and int(usrInpt) <= len(todoData) :
            # pass
            todo = todoData[int(usrInpt) - 1]
            screenShortTodo = todo.copy()

            # for i,data in enumerate(todo):
            print("Selected!!")
            print(f"[{usrInpt}]. {todo[1]} | Status: {todo[2]} | Time: {todo[3]}")
            while True:
                usrInptForEditChoice = input("('t' for Edit Title) ('l' for Edit Deadline) ('d' for Done): ")
                if usrInptForEditChoice.lower() == 'q':
                    quitProgram()
                elif usrInptForEditChoice == '':
                    print("Invalid Input!!")
                    continue
                elif usrInptForEditChoice.lower() == 't':
                    todo[1] = input("Enter New Title: ")
                elif usrInptForEditChoice.lower() == 'l':
                    todo[3] = input("Enter New time: ")
                elif usrInptForEditChoice.lower() ==  'd':
                    if screenShortTodo == todo:
                        print("Saving Done Sucessfully !! (No Changes)")
                        break
                    elif screenShortTodo != todo:
                        coll.update_one({'_id':todo[0]},{'$set':{'title':todo[1], 'due_date':todo[3]}})
                        print("Saving Done Sucessfully !!")
                        break
                    else:
                        print("Didn't save, Try again...")
                else:
                    print("Invalid Input!!")
            
            break
        else:
            print("Invalid Input!!")

def main():

    todoData = getData()
    
    printData(todoData)

    print("\033[92m", end="")
    option = input(
        "Enter ('q' for Quit). ('a' for Add new Todo). ('d' for delete a todo). ('e' for edit a todo), ('s' for set status) ('c' for clear todo): \033[94m"
    )
    print("\033[0m", end="")

    if option.lower() == 'q':
        # quit program
        quitProgram()

    elif option.lower() == 'a':
        # add todo
        addData()

    elif option.lower() == 'd':
        # delete todo
        deleteTodo(collection=coll,todoData=todoData)

    elif option.lower() == 'e':
        # edit todo
        editTodo(coll=coll, todoData=todoData)

    elif option.lower() == 's':
        # set status
        statusTodo(todoData=todoData)

    elif option.lower() == 'c':
        # clear todo
        try:
            for currentStatusDelete in ['\033[92mCompleted\033[0m','\033[91mBlocked\033[0m']:
                print("Deleting...",end='')
                print(coll.delete_many({'status':currentStatusDelete}).deleted_count)
        except:
            print("Something Wrong. Try again leter...")

    else:
        print("Invalid Input!!")



while True:
    main()

