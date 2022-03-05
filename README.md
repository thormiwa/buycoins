# buycoins
This is the solution for the Buycoins engineering challenge
## Pure Levenshtein Distance algorithm vs Damerau–Levenshtein Distance algorithm
The Pure Levenshtein computes the distance taking three possible ways into account, insertions, deletions or substitutions, of single characters.
For example it calculates the distance between two strings "moth" and "mother", The distance between those strings is 2, the Pure Levenshtein allows us to add "th" to make those strings equal and i understand it helps us solve the problem of when users accidentally miss a letter or two due to human error.

Damerau–Levenshtein Distance algorithm does the same thing but it goes further to add a fourth way, the ability to account for transposition of two adjacent characters, as a possible step. for example the edit distance between two strings "a cat" and "an abct" is 4, using the Damerau–Levenshtein we can add and transpose/swap some characters in those strings to make them equal.
