# BriefWise :spiral_notepad: :computer:
<p align="center">
<img src="https://ipfs.io/ipfs/bafybeid3djho5xvdsobutcqfw6cjgmhx2wiwx2i3nb6giil7bozdtiqsgq/logo.png" width="250" alt="Logo" >
  </p>
</br>

## Website Link: https://briefwise.streamlit.app/

## Details : 
**Name** : Harshavardhan Bajoria</br>

**Country of Residence** : India</br>

**College Name** : Amity University Kolkata

**Graduation Year**: 2024

**Experience Level** : Student</br>

## Theme : 
Empowering All with Instant Content Summarization and Sentiment Analysis.

## Problem Statement:
In today's information age, we are bombarded with an overwhelming amount of content on a daily basis. From news articles to social media posts, the sheer volume can make it difficult to stay informed and extract meaningful insights. Additionally, understanding the sentiment behind the content is crucial in comprehending public opinion and making informed decisions. 
* The process of manually summarizing lengthy articles and analyzing sentiment can be time-consuming and daunting for many individuals. 
* People often lack the resources, expertise, or time to perform content summarisation and sentiment analysis effectively.
* People with visual impairments encounter difficulties in consuming lengthy texts as they heavily rely on visual cues for content understanding.
* Existing content summarization and sentiment analysis approaches often overlook the specific needs of people with disabilities, leading to a lack of inclusivity.
* Existing platforms charge a specific fee for downloading the generated content.

## Solution: 💡 
**BriefWise** is a comprehensive solution that addresses the aforementioned problems. With BriefWise individuals can effortlessly summarize and analyze content, enhancing their ability to navigate the information landscape, understand public sentiment, and make informed choices.
* Users can submit their content in .pdf or .txt format, or enter text directly into the application's text area for processing.
* Leveraging Microsoft Azure Cognitive Services, the application utilizes cost-effective methods to summarize the content and analyze sentiment.
* The solution employs the sklearn TfidfVectorizer and spacy library in Python to generate accurate and concise summaries.
* A user-friendly UI/UX, developed using Streamlit, ensures a seamless and intuitive experience for all users.
* Microsoft Azure Text to Speech Cognitive Service is utilized to convert the generated result into an .MP3 file, enabling people with disabilities to listen to the content.
* The application includes an audio player, allowing users to listen to the generated content and download it for future use.
* Users can conveniently download the generated content, facilitating easy access and summarization of large files.
* The solution is designed for speed, simplicity, and user-friendliness, encouraging individuals to stay informed, gain meaningful insights, and make well-informed decisions.

## Tech Stack:
The following tech stacks have been used to create the application and deploy it.  
* **Python** to build the application.
* **Streamlit** to create a responsive web application along with widgets. 
* **Streamlit Community Cloud** to deploy the web application for anyone across the globe to access it. 
* **Microsoft Azure AI Cognitive Service** to summarise the content, and analyze it's sentiment using the pre-trained Azure AI models and OpenAI. 
* **Microsoft Azure Text to Speech Service** to convert the generated text to speech (.mp3) format. 
* **Python Libraries (sklearn, spacy)** to summarise the content with the help of NLP. 
* **GitHub** to host the source code, use the version control (collaboration history) to understand the changes, and go back and forth if required to complete the software. 

## Installation Guide: ⬇️
First, install the following:
* Python

For Linux users:
*Run the following command: 
```bash
sudo apt-get update
sudo apt-get install build-essential libssl-dev ca-certificates libasound2 wget
```

Then, follow this step-by-step process to run this application:
* Get your Azure subscription: https://azure.microsoft.com/free/cognitive-services
* Create an Azure Speech resource: https://azure.microsoft.com/free/cognitive-services
* Create the Azure Language resource: https://aka.ms/languageStudio 
* Travel to the directory where you wish to store the project files using the cd command.
* Clone the repository in your local system.
```bash
git clone https://github.com/HVbajoria/BriefWise
```
* Go to your project directory where all the files are present.
```bash
cd BriefWise
```
* Install the required dependencies to run the project.
```bash
pip install -r requirements.txt
```
* Replace the endpoint and key with your Azure language resource endpoint and key in azuresummarizer.py and azuresentiment.py file. 
* Replace the subscription and region with your Azure speech resource subscription and region in azurespeech.py file.
* Run the application
```bash
streamlit run main.py
```
* Enjoy the app!

## Demo Video Link :movie_camera: : https://youtu.be/HMLu0Ww4my0

## Website Link :globe_with_meridians: : https://briefwise.streamlit.app/

