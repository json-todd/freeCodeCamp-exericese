def arithmetic_arranger(problem, answer = False):
    # Ver 3: function has another parameter that allows to return a line showing arithmetic answers
      
    first_line_meta = []
    second_line_meta = []
    dash_line_meta = []
    ans_line_meta = []
    
    for a in problem:
        a_split = a.split(" ")
        num_1 = a_split[0]; num_2 = a_split[2]
        operator = a_split[1]      
       
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

res = arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])
print(res)

res2 = arithmetic_arranger(['3 + 855', '988 + 40'], True)
print(res2)
