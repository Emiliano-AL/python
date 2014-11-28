"""
Ejemplo de un módulo en python. Contiene una variable llamda mi_variable, 
una function llamada mi_funcion y una clase llamada MiClase.
"""

mi_variable = 0

def mi_funcion():
    """
    Función de ejemplo
    """
    return mi_variable
    
class MiClase:
    """
    Clase ejemplo.
    """

    def __init__(self):
        self.variable = mi_variable
        
    def asigna_variable(self, nuevo_valor):
        """
        Asigna un valor nuevo a self.variable
        """
        self.variable = nuevo_valor
        
    def regresa_variable(self):
        return self.variable