from nltk.corpus import wordnet
from nltk        import word_tokenize as wordTokenize
from nltk        import pos_tag as posTag
from random      import randint as getInt
from random      import choice as getWord
from random      import shuffle
import MySQLdb

def randomizeSentenceOrdering(textIn):
	textOut = textIn.split('.')
	s = [i for i in range(0,len(textOut))]
	shuffle(s)
	textOut = '.'.join([textOut[i] for i in s])
	return textOut

def punctuationEqualizer(dictionary):
	punctuation = []
	myKeys = []
	for key in dictionary:
		if key[1][0] == ['.','!','?']:
			punctuation.append(dictionary[key])
			myKeys.append(key)
	for i in range(0,len(myKeys)):
		dictionary[myKeys[i]] = punctuation
	return dictionary


class Markov(object):

	def __init__(self, description):
		self.memory = {}
		self.description = description
		self.words = self.grabMySQLdocument(description)
		self.wordSize = len(self.words)
		self.database()

	def grabMySQLdocument(self, description):
		db = MySQLdb.connect("localhost","dondi","","nlpText" )
		cursor = db.cursor()
		sql = """SELECT document FROM Documents WHERE description = '%s'""" % (description)
		cursor.execute(sql)
		result = (cursor.fetchall())
		db.commit()
		db.close()
		result = result[0][0].replace('_', "'")
		words = wordTokenize(result)
		words = posTag(words)
		return words

	def triples(self):

		if len(self.words) < 3:
			return

		for i in range(len(self.words) - 2):
			yield (self.words[i], self.words[i+1], self.words[i+2])


	def database(self):
		for w1, w2, w3 in self.triples():
			key = (w1, w2)
			if key in self.memory:
				self.memory[key].append(w3)
			else:
				self.memory[key] = [w3]


	def generateMarkovText(self, size=800):
		self.memory = punctuationEqualizer(self.memory)
		seed = getInt(0, self.wordSize-3)
		seedWord, nextWord = self.words[seed], self.words[seed+1]
		w1, w2 = seedWord, nextWord
		genWords = []
		for i in xrange(size):
			genWords.append(w1)
			w1, w2 = w2, getWord(self.memory[(w1, w2)])
		genWords.append(w2)
		newWords = []
		for word in genWords:
			newWords.append(word[0])
		genWords = newWords
		return ' '.join(genWords)



description = 'humorText'
markovText = Markov(description).generateMarkovText()
markovText = markovText.replace(' . ', '. ').replace(' , ', ', ')
markovText = markovText.replace(' ! ', '! ').replace(' ? ', '? ')
markovText = markovText.replace(" '", "'").replace(" n't", "n't")
uPPER = [chr(i) for i in range(ord('A'),ord('Z')+1)]
goodSentences = [sentence.strip()+"." for sentence in markovText.split('.')[1:len(markovText)-1:] \
				if (len(sentence.split()) > 6 and len(sentence.split()) < 16 and \
				len(sentence) < 120 and sentence.strip()[0] in uPPER)]

try:
	f = open('twitter_bot.txt', 'a')
except NameError:
	f = open('twitter_bot.txt', 'w+')
for sentence in goodSentences:
	f.write(sentence+'\n')
f.close()
