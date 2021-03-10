

english_spanish = {"you":"tu", "can": "puedes", "cut": "cortar", "all": "todas", "the": "las", "flowers": "flores", "but": "pero", "cannot": "no puedes", "keep": "mantener", "spring": "primavera", "from": "desde", "coming": "venir", "I": "yo", "grew": "crecio", "in" : "en", "this": "esta", "city": "ciudad", "my": "mi", "poetry": "poesía", "was": "fue", "born": "nacida", "between": "entre", "hill": "montaña", "and":"y", "river": "rio", "it": "eso", "took": "tomó", "its": "su", "voice": "voz", "rain": "lluvia", "like": "como", "timber": "madera", "stepped": "paró", "itself": "a si mismo", "in": "en", "forest": "bosque"}

# adding words to our dictionary
english_spanish["one"] = "uno"
english_spanish["two"] = "dos"
english_spanish["three"] = "tres"
english_spanish["four"] = "cuatro"
english_spanish["five"] = "cinco"
english_spanish["six"] = "seis"
english_spanish["seven"] = "siete"
english_spanish["eight"] = "ocho"
english_spanish["nine"] = "nueve"
english_spanish["ten"] = "diez"
english_spanish["eleven"] = "once"
# length of the dictionary
print(len(english_spanish))

# words included in the dictionary
for word in english_spanish:
    print(word)

print(english_spanish.get("from"))
print("cut" in english_spanish)
del(english_spanish["eleven"])
print(english_spanish)
