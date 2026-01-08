from deep_translator import GoogleTranslator

from textblob import TextBlob


with open('tekst.txt', 'r', encoding='utf-8') as plik:
    tekst_z_pliku = plik.read()

tekst_pl = GoogleTranslator(source='auto', target='pl').translate(tekst_z_pliku)
tekst_en = GoogleTranslator(source='auto', target='en').translate(tekst_z_pliku)

analiza = TextBlob(tekst_en)
wynik_emocji = analiza.sentiment.polarity

print("=" * 30)
print("RAPORT ANALIZY TEKSTU")
print("=" * 30)
print(f"Oryginał (FR): {tekst_z_pliku}")
print(f"Tłumaczenie (PL): {tekst_pl}")
print("-" * 30)

if wynik_emocji > 0:
    nastroj = "POZYTYWNY"
elif wynik_emocji < 0:
    nastroj = "NEGATYWNY"
else:
    nastroj = "NEUTRALNY"

print(f"Analiza wydźwięku: {nastroj} (Score: {wynik_emocji})")

with open('raport.txt', 'w', encoding='utf-8') as plik_raportu:
    plik_raportu.write("=== RAPORT ANALIZY LINGWISTYCZNEJ ===\n")
    plik_raportu.write(f"Oryginalny tekst: {tekst_z_pliku}\n")
    plik_raportu.write(f"Tłumaczenie: {tekst_pl}\n")
    plik_raportu.write(f"Ocena emocji: {nastroj} ({wynik_emocji})\n")
    plik_raportu.write("=====================================\n")

print("Sukces! Raport został wygenerowany w pliku raport.txt")