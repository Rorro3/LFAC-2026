from automata.fa.dfa import DFA

# Definición de tu autómata
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

# Evaluar si una cadena es aceptada o rechazada (devuelve True o False)
print(dfa.accepts_input('101'))  # Devuelve: True
print(dfa.accepts_input('100'))  # Devuelve: False

# Ver el paso a paso detallado de los estados por los que pasa
print(list(dfa.read_input_stepwise('101')))
# Muestra la ruta: ['q0', 'q1', 'q0', 'q1']

from automata.fa.nfa import NFA

# Definición del AFND
nfa = NFA(
    states={'q0', 'q1', 'q2'},
    input_symbols={'0', '1'},
    transitions={
        # En q0 con '0' puede quedarse en q0 O avanzar a q1
        'q0': {'0': {'q0', 'q1'}, '1': {'q0'}},
        # En q1 con '1' pasa a q2
        'q1': {'1': {'q2'}},
        # q2 es el estado final y atrapa el resto de símbolos
        'q2': {'0': {'q2'}, '1': {'q2'}}
    },
    initial_state='q0',
    final_states={'q2'}
)

# --- PRUEBAS DE CADENAS ---
# Devuelve True o False directamente
print(nfa.accepts_input('0010'))  # True (contiene '01')
print(nfa.accepts_input('0000'))  # False

# --- PASO A PASO (Conjuntos de estados activos) ---
# Muestra los estados posibles en cada paso del procesamiento
pasos = list(nfa.read_input_stepwise('01'))
for i, estados_actuales in enumerate(pasos):
    print(f"Paso {i}: Estados activos = {estados_actuales}")