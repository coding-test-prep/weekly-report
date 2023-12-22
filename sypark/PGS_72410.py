import string

def solution(new_id):
    
    new = list(new_id)

    upper = string.ascii_uppercase
    lower = string.ascii_lowercase
    allowed_char = ["-", "_", "."]
    sp_char = string.punctuation

    for n in range(len(new)):
        for i in range(len(upper)):
            if new[n] == upper[i]:
                new[n] = lower[i]
        for i in range(len(sp_char)):
            if new[n] == sp_char[i]:
                if sp_char[i] in allowed_char:
                    pass
                else:
                    new[n] = ""

    answer = "".join(new)

    while ".." in answer:
        answer = answer.replace("..", ".")
            

    if answer == ".":
        answer = ""
    
    try:
        while answer[0] == ".":
            answer = answer[1:]
        while answer[-1] == ".":
            answer = answer[:-1]
    except IndexError:
        answer = answer

    if not answer:
        answer = answer + ("a")

    if len(answer) >= 16:
        answer = answer[:15]

    if len(answer) > 1:
        while answer[-1] == ".":
            answer = answer[:-1]

    while len(answer) <= 2:
        answer = answer + answer[-1]

    return answer