# 基于双边偏好的选择-接受算法
import time
import copy

def bpSelectAcceptTA(workers, tasks):
    startTime = time.perf_counter()
    # 初始化
    computeCanWorkerSet(workers, tasks)
    for worker in workers:
        worker.curTaskId = -1
        worker.curUnity = 0
        worker.ctbSkill = []
        worker.waitList = []
    for task in tasks:
        task.needSkill = copy.deepcopy(task.skill)
        task.canWorkerSet = []
    computeCanWorkerSet(workers,tasks)
    switchOptTime = 0
    stopTag = True
    while(stopTag):
        stopTag = False
        for task in tasks:
            if len(task.needSkill)>0 and len(task.canWorkerSet)>0:
                stopTag = True
                bestWorkerId = computeBestPerWorker(task.id, workers, tasks)
                if bestWorkerId !=-1:
                    workers[bestWorkerId].waitList.append(task.id)
                    task.canWorkerSet.remove(bestWorkerId)
        for worker in workers:
            if len(worker.waitList)>0:
                bestChoice = computeBestPerTask(worker.id, workers, tasks)
                worker.waitList = []
                bestTaskId = bestChoice[0]
                bestTaskUnity = bestChoice[1]
                bestDis = bestChoice[2]
                if bestTaskId!=-1 and bestTaskUnity > worker.curUnity:
                    stopTag = True
                    switchOptTime += 1
                    BPJoinCoalition(worker.id, bestTaskId, workers, tasks)
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