# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

input_list = sys.stdin.readlines()

# 공백제거해줘야함!!!!!!!!!!!!!!!!!!!!!!!!!
str_list = []
for strs in input_list:
    str_list.append(strs.rstrip())

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
            answer = answer[:-2]
                
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
            answer += "()"
        elif s_type == "C" :
            answer = answer[0].upper()+answer[1:]
                

    sys.stdout.write(answer+"\n")
        
        
