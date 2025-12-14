import json

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
    

class CategoriaDAO:
    objetos = []             
    @classmethod              
    def inserir(cls, obj):
        cls.abrir()
        id = 0
        for aux in cls.objetos:
            if aux.get_id() > id: id = aux.get_id()
        obj.set_id(id + 1)    
        cls.objetos.append(obj)
        cls.salvar()
    @classmethod
    def listar(cls):
        cls.abrir()
        return cls.objetos
    @classmethod
    def listar_id(cls, id):
        cls.abrir()
        for obj in cls.objetos:
            if obj.get_id() == id: return obj
        return None    
    @classmethod
    def atualizar(cls, obj):
        # procurar o objeto que tem o id dado por obj.id
        aux = cls.listar_id(obj.get_id())
        if aux != None:
            #aux.nome = obj.nome
            # remove o objeto antigo aux e insere o novo obj
            cls.objetos.remove(aux)
            cls.objetos.append(obj)
            cls.salvar()
    @classmethod
    def excluir(cls, obj):
        # procurar o objeto que tem o id dado por obj.id
        aux = cls.listar_id(obj.get_id())
        if aux != None:
            cls.objetos.remove(aux)
            cls.salvar()
    @classmethod
    def salvar(cls):
        with open("categorias.json", mode="w") as arquivo:
                json.dump(cls.objetos, arquivo, default = Categoria.to_json, indent=4)
    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open("categorias.json", mode="r") as arquivo:
                list_dic = json.load(arquivo)
                for dic in list_dic:
                    c = Categoria.from_json(dic)
                    cls.objetos.append(c)
        except:
            pass            