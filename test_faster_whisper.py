from faster_whisper import WhisperModel
import time

# Ładowanie modelu Faster Whisper
model = WhisperModel("base")

# Rozpoczęcie pomiaru czasu
start_time = time.time()

# Transkrypcja pliku audio
segments, info = model.transcribe("input.wav")
transcription = " ".join([segment.text for segment in segments])

# Obliczanie czasu wykonania
end_time = time.time()
execution_time = end_time - start_time

# Wyświetlenie wyników
print("Czas wykonania:", execution_time, "sekundy")
print("Tekst:", transcription)
