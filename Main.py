import simpy 
import random 

env = simpy.Environment()
ram = simpy.Container(env, init=100, capacity=100)
cpu = simpy.Resource(env, capacity=1)
velocidadCpu = 3
tiempoDeLlegada = 10