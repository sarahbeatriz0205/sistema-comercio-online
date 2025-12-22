import json
from models.dao import DAO

class Cliente:
    def __init__(self, id, nome, email, telefone, senha):
        self.set_id(id)
        self.set_nome(nome)
        self.set_email(email)
        self.set_telefone(telefone)
        self.set_senha(senha)
    
    def set_id(self, id):
        self.__id = id
    def set_nome(self, nome):
            self.__nome = nome
    def set_email(self, email):
        self.__email = email
    def set_telefone(self, telefone):
        self.__telefone = telefone
    def set_senha(self, senha):
        self.__senha = senha

    def get_id(self):
        return self.__id
    def get_nome(self):
        return self.__nome
    def get_email(self):
        return self.__email
    def get_telefone(self):
        return self.__telefone
    def get_senha(self):
        return self.__senha
    
    def __str__(self):
        return f"{self.__id} - {self.__nome} - {self.__email} - {self.__telefone}"
    
    def to_json(self):
        return {"id" : self.__id, "nome" : self.__nome, "email" : self.__email, "telefone" : self.__telefone, "senha" : self.__senha} # me permite que eu ponha o nome que eu quiser para as chaves
    @staticmethod
    def from_json(dic):
        return Cliente(dic["id"], dic["nome"], dic["email"], dic["telefone"], dic["senha"]) 

class ClienteDAO(DAO):
    objetos = []

    @classmethod
    def salvar_json(cls):
        with open("clientes.json", mode="w") as arquivo:
            json.dump(cls.objetos, arquivo, default = Cliente.to_json, indent=4)
    @classmethod
    def abrir_json(cls):
        cls.objetos = []
        try:
            with open("clientes.json", mode="r") as arquivo:
                list_dic = json.load(arquivo)
                for dic in list_dic:
                    c = Cliente.from_json(dic)
                    cls.objetos.append(c)
        except:
            pass            