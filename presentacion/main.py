from datos.pedido import Pedido
from negocio.estrategiaCalculo import CalculoConDescuento, CalculadorCosto
from negocio.recivo import GeneradorReciboTexto
from negocio.procesadorPago import ProcesadorPagoFactory
from negocio.sistemaRestaurante import SistemaRestaurante
from negocio.adaptador import CriptoAdapter , PagoCripomonedas




def main():
    # Configurar la estrategia de cálculo (con descuento o sin descuento)
    descuento = CalculoConDescuento(0.1)
    calculador_costo = CalculadorCosto(descuento)

    # Configurar el procesador de pago (puedes cambiar a "tarjeta", "efectivo", o usar el adaptador de cripto)
    procesador_pago = ProcesadorPagoFactory.crear_procesador("paypal")
    
    # Alternativa con cripto:
    # cripto_pago = CriptoAdapter(PagoCripomonedas())
    # procesador_pago = cripto_pago

    # Configurar el generador de recibos
    generador_recibo = GeneradorReciboTexto()

    # Crear instancia del sistema restaurante
    sistema = SistemaRestaurante(procesador_pago, generador_recibo, calculador_costo)

    # Crear y configurar un pedido
    pedido = Pedido()
    pedido.agregar_item("Pollo", 20, 2)
    pedido.agregar_item("Jugo", 6, 1)

    # Procesar el pedido
    sistema.realizar_pedido(pedido)

if __name__ == "__main__":
    main()
