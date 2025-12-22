import json
from models.dao import DAO

class VendaItem:
    def __init__(self, id, quantidade, preco, idVenda, idProduto):
        self.set_id(id)
        self.set_quantidade(quantidade)
        self.set_preco(preco) # da compra atual
        self.set_idVenda(idVenda)
        self.set_idProduto(idProduto)
    
    def set_id(self, id):
        self.__id = id
    def set_quantidade(self, qtd):
        self.__quantidade = qtd
    def set_preco(self, preco):
        self.__preco = preco
    def set_idVenda(self, idVenda):
        self.__idVenda = idVenda
    def set_idProduto(self, idProduto):
        self.__idProduto = idProduto

    def get_id(self):
        return self.__id
    def get_quantidade(self):
        return self.__quantidade
    def get_preco(self):
        return self.__preco
    def get_idVenda(self):
        return self.__idVenda
    def get_idProduto(self):
        return self.__idProduto
    
    def to_json(self):
        return {"id" : self.__id, "quantidade" : self.__quantidade, "preco" : self.__preco, "idVenda" : self.__idVenda, "idProduto" : self.__idProduto} # me permite que eu ponha o nome que eu quiser para as chaves
    @staticmethod
    def from_json(dic):
        return VendaItem(dic["id"], dic["quantidade"], dic["preco"],  dic["idVenda"], dic["idProduto"]) 
    def __str__(self):
        return f"{self.__id}"

class VendaItemDAO(DAO):
    objetos = []

    @classmethod
    def listar_idVenda(cls, idVenda):
        cls.abrir_json()
        itens = []
        for objetoVendaItem in cls.venda_item:
            if objetoVendaItem.get_idVenda() == idVenda:
                itens.append(objetoVendaItem)
        return itens
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
            if objeto.get_id() == idProduto:
                cls.excluir(objeto)
    @classmethod
    def excluir_lote_idCliente(cls, idCliente):
        cls.abrir_json()
        for objeto in cls.venda_item:
            if objeto.get_id() == idCliente:
                cls.excluir(objeto)
    @classmethod
    def salvar_json(cls):
        with open("venda_itens.json", mode="w") as arquivo:
            json.dump(cls.objetos, arquivo, default = VendaItem.to_json, indent = 4)
    @classmethod
    def abrir_json(cls):
        cls.objetos = []
        try:
            with open("venda_itens.json", mode="r") as arquivo:
                list_dic = json.load(arquivo)
                for dic in list_dic:
                    c = VendaItem.from_json(dic)
                    cls.objetos.append(c)
        except:
            pass