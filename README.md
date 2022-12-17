# BlackJack
Python Blackjack with gui

This was part of a personal project in Programming 1: Introduction TIE-02101 2019

_The comments in the python file will be in Finnish!_

This is a simple version of the game blackjack. You can only either "Stand" to reveal the dealers cards or "Hit" to give you one more card. The goal is to get as close as possible to card sum value 21.

The cards have values of (A=1 tai A=11)* 2=2 3=3 4=4 5=5 6=6 7=7 8=8 9=9 10=10 J=10 Q=10 K=10
*A value is 11 if the upcoming sum will be 21 or less, 1 otherwise.

Cases:
- If the dealer gets closer to 21 than you, the dealer wins
- You win if you get closer to 21 than the dealer
- You lose automatically if you go over 21
- You win if the dealer busts but you have value of 21 or below
- In case of a tie, the dealer wins unless you both get a blackjack and you have fewer cards.

## How to run
Make sure that the folder Cards/ and the python file Blackjack.py are in the same folder and the Cards/ folder include the card graphics.

*python Blackjack.py* should get things running.
