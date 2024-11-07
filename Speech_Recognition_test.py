import speech_recognition as sr
import time

# Tworzenie obiektu rozpoznawania mowy
recognizer = sr.Recognizer()

# Rozpoczęcie pomiaru czasu
start_time = time.time()

# Wczytanie pliku audio i transkrypcja
with sr.AudioFile("output.wav") as source:
    audio_data = recognizer.record(source)
    transcription = recognizer.recognize_google(audio_data)  # Można użyć innej usługi

# Obliczanie czasu wykonania
end_time = time.time()
execution_time = end_time - start_time

# Wyświetlenie wyników
print("Czas wykonania:", execution_time, "sekundy")
print("Tekst:", transcription)
