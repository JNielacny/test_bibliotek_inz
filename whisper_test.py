import whisper
import time

# Ładowanie modelu Whisper
model = whisper.load_model("base")

# Rozpoczęcie pomiaru czasu
start_time = time.time()

# Transkrypcja pliku audio
result = model.transcribe("input.wav")

# Obliczanie czasu wykonania
end_time = time.time()
execution_time = end_time - start_time

# Wyświetlenie wyników
print("Czas wykonania:", execution_time, "sekundy")
print("Tekst:", result["text"])
