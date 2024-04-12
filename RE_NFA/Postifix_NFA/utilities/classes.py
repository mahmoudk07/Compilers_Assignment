class Edge:
    def __init__(self):
        self.destination = None
        self.source = None
        self.arc = None
class State:
    def __init__(self):
        self.outgoing_arcs = []
        self.name = None
class NFA:
    def __init__(self , initial_state , accepting_state , inner_states):
        self.inner_states = inner_states
        self.accepting_state = accepting_state
        self.initial_state = initial_state