from abc import ABC, abstractmethod
class IGeneradorRecibo(ABC):
    @abstractmethod
    def generar_recibo(self, pedido, total):
        pass

class GeneradorReciboTexto(IGeneradorRecibo):
    def generar_recibo(self, pedido, total):
        recibo = "Recibo:\n"
        for item in pedido.items:
            recibo = recibo + f'{item["cantidad"]}x {item["nombre"]} - ${item["precio"] * item["cantidad"]}\n'
        recibo = recibo + f"Total: ${total}\n"
        return recibo