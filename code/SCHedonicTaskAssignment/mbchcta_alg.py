import time
def matchCFTA(workers,tasks):
    start = time.perf_counter()
    stopFlag = True
    while(stopFlag):
        stopFlag = False
        for task in tasks:
            predictTag = computePredictTagA(task,workers)
            if len(task.availableWorkerA) > 0 and len(task.needSkill) > 0 and task.complishTag == 0:
                stopFlag = True
                objectWorkerId = task.availableWorkerA[0]
                del task.availableWorkerA[0]
                workers[objectWorkerId].waitList.append(task.id)
        for worker in workers:
            if len(worker.waitList) > 0:
                bestResponse = computeBestResponseMatchA(worker,tasks)
                wpredictTag = computePredictTagA(tasks[bestResponse[1]],workers)
                if bestResponse[0] > worker.unity:
                    stopFlag = True
                    if worker.currentTask != -1:
                        exitTakCoalitionMatchA(worker.id,workers,tasks)
                    worker.currentTask = bestResponse[1]
                    worker.unity = bestResponse[0]
                    tasks[bestResponse[1]].coalition.append(worker.id)
                    for covSkill in bestResponse[2]:
                        tasks[bestResponse[1]].needSkill.remove(covSkill)
                    if len(tasks[bestResponse[1]].needSkill) == 0:
                        # print('a')
                        tasks[bestResponse[1]].complishTag = 1
                worker.waitList = []
    end = time.perf_counter()
    totaltime = end - start
    numComplishTask = 0
    numComplishWorker = 0
    totalUnity = 0
    for task in tasks:
        if task.complishTag == 1:
            print(task.id,task.coalition)
            numComplishTask += 1
            numComplishWorker += len(task.coalition)
            for jworkerId in task.coalition:
                totalUnity += workers[jworkerId].unity
    result = [numComplishTask,numComplishWorker,totalUnity,totaltime]
    return result