abv = "абв"
text = "АбВ рабворста рапрену арпабв мтроснк брпоабвоп"
if abv.lower() in text.lower():
    text_1 = text.lower().replace(abv.lower(), "")
print(text)
print(text_1)
