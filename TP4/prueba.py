def actividad_A(semana=5):
    numeros_generados = [0.1931, 0.8967, 0.4885, 0.9556, 0.3583, 0.6396, 0.3843, 0.0999, 0.2068, 0.6413, 0.6139, 0.9631,
                         0.1207, 0.2246, 0.6152, 0.5444, 0.3834, 0.1605, 0.0124, 0.712, 0.6773, 0.1727, 0.3538, 0.2479,
                         0.3669, 0.2546, 0.3975, 0.3662, 0.8565, 0.71, 0.4288, 0.6479, 0.3295, 0.8503, 0.7651, 0.2238,
                         0.1427, 0.9478, 0.3452, 0.5047, 0.2677, 0.0972, 0.3342, 0.6806, 0.5487, 0.9312, 0.0891,
                         0.9219, 0.6543, 0.6611, 0.5636, 0.418, 0.5375, 0.8508, 0.7981, 0.9044, 0.7785, 0.5777,
                         0.9488, 0.8923, 0.3188, 0.2046, 0.3376, 0.355, 0.5869, 0.2027, 0.451, 0.4172, 0.537,
                         0.3164, 0.5062, 0.2894, 0.4321, 0.2213, 0.8321, 0.9447, 0.3629, 0.8442, 0.4376, 0.231, 0.9774,
                         0.3122, 0.5354, 0.741, 0.2191, 0.4433, 0.5806, 0.0289,
                         0.7985, 0.476, 0.4899, 0.8959, 0.2083, 0.8297, 0.067, 0.9894, 0.4015, 0.5851, 0.0124, 0.2052]
    cantidad_numeros=len(numeros_generados)
    intervalos= [(0,0.2499),(0.25,0.5999),(0.6,0.8499),(0.85,1)]
    intervalo1 = [(0,0.2499)]
    intervalo2 = [(0.25,0.5999)]
    intervalo3 = [(0.6,0.8499)]
    intervalo4=[(0.85,1)]
    actividadA=[]
    if semana == 5:
        for i in intervalo1:
            contadorApariciones = 0
            item = 0
            while item < cantidad_numeros:
                if numeros_generados[item] >= i[0] and numeros_generados[item] < i[1]:
                    contadorApariciones += 1

                item += 1
            actividadA.append({"semana 5":
                                   contadorApariciones})
    elif semana == 6:
        for i in intervalo2:
            contadorApariciones = 0

            item = 0

            while item < cantidad_numeros:
                if numeros_generados[item] >= i[0] and numeros_generados[item] < i[1]:
                    contadorApariciones += 1

                item += 1
            actividadA.append({"semana 6": contadorApariciones})
    elif semana == 7:
        for i in intervalo3:
            contadorApariciones = 0

            item = 0

            while item < cantidad_numeros:
                if numeros_generados[item] >= i[0] and numeros_generados[item] < i[1]:
                    contadorApariciones += 1

                item += 1
            actividadA.append({"semana 7": contadorApariciones})
    elif semana == 8:
        for i in intervalo4:
            contadorApariciones = 0

            item = 0

            while item < cantidad_numeros:
                if numeros_generados[item] >= i[0] and numeros_generados[item] < i[1]:
                    contadorApariciones += 1

                item += 1
            actividadA.append({"semana 8": contadorApariciones})
    else:
        False
    return actividadA
