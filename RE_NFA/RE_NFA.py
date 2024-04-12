# def concate_states(stack):
#     nfa_1 = stack.pop()
#     nfa_2 = stack.pop()
#     edge = Edge()
#     edge.arc = 'ε'
#     edge.destination = nfa_2.initial_state
#     nfa_1.accepting_states.outgoing_arcs.append(edge)
#     combined_nfas = NFA(nfa_1.initial_state , nfa_2.accepting_states , nfa_1.inner_states + nfa_2.inner_states)
#     stack.append(combined_nfas)
#     return combined_nfas
# def orNFA (stack, id):
#   nfa1 = stack.pop()
#   nfa2 = stack.pop()
#   newStart = State()
#   newStart.name= "S"+str(id)
#   newEnd = State()
#   newEnd.name = "S"+str(id+1)

#   nEdge1 = Edge()
#   nEdge1.arc = 'ε'
#   nEdge1.destination = nfa1.initial_state

#   nEdge2 = Edge()
#   nEdge2.arc = 'ε'
#   nEdge2.destination = nfa2.initial_state

#   newStart.outgoing_arcs.append(nEdge1)
#   newStart.outgoing_arcs.append(nEdge2)


#   nEdge3 = Edge()
#   nEdge3.arc = 'ε'
#   nEdge3.destination = newEnd

#   nfa1.accepting_states.outgoing_arcs.append(nEdge3)

#   nEdge4 = Edge()
#   nEdge4.arc = 'ε'
#   nEdge4.destination = newEnd
#   nfa2.accepting_states.outgoing_arcs.append(nEdge4)


#   result = NFA(newStart, newEnd, [newStart,newEnd]+ nfa1.inner_states + nfa2.inner_states)
#   stack.append(result)
#   return result, id+2

# def ZeroMoreNFA (stack, id):
#   nfa1 = stack.pop()



#   newStart = State()
#   newStart.name = "S"+str(id)
#   newEnd = State()
#   newEnd.name = "S"+str(id+1)

#   nEdge1 = Edge()
#   nEdge1.arc = 'ε'
#   nEdge1.destination = newStart
#   nfa1.accepting_states.outgoing_arcs.append(nEdge1)



#   nEdge2 = Edge()
#   nEdge2.arc = 'ε'
#   nEdge2.destination=nfa1.start
#   newStart.outgoing_arcs.append(nEdge2)

#   nEdge3 = Edge()
#   nEdge3.arc = 'ε'
#   nEdge3.destination = newEnd
#   nfa1.accepting_states.outgoing_arcs.append(nEdge3)



#   nEdge4 = Edge()
#   nEdge4.arc = 'ε'
#   nEdge4.destination = newEnd
#   newStart.outgoing_arcs.append(nEdge4)
  
#   result = NFA (newStart, newEnd, [newStart, newEnd] + nfa1.inner_states)
#   stack.append(result)
#   return result, id+2

# def OneMoreNFA (stack, id):
#    nfa1 = stack.pop()



#    newStart = State()
#    newStart.name = "S"+str(id)
#    newEnd = State()
#    newEnd.name = "S"+str(id+1)

#    nEdge1 = Edge()
#    nEdge1.arc ='ε'
#    nEdge1.destination = newStart
#    nfa1.accepting_states.outgoing_arcs.append(nEdge1)

#    nEdge2 = Edge()
#    nEdge2.arc='ε'
#    nEdge2.destination=nfa1.start
#    newStart.outgoing_arcs.append(nEdge2)

#    nEdge3 = Edge()
#    nEdge3.arc='ε'
#    nEdge3.destination = newEnd
#    nfa1.accepting_states.outgoing_arcs.append(nEdge3)


#    result = NFA (newStart, newEnd, [newStart, newEnd] + nfa1.inner_states)
#    stack.append(result)
#    return result, id+2

# def ZeroOneNFA (stack, id):
#   nfa1 = stack.pop()

