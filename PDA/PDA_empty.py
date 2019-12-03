def principal(automata, defAutomata):
    ##The next lines will be populate our automata from the definition file##
    handler = open(defAutomata, "r")
    lines = handler.readlines()
    handler.close()

    states = lines[0].split()
    
    #get the alphabet
    alphabet = []
    for word in lines[1]:
        if word != '\n':
            alphabet.append(word)

    stack_symbol = lines[2]
    stack = [stack_symbol]

    initial_state = lines[3]

    #get the rules
    rules = []
    for i in range(4,len(lines)):
        rules.append(lines[i].split())
    n_rules = len(lines) - 4
    
    handler = open("resultado.txt","w")
    handler.write("Alphabet: " + str(alphabet) + "\n" + "States: " +
            str(states) + "\n" + "Initial State: " + str(initial_state) + "\n" + 
            "Stack symbol: " + str(stack[0])
            + "\n\nRegras: " + "\n")

    for i in range(0,n_rules):
        aux = rules[i]
        handler.write(str(i+1) + ") " + "(" + str(aux[0]) + "," + str(aux[1]) + "," + str(aux[2]) + ") = " + str(aux[3]) +" "+ str(aux[4])+"\n")

    handler.write("\n")
    handler.close()


principal('0011','automata_empty_definition.txt')


    