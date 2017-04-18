import nltk
from nltk.corpus import wordnet
from nltk import word_tokenize as wordTokenize
from nltk import pos_tag as posTag
from random import randint as getInt
from random import choice as getWord
import MySQLdb

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

	def generateMarkovText(self, size=400):
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

description = 'aliceInWonderland'
markovText = Markov(description).generateMarkovText()
print markovText
