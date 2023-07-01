messages = ["Enter an equation",
    "Do you even know what numbers are? Stay focused!",
    "Yes ... an interesting math operation. You've slept through all classes, haven't you?",
    "Yeah... division by zero. Smart move...",
    "Do you want to store the result? (y / n):",
    "Do you want to continue calculations? (y / n):",
    " ... lazy",
    " ... very lazy",
    " ... very, very lazy",
    "You are",
    "Are you sure? It is only one digit! (y / n)",
    "Don't be silly! It's just one number! Add to the memory? (y / n)",
    "Last chance! Do you really want to embarrass yourself? (y / n)",
]

def is_one_digit(v):
    output = -10 < v < 10 and v.is_integer()
    return output


def check(v1, v2, v3):
    msg = ''
    if is_one_digit(v1) and is_one_digit(v2):
        msg += messages[6]
    if (v1 == 1 or v2 == 1) and '*' == v3:
        msg += messages[7]
    if (v1 == 0 or v2 == 0) and ['*', '+', 'i'].__contains__(v3):
        msg += messages[8]
    if msg != '':
        print(f"{messages[9]}{msg}")


memory = 0
while True:
    print(messages[0])
    calc = input()
    x, oper, y = calc.split(" ")
    if x == 'M':
        x = memory
    if y == 'M':
        y = memory
    try:
        number_x = float(x)
        number_y = float(y)
    except ValueError:
        print(messages[1])
        continue
    if oper == "+" or oper == "-" or oper == "*" or oper == "/":
        check(number_x, number_y, oper)
        if oper == "+":
            result = number_x + number_y
        elif oper == "-":
            result = number_x - number_y
        elif oper == "*":
            result = number_x * number_y
        elif oper == "/" and number_y != 0:
            result = number_x / number_y
        else:
            print(messages[3])
            continue
        print(result)
        while True:
            print(messages[4])
            answer = input()
            if answer == 'y':
                if is_one_digit(result):
                    msg_index = 10
                    while True:
                        print(messages[msg_index])
                        answer = input()
                        if answer == 'y':
                            if msg_index < 12:
                                msg_index +=1
                            else:
                                memory = result
                                break
                        elif answer == 'n':
                            break
                else:
                    memory = result
                break
            elif answer == 'n':
                break
        while True:
            print(messages[5])
            answer = input()
            if answer == 'y':
                break
            elif answer == 'n':
                exit(0)
    else:
        print(messages[2])
