# 3. Función con retorno:

def sumar (a,b): #cuando le doy dos valores 
    resultado = a + b #luego se hace el calculo matemático
    return resultado #return me devuelve un valor, te voy a devolver un valor, variables creadas dentro de la función viven dentro de ella

total = sumar (5,3) # sumar es la función con todo y le da dos parámetros
print(f"La suma es: {total}") #aqui se invoca la variable con la función 
print(sumar(10,20)) #aqui ya se coloca la función con los parámetros y luego da un resultado
print(sumar("hola","mundo"))
