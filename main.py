import os


def usun_polskie_znaki(tekst):
    mapa = str.maketrans({
        'ą': 'a', 'ę': 'e', 'ć': 'c', 'ł': 'l', 'ó': 'o',
        'ż': 'z', 'ź': 'z', 'ń': 'n', 'ś': 's',
    })
    return tekst.lower().translate(mapa).replace(',','').replace('.','')


def get_wav_files(path: str):
    wav_map = {}
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.lower().endswith('.wav'):
                file_name_only = os.path.splitext(file)[0]
                clean_key = usun_polskie_znaki(file_name_only)

                if clean_key in wav_map:
                    print(f"Uwaga: Klucz '{clean_key}' już istnieje! (Plik: {file})")

                wav_map[clean_key] = os.path.join(root, file)
    return wav_map


input_text = input("Podaj tekst ogłoszenia: ")
audio_map = get_wav_files("./audio")

# 1. Czyścimy cały tekst wejściowy
clean_text = usun_polskie_znaki(input_text)
words = clean_text.split()


wav_files_in_order = []
i = 0
while(i<len(words)):
    found = False

    for length in [3,2,1]:
        if i+ length <= len(words):
            phrase = "_".join(words[i:i + length])
            if phrase in audio_map:
                wav_files_in_order.append(audio_map[phrase])
                i += length
                found = True
                break


    if not found: i+=1


print(wav_files_in_order)