#a = abs(10) + abs(-10)
#print(a)
#b = abs(-10) + -10
#print(b)
#--------------------------------------

#funcStrDIR = list(dir('string'))
#totalNUM = len(funcStrDIR)

#def allFuncs():
#    global funcStrDIR
#    for i in range(0, totalNUM):
#        exec('''print(help('string'.%s))''' % funcStrDIR[i])
#print(help('string'.split))
#allFuncs()

#--------------------------------------

hiddenMessage = "this if is not are a reading very this good then way you to have hide done a it message wrong"
HMLIST = hiddenMessage.splitlines()
print(help('string'.splitlines))

#print(HMLIST)