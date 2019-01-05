#
from crontab import CronTab
cron = CronTab(user=True)
job = cron.new(command='/usr/local/bin/python3 /Users/premkumar/Desktop/Experiment/sherlock/example1.py')
job.minutes.every(1)
cron.write()


# from crontab import CronTab
#
# cron = CronTab(user=True)
#
# # job = cron.new(command='python3 example1.py')
# # job.minute.every(1)
# #
# #
# # cron.write()
# # print("Job created")
#
# # list all cron jobs (including disabled ones)
# for job in cron:
#     #cron.remove(job)
#     print(job)
#
# #cron.remove(job)
# print("Job removed")
#
# # list all cron jobs (including disabled ones)
# # for job in cron:
# #     print(job)