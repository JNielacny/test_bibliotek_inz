Ten projekt umożliwia transkrypcję audio (mowy) na tekst za pomocą trzech różnych bibliotek:

Whisper (opracowany przez OpenAI)
Faster Whisper (optymalizowana wersja Whisper)
SpeechRecognition (interfejs do kilku zewnętrznych API)

Instalacja
1. Stworzenie Środowiska Wirtualnego (Zalecane)

Stwórz i aktywuj środowisko wirtualne, aby łatwiej zarządzać zależnościami:

$python -m venv venv\
$.\venv\Scripts\Activate

2. Instalacja Wymaganych Bibliotek:

$pip install openai-whisper\
$pip install faster-whisper\
$pip install SpeechRecognition

3. Wymagania CUDA i cuDNN (dla Faster Whisper)

CUDA: Pobierz i zainstaluj CUDA Toolkit w wersji kompatybilnej z twoją kartą graficzną.
cuDNN: Pobierz i zainstaluj bibliotekę cuDNN, która jest zgodna z wersją CUDA. Skopiuj pliki cuDNN (np. cudnn_ops64_9.dll) do katalogu instalacyjnego CUDA i dodaj go do zmiennej PATH systemu.

4. Użycie

Obowiązkowe jest stworzenie nagrania input.wav w języku angielskim i zapisanie go w katalogu projektu.
