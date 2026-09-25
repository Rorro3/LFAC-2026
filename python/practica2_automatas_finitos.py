from visual_automata.fa.dfa import VisualDFA
from automata.fa.nfa import NFA
#Ejercicio 1. Construir autómatas finitos para los siguientes lenguajes:
#a. Cadenas sobre Σ = {0} de longitud par.

dfa = VisualDFA(
    states={'q0', 'q1'},
    input_symbols={'0'},
    transitions={
        'q0': {'0': 'q1'},
        'q1': {'0': 'q0'}
    },
    initial_state='q0',
    final_states={'q0'}
)

#print("dibujando...")
#dfa.show_diagram(view=True)
#print(dfa.dfa.accepts_input('00'))
#print(dfa.dfa.accepts_input('0'))

#b. Cadenas sobre Σ = {0, 1} con cantidad par de ceros.
dfa2 = VisualDFA(
    states={'q0', 'q1'},
    input_symbols={'0','1'},
    transitions={
        'q0': {'0': 'q1', '1':'q0'},
        'q1': {'0': 'q0', '1':'q1'}
    },
    initial_state='q0',
    final_states={'q0'}
)
#print("dibujando...")
#dfa2.show_diagram(view=True)
#print(dfa2.dfa.accepts_input('011010100100'))
#print(dfa2.dfa.accepts_input('0110101001000'))

#c. Cadenas sobre Σ = {0, 1} con cantidad impar de unos.
dfa3 = VisualDFA(
    states={'q0', 'q1'},
    input_symbols={'0','1'},
    transitions={
        'q0': {'0': 'q0', '1':'q1'},
        'q1': {'0': 'q1', '1':'q0'}
    },
    initial_state='q0',
    final_states={'q1'}
)
#print("dibujando...")
#dfa3.show_diagram(view=True)
#print(dfa3.dfa.accepts_input('011010100100'))
#print(dfa3.dfa.accepts_input('01101010010001'))
#print(dfa3.dfa.accepts_input('1'))

#d. Cadenas sobre Σ = {0, 1} con cantidad par de ceros y cantidad impar de unos.
#seria la interseccion de b y c
dfad = VisualDFA(
    states={'q0', 'q1', 'q2', 'q3'},
    input_symbols={'0', '1'},
    transitions={
        'q0': {'0': 'q3', '1': 'q1'},
        'q1': {'0': 'q2', '1': 'q0'},
        'q2': {'0': 'q1', '1': 'q3'},
        'q3': {'0': 'q0', '1': 'q2'}
    },
    initial_state='q0',
    final_states={'q1'}
)
#dfad.show_diagram(view=True)
#print(dfad.dfa.accepts_input('1'))
#print(dfad.dfa.accepts_input('10'))

#Ejercicio 2. Construir autómatas finitos para los siguientes lenguajes sobre Σ = {0, 1}:
#a. Cadenas que comiencen con 010.
dfaa2 = VisualDFA(
    states={'q0', 'q1', 'q2', 'q3','t'},
    input_symbols={'0', '1'},
    transitions={
        'q0': {'0': 'q1', '1': 't'},
        'q1': {'0': 't', '1': 'q2'},
        'q2': {'0': 'q3', '1': 't'},
        'q3': {'0': 'q3', '1': 'q3'},
        't':{'0':'t','1':'t'}
    },
    initial_state='q0',
    final_states={'q3'}
)
#dfaa2.show_diagram(view=True)
#print(dfaa2.dfa.accepts_input('10100101001'))
#print(dfaa2.dfa.accepts_input('010010101010100'))
#print(dfaa2.dfa.accepts_input('010'))

#b. Cadenas que terminen con 010.
nfab2 = NFA(
    states={'q0', 'q1', 'q2','q3'},
    input_symbols={'0', '1'},
    transitions={
        'q0': {'0': {'q0', 'q1'}, '1': {'q0'}},
        'q1': {'0': set(), '1': {'q2'}},
        'q2': {'0': {'q3'}, '1': set()},
        'q3': {'0': set(), '1': set()}
    },
    initial_state='q0',
    final_states={'q3'}
)
#graphnfab2 = nfab2.show_diagram()
#graphnfab2.draw('nfa_termina_010.png', prog='dot')
#print(nfab2.accepts_input('10010')) 
#print(nfab2.accepts_input('0101'))   

