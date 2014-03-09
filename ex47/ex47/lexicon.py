class Lexicon(object):
	def __init__(self):
		self.directions = ['north', 'south', 'east', 'west', 'down', 'up', 'left', 'right', 'back']
		self.verbs = ['go', 'stop', 'kill', 'eat']
		self.stop_words = ['the', 'in', 'of', 'from', 'at', 'it']
		self.nouns = ['door', 'bear', 'princess', 'cabinet']
		self.numbers = [x for x in range(10)]		
		
	def scan(self, sentence):
		words = sentence.split()
		sentence_list = []
		for word in words:
			try:
				sentence_list.append(('number', int(word)))
			except ValueError:
				if word in self.directions:
					sentence_list.append(('direction', word))
				elif word in self.verbs:
					sentence_list.append(('verb', word))
				elif word in self.stop_words:
					sentence_list.append(('stop', word))
				elif word in self.nouns:
					sentence_list.append(('noun', word))
				else:
					sentence_list.append(('error', word))
		return sentence_list
			
			
lexicon = Lexicon()