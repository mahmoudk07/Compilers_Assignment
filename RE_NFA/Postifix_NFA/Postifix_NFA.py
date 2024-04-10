from graphviz import Digraph
import json
from utilities.classes import Edge , State , NFA 
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
class Postifix_NFA:
    def __init__(self , postifix):
      self.postifix = postifix
      self.alpha_numeric = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x' ,'y', 'z',
                'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
                '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '@' , '#' , '$' , '%' , '_', '!', ':' , '/']
      self.stack = []
      self.id = 1
    @staticmethod
    def concat_states(self , nfa_1: NFA , nfa_2: NFA) -> NFA:
       edge = Edge()
       edge.arc = 'ε'
       edge.destination = nfa_2.initial_state
       nfa_1.accepting_state.outgoing_arcs.append(edge)
       initial_state , inner_states , accepting_state = nfa_1.initial_state , nfa_1.inner_states + nfa_2.inner_states , nfa_2.accepting_state
       concated_states = NFA(initial_state , accepting_state , inner_states)
       self.stack.append(concated_states)
       return concated_states

    @staticmethod
    def oring_states(self , nfa_1: NFA , nfa_2: NFA) -> NFA:
       start_state , end_state , edge_1 , edge_2, edge_3 , edge_4 = State() , State(), Edge() , Edge() , Edge() , Edge()
       start_state.name = "S" + str(self.id)
       end_state.name = "S" + str(self.id + 1)
       edge_1.arc = edge_2.arc = edge_3.arc = edge_4.arc = 'ε'
       edge_1.destination , edge_2.destination = nfa_1.initial_state , nfa_2.initial_state
       edge_3.destination = edge_4.destination = end_state
       start_state.outgoing_arcs.append(edge_1)
       start_state.outgoing_arcs.append(edge_2)
       nfa_1.accepting_state.outgoing_arcs.append(edge_3)
       nfa_2.accepting_state.outgoing_arcs.append(edge_4)
       or_states = NFA(start_state , end_state , [start_state , end_state] + nfa_1.inner_states + nfa_2.inner_states)
       self.stack.append(or_states)
       return or_states

    @staticmethod
    def zero_or_more_state(self , nfa_1: NFA) -> NFA:
       start_state , end_state , edge_1 , edge_2 , edge_3 , edge_4 = State() , State() , Edge() , Edge() , Edge() , Edge()
       start_state.name = "S" + str(self.id)
       end_state.name = "S" + str(self.id + 1)
       edge_1.arc = edge_2.arc = edge_3.arc = edge_4.arc = 'ε'
       edge_1.destination = edge_2.destination = end_state
       edge_3.destination, edge_4.destination = nfa_1.initial_state , start_state
       start_state.outgoing_arcs.append(edge_1)
       start_state.outgoing_arcs.append(edge_3)
       nfa_1.accepting_state.outgoing_arcs.append(edge_2)
       nfa_1.accepting_state.outgoing_arcs.append(edge_4)
       zero_or_more_states = NFA(start_state, end_state , [start_state , end_state] + nfa_1.inner_states)
       self.stack.append(zero_or_more_states)
       return zero_or_more_states
    @staticmethod
    def one_or_more_state(self , nfa_1: NFA) -> NFA:
       start_state , end_state , edge_1 , edge_2 , edge_3 = State() , State() , Edge() , Edge() , Edge()
       start_state.name = "S" + str(self.id)
       end_state.name = "S" + str(self.id + 1)
       edge_1.arc = edge_2.arc = edge_3.arc = 'ε'
       edge_1.destination, edge_2.destination, edge_3.destination = start_state, nfa_1.initial_state, end_state
       start_state.outgoing_arcs.append(edge_2)
       nfa_1.accepting_state.outgoing_arcs.append(edge_3)
       nfa_1.accepting_state.outgoing_arcs.append(edge_1)
       one_or_more_states = NFA(start_state , end_state , [start_state , end_state] + nfa_1.inner_states)
       self.stack.append(one_or_more_states)
       return one_or_more_states
    @staticmethod
    def zero_or_one_state(self, nfa_1: NFA) -> NFA:
       start_state , end_state , edge_1 , edge_2, edge_3 = State() , State() , Edge() , Edge(), Edge()
       start_state.name = "S" + str(self.id)
       end_state.name = "S" + str(self.id + 1)
       edge_1.arc = edge_2.arc = edge_3.arc = 'ε'
       edge_1.destination, edge_2.destination, edge_3.destination  = nfa_1.initial_state, end_state , end_state 
       start_state.outgoing_arcs.append(edge_1)
       start_state.outgoing_arcs.append(edge_2)
       nfa_1.accepting_state.outgoing_arcs.append(edge_3)
       zero_or_one_states = NFA(start_state , end_state , [start_state , end_state] + nfa_1.inner_states)
       self.stack.append(zero_or_one_states)
       return zero_or_one_states
    @staticmethod
    def construct_nfa(self , character:str) -> NFA:
       start_state , end_state , edge = State() , State() , Edge()
       start_state.name = "S" + str(self.id)
       end_state.name = "S" + str(self.id + 1)
       edge.arc = character
       edge.destination = end_state
       start_state.outgoing_arcs.append(edge)
       constructed_nfa = NFA(start_state , end_state , [start_state , end_state])
       self.stack.append(constructed_nfa)
       return constructed_nfa
    @staticmethod
    def visualize_nfa(nfa:NFA):
       pass
    def postfix_to_nfa(self):
       for character in self.postifix:
          if character in self.alpha_numeric:
            self.construct_nfa(self, character)
          elif character == '*':
            nfa_1 = self.stack.pop()
            self.zero_or_more_state(self , nfa_1)
          elif character == '+':
            nfa_1 = self.stack.pop()
            self.one_or_more_state(self, nfa_1)
          elif character == '?':
            nfa_1 = self.stack.pop()
            self.zero_or_one_state(self , nfa_1)
          elif character == '.':
            nfa_1 = self.stack.pop()
            nfa_2 = self.stack.pop()
            self.concat_states(self , nfa_1 , nfa_2)
            continue
          elif character == '|':
            nfa_1 = self.stack.pop()
            nfa_2 = self.stack.pop()
            self.oring_states(self , nfa_1 , nfa_2)
          else:
            print("Please enter a correct character!")
            exit(1)
          self.id += 2
       result = self.stack.pop()
       return result
          
    
postifix_nfa = Postifix_NFA("A?")
result = postifix_nfa.postfix_to_nfa()