#c. Cadenas que contengan la subcadena 000.
nfac2 = NFA(
    states={'q0', 'q1', 'q2','q3'},
    input_symbols={'0', '1'},
    transitions={
        'q0': {'0': {'q0', 'q1'}, '1': {'q0'}},
        'q1': {'0':{'q2'}, '1': set()},
        'q2': {'0': {'q3'}, '1': set()},
        'q3': {'0': {'q3'}, '1': {'q3'}}
    },
    initial_state='q0',
    final_states={'q3'}
)
#graphnfac2 = nfac2.show_diagram()
#graphnfac2.draw('nfacontiene000.png', prog='dot')
#print(nfac2.accepts_input('000')) 
#print(nfac2.accepts_input('1010100100010101001')) 
#print(nfac2.accepts_input('00011001010')) 
#print(nfac2.accepts_input('101001000')) 
#print(nfac2.accepts_input('00101010010')) 

#d. Cadenas que no contengan la subcadena 000.
#paso el c a dfa
dfa_equivalente = VisualDFA(
    states={'A', 'B', 'C', 'D', 'E'},
    input_symbols={'0', '1'},
    transitions={
        'A': {'0': 'B', '1': 'A'},  
        'B': {'0': 'C', '1': 'A'},  
        'C': {'0': 'D', '1': 'A'},  
        'D': {'0': 'D', '1': 'E'},  
        'E': {'0': 'D', '1': 'E'}   
    },
    initial_state='A',
    final_states={'C', 'D', 'E'}
)
#intercambio estados finales con no finales
#osea complemento
dfa_equivalente_complemento = VisualDFA(
    states={'A', 'B', 'C', 'D', 'E'},
    input_symbols={'0', '1'},
    transitions={
        'A': {'0': 'B', '1': 'A'},  
        'B': {'0': 'C', '1': 'A'},  
        'C': {'0': 'D', '1': 'A'},  
        'D': {'0': 'D', '1': 'E'},  
        'E': {'0': 'D', '1': 'E'}   
    },
    initial_state='A',
    final_states={'A', 'B'}  
)
#dfa_equivalente_complemento.show_diagram(view=True)
#print(dfa_equivalente_complemento.dfa.accepts_input('000')) 
#print(dfa_equivalente_complemento.dfa.accepts_input('1010100100010101001')) 
#print(dfa_equivalente_complemento.dfa.accepts_input('00011001010')) 
#print(dfa_equivalente_complemento.dfa.accepts_input('101001000')) 
#print(dfa_equivalente_complemento.dfa.accepts_input('00101010010')) 

