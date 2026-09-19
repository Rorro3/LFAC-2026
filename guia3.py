from visual_automata.fa.dfa import VisualDFA
from automata.fa.nfa import NFA

#1a
nfa1a = NFA(
    states={'q0', 'q1', 'q2','q3'},
    input_symbols={'a', 'b'},
    transitions={
        'q0': {'a': {'q0', 'q1'}, 'b': {'q0'}},
        'q1': {'a': {'q2'}, 'b': {'q0'}},
        'q2': {'a': {'q3'}, 'b': {'q0'}},
        'q3': {'a': {'q3'}, 'b': {'q3'}}
    },
    initial_state='q0',
    final_states={'q3'}
)
#graphnfa1a = nfa1a.show_diagram()
#graphnfa1a.draw('nfa_1a.png', prog='dot')
#print(nfa1a.accepts_input('aaa')) 
#print(nfa1a.accepts_input('ababababbaaabaaab')) 

dfa1a = VisualDFA(
    states={'q0','q1', 'q2', 'q3'},
    input_symbols={'a', 'b'},
    transitions={
        'q0': {'a': 'q1', 'b': 'q0'},    
        'q1': {'a': 'q2', 'b': 'q0'}, 
        'q2': {'a': 'q3', 'b': 'q0'}, 
        'q3': {'a': 'q3', 'b': 'q3'}   
    },
    initial_state='q0',
    final_states={'q3'}  
)
#dfa1a.show_diagram(view=True)
#print(dfa1a.dfa.accepts_input('aaa')) 
#print(dfa1a.dfa.accepts_input('ababababbaaabaaab'))

#1b
nfa1b = NFA(
    states={'0', '1', '2','3','4','5','6'},
    input_symbols={'a', 'b'},
    transitions={
        '0': {'a': {'1'}, 'b': {'2'}, '':{'4'}},
        '1': {'a': set(), 'b': set(),'':{'0','3'}},
        '2': {'a': set(), 'b': set(),'':{'0','3'}},
        '3': {'a': {'4'}, 'b': set(),},
        '4': {'a': set(), 'b': set(),'':{'5'}},
        '5': {'a': {'6'}, 'b': {'6'}},
        '6': {'a': set(), 'b': set(),'':{'5'}}
    },
    initial_state='0',
    final_states={'6'}
)
#graphnfa1b = nfa1b.show_diagram()
#graphnfa1b.draw('nfa_1b.png', prog='dot')
print(nfa1b.accepts_input('aaa')) 

dfa1b = VisualDFA(
    states={'0','1', '2', '3'},
    input_symbols={'a', 'b'},
    transitions={
        '0': {'a': '1', 'b': '1'},    
        '1': {'a': '2', 'b': '2'}, 
        '2': {'a': '3', 'b': '3'}, 
        '3': {'a': '3', 'b': '3'}   
    },
    initial_state='0',
    final_states={'3'}  
)
dfa1b.show_diagram(view=True)
print(dfa1b.dfa.accepts_input('aaa')) 
