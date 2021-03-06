from simuBot import simuBot
from ImprovedPotentialField import *
from pymorse import Morse

class ImprovedSimuBot(simuBot):

	def __init__(self, pose, motion, currentMap, isMorse):
		simuBot.__init__(self, pose, motion, currentMap, isMorse )
		self.otherBots = []
	
	def computePath(self, Goal, curTime):
		robotsPath = []
		for bot in self.otherBots :
			for path in bot.path:
				robotsPath.append([path])
		#print(robotsPath)
		pot =  ImprovedPotentialField( [ self.map['x'], self.map['y'] ] , self.map['obstacles'], 1, [round(self.position['x']),round(self.position['y'])], Goal, curTime, robotsPath )
		self.path = pot.getPath()
		#print("chemin:", self.path, "mission:", self.mission)
		self.pathStep = 1
		if not self.path :
			self.noPath += 1
			self.mission = []		

	def setOthersBots(self, otherBots):
		self.otherBots = otherBots
