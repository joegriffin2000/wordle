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

st.title("Wordle")

#function for incrementing the level count
def setCount():
    st.session_state['count'] = st.session_state['count'] + 1 if 'count' in st.session_state.keys() else 1

def getMatchString(RandomWord,userWord):
    matchString=[":grey",":grey",":grey",":grey",":grey"]

    for i in range(0,len(RandomWord)):
        if RandomWord[i] == userWord[i]:
            matchString[i] = ":green"
        elif (RandomWord.count(userWord[i]) > 0):
            matchString[i] = ":orange"
        
        matchString[i]+=f"[{userWord[i]}]"
    
    return matchString

guess_box = st.container(border=True, height=70 * MAX_ROUND_NUM)
column_size_designation = [2] + [3]*WORD_COUNT
rows = [guess_box.columns(column_size_designation)] * MAX_ROUND_NUM

if 'solution' not in st.session_state.keys():
    st.session_state['solution'] = ListOfWords[random.randint(0,len(ListOfWords))]

user_guess = st.text_input( 
            label="guess-box",
            key='guess-box',
            on_change=setCount,
            max_chars = WORD_COUNT,
            value = None,
            placeholder = "Guess Here",
            label_visibility="collapsed")

if user_guess in AllWordsStanford or user_guess == None:
    if 'guesses' in st.session_state.keys():
        st.session_state.update({"guesses": st.session_state['guesses'] + [getMatchString(st.session_state['solution'],user_guess.lower())]})
    elif user_guess != None:
        st.session_state['guesses'] = [getMatchString(st.session_state['solution'],user_guess.lower())]
    else:
        st.session_state['guesses'] = []

    for i in range(len(st.session_state['guesses'])):
        st.session_state['guesses'][i] = [st.session_state['guesses'][i][j][:-3] + st.session_state['guesses'][i][j][-3:].upper() for j in range(len(st.session_state['guesses'][i]))]
else:
    st.session_state['count'] = st.session_state['count']-1
    st.toast("INVALID WORD CHOICE")

if 'count' in st.session_state.keys() and st.session_state['count'] <= MAX_ROUND_NUM: 
    for j in range(st.session_state['count']):
        for i in range(1,WORD_COUNT+1):
            rows[j][i].subheader(st.session_state['guesses'][j][i-1])

if ('solution' in st.session_state.keys() and 
    'count' in st.session_state.keys() and 
    'guesses' in st.session_state.keys()):
    if user_guess == st.session_state['solution']:
        st.toast("Victory!")
        st.success("The Word Was " + st.session_state['solution'])
    elif st.session_state['count'] == MAX_ROUND_NUM:
        st.toast("Too Bad!")
        st.error("The Word Was " + st.session_state['solution'])