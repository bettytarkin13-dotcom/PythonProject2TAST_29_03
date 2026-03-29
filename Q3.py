def snake_to_camel(text:str)->str:
    if not text:
        return ""
    parts = text.split('_')
    return parts[0]+''.join(word.capitalize() for word in parts[1:])


print(snake_to_camel("hello_python"))
print(snake_to_camel("my_variable_name"))
print(snake_to_camel("python"))
print(snake_to_camel("a_b_c_d"))