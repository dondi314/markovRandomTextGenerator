# Textfiles used for generating random sentences

### The textfiles found here have been cleaned from http://www.textfiles.com

The main objective was to find text that was good for producing random sentences of length small enough to fit on twitter.  Basically I wanted it to spout out funny sayings, or philosophical sounding qoutes.  The humor and qoutes section of textfiles.com were good for this.  My file is rather small, and it took several hours to clean.  The reason for this is that the textfiles on this website are very unclean.  My algorithm does not simply convert uppercase to lowercase, because I want it to take into account people's name, and letters that begin a sentence.  A lot of the cleaning was too specific to do in python, and I just used my macbook's find and replace option.  Sometimes I rewrote a sentence to avoid the characters :, ;, and - whenever possible.

### What is important whenever cleaning the text?




### What are some improvement's to be made?

One thing that would help would be to convert all male names in the corpus to a single male name, and all the female names to a single female name.  This will help make the text generation more random.  Say that Chingbobcooney was a name in your corpus.  Since it only shows up once most likely, whenever your algorithm comes to a key in your dictionary (word, Chingbobcooney), it will always assign the same word after.  However, say Chingbobcooney is male, then we could have assigned hime the name Zeus, as well as every other proper male noun, and we would have more choices for the next word in the sentence.  Also, since we are just generating random sentences, we don't care about the name much, and the grammar should work just as well as with another name subbed in.

Similarly, it helps to change as many he/she sentences as you can to the same gender.  In otherwords, pick a gender, say female.  The a sentence that reads, 

    "He goes to the store to buy fake cheese." 
should read,

    "She goes to the store to buy fake cheese." 
