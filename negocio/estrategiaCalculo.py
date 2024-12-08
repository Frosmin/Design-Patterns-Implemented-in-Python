from abc import ABC, abstractmethod

#Strategy    

class EstrategiaCalculo(ABC):
    @abstractmethod
    def calcular(self, pedido):
        pass

class CalculoNormal(EstrategiaCalculo):
    def calcular(self, pedido):
        return sum(item["precio"] * item["cantidad"] for item in pedido.items)

class CalculoConDescuento(EstrategiaCalculo):
    def __init__(self, descuento):
        self.descuento = descuento

    def calcular(self, pedido):
        total = sum(item["precio"] * item["cantidad"] for item in pedido.items)
        return total * (1 - self.descuento)   
    
class CalculadorCosto:
    def __init__(self, estrategia: EstrategiaCalculo):
        self.estrategia = estrategia

    def calcular_total(self, pedido):
        return self.estrategia.calcular(pedido)   