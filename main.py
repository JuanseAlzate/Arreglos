import math
import functions
from fastapi import FastAPI
from datatypes import dt
app = FastAPI()

@app.post("/exer1")
def ejercicio1(body: dt.Req):

    print(body.list)
    if len(body.list) != 10:
        return {"El arreglo solo recibe 10 elementos"}

    return functions.max_num_pos(body.list)

@app.post("/exer2")
def ejercicio2(body: dt.Req):

    print(body.list)
    if len(body.list) != 10:
        return {"El arreglo solo recibe 10 elementos"}

    maxPrime = -1
    pos = -1

    for i, num in enumerate(body.list):
        if functions.primos(num) and num > maxPrime:
            maxPrime = num
            pos = i

    if pos == -1:
        return {"No hay números primos"}
    else:
        return {"Número mayor primo": maxPrime, "Posición": pos}

@app.get("/exer3")
def ejercicio3():

    primes = []
    for i in range(100, 300 + 1):
        if functions.primos(i):
            primes.append(i)
        if len(primes) == 10:
            break
    return {"Números primos entre 100 y 300": primes}

@app.post("/exer4")
def ejercicio4(body: dt.Req):

    print(body.list)
    if len(body.list) != 10:
        return {"El arreglo solo recibe 10 elementos"}

    pos = [i for i, num in enumerate(body.list) if num % 10 == 4]
    return {"Posiciones": pos}

@app.post("/exer5")
def ejercicio5(body: dt.Req):

    print(body.list)
    if len(body.list) != 10:
        return {"El arreglo solo recibe 10 elementos"}

    may = body.list[0]
    for i in range(len(body.list)):
        if body.list[i] > may:
            may = body.list[i]
    rep = body.list.count(may)

    return {"Número mayor": may, "Repeticiones": rep}

@app.post("/exer6")
def ejercicio6(body : dt.Req):

    print(body.list)
    if len(body.list) != 10:
        return {"El arreglo solo recibe 10 elementos"}

    prom = sum(body.list) // len(body.list)
    inList = prom in body.list
    return {"Promedio": prom, "Está en el arreglo": inList }

@app.post("/exer7")
def sdm(body: dt.Req):

    print(body.list)
    if len(body.list) != 10:
        return {"El arreglo solo recibe 10 elementos"}

    maxSum = -1
    pos = -1

    for i, num in enumerate(body.list):
        sum = functions.sd(num)
        if sum > maxSum:
            maxSum = sum
            pos = i

    return {"Posición": pos, "Mayor suma": maxSum}

@app.post("/exer8")
def ejercicio8(body: dt.Req):

    print(body.list)
    if len(body.list) != 10:
        return {"El arreglo solo recibe 10 elementos"}

    fact = [math.factorial(num) for num in body.list]
    ans = [{"Número": num, "Y su Factorial": fact} for num, fact in zip(body.list, fact)]
    return {"Los factoriales": ans}

@app.post("/exer9")
def ejercicio9(body: dt.Req):

    print(body.list)
    if len(body.list) != 10:
        return {"El arreglo solo recibe 10 elementos"}

    nums = {num: list(range(1, num + 1)) for num in body.list}
    return {"Números entre el 1 y el número dado": nums}