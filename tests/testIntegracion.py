import unittest
from localRopaTest.src.tienda import Tienda

class testGenerales(unittest):
    #Corre antes que todos los test
    def setUp(self):
        self.tienda = Tienda()

    def test_agregar_empleado(self):
        #given
        self.tienda.agregarEmpleado("Matias")
        self.tienda.agregarEmpleado("Maria")
        self.tienda.agregarEmpleado("Lautaro")
        self.tienda.agregarEmpleado("Lucia")

        #When
        empleado = self.tienda.buscarEmpleadoPorNombre("Matias")

        #Then
        self.assertEqual(self.tienda.cantidadDeEmpleados, 4)
        self.assertEqual(empleado.nombre(), "Matias")

    def test_agregar_cliente(self):
        #Given 
        self.tienda.agregarCliente("Marcos", 2000) #2000 es el crédito de compra
        self.tienda.agregarCliente("Juan", 150)
        self.tienda.agregarCliente("Ismael", 340)

        #Then
        self.assertEqual(self.tienda.cantidadDeClientes(), 3)

    def test_agregar_stock(self):
        #Given
        # agregarStock(prenda, stock_total, precio_por_unidad)
        self.tienda.agregarStock("Remera XS", 3, 100)
        self.tienda.agregarStock("Remera S", 2, 120)
        self.tienda.agregarStock("Remera rallada", 1, 10)
        self.tienda.agregarStock("Pantalon largo", 2, 5440)

        #Then 
        self.assertEqual(self.tienda.stockPorPrenda("Remera XS"), 3)
        self.assertEqual(self.tienda.cantidadDeStockTotal(), 8)
        self.assertEqual(self.tienda.cantidadDePrendas(), 4)

    def test_venta(self):
        #Given
        # vender(prenda, cliente, empleadp)
        self.tienda.vender("Remera rallada", "Marcos", "Matias")

        #Then
        self.assertEqual(self.tienda.stockPorPrenda("Remera rallada"), 0)
        self.assertEqual(self.tienda.ventasPorEmpleadp("Matias", 1))
        self.assertEquals(self.tienda.creditoPorCliente("Marcos"), 2000 - 100)

    def test_venta_inexistente(self):
        #Then
        self.assertRaises(Exception,  self.tienda.vender( "Basura", "Marcos", "Matias"))

    def test_venta_sin_stock(self):
        #Remera rallada no tiene stock pq se vendió el único en el test de la linea 48
        #Then
        self.assertRaises(Exception,  self.tienda.vender( "Remera rallada", "Marcos", "Matias"))

    def test_venta_sin_credito(self):
        #A juan no le alcanza su credito (150) para pagar el pantalón largo (5440)
        self.assertRaises(Exception,  self.tienda.vender( "Pantalon largo", "Juan", "Matias"))

    def test_ranking_ventas(self):
        self.tienda.vender("Remera S", "Marcos", "Matias")
        self.tienda.vender("Remera XS", "Juan",  "Lucia")  

        #Matias lleva 2 ventas mientras que Lucia 1
        self.assertEquals(self.tienda.empleadoDelMes(), "Matias")
        #Marcos tiene más compras que nadie
        self.assertEquals(self.tienda.clienteConMayorCantidadDeCompras(), "Marcos")


    


