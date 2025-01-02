
def pos(char: str):
    return ord(char[0]) - 65

def decrypt(message: str, key: str) -> str:
    message = message.upper()
    result = ""
    for idx, char in enumerate(message):
        if char.isalpha():
            cur_key = key[idx % len(key)]
            result += chr((pos(char) - pos(cur_key)) % 26 + 65)
        else:
            result += char
    return result

if __name__ == '__main__':
    message = """
    Gqfltwj emgj clgfv ! Aqltj rjqhjsksg ekxuaqs, ua xtwk
    n'feuguvwb gkwp xwj, ujts f'npxkqvjgw nw tjuwcz
    ugwygjtfkf qz uw efezg sqk gspwonu. Jgsfwb-aqmu f
    Pspygk nj 29 cntnn hqzt dg igtwy fw xtvjg rkkunqf.
    """
    key = "FCSC"
    print(decrypt(message, key))