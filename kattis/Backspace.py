def translate_less_than_to_backspace(input_str):
    
    for i in input_str:
        if i == "<":
            input_str.pop(input_str.index("<"))

a = "Hej"
print(a.pop(a.index("j")))