#   newStart = State()
#   newStart.name = "S"+str(id)
#   newEnd = State()
#   newEnd.name = "S"+str(id+1)

#   nEdge1 = Edge()
#   nEdge1.arc='ε'
#   nEdge1.destination=nfa1.initial_state
#   newStart.outgoing_arcs.append(nEdge1)

#   nEdge2 = Edge()
#   nEdge2.arc='ε'
#   nEdge2.destination = newEnd
#   nfa1.accepting_states.outgoing_arcs.append(nEdge2)

  
#   nEdge2 = Edge()
#   nEdge2.arc='ε'
#   nEdge2.destination = newEnd
#   newStart.outgoing_arcs.append(nEdge2)



#   result = NFA (newStart, newEnd, [newStart, newEnd] + nfa1.inner_states)
#   stack.append(result)
#   return result, id+2

# def ConstructNFA (c:str, id:int, stack):
#     start = State()
#     accept = State()
#     start.name = "S"+str(id)
#     accept.name = "S"+str(id+1)

#     nEdge = Edge()
#     nEdge.arc = c
#     nEdge.destination = accept
#     start.outgoing_arcs.append(nEdge)
    


    
#     result_nfa = NFA(start, accept, [start,accept])
#     stack.append(result_nfa)
#     #print(result_nfa.inner_states)

#     return result_nfa, id+2

# def Construct_NFAJson (nefa:NFA):
#   outputJson = dict()
#   outputJson["startingState"] = nefa.initial_state.name
#   for stat in nefa.inner_states:
#     stateDict = dict()
#     if stat == nefa.accepting_states:
#       stateDict["isTerminatingState"] = True
#     else:
#       stateDict["isTerminatingState"] = False
#     for edg in stat.outgoing_arcs:
#       if(edg.arc in stateDict.keys()):
#         stateDict[edg.arc] = [] + [stateDict[edg.arc]] + [edg.destination.name]
#       else:
#         stateDict[edg.arc] = edg.destination.name
#     outputJson[stat.name] = stateDict
#   nfaOutFile = open('NFA.json', 'w')
#   JsonObject = json.dump(outputJson, nfaOutFile,indent=6, ensure_ascii=False)
#   nfaOutFile.close()
#   return JsonObject




# def vizualize_NFA(resultNFA):

#   #gra = Digraph(graph_attr={'landscape':'True'})
#   gra = Digraph(graph_attr={'rankdir':'LR'})


#   #construct nodes first
#   for stat in resultNFA.inner_states:
#       if(stat.name == resultNFA.initial_state.name):
#         gra.node("", _attributes={'shape' : 'none'})
#         gra.edge("", stat.name)
#       if(stat.name == resultNFA.accepting_states.name):
#         gra.node(stat.name, _attributes={'peripheries' : '2'})
#       else:
#         gra.node(stat.name)

#   #for each node, construct edges
#   for stat in resultNFA.inner_states:
#       for edg in stat.outgoing_arcs:
#           gra.edge(stat.name, edg.destination.name, label=edg.arc)
#   gra.format = 'png'
#   gra.render('NFA', view = True)
#   return gra.source


# def PostFix_To_NFA(postfix):
#   alphabet = list("0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_:/")


#   stack = []
#   id = 1

#   for c in postfix:
#     if c in alphabet:
#       _, id = ConstructNFA(c, id, stack)
#     elif c == '*':
#       _, id = ZeroMoreNFA(stack, id)
#     elif c == '+':
#       _, id = OneMoreNFA(stack, id)
#     elif c == '?':
#       _, id = ZeroOneNFA(stack, id)
#     elif c == '.':
#       concate_states(stack)
#     elif c == '|':
#       _, id = orNFA(stack, id)
#     else:
#       raise ValueError(f"You entered an unknown Operator {c}")

#   result = stack.pop()
#   return result, vizualize_NFA(result)

# PostFix_To_NFA("ht.t.p.s?.:././.ww.w..?.ab|A|B|0|1|2|_|..co.m.or.g.|ne.t.|.")
