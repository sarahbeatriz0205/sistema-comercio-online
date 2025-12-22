import json
from models.dao import DAO

class Produto:
    def __init__(self, idProduto, descricao, preco, estoque, idCategoria):
        self.set_id(idProduto)
        self.set_descricao(descricao)
        self.set_preco(preco)
        self.set_estoque(estoque)
        self.set_idCategoria(idCategoria)
    
    def set_id(self, id):
        self.__id = id

    def set_descricao(self, descricao):
        self.__descricao = descricao

    def set_preco(self, preco):
        self.__preco = preco

    def set_estoque(self, estoque):
        self.__estoque = estoque

    def set_idCategoria(self, idCategoria):
        self.__idCategoria = idCategoria

    def get_id(self):
        return self.__id
    def get_descricao(self):
        return self.__descricao
    def get_preco(self):
        return self.__preco
    def get_estoque(self):
        return self.__estoque
    def get_idCategoria(self):
        return self.__idCategoria
    
    def to_json(self):
        return {"id" : self.__id, "descricao" : self.__descricao, "preco" : self.__preco, "estoque" : self.__estoque, "idCategoria" : self.__idCategoria} # me permite que eu ponha o nome que eu quiser para as chaves
    @staticmethod
    def from_json(dic):
        return Produto(dic["id"], dic["descricao"], dic["preco"], dic["estoque"], dic["idCategoria"])
    
    def __str__(self):
        return f"{self.__id} - {self.__descricao} - R${self.__preco} - Possui {self.__estoque} no estoque - Categoria {self.__idCategoria}"


class ProdutoDAO(DAO):
    objetos = []
    @classmethod
    def excluir_lote_idProduto(cls, idProduto):
        cls.abrir()
        for objeto in cls.venda_item:
            if objeto.get_id() == idProduto:
                cls.excluir(objeto)
    @classmethod
    def salvar_json(cls):
        with open("produtos.json", mode="w") as arquivo:
            json.dump(cls.objetos, arquivo, default = Produto.to_json, indent=4)
    @classmethod
    def abrir_json(cls):
        cls.objetos = []
        try:
            with open("produtos.json", mode="r") as arquivo:
                list_dic = json.load(arquivo)
                for dic in list_dic:
                    c = Produto.from_json(dic)
                    cls.objetos.append(c)
        except:
            pass