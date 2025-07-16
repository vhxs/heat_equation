# Code written in 2007. Unchanged since then, with the exception of migration to Python 3 syntax.

from vpython import *
from time import sleep
from copy import deepcopy
class Heat2D:
	def __init__(self, inittemp, k, max = 255):
		self.prevtemp = deepcopy(inittemp)
		self.k = k
		self.m = len(inittemp)
		self.n = len(inittemp[0])
		self.dx = 1.
		self.dt = (self.dx**2)/(4*self.k)
		self.max = max
		self.createbars()
		input()
		print("done")
		while True:
			self.step()
			print("...")
			self.updatebars()
	def createbars(self):
		self.bars = []
		for i in range(self.m):
			self.bars.append([])
			for j in range(self.n):
				h = self.prevtemp[i][j]
				c = self.heatcolor(h, self.max)
				bar = box(pos=vector(self.dx*(i-self.m/2), h/2., self.dx*(j-self.n/2)), size = vector(self.dx, h, self.dx), color = c)
				self.bars[i].append(bar)
	def heatcolor(self, value, max):
		r = sqrt(value/max)
		g = 0
		b = 1 - value/max
		return vector(r, g, b)
	def updatebars(self):
		for i in range(self.m):
			for j in range(self.n):
				h = self.prevtemp[i][j]
				c = self.heatcolor(h, self.max)
				self.bars[i][j].color = c
				self.bars[i][j].pos.y = h/2.
				self.bars[i][j].height = h
	def step(self):
		zerorow = self.n*[0]
		newtemp = []
		for i in range(self.m):
			newtemp.append(zerorow[:])
		for i in range(self.m):
			for j in range(self.n):
				if (i == 0) or (i == self.m - 1) or (j == 0) or (j == self.n - 1):
					newtemp[i][j] = self.prevtemp[i][j]
		i = 1
		while i < self.m - 1:
			j = 1
			while j < self.n - 1:
				newtemp[i][j] = self.prevtemp[i][j] + self.k*self.dt*(self.prevtemp[i+1][j]+self.prevtemp[i-1][j]-4*self.prevtemp[i][j]+self.prevtemp[i][j+1]+self.prevtemp[i][j-1])/(self.dx**2)
				j += 1
			i += 1
		self.prevtemp = deepcopy(newtemp)
n = 90
max = 20
t = []
onerow = (n+20)*[5]
t.append(onerow)
for i in range(n-2):
	x = n - 22 - 2*(i//2)
	if x >= 0:
		r = [5] + 10*[0] + (i//2)*[0] + 10*[max] + x*[0] + 10*[max] + (i//2)*[0] + 10*[0] + [5]
	else:
		r = [5] + 10*[0] + (i//2)*[0] + (x+20)*[max] + (i//2)*[0] + 10*[0] + [5]
	t.append(r)
t.append(onerow)
z = Heat2D(t, 1, max)
