class SistemaRestaurante:
    def __init__(self, procesador_pago, generador_recibo, calculador_costo):
        self.procesador_pago = procesador_pago
        self.generador_recibo = generador_recibo
        self.calculador_costo = calculador_costo

    def realizar_pedido(self, pedido):
       
        # Calcular el total del pedido
        total = self.calculador_costo.calcular_total(pedido)
        
        # Generar recibo
        recibo = self.generador_recibo.generar_recibo(pedido, total)
        print(recibo)
        
        # Procesar el pago
        self.procesador_pago.procesar_pago(total)
