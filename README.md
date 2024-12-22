# **WORDLE**
Personal version of wordle that operates through a set of bash and python scripts

### How to Play
Download the repository with all of the files in the same place. The idea should be that you can click on the file titled 'Wordle' and it will automatically start running through a terminal window. If you run into issues let me know (even if its just a file permissions issue).

Technically, you are able to run the program by just using commands but you have to activate the virtual environment and then run either wordle_**.py file. I can provide the instructions for this by request.

## SETUP
First clone the repository to your device.

```
git clone https://github.com/joegriffin2000/wordle.git
```

After cloning the repository, Create a python virtual environment with this command. Do not change the environment name. 
```
python3 -m venv .venv
source .venv/bin/activate
```

Then, use pip3 to install all necessary modules inside of the virtual environment.
```
pip3 install -r requirements.txt
```

Then, use set the wordle path in your git config to this repository.
```
git config --global wordle.path "$(pwd)"
```

Then you should be good to go! Have Fun!

ps. If you want to, this command deactivates the virtual environment.
```
deactivate
```

### FAQ

**How does this differ from Wordle provided by the New York Times?**
Other than being able to be run within the command line, a new word is chosen for every time you play. Actually, the reason that I made this program in the first place was because I really enjoyed playing wordle and got frustrated that I couldn't play it multiple times a day. This version is kind of built for that purpose. Also, the word list is slightly different as I went through and hand picked the words that I wanted to see as solutions.

**Why is the word list different?**
Sometimes I felt like the words chosen for the wordle game were unfair so I went through and chose words I thought would be fair to my everyday use. I still haven't finished refining the word list so there are a couple words there that I haven't removed as options yet. Blame Stanford. 

**Why are both of the word lists just viewable text files?**
Because I don't care if you view what words are possible solutions. There are over 2800 words in my possible words list and if you want to cheat you can go ahead. Realistically, you are only making the game less fun for yourself anyway.
