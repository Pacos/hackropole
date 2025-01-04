from Crypto.Util.strxor import strxor


with open(".resources/clairconnu/output.txt", "r") as f:
    c_flag = bytes.fromhex(f.read().strip())
    print(c_flag)
    key = strxor(c_flag[:4], b"FCSC")
    print(key)
    r_key = key * 1000
    flag = strxor(c_flag, r_key[:len(c_flag)])
    print(flag)