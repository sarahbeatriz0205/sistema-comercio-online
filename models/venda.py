from datetime import datetime
import json

class Venda:
    def __init__(self, idCompra, idCliente, total, data=None):
        self.set_idCompra(idCompra)
        if data is None:
            self.set_data()  # usa datetime.now()
        else:
            # se vier string do JSON, converte para datetime
            if isinstance(data, str):
                self.__data = datetime.strptime(data, "%d/%m/%Y %H:%M:%S")
            else:
                self.__data = data
        self.set_total(total)
        self.set_idCliente(idCliente)

    def set_idCompra(self, idCompra):
        self.__idCompra = idCompra
    def set_data(self):
        self.__data = datetime.now()
    def set_total(self, total):
        self.__total = total
    def set_idCliente(self, idCliente):
        self.__idCliente = idCliente

    def get_idCompra(self):
        return self.__idCompra
    def get_data(self):
        return self.__data
    def get_total(self):
        return self.__total
    def get_idCliente(self):
        return self.__idCliente

    def __str__(self):
        return f"ID da compra = {self.__idCompra} - Data = {self.__data} - Total da compra = {self.__total} - ID do cliente = {self.__idCliente}"
        
    def to_json(self):
        return {
            "idCompra": self.__idCompra,
            "data": self.__data.strftime("%d/%m/%Y %H:%M:%S"),
            "idCliente": self.__idCliente,
            "Total": self.__total
        }
    
    @staticmethod
    def from_json(dic):
        return Venda(dic["idCompra"], dic["idCliente"], dic["Total"], dic["data"])

class VendaDAO:
    # atributo de VendaDAO:
    vendas : list[Venda] = []

    @classmethod
    def inserir(cls, venda):
        cls.abrir_json()
        venda.set_idCompra(len(cls.vendas) + 1)
        cls.vendas.append(venda)   # <-- adiciona, não sobrescreve
        cls.salvar_json()
        return venda.get_idCompra()

    @classmethod
    def listar(cls):
        cls.abrir_json() # não pode ser "return cls.abrir_json" porque esse método não retorna nada
        return cls.vendas
    @classmethod
    def listar_meus(cls, idCliente):
        cls.abrir_json() # não pode ser "return cls.abrir_json" porque esse método não retorna nada
        vendas = []
        for objetoVenda in cls.vendas:
            if objetoVenda.get_idCliente() == idCliente: vendas.append(objetoVenda)
        return vendas
    @classmethod
    def listar_idCliente(cls, idCompra, idCliente):
        for obj in cls.vendas:
            if obj.get_idCompra() == idCompra and obj.get_idCliente() == idCliente:
                return obj
        return None
    @classmethod
    def listar_id(cls, idCompra):
        for obj in cls.vendas:
            if obj.get_idCompra() == idCompra:
                return obj
        return None
    @classmethod
    def atualizar(cls, venda):
        for i, v in enumerate(cls.vendas):
            if v.get_idCompra() == venda.get_idCompra():
                cls.vendas[i] = venda
                break
        cls.salvar_json()
    @classmethod
    def excluir(cls, obj):
        aux = cls.listar_id(obj.get_idCompra())
        if aux != None:
            cls.vendas.remove(aux)
        cls.salvar_json()
    @classmethod
    def excluir_lote_idCliente(cls, idCliente):
        cls.abrir_json()
        for objeto in cls.vendas:
            if objeto.get_idCliente() == idCliente:
                cls.excluir(objeto)
    @classmethod
    def salvar_json(cls):
        with open("vendas.json", "w", encoding="utf-8") as arquivo:
            json.dump([v.to_json() for v in cls.vendas], arquivo, indent=4)

    @classmethod
    def abrir_json(cls):
        cls.vendas = []
        try:
            with open("vendas.json", mode="r") as arquivo:
                list_dic = json.load(arquivo)
                for dic in list_dic:
                    c = Venda.from_json(dic)
                    cls.vendas.append(c)
        except:
            pass