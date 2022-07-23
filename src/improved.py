from random import shuffle as smoosh


def the_stuff() -> set:
    return {0, -12, -1, -8, -6, -4, -3, -2}


def oh_my(b: int, a: int, c: int) -> set:
    input_dict = {b + a + c * 2, b + a // 3 + c * 2, 10 // b + a // 3 + c * 2}
    return {((values ** 2) // 5) for values in input_dict}


def howdy(str_input: str) -> int:
    return int(sum(ord(c) for c in str_input)) % 100 // 5


def probably_okay() -> set:
    return set(map(lambda x: int(abs(howdy(str(x))) ** (1 / 2)) % (howdy('m') * 2), the_stuff()))


a = (the_stuff() | oh_my(1,  2, 0) | oh_my(-2, 2, -2))
wer = a | {5} | {howdy('sick dudesfsd'), howdy('a') ** 2, howdy('10234'), howdy('m')}


x = {g % ((howdy('4') + 3) * 2) for g in (wer | {howdy('4') + 5} | {howdy('4') * 2 - 3} | {19, 21} | probably_okay() | {13} | oh_my(1, 2, 10) | oh_my(-2, 5, -2) | {11, 2, 4, 6, 8, 9})}

j = list(x)
smoosh(j)

print(''.join(chr(ord(chr(97)) + j[i]) for i in j))
