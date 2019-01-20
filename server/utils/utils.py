def pseudo_byte_to_int(byte_value):
    str_value = ""

    for char in str(byte_value):
        if char not in ['b', '\'']:
            str_value += char

    return float(str_value)
