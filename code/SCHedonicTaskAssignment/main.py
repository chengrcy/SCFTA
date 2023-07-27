import json
import copy

if __name__ == '__main__':
    a = open(r"D:/Data/workerdata.txt", "r", encoding='UTF-8')
    workerdata = a.read()
    workerdata = json.loads(workerdata)
    b = open(r"D:Data/taskdata.txt", "r", encoding='UTF-8')
    taskdata = b.read()
    taskdata = json.loads(taskdata)

    numWorker = len(workerdata)
    numTask = len(taskdata)

    workers = []
    tasks = []
    numw = 0
    numt = 0
    for i in range(numWorker):
        if numw>6000:
            break
        workers.append(Worker(workerdata[i]))
        numw += 1
    for j in range(numTask):
        if numt>5000:
            break
        tasks.append(Task(taskdata[j]))
        numt += 1


    greedyCFTA(workers, tasks)
    BRCoalitionTA(workers, tasks)
    bpSelectAcceptTA(workers, tasks)
    hedonicCFTA(workers,tasks)
