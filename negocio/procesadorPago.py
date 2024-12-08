from abc import ABC, abstractmethod

class ProcesadorPago(ABC):
    @abstractmethod
    def procesar_pago(self, monto):
        pass

class PagoTarjeta(ProcesadorPago):
    def procesar_pago(self, monto):
        print(f"Procesando pago de ${monto} con tarjeta de crédito.")

class PagoEfectivo(ProcesadorPago):
    def procesar_pago(self, monto):
        print(f"Procesando pago de ${monto} en efectivo.")

class PagoPayPal(ProcesadorPago):
    def procesar_pago(self, monto):
        print(f"Procesando pago de ${monto} a través de PayPal.")
        
class ProcesadorPagoFactory:
    @staticmethod
    def crear_procesador(tipo):
        if tipo == "tarjeta":
            return PagoTarjeta()
        elif tipo == "efectivo":
            return PagoEfectivo()
        elif tipo == "paypal":
            return PagoPayPal()
        else:
            raise ValueError("Tipo de procesador de pago no soportado.")