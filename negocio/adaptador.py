
from .procesadorPago import ProcesadorPago


# sistema externo
class PagoCripomonedas:
    def procesar(self, cantidad):
        print(f"Procesando ${cantidad} con cripto.")

# Adaptador
class CriptoAdapter(ProcesadorPago):
    def __init__(self, cripto_pago):
        self.cripto_pago = cripto_pago

    def procesar_pago(self, monto):
        self.cripto_pago.procesar(monto)
