#wordle dupe
#by joegriffin2000
import random
import os
import streamlit as st

WORDLIST_DIR = "word_lists"
SOLUTIONS_FILE = os.path.join(WORDLIST_DIR,"JoeWordList.txt")
POSSIBILITIES_FILE = os.path.join(WORDLIST_DIR,"StanfordWordList.txt")

MAX_ROUND_NUM=6
WORD_COUNT=5

#loading list of all possible solution words
with open(SOLUTIONS_FILE,"r") as f:
    ListOfWords = f.read().split()

#loading list of all possible guess words
with open(POSSIBILITIES_FILE,"r") as f:
    AllWordsStanford = f.read().split()

#placing of the solution in the session state
if 'solution' not in st.session_state.keys():
    st.session_state['solution'] = ListOfWords[random.randint(0,len(ListOfWords))]

#function for incrementing the level count
def setCount():
    st.session_state['count'] = st.session_state['count'] + 1 if 'count' in st.session_state.keys() else 1

#function for added guesses into the session state
def addGuess(guess):
    if 'guesses' in st.session_state.keys():
        st.session_state.update({"guesses": st.session_state['guesses'] + [getMatchString(st.session_state['solution'],guess.lower())]})
    elif guess != None:
        st.session_state['guesses'] = [getMatchString(st.session_state['solution'],guess.lower())]
    else:
        st.session_state['guesses'] = []

#Dialog Boxes for either winning or losing
@st.dialog("Defeat!")
def isLose(roundNum):
    st.error(f"Too Bad! The Word Was {st.session_state['solution'].capitalize()}")
@st.dialog("Victory!")
def isWin(roundNum):
    match roundNum:
        case 1:
            st.header("Hole in One")
        case 2:
            st.header("Eagle")
        case 3:
            st.header("Birdie")
        case 4:
            st.header("Par")
        case 5:
            st.header("Bogey")
        case _:
            st.header("Double Bogey")
    st.success(f"Congrats! The Word Was {st.session_state['solution'].capitalize()}")
    
#Used for creating the characters that will show up in the main screen
def getMatchString(RandomWord,userWord):
    matchString=[":grey",":grey",":grey",":grey",":grey"]

    for i in range(0,len(RandomWord)):
        if RandomWord[i] == userWord[i]:
            matchString[i] = ":green"
        elif (RandomWord.count(userWord[i]) > 0):
            matchString[i] = ":orange"
        
        matchString[i]+=f"[{userWord[i]}]"
    
    return matchString

#Start of the actual streamlit code (at least the stuff that shows up on screen)
st.title("Wordle")

guess_box = st.container(border=True, height=70 * MAX_ROUND_NUM)
column_size_designation = [2] + [3]*WORD_COUNT
rows = [guess_box.columns(column_size_designation)] * MAX_ROUND_NUM

#text input that allows the player to submit guesses
user_guess = st.text_input( 
            label="guess-box",
            key='guess-box',
            on_change=setCount,
            max_chars = WORD_COUNT,
            value = None,
            placeholder = "Guess Here",
            label_visibility="collapsed")

#handling user guesses
if user_guess in AllWordsStanford or user_guess == None:
    addGuess(user_guess)
    for i in range(len(st.session_state['guesses'])):
        st.session_state['guesses'][i] = [st.session_state['guesses'][i][j][:-3] + st.session_state['guesses'][i][j][-3:].upper() for j in range(len(st.session_state['guesses'][i]))]
else:
    st.session_state['count'] = st.session_state['count']-1
    st.toast("INVALID WORD CHOICE")

#if the count exists in the session state and its less than max round number > print guesses on the main screen
if 'count' in st.session_state.keys() and st.session_state['count'] <= MAX_ROUND_NUM: 
    for j in range(st.session_state['count']):
        for i in range(1,WORD_COUNT+1):
            rows[j][i].subheader(st.session_state['guesses'][j][i-1])

#End Game Checker (only triggers if a solution, word count and guesses exists in the session state)
if ('solution' in st.session_state.keys() and 
    'count' in st.session_state.keys() and 
    'guesses' in st.session_state.keys()):
    if user_guess == st.session_state['solution']:
        isWin(st.session_state['count'])
    elif st.session_state['count'] == MAX_ROUND_NUM:
        isLose(st.session_state['count'])
    else:
        pass
