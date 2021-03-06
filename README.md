# markovRandomTextGenerator

### markovRandomTextGenerator.py

This program will generate random text using a Markov chain.  The program pulls the text from a MySQL database named "nlpText".

### markovRandomTextGeneratorVer2.py

#### NOTE: I know have version markovRandomTextGeneratorVer3.py which gives much better results

This program will generate random text using a Markov chain.  The program pulls the text from a MySQL database named "nlpText".  This is the version I used to get the data which you will find in the myResults folder.  I decided to leave the other version because it has less to it, and you can modify it to your liking if you wish.  I added in a function called randomizeSentenceOrdering at the top of the file.  The input is a string, and what it does is takes a sentence such as,

    I really like the cat. The cat likes me. It does bite me though. The cat is mean sometimes.
converts it to a list split by the periods,

    ["I really like the cat","The cat likes me","It does bite me though","The cat is mean sometimes"]
and then randomly rearranges the words, for example like this:

    ["The cat is mean sometimes","The cat likes me","I really like the cat","It does bite me though"]
Then it adds back the periods joining all the words into a single string, giving:

    The cat is mean sometimes. The cat likes me. I really like the cat. It does bite me though.
    
Before I do word_tokenize and pos_tag, I concatenate the two strings, giving:
 
     I really like the cat. The cat likes me. It does bite me though. The cat is mean sometimes. 
     The cat is mean sometimes. The cat likes me. I really like the cat. It does bite me though.   
Now, after we tokenize we get:
 
     ['I', 'really', 'like', 'the', 'cat', '.', 'The', 'cat', 'likes', 'me', '.', 'It', 'does', 
      'bite', 'me', 'though', '.', 'The', 'cat', 'is', 'mean', 'sometimes', '.', 'The', 'cat', 
      'is', 'mean', 'sometimes', '.', 'The', 'cat', 'likes', 'me', '.', 'I', 'really', 'like', 
      'the', 'cat', '.', 'It', 'does', 'bite', 'me', 'though', '.']
Then after pos_tag we get:
 
     [('I', 'PRP'), ('really', 'RB'), ('like', 'IN'), ('the', 'DT'), ('cat', 'NN'), ('.', '.'), 
      ('The', 'DT'), ('cat', 'NN'), ('likes', 'VBZ'), ('me', 'PRP'), ('.', '.'), ('It', 'PRP'), 
      ('does', 'VBZ'), ('bite', 'VB'), ('me', 'PRP'), ('though', 'IN'), ('.', '.'), ('The', 'DT'), 
      ('cat', 'NN'), ('is', 'VBZ'), ('mean', 'JJ'), ('sometimes', 'RB'), ('.', '.'), ('The', 'DT'), 
      ('cat', 'NN'), ('is', 'VBZ'), ('mean', 'JJ'), ('sometimes', 'RB'), ('.', '.'), ('The', 'DT'), 
      ('cat', 'NN'), ('likes', 'VBZ'), ('me', 'PRP'), ('.', '.'), ('I', 'PRP'), ('really', 'RB'), 
      ('like', 'IN'), ('the', 'DT'), ('cat', 'NN'), ('.', '.'), ('It', 'PRP'), ('does', 'VBZ'), 
      ('bite', 'VB'), ('me', 'PRP'), ('though', 'IN'), ('.', '.')]
      
The idea is that: 
 
     ('cat', 'NN'), ('.', '.'), ('The', 'DT') and ('cat', 'NN'), ('.', '.'), ('It', 'PRP') 
create the same key in our dictionary of 
 
     (('cat', 'NN'), ('.', '.')), 
and that 
 
     ('The', 'DT') and ('It', 'PRP') 
should be equally likely to occur afterwards.  This is a pretty hacked solution to the problem of "We don't care what happens after the period." and I plan on making a better solution later on (which would be easy to implement I admit).  However, running this hacked solution gave good results for my purposes, although it would cause considerable slowdown for bigger cases.

      
      
    

### markovRandomTextGenerator.hs

I am learning how to program in haskell, so I decided to implement a random text generator in haskell.  This program is much slower than the one I made in python, and I have not implemented any of the nltk sorts of features in this program.

### twitter_bot.py

This program will automatically post tweets for you at set intervals of time.
You will need to set the passwords.
To run, type 
    
    python twitter_bot.py mytextfilename.txt
