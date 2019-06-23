class Room:
	def __init__(self, name,desc,quest,north,west,east,south):
		self.name=name
		self.desc=desc
		self.quest=quest
		self.north=north
		self.south=south
		self.east=east
		self.west=west




	def get_name(self):
		return self.name

	def get_short_desc(self):

		if self.quest.complete_or_not==False:

					return self.desc

		return "theres nothing in this room"

	def get_quest_action(self):

		if self.quest.complete_or_not==False:

				return self.quest.action

	def set_quest(self, q):

		if self.quest.complete_or_not==True:

			self.quest=q

	def get_quest(self):

		if self.quest.complete_or_not==False:

			return self.quest

	def set_path(self, dir, dest):

		return "???????????"

	def draw(self):

		for i in range(8):

			print("-",end="")

			if i==3 and self.north:

				print("N",end="")

		print("  ")

		for i in range(4):

			print("_      _")

			if i==1:

				if self.west and self.east:

					print("W      E")

				elif self.west:

					print("W      _")

				elif self.east:

					print("       E")

		for i in range(8):

			print("-",end="")

			if i==3 and self.south:

				print("S",end="")

		print("  ")

	def move(self, dir):

		"""TODO: Returns an adjoining Room object based on a direction given. (i.e. if dir == "NORTH", returns a Room object in the north)."""

		diresctions=("north","south","east","west")
		rooms_next_to=(self.north,self.south,self.east,self.west)
		return rooms_next_to[diresctions.index(dir.lower())]


