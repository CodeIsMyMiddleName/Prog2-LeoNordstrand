dic = {"Sverige": "Stockholm", "Norge": "Oslo", "Finland": "Helsingfors"}
dic.update({"Danmark": "Köpenhamn"})
print(dic)
dic.pop("Finland")
print(dic)

hej = {"Banan", "Päron", "Äpple"}
då = {"Kiwi", "Annanas", "Päron"}
print(hej)
print(då)
print(hej.union(då)) #Bara ett exemplar av "Päron" finns pga att det inte får finnas mer än en av varje ""data""