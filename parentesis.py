

abrir_lista = ["[", "{", "("]
cerrar_lista = ["]", "}", ")"]


def Parentesis(c):
    lista = []
    for i in c:
        if i in abrir_lista:
            lista.append(i)
        elif i in cerrar_lista:
            p = cerrar_lista.index(i)
            if ((len(lista) > 0) and
                    (abrir_lista[p] == lista[len(lista) - 1])):
                lista.pop()
            else:
                return "Incorrecto"
    if len(lista) == 0:
        return "Correcto"
    else:
        return "Incorrecto"


cadena = "[{((())())}]{[]}"
print(cadena, "-", Parentesis(cadena))

cadena = "(({}))[]"
print(cadena, "-", Parentesis(cadena))

cadena = ")([])("
print(cadena, "-", Parentesis(cadena))

cadena = "(){[]([]"
print(cadena, "-", Parentesis(cadena))
