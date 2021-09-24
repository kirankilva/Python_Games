# Python | Program to implement simple FLAMES game

FLAMES is a popular game named after the acronym: Friends, Lovers, Affectionate, Marriage, Enemies, Sibling. This game does not accurately predict whether or not an individual is right for you, but it can be fun to play this with your friends.

### There are few steps in this game:
1. Take the two names.
2. Remove the common characters with their respective common occurrences.
3. Get the count of the characters that are left .
4. Take FLAMES letters as [“Friends”, “Love”, “Affection”, “Marriage”, “Enemy”, “Siblings”]
5. Start removing letter using the count we got.
6. The letter which last the process is the result.

### Example
INPUT:                                                                                                                                                                              
Enter the name: kiran                                                                                                                                                                
Enter the name: kilva                                                                                                                                                                
OUTPUT:                                                                                                                                                                              
Relationship Status : Enemy

### Explanation
In above given two names K, I and A are common letters which are occurring one time(common count) in both names so we are removing these letters from both names. Now count the total letters that are left here it is 4. Now start removing letters one by one from FLAMES using the count we got and the letter which lasts the process is the result.

Counting is done in anti-clockwise circular fashion.
