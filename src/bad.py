import random
import string


def the_stuff() -> set:
    return {0, -12, -1, -8, -6, -4, -3, -2}


def oh_my(b: int, a: int, c: int) -> set:
    input_dict = {b + a + c * 2, b + a // 3 + c * 2, 10 // b + a // 3 + c * 2}
    return {((values**2) // 5) for values in input_dict}


def howdy(str_input: str) -> int:
    return int(sum(ord(c) for c in str_input)) % 100 // 5


def probably_okay() -> set:
    return set(
        map(
            lambda x: int(abs(howdy(str(x))) ** (1 / 2)) % (howdy("m") * 2), the_stuff()
        )
    )


def generate_random_alphabet() -> str:
    alphabet = list(string.ascii_lowercase)
    random.shuffle(alphabet)
    return "".join(alphabet)


if __name__ == "__main__":
    print(generate_random_alphabet())
