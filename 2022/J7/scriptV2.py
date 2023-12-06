f = open('input')

data = list(map(lambda x : x.split('\n')[0], f.readlines()))

f.close()

class File():

	def __init__(self, name, size):

		self.name = name
		self.size = size

	def get_size(self):
		return self.size

class Directorie():

	def __init__(self, name, parent = None):

		self.parent = parent
		self.name = name
		self.innerFile = []

	def add_file(self, string, setDirectories):

		list_string = string.split(' ')
		if self.get_directorie_by_name(list_string[1]) == None:
			if list_string[0] == "dir":

				newDir = Directorie(list_string[1], parent = self)
				self.innerFile.append(newDir)

				if not(newDir in setDirectories):
					setDirectories.add(newDir)

			else:
				self.innerFile.append(File(list_string[1], int(list_string[0])))

	def get_size(self):

		size = 0

		for file in self.innerFile:
			size += file.get_size()

		return size

	def get_parent(self):

		return self.parent

	def get_directorie_by_name(self, name):
		for file in self.innerFile:
			if file.name == name:
				return file

		return None

setDirectories = set()
root = Directorie("/")
setDirectories.add(root)

currentFile = None

for i, command in enumerate(data):

	list_command = command.split(' ')

	if list_command[0] == "$":

		if list_command[1] == "cd":

			if list_command[2] == "/":
				currentFile = root

			elif list_command[2] == "..":
				currentFile = currentFile.get_parent()

			else:
				currentFile = currentFile.get_directorie_by_name(list_command[2])

	else:
		currentFile.add_file(command, setDirectories)


result1 = 0

for directorie in setDirectories:

	dir_size = directorie.get_size()

	if dir_size <= 100000:

		result1 += dir_size

print("result 1 :", str(result1))

disk_space = 70000000

unused_space_needed = 30000000

unused_space = disk_space - root.get_size()

space_to_clear = unused_space_needed - unused_space

print("result 2 : " + str(min(setDirectories, key = lambda x : x.get_size() if x.get_size() >= space_to_clear else 1000000000).get_size()))