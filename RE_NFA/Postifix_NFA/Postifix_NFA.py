from graphviz import Digraph
import json
from utilities.classes import Edge , State , NFA 
class Postifix_NFA:
    def __init__(self , postifix):
      self.postifix = postifix
      self.alpha_numeric = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x' ,'y', 'z',
                'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
                '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '@' , '.' , '$' , '%' , '_', '!', ':' , '/']
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
    def visualize_nfa(nfa : NFA):
      gra = Digraph(graph_attr={'rankdir':'LR'})
      for stat in nfa.inner_states:
          if(stat.name == nfa.initial_state.name):
            gra.node("", _attributes={'shape' : 'none'})
            gra.edge("", stat.name)
          if(stat.name == nfa.accepting_state.name):
            gra.node(stat.name, _attributes={'peripheries' : '2'})
          else:
            gra.node(stat.name)
      for stat in nfa.inner_states:
          for edg in stat.outgoing_arcs:
              gra.edge(stat.name, edg.destination.name, label=edg.arc)
      gra.format = 'png'
      gra.render('NFA', view = True)
      return gra.source
    def postfix_to_nfa(self):
      i = 0
      range_string : str = ""
      while i < len(self.postifix):
        if self.postifix[i] in self.alpha_numeric:
          self.construct_nfa(self, self.postifix[i])
        elif self.postifix[i] == '[':
          j = i
          while self.postifix[j] != ']':
            range_string += self.postifix[j]
            j += 1
          range_string += ']'
          self.construct_nfa(self , range_string)
          range_string = ""
          i = j
        elif self.postifix[i] == '*':
          nfa_1 = self.stack.pop()
          self.zero_or_more_state(self , nfa_1)
        elif self.postifix[i] == '+':
          nfa_1 = self.stack.pop()
          self.one_or_more_state(self, nfa_1)
        elif self.postifix[i] == '?':
          nfa_1 = self.stack.pop()
          self.zero_or_one_state(self , nfa_1)
        elif self.postifix[i] == '#':
          nfa_1 = self.stack.pop()
          nfa_2 = self.stack.pop()
          self.concat_states(self , nfa_2, nfa_1)
          i += 1
          continue
        elif self.postifix[i] == '|':
          nfa_1 = self.stack.pop()
          nfa_2 = self.stack.pop()
          self.oring_states(self , nfa_1 , nfa_2)
        else:
          print("Please enter a correct character!")
          exit(1)
        self.id += 2
        i += 1
      result = self.stack.pop()
      return result
    @staticmethod
    def write_output(nfa : NFA) -> json:
      result = dict()
      result["startingState"] = nfa.initial_state.name
      for state in nfa.inner_states:
        isTerminatingState = (state.name == nfa.accepting_state.name)
        result[state.name] = {
          "isTerminatingState": isTerminatingState,
        }
        for transition in state.outgoing_arcs:
          # result[state.name].update({**result[state.name] , transition.arc: transition.destination.name})
          # result[state.name].append({transition.arc : transition.destination.name})
          if state.name in result and transition.arc in result[state.name]:
                # If the transition already exists, append to it
            if isinstance(result[state.name][transition.arc], list):
              result[state.name][transition.arc].append(transition.destination.name)
            else:
              result[state.name][transition.arc] = [result[state.name][transition.arc], transition.destination.name]
          else:
            result[state.name][transition.arc] = [transition.destination.name]  # Store as a list
      result_in_json = json.dumps(result , indent = 4 , ensure_ascii = False)
      with open("RE_NFA/output.json" , "w") as outputfile:
         outputfile.write(result_in_json)
      return result_in_json
         
          
    
postifix_nfa = Postifix_NFA("[0-9A-B]AB|#")
result = postifix_nfa.postfix_to_nfa()
outputfile = postifix_nfa.write_output(result)
print(outputfile)
postifix_nfa.visualize_nfa(result)