## Methodology :
The methodology for the seamless execution of the whole application is given below. It describes how the application works behind the application to securely fetch, and generate the content. 

#### For summarising and analyzing the sentiment of the document:
<p align="center">
<img src="https://ipfs.io/ipfs/bafybeidt565y6lu6dqhvfm5akbwq6ul3jm532zkge5xebckxphrov7b65m/M1.png" width="520" alt="accessibility text" >
  </p>
  </br>
  
#### For displaying the generated results:
<p align="center">
<img src="https://ipfs.io/ipfs/bafybeib2enndszvl6gnulpimop3kpqq2jyghhl5bepcmzfscwc76kq7i3u/M2.png" width="580" alt="accessibility text" >
  </p>
</br>

#### Complete Application Architecture:
<p align="center">
<img src="https://datasetlegitlens.blob.core.windows.net/dataset/BriefWise%20(1).png?sp=r&st=2023-12-02T08:57:55Z&se=2023-12-02T16:57:55Z&sv=2022-11-02&sr=b&sig=nJVPVJL0ds43%2F3UDh%2FDaevmoTW%2FTQ4QVBk28oUEJjXg%3D" width="980" alt="accessibility text" >
  </p>
</br>

 ## Social Impact / Novelty:
This application will redefine the way we consume knowledge, and make decisions in a fast-paced world with tons of information generated every minute.  
* This will help everyone free their mind and get relaxed and not go through stress, depression which is becoming common nowadays. 
* BriefWise breaks down barriers, ensuring that individuals of all backgrounds and abilities can simplify and understand complex content.
* Leveraging Microsoft Azure Cognitive Services, the solution offers efficient and cost-effective content summarization and sentiment analysis.
* With a streamlined UI developed using Streamlit, BriefWise provides an intuitive and accessible user experience for individuals of varying technical expertise.
* Integration of Microsoft Azure Text-to-Speech Cognitive Service allows users with visual impairments to listen to the generated content, promoting inclusivity.
* BriefWise provides an audio player feature, enabling users to download the generated content as an .MP3 file for convenient access and future reference.
* The application facilitates easy summarization of large files, allowing users to efficiently process extensive amounts of information.
* By simplifying content understanding and sentiment analysis, BriefWise empowers individuals to make informed decisions and engage in meaningful discussions.
* BriefWise fuels curiosity, encouraging users to explore diverse perspectives and think critically about the information they encounter.
* The solution fosters inclusivity, connecting individuals and bridging gaps between information overload, accessibility, and participation.
* Through accessibility and simplified information, BriefWise unlocks the true potential of individuals, empowering them to actively participate in a knowledge-driven society. 

## Future Scope:
The impact of BriefWise extends far beyond its current capabilities, paving the way for an exciting future where information is accessible, insights are abundant, and opportunities for growth are limitless. As we envision the road ahead, here are some key areas where the application can continue to evolve and make a profound difference:
* Expanding BriefWise to support a wider range of languages, ensuring that individuals worldwide can benefit from content summarization and sentiment analysis in their native tongue.
* Continuously integrating state-of-the-art natural language processing techniques and algorithms, enabling even more accurate and nuanced content summaries and sentiment analysis.
* Going beyond text-to-speech, incorporating additional accessibility features such as braille output, enhanced screen reader compatibility, and support for alternative communication methods, further empowering individuals with disabilities.
* Enabling real-time content summarization and sentiment analysis, allowing users to stay updated on evolving topics and emerging trends, providing timely insights for decision-making.
* Introducing customization options that allow users to tailor the summarization and sentiment analysis algorithms to their specific preferences, needs, and domains of interest.
* Seamlessly integrating BriefWise with Internet of Things (IoT) devices and smart assistants, enabling users to access content summaries and sentiment analysis effortlessly through voice commands and interconnected systems.
* Introducing collaborative capabilities, allowing users to share and collaborate on content summaries and sentiment analysis, fostering knowledge exchange and collective intelligence.
* Broadening the range of supported content sources, including social media platforms, scientific articles, industry reports, and more, to cater to diverse information needs across various domains.
* Leveraging advancements in machine learning and deep learning to continually refine and enhance the accuracy, speed, and capabilities of content summarization and sentiment analysis.

With each stride forward, BriefWise will revolutionize the way we consume, analyze, and understand information, empowering individuals, organizations, and societies to unlock their full potential. Together, let's shape the future, where knowledge is accessible, insights are boundless, and the possibilities for growth and innovation are limitless with BriefWise at our side.

### Build with :heart: by Harshavardhan Bajoria 
