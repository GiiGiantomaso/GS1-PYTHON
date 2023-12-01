class Farmacia:
   def __init__(self):
       self.medicamentos_disponiveis = {"Paracetamol": 10, "Aspirina": 15, "antiinflamatorio": 5}
       self.pedidos = []
   def exibir_menu_principal(self):
       print("Bem-vindo à Farmácia Online")
       print("1. Consultar Medicamentos")
       print("2. Realizar Compra")
       print("3. Consultar Pedidos")
       print("4. Sair")
   def consultar_medicamentos(self):
       print("Lista de Medicamentos Disponíveis:")
       for medicamento, estoque in self.medicamentos_disponiveis.items():
           print(f"{medicamento}: {estoque} unidades")
