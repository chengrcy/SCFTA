import copy
import time

def greedyCFTA(workers,tasks):
    startTime = time.perf_counter()
    computeCanWTA(workers, tasks)
    for worker in workers:
        worker.curTaskId = -1
        worker.curUnity = 0
        worker.ctbSkill = []
    for task in tasks:
        task.needSkill = copy.deepcopy(task.skill)
        task.coalition = []
        task.startTime = 0
    for worker in workers:
        nearChoice = computeNearTask(worker.id, workers, tasks)
        nearTaskId = nearChoice[0]
        greedyJoinCoalition(worker.id, nearTaskId, workers, tasks)
    stopTag = True
    switchOptTime = 0
    while stopTag:
        stopTag = False
        for worker in workers:
            if len(worker.canTaskSet) == 0:
                if worker.curTaskId != -1:
                    if worker.curUnity<=0:
                        stopTag = True
                        switchOptTime += 1
                        greedyExitCoalition(worker.id, workers, tasks)
                else:
                    nearChoice = computeNearTask(worker.id, workers, tasks)
                    nearTaskId = nearChoice[0]
                    if nearTaskId != -1:
                        etiUnity = estimateWorkerUnity(worker.id, nearTaskId, workers, tasks)
                        if etiUnity > worker.curUnity:
                            stopTag = True
                            switchOptTime += 1
                            greedyJoinCoalition(worker.id, nearTaskId, workers, tasks)

    endTime = time.perf_counter()
    totalTime = endTime - startTime
    totalTaskNum = 0
    totalWorkerNum = 0
    totalUnity = 0
    minUnity = 10000
    totalUsedSkillNum = 0
    totalSkillNum = 0
    for task in tasks:
        if (len(task.needSkill) == 0):
            totalTaskNum += 1
            totalWorkerNum += len(task.coalition)
            for wId in task.coalition:
                if (workers[wId].curUnity < minUnity):
                    minUnity = workers[wId].curUnity
                totalUnity += workers[wId].curUnity
                totalSkillNum += len(workers[wId].skill)
            totalUsedSkillNum += len(task.skill)