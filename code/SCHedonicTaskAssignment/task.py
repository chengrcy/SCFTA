import copy

class Task():
    def __init__(self,task):
        self.id = task[0]
        self.location = task[1]
        self.skill = task[2]
        self.skillVec = task[3]
        self.deadline = task[4]
        self.reward = task[5]
        self.pcoTime = task[6]
        self.comTag = 0
        self.needSkill = copy.deepcopy(task[2])
        self.coalition = []
        self.canWorkerSet = []
        self.startTime = 0