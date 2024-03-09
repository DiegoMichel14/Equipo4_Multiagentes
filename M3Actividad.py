# Diego Alejandro Michel Castro | A01641907
# Ejercicio de semáforos inteligentes
# 7/03/2024

import agentpy as ap

# -------- Definición de agentes -------

class Vehicle(ap.Agent):     # Agente que se acerca a la intersección 
    def setup(self):
        self.eta = self.model.random.randint(1,8) # Se origina un tiempo estimado de llegada entre 1 y 10, eta = estimate time arrival
        self.direction = self.model.random.choice(['N-S', 'E-W']) # Direcciones de aproximación en los cruces
    

class TrafficLight(ap.Agent):  # Agente del semáforo de intersección
    def setup(self, direction):
        self.direction = direction # Dirección que controla el semáforo (De norte a sur o de este a oeste)
        self.state = 'AMARILLO'   # Se incia con un estado actual amarillo al no haber coches cerca
        
    def change_state(self, new_state):   # Función para el cambio de estado dependiendo de los agentes coche 
        self.state = new_state

# ----------- Definición del modelo/ambiente a trabajar -------------

class IntersectionModel(ap.Model):  # Modelo controlado por semáforos inteligentes

    def setup(self):
        self.vehicles = ap.AgentList(self, self.p['num_vehicles'], Vehicle)  # Se crean vehículos dado el número de los mismos en el diccionario de parámetros
        
        #Crear dos semáforos para las direcciones correspondientes
        directions = ['N-S', 'E-W'] # Direcciones que controlan los semáforos
        self.traffic_lights = ap.AgentList(self, [TrafficLight(self, direction=d) for d in directions])  # Creación de uno o más semáforos
    
    def step(self):

        # Determinamos la presencia y tiempo estimadoi de llegada de los vehículos para cada direccion
        ns_vehicles_nearby = any(v.eta < 5 and v.direction == 'N-S' for v in self.vehicles) # Tomamos un vehículo cercano a la intersección si si tiempo estimado de llegada es menor a 5
        ew_vehicles_nearby = any(v.eta < 5 and v.direction == 'E-W' for v in self.vehicles)
        
        #Lógica para cambiar los estados del semáforo
        if ns_vehicles_nearby and not ew_vehicles_nearby:
            self.traffic_lights[0].state = 'VERDE' # Norte-Sur a verde
            self.traffic_lights[1].state = 'ROJO' # Este-Oeste a rojo
        if ew_vehicles_nearby and not ns_vehicles_nearby:
            self.traffic_lights[0].state = 'ROJO' # Norte-Sur a rojo
            self.traffic_lights[1].state = 'VERDE' # Este-Oeste a verde
        else:
            # Si ambos o ninguno de los lados tienen vehículos cercanos los dos se colocan en amarillo
            for light in self.traffic_lights:
                light.state = 'AMARILLO'
    
    def update(self):
        pass
    
    def end(self):
        # Resumen de resultados al final de la simulación
        for light in self.traffic_lights:
            print(f"Semaforo {light.direction}: {light.state}")
    
    def run_model(self, steps):   # Método para no mostrar información de más como los pasos completados, ayuda mucho a mantener una salida
        self.setup()             # limpia
        for step in range(steps):
            self.step()
        self.end()
    
# -------------- Ejecuciones/runs ----------------

parameters = {   # Diccionario de parámetros para la simulación
    'num_vehicles': 10
}

model = IntersectionModel(parameters)  # Creación del modelo definodo con parámetros dados
results = model.run_model(steps = 100)




