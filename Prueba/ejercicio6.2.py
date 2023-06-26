def text_to_number(text):
    text_to_number_dict = {"un": 1, "dos": 2, "tres": 3, "cuatro": 4, "cinco": 5, 
                           "seis": 6, "siete": 7, "ocho": 8, "nueve": 9, "diez": 10, 
                           "once": 11, "doce": 12}
    number_text = text.split()[0]
    return text_to_number_dict[number_text]

def order_verses(verses):
    return sorted(verses, key=text_to_number, reverse=True)

verses = ["10 señores un salto,", 
          "El dia 12 de Navidad mi verdadero amor me dio",
          "3 gallinas francesas,", 
          "8 criadas un ordeño,", 
          "1 perdiz en un peral.",
          "6 gansos una puesta,", 
          "5 anillos de oro,", 
          "9 damas bailando,", 
          "4 pájaros cantando,", 
          "7 cisnes nadando,", 
          "tubería de 11 gaiteros,", 
          "2 tórtolas y"]

ordered_verses = order_verses(verses)

for verse in ordered_verses:
    print(verse)
