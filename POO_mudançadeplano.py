class Clientes:
    def __init__(self, nome, email, plano):
        self.nome = nome
        self.email = email
        self.lista_planos = ["basic","premium","duo"]
        if plano in self.lista_planos:
            self.plano = plano
        else: 
            raise Exception("Plano inválido")    
        
    def mudar_plano(self, novo_plano):
        if novo_plano in self.lista_planos:
            self.plano = novo_plano
            print("Plano Alterado com sucesso")
        else: 
            print("plano Inválido")

    def ver_filme(self, filme, plano_filme) :  
        if self.plano == plano_filme:
            print(f"ver filme{filme}")
        elif self.plano == "premium":
            print(f"Ver filme{filme}")
        elif self.plano == "basic":
            print("é necessário fazer um upgrade no seu plno para ver esse filme")             
        elif self.plano == "duo":
            print(f"ver filme{filme}")     
        else:
            print("plano inválido")    
        
        

cliente = Clientes("ingrid", "ingrid18imc@gmail.com","basic")
print(cliente.plano)
cliente.ver_filme("vingadores","premium" or "duo")
cliente.mudar_plano("premium")
print(cliente.plano)
cliente.ver_filme("vingadores","premium" or "duo")
