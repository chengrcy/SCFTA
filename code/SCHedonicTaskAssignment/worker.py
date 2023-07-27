class Worker():
    def __init__(self, worker):
        self.id = worker[0]
        self.location = worker[1]
        self.skill = worker[2]
        self.skillVec = worker[3]
        self.ecpUnity = 0.5
        self.speed = 1
        self.movCost = 0.01
        self.awtCost = 0.01
        self.exeCost = 0.01
        self.curTaskId = -1
        self.curUnity = 0
        self.canTaskSet = []
        self.waitList = []
        self.ctbSkill = []