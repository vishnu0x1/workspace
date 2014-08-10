class task:
	def __init__(self, deadline, penalty):
		self.deadline = deadline
		self.penalty = penalty
	def __str__(self):
		return "(" + self.deadline + "," + self.penalty + ")"

def sortByDeadline(taskList):
	return sorted(taskList, key=lambda task: task.penalty, reverse=True)

def scheduleTask(taskList):
	taskList = sortByDeadline(taskList)
	scheduledList = []
	nr_tasks = len(taskList)
	nr_early = [0] * (nr_tasks + 1)
	nr_early_limit = range(0, nr_tasks + 1)
	for x in taskList:
		t = x.deadline
		if all(a < b for a, b in zip(nr_early[t:], nr_early_limit[t:])):
			nr_early[t:] = [i + 1 for i in nr_early[t:]]
			scheduledList.append(x)
	return scheduledList

taskList = [ task(4, 70), task(2, 60), task(4, 50), task(3, 40),
                task(1, 30), task(4, 20), task(6, 10) ]

for x in scheduleTask(taskList):
	print (x.deadline, x.penalty)
