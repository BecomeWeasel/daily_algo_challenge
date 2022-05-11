def solution(new_id):
    answer = ""

    alphabet = {
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
    }
    num = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}
    char = {"-", "_", "."}

    def solve(s):
        nonlocal alphabet, num, char
        s = s.lower()
        n_s = ""

        for i, c in enumerate(s):
            if c in alphabet or c in num or c in char:
                n_s += c

        prev = ""

        s = n_s
        counter = 0
        n_s = ""
        for idx, c in enumerate(s):
            # 첫 . 등장
            if c == "." and prev != ".":
                n_s += c
                prev = "."
            elif c == "." and prev == ".":
                continue
            elif c != ".":
                n_s += c
                prev = c
        s = "".join(map(str, n_s))

        s = list(s)

        if s[0] == ".":
            del s[0]

        # if len(s)!=0 and s[-1]=='.':
        #     del s[-1]

        if len(s) == 0:
            s = ["a"]

        if len(s) >= 16:
            s = s[:15]

        if s[-1] == ".":
            del s[-1]

        if len(s) <= 2:
            last_char = s[-1]

            while len(s) < 3:
                s = s + [last_char]

        return "".join(map(str, s))

    return solve(new_id)
