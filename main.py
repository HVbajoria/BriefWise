import re
from sentiment import analyze_sentiment
import streamlit as st
from io import StringIO
from pdf_txt import pdf_to_text
from summarizer1 import summarizer
from summarizer2 import generate_summary
from pathlib import Path
import os
from PyPDF2 import PdfReader
import numpy as np
from text2speech import speech_mp3_generator

st.set_page_config(page_title="BriefWise", page_icon="📝", layout="centered")

left_co, cent_co,last_co = st.columns(3)
with cent_co:
    st.image("logo.png", width=200)
st.markdown("<h1 style='text-align: center;'>BriefWise</h1>",
            unsafe_allow_html=True)


file = st.file_uploader("Please choose a file", type=['txt', 'pdf'])
st.markdown("<h5 style='text-align: center;'>OR</h5>", unsafe_allow_html=True)
text = st.text_area("Input Text For Summary", height=200)
sentimenter = st.checkbox("Analyze Sentiment")
col1,  col2, col3 = st.columns(3)
if col1.button('SUMMARIZE'):
    #try:
        if file is not None:
            if bool(text)== True:
                st.error("ERROR: YOU CAN'T ENTER BOTH", icon="🚨")
                st.stop()
            else:
                st.snow()
                st.success('Results Generating below ....!', icon="✅")
                if file.name[-3:] == "pdf":
                    pdfReader = PdfReader(file)
                    num = len(pdfReader.pages)
                    for i in range(0,num):
                        pageobj = pdfReader.pages[i]
                        resulttext = pageobj.extract_text()
                        text = text.join(resulttext)
                        text = re.sub(r'(?<=\S)\s{2,}(?=\S)', ' ', text)
                        text = re.sub(r'\n', ' ', text)
                   

                else:
                    stringio = StringIO(file.getvalue().decode("utf-8"))
                    text=stringio.read()
    
        textfile = open("content.txt","w")
        textfile.write(text)
        textfile.close()

        # To generate sentiment
        sentiment = analyze_sentiment("content.txt")
        if sentimenter:
            st.markdown("<h3> Sentiment : </h3>" ,  unsafe_allow_html=True)
            st.write(sentiment)

        # To generate summarize
        summary1=summarizer(text)
        summary2=generate_summary("content.txt")
        st.markdown("<h2> Your Summary : </h2>" ,  unsafe_allow_html=True)        
        st.markdown("<h3> > Summary 1 : </h3>" ,  unsafe_allow_html=True)                                
        st.write(summary1)
        st.markdown("<h3> > Summary 2 : </h3>" ,  unsafe_allow_html=True)
        st.write(summary2)

        # To generate output text file
        textfile = open("output.txt","w")
        text = "Sentiment of the document: "+sentiment+"\n\nSummary 1:\n"+summary1+"\n\nSummary 2:\n"+summary2
        textfile.write(text)
        textfile.close()

        # To show audio
        with open("output.txt", 'r') as file:
            text_to_speak = file.read()
        tts = gTTS(text=text_to_speak, lang='en')
        tts.save("outputaudio.mp3")
        audio_file = open('outputaudio.mp3', 'rb')
        audio_bytes = audio_file.read()
        st.audio(audio_bytes, format='audio/,mp3')

        # Download buttons
        # Download text file
        with open('output.txt', 'r') as file:
            output = file.read()
        st.download_button(
        label="Download Text",
        data=output,
        file_name='output.txt',
        help="To download a text file of the generated results"
        )

        # Download mp3 file
        with open('outputaudio.mp3', 'rb') as file:
            output = file.read()
        
        st.download_button(
        label="Download Audio",
    data=output,
    file_name='output.mp3',
    mime="audio/mpeg",
    help="To download an audio file of the generated results"
)
