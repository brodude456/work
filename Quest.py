class Quest:
	def __init__(self, reward, action, desc, before, after, room, fail_msg, pass_msg,needed,):
		"""TODO: Initialises a quest."""
		self.reward=reward
		self.action=action
		self.desc=desc
		self.befored=before
		self.afterd=after
		self.fail_msg=fail_msg
		self.pass_msg=pass_msg
		self.needed=needed
		self.room=room
		self.complete_or_not=False

	def get_info(self):

		return self.desc

	def is_complete(self,action):

		if self.complete_or_not==True:
			return "the quest is complete"


	def get_action(self):

		return self.action

	def get_room_desc(self):

		return self.room.get_short_desc()

	def attempt(self, player):

		skill,will=self.needed.split(",")

		if player.get_skill()>=skill and player.get_will()>=will:

			player.inventory.append(self.reward)
			self.room.desc="theres nothing in this room"

