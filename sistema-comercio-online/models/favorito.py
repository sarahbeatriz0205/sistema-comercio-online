import json

class Favorito:
    def __init__(self, idProduto, idCliente):
        self.set_idProduto(idProduto)
        self.set_idCliente(idCliente)
    
    def set_idProduto(self, idProduto):
        self.__idProduto = idProduto
    def set_idCliente(self, idCliente):
        self.__idCliente = idCliente
    
    def get_idProduto(self):
        return self.__idProduto
    def get_idCliente(self):
        return self.__idCliente
    
    def __str__(self):
        return f"{self.__idProduto} - {self.__idCliente}"
    @staticmethod
    def to_json(obj):
        return {"idProduto" : obj.get_idProduto(), "idCliente" : obj.get_idCliente()}
    
    @staticmethod
    def from_json(dic):
        return Favorito(dic["idProduto"], dic["idCliente"]) 

class FavoritoDAO:
    objetos = []     
    @classmethod              
    def favoritar(cls, obj : Favorito):
        cls.abrir()
        aux = cls.favoritos_produto(obj.get_idProduto(), obj.get_idCliente())
        if aux == None:
            cls.objetos.append(obj)
            cls.salvar()
    @classmethod
    def favoritos_produto(cls, idProduto, idCliente):
        cls.abrir()
        for obj in cls.objetos:
            if obj.get_idProduto() == idProduto and obj.get_idCliente() == idCliente: return obj
        return None
    @classmethod 
    def favoritos(cls, idCliente):
        cls.abrir()
        favoritados = []
        for obj in cls.objetos:
            if obj.get_idCliente() == idCliente: favoritados.append(obj)
        return favoritados
    @classmethod
    def desfavoritar(cls, obj):
        aux = cls.favoritos_produto(obj.get_idProduto(), obj.get_idCliente())
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
    def excluir(cls, obj):
        aux = cls.favoritos_produto(obj.get_idProduto(), obj.get_idCliente())
        if aux != None:
            cls.objetos.remove(aux)
            cls.salvar()
    @classmethod
    def salvar(cls):
        with open("favorito.json", mode="w") as arquivo:
                json.dump(cls.objetos, arquivo, default=Favorito.to_json, indent=4)
    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open("favorito.json", mode="r") as arquivo:
                list_dic = json.load(arquivo)
                for dic in list_dic:
                    c = Favorito.from_json(dic)
                    cls.objetos.append(c)
        except:
            pass            