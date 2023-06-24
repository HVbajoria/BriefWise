import subprocess
import azure.cognitiveservices.speech as speechsdk
from pydub import AudioSegment
import azure.cognitiveservices.speech as speechsdk

def speech_mp3_generator(file_path):
    # Creates an instance of a speech config with specified subscription key and service region.
    speech_config = speechsdk.SpeechConfig(subscription=st.secrets["subscription_key"], region=st.secrets["region"])
    # Sets the synthesis output format.
    # The full list of supported format can be found here:
    # https://docs.microsoft.com/azure/cognitive-services/speech-service/rest-text-to-speech#audio-outputs
    speech_config.set_speech_synthesis_output_format(speechsdk.SpeechSynthesisOutputFormat.Audio16Khz32KBitRateMonoMp3)
    # Creates a speech synthesizer using file as audio output.
    # Replace with your own audio file name.
    file_name = "outputaudio.mp3"
    file_config = speechsdk.audio.AudioOutputConfig(filename=file_name)
    speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=file_config)

    # Input text to be converted to speech
    with open(file_path, 'r') as file:
        text_to_speak = file.read()
    result = speech_synthesizer.speak_text_async(text_to_speak).get()

    # # Check result
    # if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
    #     print("Speech synthesized for text [{}], and the audio was saved to [{}]".format(text_to_speak, file_name))        
    # elif result.reason == speechsdk.ResultReason.Canceled:
    #     cancellation_details = result.cancellation_details
    #     print("Speech synthesis canceled: {}".format(cancellation_details.reason))
    #     if cancellation_details.reason == speechsdk.CancellationReason.Error:
    #         print("Error details: {}".format(cancellation_details.error_details))