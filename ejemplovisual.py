from visual_automata.fa.dfa import VisualDFA

# Definís el autómata de la misma forma
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

# Muestra el diagrama directamente abriendo una ventana/imagen
print("dibujando...")
dfa.show_diagram(view=True)
