inputstring = str(input("Input string: "))

def solution(input):
    cut = ''
    arr = []
    right_round_bracket = []
    switcher = False
    #cut string inside round brackets
    for i in range(len(inputstring)):
        if (switcher == True and input[i] != ')'):
            cut = cut + input[i]
        else:
            pass
        if (input[i] == '('):
            switcher = True
            index = i
            right_round_bracket.append(i)
            if (switcher == True and input[i] == '('):
                switcher = False
                cut = ''
                switcher = True
        elif (input[i] == ')' and switcher == True):
            switcher = False
            arr.append(index)
            arr.append(cut)
            cut = ''
    #rotate position
    for i in range(len(arr)):
        if (i % 2 == 1):
            string = arr[i]
            new_string = ''
            for v in range(len (string)):
                new_string = new_string + string[len(string) - 1 - v]
            arr[i] = new_string
        elif(i%2 == 0):
            for v in range(1,len(right_round_bracket)-1):
                try:
                    arr.index(right_round_bracket[v-1])
                except:
                    not_exist_in_arr = True
                if (arr[i] == right_round_bracket[v] and not_exist_in_arr):
                    arr[i] = right_round_bracket[v-1]
                    not_exist_in_arr = False
    outputstring = ''
    for i in range(len(input)):
        #check if i exist in arr
        try:
            v = arr.index(i)
            exist = True
        except:
            exist = False
        
        if(exist == False):
            outputstring = outputstring + input[i]
        else:
            outputstring = outputstring + arr[v+1] + '(' 
    #clear inside brackets
    switcher = False
    cut = ''
    cut_arr = []
    for i in range(len(outputstring)):
        if (switcher == True and outputstring[i] != ')'):
            cut = cut + outputstring[i]
        else:
            pass
        if (outputstring[i] == '('):
            switcher = True
            if (switcher == True and outputstring[i] == '('):
                switcher = False
                cut = ''
                switcher = True
        elif (outputstring[i] == ')' and switcher == True):
            switcher = False
            cut_arr.append(cut)
            cut = ''
    for i in range(len(cut_arr)):
        outputstring = outputstring.replace(cut_arr[i], '')
    outputstring_2 = ''
    for i in range (len(outputstring)):
        if (outputstring[i] == '(' or outputstring[i] == ')'):
            pass
        else:
            outputstring_2 = outputstring_2 + outputstring[i]
    print(outputstring_2)
solution(inputstring)