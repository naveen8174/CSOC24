import os
import pandas as pd
name=input("enter your name: ")
print("hello", name, "let's start!!\n")
task={"task":[],"status":[]}
print("1.enter the task\n2.print the tasks\n3.mark the task as completed\n4.save the file\n5.exit\nother.exit")
while True:
  opt=input("enter the option: ")
  if opt=='1':
    task1=input("enter the new task!!:  ")
    task["task"].append(task1)
    task["status"].append("no")
  elif opt=='2':
    printtask=pd.DataFrame(task)
    print(printtask)
  elif opt=='3':
    print("enter the completed task!!:  ")
    taskc=input()
    ind=task["task"].index(taskc)
    task["status"][ind]='yes'
  elif opt=='4':
    printtask=pd.DataFrame(task)
    file1=printtask.to_csv("todo-list.csv",index=False)
    location=os.getcwd()
    path=os.path.join(location,"todo-list.csv")
    print("file saved successfully:{")
  elif opt=='5':
    break
  else:
    print("enter valid input:>")
