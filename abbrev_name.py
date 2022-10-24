def abbrev_name(name):
    split_name = name.split(" ")
    get_first_char =split_name[0][0]+"." + split_name[1][0].upper()
    return get_first_char
print(abbrev_name(name="Sam Harris")) # Forventet svar S.H