'''e. Cadenas que contengan la subcadena 000 exactamente una vez
(la cadena 0000 no pertenece a este lenguaje).'''
dfae2 = VisualDFA(
    states={'q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 't'},
    input_symbols={'0', '1'},
    transitions={
        'q0': {'0': 'q1', '1': 'q0'},
        'q1': {'0': 'q2', '1': 'q0'},
        'q2': {'0': 'q3', '1': 'q0'},
        'q3': {'0': 't',  '1': 'q4'},
        'q4': {'0': 'q5', '1': 'q4'}, 
        'q5': {'0': 'q6', '1': 'q4'},  
        'q6': {'0': 't',  '1': 'q4'}, 
        't':  {'0': 't',  '1': 't'}
    },
    initial_state='q0',
    final_states={'q3', 'q4', 'q5', 'q6'} 
)
#dfae2.show_diagram(view=True)
#print(dfae2.dfa.accepts_input('000')) 
#print(dfae2.dfa.accepts_input('0000')) 
#print(dfae2.dfa.accepts_input('0001010100100')) 
#print(dfae2.dfa.accepts_input('10101001010'))

#f. Cadenas que no contengan la subcadena 000 ni la 010.
dfaf2 = VisualDFA(
    states={'q0', 'q1', 'q2', 'q3', 't'},
    input_symbols={'0', '1'},
    transitions={
        'q0': {'0': 'q1', '1': 'q0'},  
        'q1': {'0': 'q2', '1': 'q3'},  
        'q2': {'0': 't', '1': 'q3'},  
        'q3': {'0': 't', '1': 'q0'},  
        't':{'0':'t','1':'t'}   
    },
    initial_state='q0',
    final_states={'q3'}  
)
#dfaf2.show_diagram(view=True)
#print(dfaf2.dfa.accepts_input('000')) 
#print(dfaf2.dfa.accepts_input('101001001001001010')) 

'''Ejercicio 7. Dar un autómata finito determinístico que acepte todas las cadenas sobre el
alfabeto {𝑎, 𝑏, 𝑐} que cumplan simultáneamente las siguientes reglas:'''
#a. Cada 𝑎 debe estar seguida inmediatamente de una b
dfaa7 = VisualDFA(
    states={'q0', 'q1', 'q2', 't'},
    input_symbols={'a', 'b','c'},
    transitions={
        'q0': {'a': 'q1', 'b': 'q0', 'c':'q0'},  
        'q1': {'a': 't', 'b': 'q2', 'c':'t'},  
        'q2': {'a': 'q1', 'b': 'q2', 'c':'q2'}, 
        't':{'a':'t','b':'t','c':'t'}   
    },
    initial_state='q0',
    final_states={'q0','q2'}  
)
#dfaa7.show_diagram(view=True)
#print(dfaa7.dfa.accepts_input('ababababababbbbbbbccccab')) 
#print(dfaa7.dfa.accepts_input('bbcbbcbcbcbcbbcba')) 
#print(dfaa7.dfa.accepts_input('')) 

#b. La cantidad de 𝑏 debe ser par.
dfab7 = VisualDFA(
    states={'q0', 'q1'},
    input_symbols={'a', 'b','c'},
    transitions={
        'q0': {'a': 'q0', 'b': 'q1', 'c':'q0'},  
        'q1': {'a': 'q1', 'b': 'q0', 'c':'q1'}   
    },
    initial_state='q0',
    final_states={'q0'}  
)
#dfab7.show_diagram(view=True)
#print(dfab7.dfa.accepts_input('bb'))
#print(dfab7.dfa.accepts_input('bbaccacacacaccacac'))
#print(dfab7.dfa.accepts_input('acaccacacacaccabacaccacacbacacacacacac'))
#print(dfab7.dfa.accepts_input('bacaccabcacacabb'))

#c. La cadena no debe terminar en 𝑐.
dfac7 = VisualDFA(
    states={'q0', 'q1'},
    input_symbols={'a', 'b', 'c'},
    transitions={
        'q0': {'a': 'q0', 'b': 'q0', 'c': 'q1'},  
        'q1': {'a': 'q0', 'b': 'q0', 'c': 'q1'}
    },
    initial_state='q0',
    final_states={'q0'}  
)
dfac7.show_diagram(view=True)
print(dfac7.dfa.accepts_input('bbc'))
print(dfac7.dfa.accepts_input('bbcababbabcbabab'))
print(dfac7.dfa.accepts_input('ccccca'))

'''Ejercicio 8. Decimos que una subcadena de otra cadena es un grupo de repetición (o meseta)
si todos sus símbolos son iguales y ninguno de los símbolos adyacentes a ella coincide con los
que la forman. Por ejemplo, en la palabra aaabbbbaaa hay tres grupos de repetición (aaa, bb
bb y aaa).
Se considera el lenguaje ℒ sobre el alfabeto {𝑎, 𝑏} formado por las cadenas en las que, si
existen grupos de repetición, su longitud es alternativamente par e impar. Es decir, la palabra
aabbbaaaab pertenece al lenguaje ℒ, ya que esta formada por cuatro grupos de repetición de
longitudes 2, 3, 4 y 1, mientras que la palabra bbaa no pertenece, al estar formada por dos
grupos de repetición de longitudes 2 y 2.
Dar un autómata finito que acepte ℒ.
'''
nfa8 = NFA(
    states={'q0', 'qa_inicial', 'qa_par','qb_impar','qb_impar2',
            'qb_inicial','qb_par','qa_impar','qa_impar2'},
    input_symbols={'a','b'},
    transitions={
        'q0': {'a': {'qa_inicial','qa_impar'}, 'b': {'qb_inicial','qb_impar'}},
        'qa_inicial': {'a': {'qa_par'}, 'b':set()},
        'qa_par': {'a': {'qa_inicial'}, 'b': {'qb_impar'}},
        'qb_impar': {'a': {'qa_inicial'}, 'b': {'qb_impar2'}},
        'qb_impar2':{'a':set(), 'b':{'qb_impar'}},
        'qb_inicial':{'a':set(), 'b':{'qb_par'}},
        'qb_par':{'a':{'qa_impar'},'b':{'qb_inicial'}},
        'qa_impar':{'a':{'qa_impar2'},'b':{'qb_inicial'}},
        'qa_impar2':{'a':{'qa_impar'},'b':set()}
    },
    initial_state='q0',
    final_states={'q0','qa_par','qb_par','qb_impar','qa_impar'}
)
#graphnfa8 = nfa8.show_diagram()
#graphnfa8.draw('nfa8.png', prog='dot')
#print(nfa8.accepts_input('aabbbaab')) 
#print(nfa8.accepts_input('aabb')) 
#print(nfa8.accepts_input('a')) 