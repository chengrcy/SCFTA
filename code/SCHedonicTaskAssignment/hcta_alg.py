import time

def hedonicCFTA(workers,tasks):
    startTme = time.perf_counter()
    switchOptTime = 0
    computeCanWTA(workers,tasks)
    for worker in workers:
        worker.curTaskId = -1
        worker.curUnity = 0
        worker.ctbSkill=[]
    stopTag = True
    while(stopTag):
        stopTag = False
        for worker in workers:
            if(worker.curTaskId!=-1 and len(worker.ctbSkill)==0):
                stopTag = True
                tasks[worker.curTaskId].coalition.remove(worker.id)
                worker.curTaskId = -1
                worker.curUnity = 0
                switchOptTime += 1
            if(worker.curTaskId!=-1 and worker.curUnity<=0):
                stopTag = True
                switchOptTime += 1
                ExitOldCoalition(worker.id,worker.curTaskId, workers, tasks)
                worker.curTaskId = -1
                worker.curUnity = 0
                worker.ctbSkill=[]
            bestTaskandUnity = computeBestTask(worker.id,workers,tasks)
            bestUnity = bestTaskandUnity[0]
            bestTaskId = bestTaskandUnity[1]
            if(bestUnity>worker.curUnity):
                stopTag = True
                switchOptTime += 1
                JoinNewCoalition(worker.id,bestTaskId,workers,tasks)
                worker.canTaskSet.remove(bestTaskId)

    endtime = time.perf_counter()

    totalTime = endtime-startTme
    totalTaskNum = 0
    totalWorkerNum = 0
    totalUnity = 0
    minUnity = 10000
    totalUsedSkillNum = 0
    totalSkillNum = 0
    for task in tasks:
        if(len(task.needSkill) == 0):
            totalTaskNum += 1
            totalWorkerNum += len(task.coalition)
            for wId in task.coalition:
                if(workers[wId].curUnity < minUnity):
                    minUnity = workers[wId].curUnity
                totalUnity += workers[wId].curUnity
                totalSkillNum += len(workers[wId].skill)
            totalUsedSkillNum += len(task.skill)