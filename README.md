# wordle-game

If you have fun playing wordle game checkout https://www.nytimes.com/games/wordle/index.html and if like it so much 
that you want no limitaions in playing it (which I do) there's something for you!
By the way if you want to know what is the logic of the game chckout [wiki](https://en.wikipedia.org/wiki/Wordle)

This script uses python3 and tkinter as UI which you can install it in linux via 
```
sudo apt-get install python3-tk -y # and the same package if you are on a redhat or arch based ditro!
```
As soon as you execute the script using python, it will spawn a window (which comes from tkinter) so you can guess the
word and get feedback until you reach the word (or not!) 
![Screenshot from 2025-01-24 19-30-25](https://github.com/user-attachments/assets/bde8886c-1b85-411f-8a5f-95b2fc5ad976)

for example you can see up here it took me 4 guesses to reach the word "humps" (because i have another script which helps me solve wordle game you can visit it [here](https://github.com/seyedalialetaha/wordle-resolver)
every guess if entered the game provides me feedback
green: if the character was in the right place
yellow: if the character was present in the word but not in the right place
black: if the character wasnt there at all
Fell free to play with it and reposrt any issues and also have fun!
