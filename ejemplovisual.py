from visual_automata.fa.dfa import VisualDFA
from automata.fa.nfa import NFA

#para los dfa uso visualDFA porque me los grafica mas facil
#para los nfa uso el NFA porque no me sale con visualNFA

dfa = VisualDFA(
    states={'q0', 'q1'},
    input_symbols={'0', '1'},
    transitions={
        'q0': {'0': 'q0', '1': 'q1'},
        'q1': {'0': 'q0', '1': 'q1'}
    },
    initial_state='q0',
    final_states={'q1'}
)

#asi te lo dibuja al dfa:
print("dibujando...")
dfa.show_diagram(view=True)

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

#asi te lo dibuja al nfa:
graphnfa = nfa.show_diagram()
graphnfa.draw('nfa.png', prog='dot')