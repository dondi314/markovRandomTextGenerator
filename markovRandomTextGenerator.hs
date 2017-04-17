import Data.List.Split (splitOneOf)
import Data.List.Split (splitOn)
import Data.List.Split (chunksOf)


-- This program will randomly generate markov sentences
-- To run this program, run it in a directory with a file name output.txt which will be written to.
-- open haskell in the terminal and type "text <- readFile yourfilenamewithqoutes"
-- Then type "program text anypositivenumber" (this is a 'random seed')
-- This program doesn't work great, put its a start!


wordList text = [word | word <- (splitOneOf " \n" text), word /= "", word /= "\n"]

makeRandomList seed = [ floor (1000*abs(sin(seed+(x^5+2*x+9)))) | x <- [1..300]]

markovWord n words randomList
  | n == 0 = words!!(randomList!!0 `mod` (length words + (-2)))
  | n == 1 = words!!(1 + randomList!!0 `mod` (length words + (-2)))
  | otherwise = random (markovWord (n-2) words randomList) (markovWord (n-1) words randomList) (randomList!!n)
          where random x y z = [w | (x,y,w) <- myTriples]!!(z `mod` length [w | (x,y,w) <- myTriples]) ;
                myTriples = triples
                            where words2 = tail words
                                  words3 = tail words2
                                  list1 = [(head x, head (tail x),last x) | x <- chunksOf 3  words, length x == 3]
                                  list2 = [(head x, head (tail x),last x) | x <- chunksOf 3 words2, length x == 3]
                                  list3 = [(head x, head (tail x),last x) | x <- chunksOf 3 words3, length x == 3]
                                  triples = list1++list2++list3

markovText n words randomList
  | n == 0 = words!!(randomList!!0 `mod` (length words + (-2)))
  | n == 1 = words!!(randomList!!0 `mod` (length words + (-2))) ++ " " ++ words!!(1 + randomList!!0 `mod` (length words + (-2)))
  | otherwise = markovText (n-1) words randomList ++ " " ++ markovWord n words randomList

makeIntoSentences text seed = concat (init (tail [x++".\n" | x <- (splitOn ". " (markovText 200 (wordList text) (makeRandomList seed)))]))

program text seed = writeFile "output.txt" (makeIntoSentences text seed)
