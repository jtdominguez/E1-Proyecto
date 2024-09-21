from sympy import *
init_printing(use_unicode=True)

def EnsamblarBf(XYZ, IEN):
    Bs=[] #en volá podemos armar la matriz vacía al toque
    for i in range(len(XYZ)):
        elementos_del_nodo=[]
        nodo_actual=i+1
        for j in range(len(IEN)):
            elemento_actual=j+1
            if nodo_actual == IEN[j][0] or nodo_actual==IEN[j][1]:
                elementos_del_nodo.append([elementoactual,IEN[j]])
        #print(elementos_del_nodo)
        Bsx=[]
        Bsy=[]
        for j in range (len(elementos_del_nodo)):
            elemento_x=XYZ[elementos_del_nodo[j][2]-1][0]-XYZ[i][0]
            elemento_y=XYZ[elementos_del_nodo[j][2]-1][1]-XYZ[i][1]
            if nodo_actual==elementos_del_nodo[j][2]:
                elemento_x=-1*elemento_x
                elemento_y=-1*elemento_y
            
            
                
            
                
                
        
    return Bs

def EnsamblarLr(XYZ, Ap):
    return

def EnsamblarF(XYZ, Fext):
    return

def Solver(XYZ, IEN, Ap, Fext):
    return

A=Matrix([[-1,1,1],[-2,-3,1],[3,1,-2]])
pprint(A)
