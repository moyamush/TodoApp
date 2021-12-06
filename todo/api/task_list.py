
import os
import shutil


class TaskList: 
    def create_task(self, task, user):
        f = open(os.path.dirname(__file__)+"/task_list.txt", mode="a")
        f.write(f"task_id${task['id']},taskname${task['taskname']},deadline_at${task['deadline_at']},group${task['group']},user_name${user.username},email${user.email}"+'\n')
        f.close()

    def delete_task(self, task_id):
        dir = os.path.dirname(__file__)
        of = open(dir+"/task_list.txt", mode="r")
        wf = open(dir+"/_task_list.txt", mode="w")
        for line in of.readlines():
            taskline = line.rstrip('\n').split(",")
            id = taskline[0].split("$")[1]
            if(id != task_id):
                wf.write(f"{taskline[0]},{taskline[1]},{taskline[2]},{taskline[3]},{taskline[4]},{taskline[5]}"+'\n')
        wf.close()
        of.close()
        shutil.copy(dir+'/_task_list.txt', dir+'/task_list.txt')
    
    def edit_task(self, task, user):
        dir = os.path.dirname(__file__)
        of = open(dir+"/task_list.txt", mode="r")
        wf = open(dir+"/_task_list.txt", mode="w")
        for line in of.readlines():
            taskline = line.rstrip('\n').split(",")
            id = taskline[0].split("$")[1]
            if(id != str(task.id)):
                wf.write(f"{taskline[0]},{taskline[1]},{taskline[2]},{taskline[3]},{taskline[4]},{taskline[5]}"+'\n')
            else:
                wf.write(f"task_id${task.id},taskname${task.taskname},deadline_at${task.deadline_at},group${task.group},user_name${user.username},email${user.email}"+'\n')
        wf.close()
        of.close()
        shutil.copy(dir+'/_task_list.txt', dir+'/task_list.txt')