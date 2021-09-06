def arithmetic_arranger(problem, answer = False):
    # Ver 4: include rules in the function
  
    first_line_meta = []
    second_line_meta = []
    dash_line_meta = []
    ans_line_meta = []
    
    def checkRule1():
        if len(problem) > 5 :
            return 'Error: Too many problems.'
    if checkRule1():
        return checkRule1()

    for a in problem:
        a_split = a.split(" ")
        num_1 = a_split[0]; num_2 = a_split[2]
        operator = a_split[1]
        
        def checkMoreRules():
            def checkRule2():
                if operator != "+" and operator != "-":
                    return "Error: Operator must be '+' or '-'."

            def checkRule3():
                try:
                    int(num_1)
                    int(num_2)
                except:
                    return "Error: Numbers must only contain digits."           
            
            def checkRule4():
                if len(num_1) > 4 or len(num_2) > 4:
                    return "Error: Numbers cannot be more than four digits."

            if checkRule2():
                return checkRule2()
            if checkRule3():
                return checkRule3()
            if checkRule4():
                return checkRule4() 

        if checkMoreRules():
            return checkMoreRules()

        def getWorkSpace():
            max_length = max(len(num_1), len(num_2))
            return max_length + 2

        work_space = getWorkSpace()

        def makeFirstLine():
            empty_space = work_space - len(num_1)
            return " " * empty_space + num_1
        def makeSecondLine():
            empty_space = work_space - 1 - len(num_2)
            return operator + " " * empty_space + num_2
        def makdeDashLine():
            return "-" * work_space
        
        first_line_meta.append( makeFirstLine() )
        second_line_meta.append( makeSecondLine() )
        dash_line_meta.append( makdeDashLine() )
        
        if answer == True:
            if operator == '+':
                ans = int(num_1) + int(num_2)
            elif operator == '-':
                ans = int(num_1) - int(num_2)
            
            ans = str(ans)

            def makeAnsLine():
                empty_space = work_space - len(ans)
                return " " * empty_space + ans
            
            ans_line_meta.append( makeAnsLine() )
 
    first_line = "    ".join(first_line_meta) 
    second_line = "    ".join(second_line_meta)  
    dash_line = "    ".join(dash_line_meta)
    ans_line = "    ".join(ans_line_meta)
    
    if answer == True:
        return first_line + "\n" + second_line + "\n" + dash_line + "\n" + ans_line
    else: 
        return first_line + "\n" + second_line + "\n" + dash_line

res2 = arithmetic_arranger(["11 + 4", "3801 - 2999", "1 + 2", "123 + 49", "1 - 9380"],True)
print(res2)
