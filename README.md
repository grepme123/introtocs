# Content
This repository contains the programming assignments I completed for the **Introduction to Computer Science** course.  
The assignments cover fundamental programming concepts, problem-solving strategies, and hands-on practice with Python.  

The goal of this repository is to document my progress throughout the course and provide working implementations of each assignment.  

## Assignments  

- **Assignment 1 – Joker Twins**
  
  Joker Twins is a modified version of the classical Memory game that requires observation, concentration and a good memory to win. The game is also known as Concentration, Pelmanism, Shinkei-suijaku, Pexeso and Pairs.

  Here, the Joker Twins game is a two-player game and is played on a two-dimensional board where the memory cards are represented as letters. That is, the "twins" are the upper and lower case of letters, for example "A" and "a". Each card and its twin are randomly placed on the board and hidden from the players. The two players take turns to turn over two cards in each turn. If the two cards have the same letter (upper and lower case), then the player "keeps" the cards, the cards will be removed from the game, and the player continues playing until two cards are turned over that are not twins. In that case, the cards will turn face down again and the game continues with the other player's turn. The winner is the player with the most cards (i.e. twins) when no cards are left in the game.

  What sets the Joker Twins game apart from the classical memory game is that the game contains Joker cards that are added to the other cards. The Joker card, once turned over by a player, forms a twin with the next or previous turned over card. As a result, both cards comprising the twin plus the Joker will be turned over and 2 points are added to the player's score (1 for the twin cards + 1 for the Joker). Once a Joker card is utilized, it will also be removed from the board. In case all twins have been turned over and only one Joker remains on the board, this Joker will automatically be turned over and counts as 1 point towards the score of the last player that turned over the last twin.

- **Assignment 2 – Connect 4**
  
  Connect 4 is a simple board game for multiple players. The goal of this assignment is to implement the Connect 4 game in Python3. This will give you practice in working with lists, decision structures, loops, functions, and other concepts learnt in class. Additionally, it is a good exercise in decomposing larger problems into smaller and more
manageable parts.

  Connect 4 is typically a two player game and is played on a two-dimensional board with 7 columns and 6 rows. The players take turns by dropping their checker into a column of the board. The checkers fall straight down, occupying the lowest available space within the column. The first player who gets 4 checkers in a row - horizontally, vertically or diagonally - wins the game.

