from abc import ABC

class DAO(ABC):
    @classmethod
    def inserir(cls, obj):
        cls.abrir_json()
        id = 0
        for objeto in cls.objetos:
            if objeto.get_id() > id: 
                id = objeto.get_id()
        obj.set_id(id + 1)
        cls.objetos.append(obj)
        cls.salvar_json()
    @classmethod
    def listar(cls):
        cls.abrir_json() # não pode ser "return cls.abrir_json" porque esse método não retorna nada
        return cls.objetos
    @classmethod
    def listar_id(cls, id):
        cls.abrir_json()
        for obj in cls.objetos:
            if obj.get_id() == id:
                return obj
        return None
    @classmethod
    def atualizar(cls, obj):
        aux = cls.listar_id(obj.get_id())
        if aux != None:
            cls.objetos.remove(aux)
            cls.objetos.append(obj)
        cls.salvar_json()
    @classmethod
    def excluir(cls, obj):
        aux = cls.listar_id(obj.get_id())
        if aux != None:
            cls.objetos.remove(aux)
        cls.salvar_json()