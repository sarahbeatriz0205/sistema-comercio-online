import json

class Carrinho:
    def __init__(self, idProduto, qtd, idCliente):
        self.set_idProduto(idProduto)
        self.set_qtd(qtd)
        self.set_idCliente(idCliente)
    
    def set_idProduto(self, idProduto):
        self.__idProduto = idProduto
    def set_qtd(self, qtd):
        self.__qtd = qtd
    def set_idCliente(self, idCliente):
        self.__idCliente = idCliente
    
    
    def get_idProduto(self):
        return self.__idProduto
    def get_qtd(self):
        return self.__qtd
    def get_idCliente(self):
        return self.__idCliente
    
    def __str__(self):
        return f"{self.__idProduto} - {self.__idCliente} - {self.__qtd}"
    
    def to_json(self):
        return {"idProduto" : self.__idProduto, "qtd" : self.__qtd, "idCliente" : self.__idCliente}
    @staticmethod
    def from_json(dic):
        return Carrinho(dic["idProduto"], dic["qtd"], dic["idCliente"]) 

class CarrinhoDAO:
    objetos = []             
    @classmethod              
    def inserir(cls, obj):
        aux = cls.listar_id(obj.get_idProduto(), obj.get_idCliente())
        if aux == None:
            cls.objetos.append(obj)
            cls.salvar()
        else:
            aux.set_qtd(obj.get_qtd() + aux.get_qtd())
            cls.atualizar(aux)
    @classmethod
    def listar(cls, idCliente):
        cls.abrir()
        carrinho = []
        for objeto in cls.objetos:
            if objeto.get_idCliente() == idCliente: 
                carrinho.append(objeto)
        return carrinho
    @classmethod
    def listar_id(cls, id, idCliente):
        cls.abrir()
        for obj in cls.objetos:
            if obj.get_idProduto() == id and obj.get_idCliente() == idCliente: return obj
        return None    
    @classmethod
    def atualizar(cls, obj):
        aux = cls.listar_id(obj.get_idProduto(), obj.get_idCliente())
        if aux != None:
            cls.objetos.remove(aux)
            cls.objetos.append(obj)
            cls.salvar()
    @classmethod
    def excluir(cls, obj):
        aux = cls.listar_id(obj.get_idProduto(), obj.get_idCliente())
        if aux != None:
            cls.objetos.remove(aux)
            cls.salvar()
    @classmethod
    def excluir_lote_idCliente(cls, idCliente):
        cls.abrir()
        for objeto in cls.objetos:
            if objeto.get_idCliente() == idCliente:
                cls.excluir(objeto)
    @classmethod
    def excluir_lote_idProduto(cls, idProduto):
        cls.abrir()
        for objeto in cls.objetos:
            if objeto.get_idProduto() == idProduto:
                cls.excluir(objeto)
    @classmethod
    def salvar(cls):
        with open("carrinho.json", mode="w") as arquivo:
                json.dump(cls.objetos, arquivo, default = Carrinho.to_json, indent=4)
    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open("carrinho.json", mode="r") as arquivo:
                list_dic = json.load(arquivo)
                for dic in list_dic:
                    c = Carrinho.from_json(dic)
                    cls.objetos.append(c)
        except:
            pass            