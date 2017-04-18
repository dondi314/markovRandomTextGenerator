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

'''
#markovText = ''.join([c for c in data if ord(c) < 128]).replace("``",'"').replace("''",'"')
#print data
data='"'+data
data = re.findall('"([^"]*)"', data)
#for item in data:
#    print item+'\n'+'\n'
data = [sentence.replace(' . ', '. ').replace("you 'd", "you'd").replace("I 'd", "I'd").replace(" 've", "'ve").replace(" !","!").replace(" 's", "'s").replace("I 'm", "I'm").replace(' , ', ', ').replace(" 're", "'re").replace(' ? ', '? ').replace(" 'll", "'ll").replace(" n't", "n't").strip() for sentence in data]
#for item in data:
#    print item+'\n'+'\n'
data = [sentence for sentence in data if (len(sentence) > 2 and ord(sentence[len(sentence)-1]) == ord('.'))]
for item in data[1::]:
    print item+'\n'+'\n'
#data = [sentence.replace('\n',' ') for sentence in data]
#alpha = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
#data = [sentence for sentence in data if sentence[1] in alpha]
f = open('outty.txt', 'a')
for sentence in data[1::]:
	if len(sentence) < 100 and len(sentence) > 25:
		f.write('"'+sentence+'"'+"\n")
f.close()

f = open('mytext.txt', 'a')
for sentence in data[1::]:
	text = sentence
	output = ""

	# Load the pretrained neural net
	tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')

	# Tokenize the text
	tokenized = tokenizer.tokenize(text)

	# Get the list of words from the entire text
	words = word_tokenize(text)

	# Identify the parts of speech
	tagged = nltk.pos_tag(words)

	for i in range(0,len(words)):
	    replacements = []

	    # Only replace nouns with nouns, vowels with vowels etc.
	    for syn in wordnet.synsets(words[i]):

	        # Do not attempt to replace proper nouns or determiners
	        if tagged[i][1] == 'NNP' or tagged[i][1] == 'DT':
	            break

	        # The tokenizer returns strings like NNP, VBP etc
	        # but the wordnet synonyms has tags like .n.
	        # So we extract the first character from NNP ie n
	        # then we check if the dictionary word has a .n. or not
	        word_type = tagged[i][1][0].lower()
	        if syn.name().find("."+word_type+"."):
	            # extract the word only
	            r = syn.name()[0:syn.name().find(".")]
	            replacements.append(r)

	    if len(replacements) > 0:
	        # Choose a random replacement
	        replacement = replacements[randint(0,len(replacements)-1)]
	        output = output + " " + replacement
	    else:
	        # If no replacement could be found, then just use the
	        # original word
	        output = output + " " + words[i]
	output = output.replace("_", " ")
	data = output
	#print data
	data = data.replace(' . ', '. ').replace("you 'd", "you'd").replace("I 'd", "I'd").replace(" 've", "'ve").replace(" !","!").replace(" 's", "'s").replace("I 'm", "I'm").replace(' , ', ', ').replace(" 're", "'re").replace(' ? ', '? ').replace(" 'll", "'ll").replace("n't", "not").strip()

	f.write('"'+data+'"'+"\n")
f.close()
'''
""" ========================================================
		This generates triples from the given data string. So if our
		string were "The kitty is adorable", we would generate
		(The, kitty, is) and then (kitty, is, adorable).
		======================================================== """
'''	def fileToWords(self):
		charactersToKeep = [32,33,39,44,45,46,48,49,50,51,52,53,54,55,56,57,63]+
						   [i for i in range(65,91)]+
						   [i for i in range(97,123)]
		self.openFile.seek(0)
		data = self.openFile.read()
		data = ''.join([c for c in data if ord(c) in charactersToKeep])
		words = nltk.word_tokenize(data)
		words = nltk.pos_tag(words)
		return words '''



'''	def triples(self):

		if len(self.words) < 3:
			return

		for i in range(len(self.words) - 2):
			yield (self.words[i], self.words[i+1], self.words[i+2])'''