def actividad_B_otra_version(semana=5):
    numeros_generados = [0.1931, 0.8967, 0.4885, 0.9556, 0.3583, 0.6396, 0.3843, 0.0999, 0.2068, 0.6413, 0.6139, 0.9631,
                         0.1207, 0.2246, 0.6152, 0.5444, 0.3834, 0.1605, 0.0124, 0.712, 0.6773, 0.1727, 0.3538, 0.2479,
                         0.3669, 0.2546, 0.3975, 0.3662, 0.8565, 0.71, 0.4288, 0.6479, 0.3295, 0.8503, 0.7651, 0.2238,
                         0.1427, 0.9478, 0.3452, 0.5047, 0.2677, 0.0972, 0.3342, 0.6806, 0.5487, 0.9312, 0.0891,
                         0.9219, 0.6543, 0.6611, 0.5636, 0.418, 0.5375, 0.8508, 0.7981, 0.9044, 0.7785, 0.5777,
                         0.9488, 0.8923, 0.3188, 0.2046, 0.3376, 0.355, 0.5869, 0.2027, 0.451, 0.4172, 0.537,
                         0.3164, 0.5062, 0.2894, 0.4321, 0.2213, 0.8321, 0.9447, 0.3629, 0.8442, 0.4376, 0.231, 0.9774,
                         0.3122, 0.5354, 0.741, 0.2191, 0.4433, 0.5806, 0.0289,
                         0.7985, 0.476, 0.4899, 0.8959, 0.2083, 0.8297, 0.067, 0.9894, 0.4015, 0.5851, 0.0124, 0.2052]
    cantidad_numeros = len(numeros_generados)
    intervalos = [(0, 0.1999), (0.20, 0.7499), (0.75,1)]
    intervalo1 = [(0.75, 1)]
    intervalo2 = [(0.20, 0.7499)]
    intervalo3 = [(0, 0.1999)]
    actividadB = []
    if semana==7:
        for i in intervalo1:
            contadorApariciones = 0
            item = 0
            while item < cantidad_numeros:
                if numeros_generados[item] >= i[0] and numeros_generados[item] < i[1]:
                    contadorApariciones += 1

                item += 1
            actividadB.append({"semana 7":
                               contadorApariciones})
    elif semana==5:
        for i in intervalo2:
            contadorApariciones = 0

            item = 0

            while item < cantidad_numeros:
                if numeros_generados[item] >= i[0] and numeros_generados[item] < i[1]:
                    contadorApariciones += 1

                item += 1
            actividadB.append({"semana 5":contadorApariciones})
    elif semana==3:
        for i in intervalo3:
            contadorApariciones = 0

            item = 0

            while item < cantidad_numeros:
                if numeros_generados[item] >= i[0] and numeros_generados[item] < i[1]:
                    contadorApariciones += 1

                item += 1
            actividadB.append({"semana 3":contadorApariciones})
    else:
        False
    return actividadB

def actividad_C(semana=14):
    numeros_generados = [0.1931, 0.8967, 0.4885, 0.9556, 0.3583, 0.6396, 0.3843, 0.0999, 0.2068, 0.6413, 0.6139, 0.9631,
                         0.1207, 0.2246, 0.6152, 0.5444, 0.3834, 0.1605, 0.0124, 0.712, 0.6773, 0.1727, 0.3538, 0.2479,
                         0.3669, 0.2546, 0.3975, 0.3662, 0.8565, 0.71, 0.4288, 0.6479, 0.3295, 0.8503, 0.7651, 0.2238,
                         0.1427, 0.9478, 0.3452, 0.5047, 0.2677, 0.0972, 0.3342, 0.6806, 0.5487, 0.9312, 0.0891,
                         0.9219, 0.6543, 0.6611, 0.5636, 0.418, 0.5375, 0.8508, 0.7981, 0.9044, 0.7785, 0.5777,
                         0.9488, 0.8923, 0.3188, 0.2046, 0.3376, 0.355, 0.5869, 0.2027, 0.451, 0.4172, 0.537,
                         0.3164, 0.5062, 0.2894, 0.4321, 0.2213, 0.8321, 0.9447, 0.3629, 0.8442, 0.4376, 0.231, 0.9774,
                         0.3122, 0.5354, 0.741, 0.2191, 0.4433, 0.5806, 0.0289,
                         0.7985, 0.476, 0.4899, 0.8959, 0.2083, 0.8297, 0.067, 0.9894, 0.4015, 0.5851, 0.0124, 0.2052]
    cantidad_numeros = len(numeros_generados)
    intervalos = [(0, 0.0999), (0.10, 0.3499), (0.35,0.7499), (0.75,0.9499),(0.95,1)]
    intervalo1=[(0, 0.0999)]
    intervalo2= [(0.10, 0.3499)]
    intervalo3 = [(0.35,0.7499)]
    intervalo4 = [(0.75,0.9499)]
    intervalo5 =[(0.95,1)]
    actividadC = []
    if semana == 10:
        for i in intervalo1:
            contadorApariciones = 0
            item = 0
            while item < cantidad_numeros:
                if numeros_generados[item] >= i[0] and numeros_generados[item] < i[1]:
                    contadorApariciones += 1

                item += 1
            actividadC.append({"semana 10": contadorApariciones})
    elif semana == 12:
        for i in intervalo2:
            contadorApariciones = 0

            item = 0

            while item < cantidad_numeros:
                if numeros_generados[item] >= i[0] and numeros_generados[item] < i[1]:
                    contadorApariciones += 1

                item += 1
            actividadC.append({"semana 12": contadorApariciones})
    elif semana == 14:
        for i in intervalo3:
            contadorApariciones = 0

            item = 0

            while item < cantidad_numeros:
                if numeros_generados[item] >= i[0] and numeros_generados[item] < i[1]:
                    contadorApariciones += 1

                item += 1
            actividadC.append({"semana 14": contadorApariciones})
    elif semana == 16:
        for i in intervalo4:
            contadorApariciones = 0

            item = 0

            while item < cantidad_numeros:
                if numeros_generados[item] >= i[0] and numeros_generados[item] < i[1]:
                    contadorApariciones += 1

                item += 1
            actividadC.append({"semana 16": contadorApariciones})
    elif semana == 18:
        for i in intervalo4:
            contadorApariciones = 0

            item = 0

            while item < cantidad_numeros:
                if numeros_generados[item] >= i[0] and numeros_generados[item] < i[1]:
                    contadorApariciones += 1

                item += 1
            actividadC.append({"semana 18": contadorApariciones})
    else:
        False
    return actividadC
