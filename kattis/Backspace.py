def translate_less_than_to_backspace(input_str):
    
    input_list = list(input_str)

    # Hoppas han inte trycker backspace innan nån annan karaktär...
    for i in input_str:

        if i == "<":
            input_list.pop(input_list.index("<") - 1)
            input_list.pop(input_list.index("<"))
    
    output_str = "".join(input_list)

    return output_str

print(translate_less_than_to_backspace("Din<< internet<<<<<<< hej< på< dig < <<"))

