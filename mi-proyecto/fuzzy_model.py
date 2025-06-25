# fuzzy_model.py

import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# (define variables, funciones de pertenencia, reglas, sistema_calidad como ya lo tienes...)

# Sistema de control
sistema_calidad = ctrl.ControlSystem([
    # ... tus reglas
])

def evaluar_calidad_cafe(acidez_val, cafeina_val, humedad_val, aroma_val):
    try:
        simulador = ctrl.ControlSystemSimulation(sistema_calidad)
        simulador.input['acidez'] = np.clip(acidez_val, 0, 8)
        simulador.input['cafeina'] = np.clip(cafeina_val, 0, 3)
        simulador.input['humedad'] = np.clip(humedad_val, 0, 12)
        simulador.input['aroma'] = np.clip(aroma_val, 0, 10)
        simulador.compute()
        calidad_val = simulador.output['calidad']

        if calidad_val <= 40:
            categoria = "Baja"
        elif 40 < calidad_val <= 70:
            categoria = "Media"
        else:
            categoria = "Alta"

        return round(calidad_val, 1), categoria
    except Exception as e:
        return 0, "Error"
