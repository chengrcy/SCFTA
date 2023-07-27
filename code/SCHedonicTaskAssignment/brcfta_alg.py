import copy
import time

def BRCoalitionTA(workers, tasks):
    startTime = time.perf_counter()
    # 初始化
    computeCanWTA(workers, tasks)
    for worker in workers:
        worker.curTaskId = -1
        worker.curUnity = 0
        worker.ctbSkill = []
    for task in tasks:
        task.needSkill = copy.deepcopy(task.skill)
    stopTag = True
    switchOptTime = 0
    while(stopTag):
        stopTag = False
        for worker in workers:
            if worker.curUnity < worker.ecpUnity and worker.curTaskId != -1:
                stopTag=True
                switchOptTime += 1
                BRExitCoalition(worker.id,workers,tasks)
            if len(worker.canTaskSet)>0:
                bestTaskIdandUnity = computeBestResponse(worker.id, workers, tasks)
                bestTaskId = bestTaskIdandUnity[0]
                bestTaskUnity = bestTaskIdandUnity[1]
                if bestTaskId != -1 and bestTaskUnity>worker.ecpUnity:
                    stopTag = True
                    switchOptTime += 1
                    BRJoinCoalition(worker.id,bestTaskId,workers,tasks)
                    worker.canTaskSet.remove(bestTaskId)
    endTime = time.perf_counter()

    totalTime = endTime-startTime
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