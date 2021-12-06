
import os
import datetime
import shutil

from django.core.mail import (
    send_mail, send_mass_mail, mail_admins, mail_managers, EmailMessage, EmailMultiAlternatives)

from apscheduler.schedulers.background import BackgroundScheduler

class MailScheduler:

    def __init__(self):
        pass

    def mail_create(self, task):
        self.subject = f'タスクの締め切りまで残り1日を切りました。'
        self.message = f"ユーザー名：{task[0]}, タスク名：{task[2]}、グループ名：{task[3]}"
        self.from_email = 'moyashi0324@gmail.com'
        self.to = [task[1]]
        print("email: ", task[1])
        send_mail(self.subject, self.message, self.from_email, self.to)

    def create_deadline(self, deadline_at):
        self.year = int(deadline_at[0:4])
        self.month = int(deadline_at[5:7])
        self.day = int(deadline_at[8:10])
        self.hour = int(deadline_at[11:13])
        self.minute = int(deadline_at[14:16])
        self.second = int(deadline_at[17:19])
        self.deadline = datetime.datetime(self.year, self.month, self.day, self.hour, self.minute, self.second)
        return self.deadline

    def get_task_list(self):
        dir = os.path.dirname(__file__)
        mailing_list = []
        f = open(dir+"/task_list.txt", mode="r")
        for l in f.readlines():
            line = l.rstrip('\n').split(",")
            deadline_before_one_day = self.create_deadline(line[2].split("$")[1]) + datetime.timedelta(days=-1)
            now = datetime.datetime.now()
            mail = []
            if((now - deadline_before_one_day).seconds <= 60):
                print("add mail")
                mail.append(line[4].split("$")[1])
                mail.append(line[5].split("$")[1])
                mail.append(line[1].split("$")[1])
                mail.append(line[3].split("$")[1])

            if len(mail) > 0:
                print("append")
                mailing_list.append(mail)
        f.close()

        return mailing_list

    def send_mail(self):
        task_list = self.get_task_list()
        for task in task_list:
            self.mail_create(task)

    def start(self):
        scheduler = BackgroundScheduler()
        scheduler.add_job(self.send_mail, 'interval', minutes=1)
        scheduler.start()
