from dataclasses import dataclass

from Crypto.Util.number import long_to_bytes

@dataclass
class RSA:
    n: int
    e: int
    c: int


def parse_file(filename) -> RSA:
    with open(filename) as f:
        n = e = c = 0
        for idx, line in enumerate(f):
            match idx:
                case 0:
                    n = int(line[4:])
                case 1:
                    e = int(line[4:])
                case 2:
                    c = int(line[4:])
                case _:
                    pass
        return RSA(n=n, e=e, c=c)


if __name__ == '__main__':
    rsa = parse_file("resources/adversarial/output.txt")
    # https://en.wikipedia.org/wiki/RSA_(cryptosystem)
    # since only one prime coefficient was used, we know that lambda(n) = n-1
    # that gives us an easy reverse compute of the private key :
    pkey = pow(rsa.e, -1, rsa.n-1)
    # then we only need to decypher the text as usually done when in possession
    # of the private key
    message = long_to_bytes(pow(rsa.c, pkey, rsa.n))
    print(message)