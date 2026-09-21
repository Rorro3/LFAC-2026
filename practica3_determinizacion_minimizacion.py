from visual_automata.fa.dfa import DFA, VisualDFA
from automata.fa.nfa import NFA

'''Ejercicio 1. Para los siguientes automatas finitos no deterministicos, 
dar un automata deterministico minimo que reconozca el mismo lenguaje:
'''
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

#######################################################

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
#print(nfa1b.accepts_input('aaa')) 

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
#dfa1b.show_diagram(view=True)
#print(dfa1b.dfa.accepts_input('aaa')) 

#######################################################

#1c
nfa1c = NFA(
    states={'p', 'q', 'r','s'},
    input_symbols={'0', '1'},
    transitions={
        'p': {'0': {'q', 's'}, '1': {'q'}},
        'q': {'0': {'r'}, '1': {'q','r'}},
        'r': {'0': {'s'}, '1': {'p'}},
        's': {'0': set(), '1': {'p'}}
    },
    initial_state='p',
    final_states={'q','s'}
)
#graphnfa1c = nfa1c.show_diagram()
#graphnfa1c.draw('nfa_1c.png', prog='dot')

dfa1c = VisualDFA(
    states={'p','qs', 'r', 's', 't', 'q', 'pqr', 'qrs', 'rs'},
    input_symbols={'0', '1'},
    transitions={
        'p': {'0': 'qs', '1': 'q'},    
        'qs': {'0': 'r', '1': 'pqr'}, 
        'r': {'0': 's', '1': 'p'}, 
        's': {'0': 't', '1': 'p'},
        't': {'0': 't', '1': 't'},
        'q': {'0': 'r', '1': 'qrs'},
        'pqr': {'0': 'qrs', '1': 'pqr'},
        'qrs': {'0': 'rs', '1': 'pqr'},
        'rs': {'0': 's', '1': 'p'}   
    },
    initial_state='p',
    final_states={'qs','s','q','pqr','qrs','rs'}  
)
#dfa1c.show_diagram(view=True)

#######################################################

#2: te la debo

'''Ejercicio 3. Dado el alfabeto Σ = {0, 1} y los siguientes lenguajes L1 y L2, dar un automata
finito deterministico minimo para L1 ∩ L2:
L1 = {α | α ∈ Σ∗ ∧ 01 es subcadena de α}.
L2 = {α | α ∈ Σ∗ ∧ α tiene una cantidad par de ceros}.
'''
nfaL1 = NFA(
    states={'q0', 'q1', 'q2'},
    input_symbols={'0', '1'},
    transitions={
        'q0': {'0': {'q0', 'q1'}, '1': {'q0'}},
        'q1': {'0': set(), '1': {'q2'}},
        'q2': {'0': {'q2'}, '1': {'q2'}}
    },
    initial_state='q0',
    final_states={'q2'}
)

dfaL2 = DFA(
    states={'q0','q1'},
    input_symbols={'0', '1'},
    transitions={
        'q0': {'0': 'q1', '1': 'q0'},    
        'q1': {'0': 'q0', '1': 'q1'}  
    },
    initial_state='q0',
    final_states={'q0'}  
)

dfaL1 = DFA(
    states={'q0','q1','q2'},
    input_symbols={'0', '1'},
    transitions={
        'q0': {'0': 'q1', '1': 'q0'},    
        'q1': {'0': 'q1', '1': 'q2'},
        'q2':{'0':'q2','1':'q2'}  
    },
    initial_state='q0',
    final_states={'q2'}  
)

dfaInterseccionL1L2 = DFA(
    states={'q0','q1','q2','q3','q4'},
    input_symbols={'0','1'},
    transitions={
        'q0':{'0':'q1','1':'q0'},
        'q1':{'0':'q2','1':'q4'},
        'q2':{'0':'q1','1':'q3'},
        'q3':{'0':'q4','1':'q3'},
        'q4':{'0':'q3','1':'q4'}
    },
    initial_state='q0',
    final_states={'q3'}
)
#:)