def actividad_D(semana=8):
    numeros_generados = [0.1931, 0.8967, 0.4885, 0.9556, 0.3583, 0.6396, 0.3843, 0.0999, 0.2068, 0.6413, 0.6139, 0.9631,
                         0.1207, 0.2246, 0.6152, 0.5444, 0.3834, 0.1605, 0.0124, 0.712, 0.6773, 0.1727, 0.3538, 0.2479,
                         0.3669, 0.2546, 0.3975, 0.3662, 0.8565, 0.71, 0.4288, 0.6479, 0.3295, 0.8503, 0.7651, 0.2238,
                         0.1427, 0.9478, 0.3452, 0.5047, 0.2677, 0.0972, 0.3342, 0.6806, 0.5487, 0.9312, 0.0891,
                         0.9219, 0.6543, 0.6611, 0.5636, 0.418, 0.5375, 0.8508, 0.7981, 0.9044, 0.7785, 0.5777,
                         0.9488, 0.8923, 0.3188, 0.2046, 0.3376, 0.355, 0.5869, 0.2027, 0.451, 0.4172, 0.537,
                         0.3164, 0.5062, 0.2894, 0.4321, 0.2213, 0.8321, 0.9447, 0.3629, 0.8442, 0.4376, 0.231, 0.9774,
                         0.3122, 0.5354, 0.741, 0.2191, 0.4433, 0.5806, 0.0289,
                         0.7985, 0.476, 0.4899, 0.8959, 0.2083, 0.8297, 0.067, 0.9894, 0.4015, 0.5851, 0.0124, 0.2052]
    cantidad_numeros = len(numeros_generados)
    intervalos = [(0, 0.5999),(0.60,1)]
    intervalo1=[(0, 0.5999)]
    intervalo2=[(0.60,1)]
    actividadD = []

    if semana == 8:
        for i in intervalo1:
            contadorApariciones = 0
            item = 0
            while item < cantidad_numeros:
                if numeros_generados[item] >= i[0] and numeros_generados[item] < i[1]:
                    contadorApariciones += 1

                item += 1
            actividadD.append({"semana 8": contadorApariciones})
    elif semana == 10:
        for i in intervalo2:
            contadorApariciones = 0

            item = 0

            while item < cantidad_numeros:
                if numeros_generados[item] >= i[0] and numeros_generados[item] < i[1]:
                    contadorApariciones += 1

                item += 1
            actividadD.append({"semana 10": contadorApariciones})

    else:
        False
    return actividadD


print(actividad_B_otra_version())
print(actividad_A())
print(actividad_C())
print(actividad_D())

def calcularprobabilidad_A(semana=6):
    #23, 42, 19, 16
    if semana==5:
        A=(23*0.25+42*0.35+19*0.25+16*0.15)-(23*0.25)
    elif semana==6:
        A=(23*0.25+42*0.35+19*0.25+16*0.15)-(42*0.35)
    elif semana==7:
        A=19*0.25
    elif semana==8:
        A=16*0.15

    return A
print(calcularprobabilidad_A())

def calcularProbabilidad_B():
    return 0


def calcularProbabilidad_C():
    return 0


def calcularProbabilidad_D():
    return 0

def calcularProbabilidadTotal():
    A=actividad_A()
    B=actividad_B_otra_version()
    C=actividad_C()
    D=actividad_D()

    E=A+B+C+D

    probabilidadA=0
    probabilidadB = 0
    probabilidadC = 0
    probailidadD=0
    #if E >=33:
    #    probTot=round(probabilidadA+probabilidadB+probabilidadC+probabilidadD)/4,4)


