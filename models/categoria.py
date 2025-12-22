import json
from models.dao import DAO

class Categoria:
    def __init__(self, id, descricao):
        self.set_id(id)
        self.set_descricao(descricao)
    
    def set_id(self, id):
        self.__id = id
    def set_descricao(self, descricao):
        self.__descricao = descricao


    def get_id(self):
        return self.__id
    def get_descricao(self):
        return self.__descricao

    def __str__(self):
        return f"{self.__id} - {self.__descricao}"
    
    def to_json(self):
        return {"id" : self.__id, "descricao" : self.__descricao} # me permite que eu ponha o nome que eu quiser para as chaves
    @staticmethod
    def from_json(dic):
        return Categoria(dic["id"], dic["descricao"]) 
    

class CategoriaDAO(DAO):
    objetos = []

    @classmethod
    def salvar_json(cls):
        with open("categorias.json", mode="w") as arquivo:
                json.dump(cls.objetos, arquivo, default = Categoria.to_json, indent=4)
    @classmethod
    def abrir_json(cls):
        cls.objetos = []
        try:
            with open("categorias.json", mode="r") as arquivo:
                list_dic = json.load(arquivo)
                for dic in list_dic:
                    c = Categoria.from_json(dic)
                    cls.objetos.append(c)
        except:
            pass            