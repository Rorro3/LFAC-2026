from automata.fa.dfa import DFA
from automata.fa.nfa import NFA

#como usar las cosas:

#definir dfa
dfa = DFA(
    states={'q0', 'q1'},
    input_symbols={'0', '1'},
    transitions={
        'q0': {'0': 'q0', '1': 'q1'},
        'q1': {'0': 'q0', '1': 'q1'}
    },
    initial_state='q0',
    final_states={'q1'}
)

#saber si acepta o no
print(dfa.accepts_input('101')) 
print(dfa.accepts_input('100'))  

#mostrar los pasos que hace
print(list(dfa.read_input_stepwise('101')))

#definir nfa
nfa = NFA(
    states={'q0', 'q1', 'q2'},
    input_symbols={'0', '1'},
    transitions={
        'q0': {'0': {'q0', 'q1'}, '1': {'q0'}},
        'q1': {'1': {'q2'}},
        'q2': {'0': {'q2'}, '1': {'q2'}}
    },
    initial_state='q0',
    final_states={'q2'}
)

#saber si acepta o no
print(nfa.accepts_input('0010')) 
print(nfa.accepts_input('0000'))  

#muestra los estados posibles en cada paso que hace
pasos = list(nfa.read_input_stepwise('01'))
for i, estados_actuales in enumerate(pasos):
    print(f"Paso {i}: Estados activos = {estados_actuales}")