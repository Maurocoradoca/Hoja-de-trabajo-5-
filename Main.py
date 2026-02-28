import simpy 
import random 

env = simpy.Environment()
ram = simpy.Container(env, init=100, capacity=100)
cpu = simpy.Resource(env, capacity=1)
velocidadCpu = 3
tiempoDeLlegada = 10
velocidad_global_cpu = 3 
lista_tiempos = []

def proceso(env, nombre, ram_sistema, cpu_sistema, instrucciones_totales, memoria_necesaria):
    llegada = env.now
    print(f"T={llegada}: {nombre} llega (pide {memoria_necesaria} RAM)")
    yield ram_sistema.get(memoria_necesaria)
    while instrucciones_totales > 0:
        with cpu_sistema.request() as req:
            yield req 
            print(f"T={env.now}: {nombre} inicia ejecución ({instrucciones_totales} pendientes)")
            instrucciones_totales -= velocidad_global_cpu
            yield env.timeout(1)
        if instrucciones_totales > 0:
            decision = random.randint(1, 2)
            if decision == 1:
                yield env.timeout(1)
    yield ram_sistema.put(memoria_necesaria)
    tiempo_total = env.now - llegada
    lista_tiempos.append(tiempo_total) 
    print(f"T={env.now}: {nombre} termina (estuvo {tiempo_total} unidades)")