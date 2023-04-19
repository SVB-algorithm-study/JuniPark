# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

str_list = sys.stdin.readlines()
# print(str_list)

for str_input in str_list :
    wtd = str_input[0] # what to do S/C
    s_type = str_input[2] #str type M/C/V
    title = str_input[4:]
    answer = ""

    if wtd == "S":
        # Split
        answer += title[0].lower()
        for i in title[1:] :
            if i.isupper():
                answer += " "+i.lower()
            else :
                answer += i
        if "()" in answer :
            answer = answer[:-3]+"\n"

    elif wtd == "C":
        # Combine
        prev = False
        for i in title:
            if i == " " :
                prev = True
                pass
            elif prev :
                prev = False
                answer += i.upper()
            else :
                answer += i

        if s_type == "M" :
            answer = answer[:-1]+"()\n"
        elif s_type == "C" :
            answer = answer[0].upper()+answer[1:]


    sys.stdout.write(answer)
