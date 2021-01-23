def turing_M (state = None, #estados de la maquina de turing
              blank = None, #simbolo blanco del alfabeto dela cinta
              rules = [],   #reglas de transicion
              tape = [],    #cinta
              final = None,  #estado valido y/o final
              pos = 0):#posicion siguiente de la maquina de turing

    st = state
    if not tape: tape = [blank]
    if pos <0 : pos += len(tape)
    if pos >= len(tape) or pos < 0 : raise Exception ("Se inicializa mal la posición")

    rules = dict(((s0, v0), (v1, dr, s1)) for (s0, v0, v1, dr, s1) in rules)
    """
Estado	Símbolo leído	Símbolo escrito	       Mov. 	Estado sig.
  p(s0)	       1(v0)	         x(v1)         R(dr)	     p(s1)
"""
    while True:
        print (st, '\t', end=" ")
        for i, v in enumerate(tape):
             if i==pos: print ("[%s]"%(v,),end=" ")
             else: print (v, end=" ")
        print()
        
        if st == final: break #Si ya llegó al estado final, se rompe el ciclo
        if (st, tape[pos]) not in rules: break #Si no encuentra reglas, se rompe el ciclo
        
        (v1,dr,s1) = rules [(st, tape[pos])]
        tape[pos]=v1 #rescribe el simbolo de la cinta
    
    #movimiento del cabezal
        if dr == 'left':
            if pos > 0: pos -= 1
            else: tape.insert(0, blank)
        if dr == 'right':
            pos += 1
            if pos >= len(tape): tape.append(blank)
        st = s1


opcion = 0
while opcion != 5:
    print("\n----------------------MÁQUINAS DE TURING----------------------")
    print("\nBIENVENIDO, SELECCIONE LA MÁQUINA DE TURING QUE DESEE EJECUTAR")
    print("\n1.-COPIA LOS 1'S INGRESADOS Y LOS COLOCA DESPUÉS DE UN O\n"
         +"2.-CALCULA EL SUCESOR DE UN NÚMERO BINARIO\n"
         +"3.-CALCULA LA SUMA DE DOS NÚMEROS\n"
         +"4.-INTEGRANTES DEL EQUIPO\n"
         +"5.-SALIR")
    opcion = int(input("Ingresa una opción: "))


    if opcion == 1:
        print("COPIA LOS 1'S INGRESADOS Y LOS COLOCA DESPUÉS DE UN O")
        entrada = input("Ingrese los simbolos: ")
        turing_M (state = 's1', #estado inicial de la maquina de turing
                  blank = '0', #simbolo blanco de el alfabeto dela cinta
                  tape = list(entrada),#inserta los elementos en la cinta
                  final = 's6',  #estado valido y/o final
                  rules = map(tuple,#reglas de transicion
                          [
                          "s1 1 0 right s2".split(),
                          "s2 1 1 right s2".split(),
                          "s2 0 0 right s3".split(),
                          "s3 0 1 left s4".split(),
                          "s3 1 1 right s3".split(),
                          "s4 1 1 left s4".split(),
                          "s4 0 0 left s5".split(),
                          "s5 1 1 left s5".split(),
                          "s5 0 1 right s1".split(),
                          ]   
                         )
             ) 
    
    elif opcion == 2:
        print("CALCULA EL NúMERO CONSECUTIVO DE UN NUMERO DADO EN BINARIO")
        entrada2 = input("Ingrese el número binario: ")
        turing_M (state = 'q0', #estado inicial de la maquina de turing
                  blank = 'B', #simbolo blanco de el alfabeto dela cinta
                  tape = list(entrada2),#inserta los elementos en la cinta
                  final = 'q2',  #estado valido y/o final
                  rules = map(tuple,#reglas de transicion
                          [
                          "q0 0 0 right q0".split(),
                          "q0 1 1 right q0".split(),
                          "q0 B B left q1".split(),
                          "q1 0 1 right q2".split(),
                          "q1 1 0 left q1".split(),
                          "q1 0 1 left q2".split(),
                          "q1 B 1 left q2".split(),
                          ]   
                         )
             ) 

    elif opcion == 3:
        print("CALCULA LA SUMA DE DOS NÚMEROS")
        entrada3 = input("Ingrese la cadena: ")
        turing_M (state = 'q0', #estado inicial de la maquina de turing
                  blank = 'B', #simbolo blanco de el alfabeto dela cinta
                  tape = list(entrada3),#inserta los elementos en la cinta
                  final = 'q4',  #estado valido y/o final
                  rules = map(tuple,#reglas de transicion
                          [
                          "q0 1 1 right q1".split(),
                          "q1 1 1 right q1".split(),
                          "q1 0 1 right q2".split(),
                          "q2 1 1 right q2".split(),
                          "q2 B B left q3".split(),
                          "q3 1 B right q4".split(),
                          ]   
                         )
             )

    elif opcion == 4:
        print("\nPrograma elaborado por:"+"\n"
        +"<<Mis Oy Cristina de Jesus>>"+"\n"
        +"<<Poot Can Gener Emmanuel>>"+"\n"
        +"<<Uicab Balam Nanci Arai>>")

    elif opcion == 5:
        print("¡Finalizado con exito!")
    else:
        print("\n¡¡¡La opción seleccionada es incorrecta!!!")  
