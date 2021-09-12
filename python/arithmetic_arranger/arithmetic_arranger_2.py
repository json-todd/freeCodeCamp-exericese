def arithmetic_arranger(problem):
    # Ver 2: Display the arithmetic side-by-side

    first_line_meta = []
    second_line_meta = []
    dash_line_meta = []
    
    for a in problem:
        a_split = a.split(" ")
        num_1 = a_split[0]; num_2 = a_split[2]
        operator = a_split[1]

        def getWorkSpace():
            max_length = 0
            for digit in a_split:
                length = len(digit)
                if max_length < length:
                    max_length = length
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
         
    first_line = "    ".join(first_line_meta) 
    second_line = "    ".join(second_line_meta)  
    dash_line = "    ".join(dash_line_meta)

    return first_line + "\n" + second_line + "\n" + dash_line

res = arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])
print(res)
