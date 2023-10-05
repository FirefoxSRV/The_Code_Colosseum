def profit(job,time):
    job.sort(key=lambda x: x[2], reverse=True)
    jobsPerformed = [-1]*time
    freeSlots = [False]*time
    profit = 0
    for i in range(len(job)):
        for j in range(min(time-1,job[i][1]-1),-1,-1):
            if freeSlots[j] == False:
                freeSlots[j]=True
                jobsPerformed[j]=job[i][0]
                profit+=job[i][2]
                break
    return jobsPerformed


jobs = [('a', 4, 70), ('b', 1, 80), ('c', 1, 60), ('d', 2, 50), ('e', 3, 40), ('f', 1, 30)]
t = 3
x = profit(jobs,t)
print(x)
