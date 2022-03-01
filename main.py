#  You can experiment here, it won’t be checked

def isDigitFloat(x):
    try:
        float(x)
        return True
    except ValueError:
        return False

def isDigitInt(x):
    try:
        int(x)
        return True
    except ValueError:
        return False

def check(v1, v2, v3):
    msg = ""
    if is_one_digit(v1) and is_one_digit(v2):
        msg = msg + msg_[6]
    if (v1 == 1 or v2 ==1) and v3 == "*":
        msg = msg + msg_[7]
    if (v1 == 0 or v2 ==0) and (v3 == "*" or v3 == "+" or v3 == "-"):
        msg = msg + msg_[8]

    if msg != "":
        msg = msg_[9] + msg
        print(msg)



def is_one_digit(v):
    if v > -10 and v < 10 and v.is_integer():
        output = True
    else:
        output = False
    return output

msg_ = []

msg_.append("")
msg_[0] = "Enter an equation"

msg_.append("")
msg_[1] = "Do you even know what numbers are? Stay focused!"

msg_.append("")
msg_[2] = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"

msg_.append("")
msg_[3] = "Yeah... division by zero. Smart move..."

msg_.append("")
msg_[4] = "Do you want to store the result? (y / n):"

msg_.append("")
msg_[5] = "Do you want to continue calculations? (y / n):"

msg_.append("")
msg_[6] = " ... lazy"

msg_.append("")
msg_[7] = " ... very lazy"

msg_.append("")
msg_[8] = " ... very, very lazy"

msg_.append("")
msg_[9] = "You are"

msg_.append("")
msg_[10] = "Are you sure? It is only one digit! (y / n)"

msg_.append("")
msg_[11] = "Don't be silly! It's just one number! Add to the memory? (y / n)"

msg_.append("")
msg_[12] = "Last chance! Do you really want to embarrass yourself? (y / n)"

end_of_calc = False

memory = 0.0


while end_of_calc == False:
    zero_division = False
    equation = input(f"{msg_[0]}\n")
    x, oper, y = equation.split()
    if x == 'M':
        x = memory
    if y == 'M':
        y = memory
    if (isDigitInt(x) or isDigitFloat(x)) and (isDigitFloat(y) or isDigitFloat(y)):
        x = float(x)
        y = float(y)
        if oper == '+' or oper == '-' or oper == '*' or oper == '/':
            check(x, y, oper)
            if oper == '+':
                result = float(x + y)
                print(result)
               # end_of_calc = True
            if oper == '-':
                result = float(x - y)
                print(result)
               # end_of_calc = True
            if oper == '*':
                result = float(x * y)
                print(result)
               # end_of_calc = True
            if oper == '/':
                if y == 0:
                    print(f"{msg_[3]}")
                    zero_division = True
                   # end_of_calc = True
                else:
                    result = float(x / y)
                    print(result)
                   # end_of_calc = True

            if zero_division == False:
                choice_store = input(f"{msg_[4]}\n").lower()
                if choice_store == 'y':

                    if is_one_digit(result):
                        msg_index = 10
                        choice_store_one_digit = input(f"{msg_[msg_index]}\n").lower()
                        # if choice_store_one_digit == 'y':
                        while msg_index < 12 and choice_store_one_digit == 'y':
                            msg_index += 1
                            choice_store_one_digit = input(f"{msg_[msg_index]}\n").lower()

                        if choice_store_one_digit == 'y':
                            memory = result
                    else:
                        memory = result
                #print(f"memory:{memory}")


                #elif choice_store == 'n':
                    #memory = 0.0
                choice_continue = input(f"{msg_[5]}\n").lower()
                if choice_continue == 'n':
                    end_of_calc = True


        else:
            print(f"{msg_[2]}\n")
    else:
        print(f"{msg_[1]}\n")






