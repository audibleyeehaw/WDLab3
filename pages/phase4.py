import streamlit as st
import pandas as pd
import Marvel_API as marv
import random
import requests as r
from PIL import Image
from io import BytesIO


def description():
    st.header("Superhero API")
    st.write(marv.description)
    st.write('---')
    
description()

character = 0
def character_generation():
    base = "https://superheroapi.com/api/0831848928b7f77eef4f2137eaf00029/"
    vowels = ['a', 'e', 'i', 'o', 'u']
    name = st.text_input("What's your name?")

    if st.button('Generate Character'):
        first = name[0].lower()
        if first in vowels:
            charID = str(random.randrange(1, 250))
            response = r.get(base + charID)
            supers = response.json()
            picture = supers['image']['url']
            img = Image.open(r.get(picture, stream = True).raw)
            img.show()
            character = supers['id']
            st.write(supers['name'])
        else:
            charID = str(random.randrange(250, 501))
            response = r.get(base + charID)
            supers = response.json()
            picture = supers['image']['url']
            img = Image.open(r.get(picture, stream = True).raw)
            img.show()
            character = supers['id']
            st.write(supers['name'])

character_generation()

def powerGuesser():
    userGuess = st.number_input("Guess the power level?", value = None, placeholder = "0")
    if userGuess:
        base = "https://superheroapi.com/api/0831848928b7f77eef4f2137eaf00029/"
        response = r.get(base + str(character) + "/powerstats" )
        charDict = response.json()
        st.write(powerLevel)
        if powerLevel:
            if powerLevel > userGuess:
                st.write("You're stronger than that!")
            elif powerLevel < userGuess:
                st.write("You've got to start training!")
            else:
                st.write("Wow! Good guess!")
            
        
powerGuesser()


