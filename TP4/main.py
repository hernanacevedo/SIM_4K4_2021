from random import uniform

def generarMetodoProvistoPorElLenguaje(cantidad=100):
    # Convierto tipos de datos
    cantidad = int(cantidad)

    # Inicializo datos
    numeros_generados = []

    # Genero lista de numeros aleatorios
    for i in range(0, cantidad):
        aleatorio_decimal = round(uniform(0, 1), 4)
        numeros_generados.append(
             aleatorio_decimal)
    return numeros_generados



def actividad_A():
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
    actividadA=[]
    for i in intervalos:
        contadorApariciones = 0

        item = 0

        while item < cantidad_numeros:
            if numeros_generados[item] >= i[0] and numeros_generados[item] < i[1]:
                contadorApariciones += 1

            item += 1
        actividadA.append(contadorApariciones)
    return intervalos ,actividadA
print(actividad_A())


def actividad_B():
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
    actividadB = []
    for i in intervalos:
        contadorApariciones = 0

        item = 0

        while item < cantidad_numeros:
            if numeros_generados[item] >= i[0] and numeros_generados[item] < i[1]:
                contadorApariciones += 1

            item += 1
        actividadB.append(contadorApariciones)
    return intervalos, actividadB

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
    return  actividadB

print(actividad_B())
print(actividad_B_otra_version())




def actividad_C(semana=10):
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
    actividadC = []
    if semana == 10 or semana == 12 or semana == 14 or semana == 16 or semana == 18:
        for i in intervalos:
            contadorApariciones = 0

            item = 0

            while item < cantidad_numeros:
                if numeros_generados[item] >= i[0] and numeros_generados[item] < i[1]:
                    contadorApariciones += 1

                item += 1
            actividadC.append(contadorApariciones)
        return intervalos, actividadC
    else:
        False
    actividad_B_otra_version()

print(actividad_C())


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
    actividadD = []
    if semana == 8 or semana == 10:
        for i in intervalos:
            contadorApariciones = 0

            item = 0

            while item < cantidad_numeros:

                if numeros_generados[item] >= i[0] and numeros_generados[item] < i[1]:
                    contadorApariciones += 1

                item += 1
            actividadD.append(contadorApariciones)
        return intervalos, actividadD

print(actividad_D())