# wordle_game
Wordle! game written in python with pygame.
I used code from https://github.com/Gunnar50/Wordle_game and https://github.com/baraltech/Wordle-PyGame and made some improvements
#1 - Wordle! as first published uses two word lists.  A large one of 13K words that are acceptable and a smaller one 2K of answers
that are more common and familiar words. 
#2 If you allow any word to be entered, then someone will just enter all vowels, etc. to quickly solve.  So I made the game accept only
allowable real words.  If you just use the large list to select the secret word, then you will end up with some really arcane and
unusual words that most people never heard of to solve.  So the game needs to pick words from the shorter more common word list.
#3 - if you look at the original games above, both had little flaws or things missing. so most of my improvements were minor and just
making the game more like the official one at wordlegame.org or the one on the NY Times website.
#4 baraltech's version had indicators of which letters were used at the bottom of the screen.  gunnar50's version was more accurate
at displaying colors if the word had two of the same letters, but did not have the indicator keyboard at the bottom, so this version
incorporates the best features of both games and cleans up some little nagging issues
$5 - I'm a novice python programmer and this is my first attempt at pygame.  So, if you have better ways of coding this, I would appreciate
your feedback.
