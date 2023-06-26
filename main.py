import re
from azuresentiment import analyze_sentiment
import streamlit as st
from io import StringIO
from pdf_txt import pdf_to_text
from summarizer1 import summarizer
from azuresummarizer import generate_summary
from pathlib import Path
import os
from PyPDF2 import PdfReader
import numpy as np
from azurespeech import speech_mp3_generator
from gtts import gTTS

st.set_page_config(page_title="BriefWise", page_icon="📝", layout="centered")

# Header styling
def gradient_text(text, color1, color2):
    gradient_css = f"""
        background: -webkit-linear-gradient(left, {color1}, {color2});
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: bold;
        font-size: 42px;
    """
    return f'<span style="{gradient_css}">{text}</span>'

color1 = "red"
color2 = "blue"
text = "BriefWise"

left_co, cent_co,last_co = st.columns(3)
with cent_co:
    st.image("logo.png", width=200)
styled_text = gradient_text(text, color1, color2)
st.write(f"<div style='text-align: center;'>{styled_text}</div>", unsafe_allow_html=True)



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

# Adding a footer
footer="""<style>
a:link , a:visited{
color: blue;
background-color: transparent;
text-decoration: underline;
}

a:hover,  a:active {
color: red;
background-color: transparent;
text-decoration: underline;
}

.footer {
position: fixed;
left: 0;
bottom: 0;
width: 100%;
background-color: white;
color: black;
text-align: center;
}
</style>
<div class="footer">
<p>Developed with ❤️ by <a style='display: inline; text-align: center;' href="https://www.linkedin.com/in/harshavardhan-bajoria/" target="_blank">Harshavardhan Bajoria</a></p>
</div>
"""
st.markdown(footer,unsafe_allow_html=True)
