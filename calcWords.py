import re

s = ""

while (s != "quit!"):
    print("enter words: ")
    s = input()
    new = ""
    if re.search("[kmvwxz]", s):
        print('invalid character. Cannot convert kmvwxz')
    else:
        for c in s:
            if (c == 'a'):
                c = """
                 _ 
                |_|
                | |
                """
            elif (c == 'b'):
                c = """
                |_
                |_|
                """
            elif (c == 'c'):
                c = """
                 _
                |_
                """
            elif (c == 'd'):
                c = """
                 _|
                |_|
                """
            elif (c == 'e'):
                c = """
                 _
                |_
                |_
                """
            elif (c == 'd'):
                c = """
                 _|
                |_|
                """
            elif (c == 'e'):
                c = """
                 _
                |_
                |_
                """
            elif (c == 'f'):
                c = """
                 _
                |_
                |
                """
            elif (c == 'g'):
                c = """
                 _
                |_|
                 _|
                """
            elif (c == 'h'):
                c = """
                |_|
                | |
                """
            elif (c == 'i'):
                c = """
                  |
                  |
                """
            elif (c == 'j'):
                c = """
                  |
                |_|
                """
            elif (c == 'l'):
                c = """
                |
                |_
                """
            elif (c == 'n'):
                c = """
                 _ 
                | |
                """
            elif (c == 'o'):
                c = """
                 _
                |_|
                """
            elif (c == 'p'):
                c = """
                 _
                |_|
                |
                """
            elif (c == 'q'):
                c = """
                 _
                |_|
                  |
                """
            elif (c == 'r'):
                c = """
                 _
                |
                """
            elif (c == 's'):
                c = """
                 _
                |_
                 _|
                """
            elif (c == 't'):
                c = """
                 _|
                  |
                """
            elif (c == 'u'):
                c = """

                |_|
                """
            elif (c == 'y'):
                c = """
                |_|
                 _|
                 """
            elif (c == ' '):
                c = """


                """
            elif (c == '1'):
                c = """
                  |
                  |
                """
            elif (c == '2'):
                c = """
                 _
                 _|
                |_
                """
            elif (c == '3'):
                c = """
                 _
                 _|
                 _|
                """
            elif (c == '4'):
                c = """
                |_|
                  |
                """
            elif (c == '5'):
                c = """
                 _
                |_
                 _|
                """
            elif (c == '6'):
                c = """
                 _
                |_
                |_|
                """
            elif (c == '7'):
                c = """
                 _
                  |
                  |
                """
            elif (c == '8'):
                c = """
                 _
                |_|
                |_|
                """
            elif (c == '9'):
                c = """
                 _
                |_|
                 _|
                """
            elif (c == '0'):
                c = """
                 _
                | |
                |_|
                """
            else:
                temp = c
                c = f"""
                {temp}
                """
            new += c
        print(new)