import json

class Cliente:
    def __init__(self, idCliente, nome, email, telefone, senha):
        self.set_idCliente(idCliente)
        self.set_nome(nome)
        self.set_email(email)
        self.set_telefone(telefone)
        self.set_senha(senha)
    
    def set_idCliente(self, idCliente):
        self.__idCliente = idCliente
    def set_nome(self, nome):
            self.__nome = nome
    def set_email(self, email):
        self.__email = email
    def set_telefone(self, telefone):
        self.__telefone = telefone
    def set_senha(self, senha):
        self.__senha = senha

    def get_idCliente(self):
        return self.__idCliente
    def get_nome(self):
        return self.__nome
    def get_email(self):
        return self.__email
    def get_telefone(self):
        return self.__telefone
    def get_senha(self):
        return self.__senha
    
    def __str__(self):
        return f"{self.__idCliente} - {self.__nome} - {self.__email} - {self.__telefone}"
    
    def to_json(self):
        return {"idCliente" : self.__idCliente, "nome" : self.__nome, "email" : self.__email, "telefone" : self.__telefone, "senha" : self.__senha} # me permite que eu ponha o nome que eu quiser para as chaves
    @staticmethod
    def from_json(dic):
        return Cliente(dic["idCliente"], dic["nome"], dic["email"], dic["telefone"], dic["senha"]) 

class ClienteDAO:
    clientes = []   # atributo da classe ClienteDAO -> DAO = Um objeto usado para acessar e salvar dados de outra classe          
    @classmethod              
    def inserir(cls, obj):
        cls.abrir()
        idC = 0 # aux.idCliente sempre vai ser maior que idC
        for aux in cls.clientes: # aux -> é um objeto da classe Cliente que está armazenado no clientes.json
            if aux.get_idCliente() > idC: idC = aux.get_idCliente() # aux.idCliente -> identifica o id do objeto aux
        obj.set_idCliente(idC + 1)    #obj vai ser o objeto que foi recebido no momento
        cls.clientes.append(obj)
        cls.salvar()
    @classmethod
    def listar(cls):
        cls.abrir()
        return cls.clientes
    @classmethod
    def listar_id(cls, idCliente):
        cls.abrir() # tenho que abrir o json
        for obj in cls.clientes: # percorrer a lista
            if obj.get_idCliente() == idCliente: return obj
        return None    
    @classmethod
    def atualizar(cls, obj):
        # procurar o objeto que tem o idCliente dado por obj.idCliente
        aux = cls.listar_id(obj.get_idCliente())
        if aux != None:
            cls.clientes.remove(aux)
            cls.clientes.append(obj)
            cls.salvar()
    @classmethod
    def excluir(cls, obj):
        # procurar o objeto que tem o idCliente dado por obj.idCliente
        aux = cls.listar_id(obj.get_idCliente())
        if aux != None:
            cls.clientes.remove(aux)
            cls.salvar()
    @classmethod
    def salvar(cls):
        with open("clientes.json", mode="w") as arquivo:
            json.dump(cls.clientes, arquivo, default = Cliente.to_json, indent=4)
    @classmethod
    def abrir(cls):
        cls.clientes = []
        try:
            with open("clientes.json", mode="r") as arquivo:
                list_dic = json.load(arquivo)
                for dic in list_dic:
                    c = Cliente.from_json(dic)
                    cls.clientes.append(c)
        except:
            pass            