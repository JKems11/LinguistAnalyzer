from deep_translator import GoogleTranslator

from textblob import TextBlob

tekst_od_użytkownika = input("Wpisz zdanie w dowolnym języku: ")

tekst_en = GoogleTranslator(source='auto', target='en').translate(tekst_od_użytkownika)
tekst_pl = GoogleTranslator(source='auto', target='pl').translate(tekst_od_użytkownika)

analiza = TextBlob(tekst_en)
emocje = analiza.sentiment.polarity

print("-" * 30)
print(f"Tłumaczenie: {tekst_pl}")

if emocje > 0:
    wynik_opisowy = "POZYTYWNY"
elif emocje < 0:
    wynik_opisowy = "NEGATYWNY"
else:
    wynik_opisowy = "NEUTRALNY"

print(f"Wydźwięk tekstu: {wynik_opisowy} (Wynik: {emocje})")