class Task:
    def __init__(self,id,task,status) -> None:
        self.id =id 
        self.task = task
        self.status = status
        

class ToDo:
    def __init__(self) -> None:
        self.tasks = []

    def addTask(self,work):
        if work.status == False:
            work.status = "UnFinished"
        self.tasks.append({"id":work.id,"Task":work.task,"Status":work.status})


    def displayTasks(self):
        print("Tasks: ")
        for i in self.tasks:
            print(f"Task Id: {i['id']} \t\t Task: {i['Task']}\t Status: {i['Status']}")


    def taskStatus(self,task_id):
        for i in self.tasks:
            if  i['id']== task_id :
                print(f"Task Id: {i['id']} \t\t Task: {i['Task']}\t Status: {i['Status']}")
                return
            else:
                print("Not found the task ")
    
    def updateId(self):
        for i in range(1,len(self.tasks)+1):
            self.tasks[i-1]['id'] = i

    def deleteTask(self,task_id):
        for i in self.tasks :
            if i['id'] == task_id:
                self.tasks.remove(i)
                self.updateId()
                print("Task Delted Successfully!!")
                return 
        else:
            print("Not found the task ")
    
    def markComplete(self,task_id):
        for i in self.tasks :
            if i['id'] == task_id:
                i['Status'] = "Finished"
                print(f"Task Id: {i['id']} \t\t Task: {i['Task']}\t Status: {i['Status']}")
                return
        else:
            print("Not found the task ")


def main():
    list = ToDo()
    id = 0

    while True:
        print("\n1)Add Task")
        print("2)Display Task")
        print("3)Mark as Complete")
        print("4)Delete The Task")
        print("5)Check Status")
        print("6)Exit")


        choice = int (input("Enter Your Choice : "))
        
        if choice == 1:
            id +=1 
            task = input("What is the Task : ")
            status = False
            
            work = Task(id,task,status)
            
            list.addTask(work)
        
        elif choice == 2:
            list.displayTasks()
        
        elif choice == 3:
            mark_id = int(input("Enter the ID : "))
            list.markComplete(mark_id)
            
        elif choice == 4:
            delete_id = int(input("Enter the ID :  "))
            list.deleteTask(delete_id)

        elif choice == 5:
            task_id = int (input("Enter the id to check Status : "))
            list.taskStatus(task_id)

        elif choice == 6:
            break
        else:
            print("invalid Choice!!")
main()