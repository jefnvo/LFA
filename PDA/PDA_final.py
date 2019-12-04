def handleStack(stack):
    global register

    current = register.pop()

    if current[1] == 'E':
        stack.append(current[2])

    elif len(current) >= 3:
        for i in range(1,len(current)-1):
            stack.pop()

def getMoves(state,automata):#q0 - 0011
    global index, flag, final_state, register, stack

    nextState = state
    

    for r in rules: #[q0 0 z0 [q0 0 z0 ]]    
        if index < len(automata) or r[1] == 'E':
            if r[1] == 'E':
                if state == r[0]:
                    if len(stack) > 0:
                        if stack[len(stack)-1] == r[2]:                            
                            topStack = r[3]                        
                            print("E - state change of " + str(state) + " to " + str(topStack[0]) + "\n")
                            if topStack[1] == 'E':
                                stack.pop()
                                topStack.append(r[2])
                                register.append(topStack)
                            else:
                                if len(topStack) >= 3:
                                    for i in range(1,len(topStack)-1):
                                        stack.append(topStack[i])                                    
                                register.append(topStack)
                            print("stack: " + str(stack) + "\n\n")
                            nextState = topStack[0]                            
                            getMoves(nextState,automata)                            
                            handleStack(stack)
                            print("Rollback to state " + str(state) + " with stack " + str(stack) + "\n\n")

            elif automata[index] == r[1]: #[q0 0 z0 [q0 0 z0]]                
                if state == r[0]:
                    if len(stack) > 0:
                        if stack[len(stack)-1] == r[2]: 
                            topStack = r[3] #[q0 0 z0]                            
                            print(str(automata[index]) + " - state change from " + str(state) + " to " + str(topStack[0]) + "\n")                            
                            if topStack[1] == 'E':
                                stack.pop()
                            elif len(topStack) >= 3:
                                    #get the word and push in stack                                    
                                    for i in range(1,len(topStack)-1):
                                        stack.append(topStack[i])
                            if topStack[1] == 'E':
                                topStack.append(r[2])
                                register.append(topStack)
                            else:
                                register.append(topStack)
                            print("stack: " + str(stack) + "\n\n")                            
                            nextState = topStack[0]
                            index = index + 1                            
                            getMoves(nextState,automata)
                            index = index - 1                            
                            handleStack(stack)
                            print("Rollback to state " + str(state) + " with stack " + str(stack) + "\n\n")
        elif nextState in final_state:
            flag = 1
            print("Estado " + str(nextState) + " eh final\n\n")
            print("------ACCEPTED HERE!------\n\n")            
            return

def main(automata, defAutomata):
    global handler, final_state, index, flag, rules, register, stack
    ##The next lines will be populate our automata from the definition file##
    handler = open(defAutomata, "r")
    lines = handler.readlines()
    handler.close()

    #get the alphabet
    alphabet = []
    for word in lines[0]:
        if word != '\n':
            alphabet.append(word)

    states = lines[1].split()
    initial_state = lines[2].split()
    final_state = lines[3].split()

    stack_symbol = lines[4].split()
    stack = [stack_symbol[0]]

    #get the rules
    rules = []
    n_rules = len(lines) - 5
    for i in range(5,len(lines)):
        rules.append(lines[i].split())
    
    
    for i in range(0,n_rules):
        aux = rules[i] # q0 0 z0 q0 0,z0 
        aux2 = aux[4].split(",") #[0 z0]
        aux2.insert(0,aux[3]) # [q0 0 z0]
        del(aux[4]) # q0 0 z0 q0
        del(aux[3]) # q0 0 z0 
        aux.append(aux2) # [q0 0 z0 [q0 0 z0 ]]
        rules[i] = aux #[q0 0 z0 [q0 0 z0 ]]
    
    
    
    print("Alphabet: " + str(alphabet) + "\n" + 
          "States: " + str(states) + "\n" + 
          "Initial State: " + str(initial_state) + "\n" + 
          "Final State: " + str(final_state) + "\n" + 
          "Stack Symbol: " + str(stack_symbol[0])+ "\n")

    print("The automata has the follow definition: \n\n")
    for i in range(0,n_rules):
        aux = rules[i]
        print(str(i+1) + ") " + "(" + str(aux[0]) + "," + str(aux[1]) + "," + str(aux[2]) + ") = " + str(aux[3])+"\n")

    print("\n")

    print("\n----------ID generates of PDA---------\n\n")
    print("automata at level: " + automata + "\n")

    print('\n')

    index = 0
    flag = 0

    register = []
    getMoves(initial_state[0],automata)

    if flag == 0:
        print(automata+ " -> The tape was reject!")
    elif flag == 1:
        print(automata+ " -> The tape was accept!")


main('1011','./automata_final_definition.txt')




