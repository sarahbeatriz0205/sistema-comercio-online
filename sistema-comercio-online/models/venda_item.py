import json

class VendaItem:
    def __init__(self, idVendaItem, quantidade, preco, idVenda, idProduto):
        self.set_idVendaItem(idVendaItem)
        self.set_quantidade(quantidade)
        self.set_preco(preco) # da compra atual
        self.set_idVenda(idVenda)
        self.set_idProduto(idProduto)
    
    def set_idVendaItem(self, idVendaItem):
        self.__idVendaItem = idVendaItem
    def set_quantidade(self, qtd):
        self.__quantidade = qtd
    def set_preco(self, preco):
        self.__preco = preco
    def set_idVenda(self, idVenda):
        self.__idVenda = idVenda
    def set_idProduto(self, idProduto):
        self.__idProduto = idProduto

    def get_idVendaItem(self):
        return self.__idVendaItem
    def get_quantidade(self):
        return self.__quantidade
    def get_preco(self):
        return self.__preco
    def get_idVenda(self):
        return self.__idVenda
    def get_idProduto(self):
        return self.__idProduto

    
    def to_json(self):
        return {"idVendaItem" : self.__idVendaItem, "quantidade" : self.__quantidade, "preco" : self.__preco, "idVenda" : self.__idVenda, "idProduto" : self.__idProduto} # me permite que eu ponha o nome que eu quiser para as chaves
    @staticmethod
    def from_json(dic):
        return VendaItem(dic["idVendaItem"], dic["quantidade"], dic["preco"],  dic["idVenda"], dic["idProduto"]) 
    def __str__(self):
        return f"{self.__idVendaItem}"

class VendaItemDAO:
    venda_item = []

    @classmethod
    def inserir(cls, objeto):
        cls.abrir_json()
        idVendaItem = 0 # aux.idCliente sempre vai ser maior que idC
        for aux in cls.venda_item: # aux -> é um objeto da classe Cliente que está armazenado no clientes.json
            if aux.get_idVendaItem() > idVendaItem: idVendaItem = aux.get_idVendaItem() # aux.idCliente -> identifica o id do objeto aux
        objeto.set_idVendaItem(idVendaItem + 1)    #obj vai ser o objeto que foi recebido no momento
        cls.venda_item.append(objeto)
        cls.salvar_json()
    @classmethod
    def listar(cls):
        cls.abrir_json()
        return cls.venda_item
    @classmethod
    def listar_id(cls, idVendaItem):
        cls.abrir_json()
        for objetoVendaItem in cls.venda_item:
            if objetoVendaItem.get_idVendaItem() == idVendaItem:
                return objetoVendaItem
            return None
    @classmethod
    def listar_idVenda(cls, idVenda):
        cls.abrir_json()
        itens = []
        for objetoVendaItem in cls.venda_item:
            if objetoVendaItem.get_idVenda() == idVenda:
                itens.append(objetoVendaItem)
        return itens
    @classmethod
    def atualizar(cls, objetoVendaItem):
        aux = cls.listar_id(objetoVendaItem.get_idVendaItem())
        if aux != None:
            cls.venda_item.remove(aux)
            cls.venda_item.append(objetoVendaItem)
    @classmethod
    def excluir(cls, objetoVendaItem):
        aux = cls.listar_id(objetoVendaItem.get_idVendaItem())
        if aux != None:
            cls.venda_item.remove(aux)
            cls.salvar_json()
    @classmethod
    def excluir_lote_idVenda(cls, idVenda):
        cls.abrir_json()
        for objeto in cls.venda_item:
            if objeto.get_idVenda() == idVenda:
                cls.excluir(objeto)
    @classmethod
    def excluir_lote_idProduto(cls, idProduto):
        cls.abrir_json()
        for objeto in cls.venda_item:
            if objeto.get_idProduto() == idProduto:
                cls.excluir(objeto)
    @classmethod
    def excluir_lote_idCliente(cls, idCliente):
        cls.abrir_json()
        for objeto in cls.venda_item:
            if objeto.get_idCliente() == idCliente:
                cls.excluir(objeto)
    @classmethod
    def salvar_json(cls):
        with open("venda_itens.json", mode="w") as arquivo:
            json.dump(cls.venda_item, arquivo, default = VendaItem.to_json, indent = 4)
    @classmethod
    def abrir_json(cls):
        cls.venda_item = []
        try:
            with open("venda_itens.json", mode="r") as arquivo:
                list_dic = json.load(arquivo)
                for dic in list_dic:
                    c = VendaItem.from_json(dic)
                    cls.venda_item.append(c)
        except:
            pass