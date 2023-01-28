#a = abs(10) + abs(-10)
#print(a)
#b = abs(-10) + -10
#print(b)
#--------------------------------------

funcStrDIR = list(dir('string'))
totalNUM = len(funcStrDIR)

def allFuncs():
    global funcStrDIR
    for i in range(0, totalNUM):
        exec('''print(help('string'.%s))''' % funcStrDIR[i])
#print(help('string'.split))
allFuncs()