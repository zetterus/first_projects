import streamlit as st
from pydub import AudioSegment, silence
import speech_recognition as sr
# import os


recog = sr.Recognizer()

st.markdown("<h1 style='text-align: center;'>Audio To Text Converter</h1>", unsafe_allow_html=True)
st.markdown("---")
audio = st.file_uploader("Upload Your File", type=["mp3", "wav"])

if audio:
    st.audio(audio)
    audio_segment = AudioSegment.from_file(audio)
    chunks = silence.split_on_silence(audio_segment, min_silence_len=500, silence_thresh=audio_segment.dBFS-20, keep_silence=100)

    final_result = ""

    for index, chunk in enumerate(chunks):
        chunk.export(str(index) + ".wav", format="wav")
        with sr.AudioFile(str(index) + ".wav") as source:
            recorded = recog.record(source)
            try:
                # Использование оффлайн распознавания с CMU Sphinx
                text = recog.recognize_sphinx(recorded)
                final_result += text + " "
                # st.write(text)
            except sr.UnknownValueError:
                st.write("Sphinx не смог распознать аудио")
                final_result += " Unaudible"
            except sr.RequestError as e:
                st.write(f"Ошибка сервиса Sphinx: {e}")
                final_result += " Unaudible"
    with st.form("Result"):
        result = st.text_area("Text Area", value=final_result)
        d_btn = st.form_submit_button("Download")
        if d_btn:
            # envir_var = os.environ
            # usr_loc = envir_var.get("USERPROFILE")
            loc = "D:\\downloads\\transcript.txt"
            with open(loc, "w") as file:
                file.write(result)


