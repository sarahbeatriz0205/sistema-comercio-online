from models.cliente import Cliente, ClienteDAO
from models.categoria import Categoria, CategoriaDAO
from models.produto import Produto, ProdutoDAO 
from models.venda_item import VendaItem, VendaItemDAO
from models.venda import Venda, VendaDAO
from models.carrinho import Carrinho, CarrinhoDAO
from models.favorito import Favorito, FavoritoDAO

class View:
    @staticmethod
    def cliente_criar_admin(email, senha):
        id = 0
        nome = ""
        telefone = 0
        for obj in ClienteDAO.listar():
            if obj.get_email() == "admin@" and obj.get_senha() == "admin": return
        ClienteDAO.inserir(Cliente(id, nome, email, telefone, senha)) # se o if não for verdadeiro, ele passa para a próxima linha e cria um novo admin
    @staticmethod
    def cliente_autenticar(email, senha):
        for obj in View.cliente_listar():
            if obj.get_email() == email and obj.get_senha() == senha: 
                return { "id" : obj.get_idCliente(), "nome" : obj.get_nome(), "email": obj.get_email(), "senha" : obj.get_senha()}
        return None
    @staticmethod
    def get_cliente_id(email, senha):
        for obj in View.cliente_listar():
            if obj.get_email() == email and obj.get_senha() == senha: 
                return obj.get_idCliente()
        return None
    def cliente_inserir(nome, email, telefone, senha):
        id = 0
        if nome == "" or email == "" or telefone == "" or senha == "":
            raise ValueError("Erro! O preenchimento de todos os campos é obrigatório.")
        if "0" in nome or "1" in nome or "2" in nome or "3" in nome or "4" in nome or "5" in nome or "6" in nome or "7" in nome or "8" in nome or "9" in nome:
            raise ValueError("Erro! O nome fornecido não pode conter números.")
        if "@" not in email:
            raise ValueError("Erro! O email fornecido é inválido.")
        ddds_brasil = [11, 12, 13, 14, 15, 16, 17, 18, 19, 21, 22, 24, 27, 28, 31, 32, 33, 34, 35, 37, 38, 41, 42, 43, 44, 45, 46, 47, 48, 49, 51, 53, 54, 55, 61, 62, 64, 63, 65, 66, 67, 68, 69, 71, 73, 74, 75, 77, 79, 81, 87, 82, 83, 84, 85, 88,86, 89, 91, 93, 94, 92, 97, 95, 96, 98, 99]
        if len(telefone) <= 0 or len(telefone)< 11 or len(telefone) > 11 or int(telefone[:2]) not in ddds_brasil:
            raise ValueError("Erro! O número de telefone fornecido é inválido.")
        c = Cliente(id, nome, email, telefone, senha)
        ClienteDAO.inserir(c)
      
    def cliente_listar():
        return ClienteDAO.listar()
    
    def cliente_listar_id(id):
        return ClienteDAO.listar_id(id)

    def cliente_atualizar(id, nome, email, telefone, senha):
        if nome == "" or email == "" or telefone == "" or senha == "":
            raise ValueError("Erro! O preenchimento de todos os campos é obrigatório.")
        if "0" in nome or "1" in nome or "2" in nome or "3" in nome or "4" in nome or "5" in nome or "6" in nome or "7" in nome or "8" in nome or "9" in nome:
            raise ValueError("Erro! O nome não pode conter números.")
        if "@" not in email:
            raise ValueError("Erro! O email fornecido é inválido.")
        ddds_brasil = [11, 12, 13, 14, 15, 16, 17, 18, 19, 21, 22, 24, 27, 28, 31, 32, 33, 34, 35, 37, 38, 41, 42, 43, 44, 45, 46, 47, 48, 49, 51, 53, 54, 55, 61, 62, 64, 63, 65, 66, 67, 68, 69, 71, 73, 74, 75, 77, 79, 81, 87, 82, 83, 84, 85, 88,86, 89, 91, 93, 94, 92, 97, 95, 96, 98, 99]
        if len(telefone) == 0 or int(telefone[:2]) not in ddds_brasil:
            raise ValueError("Erro! O número de telefone fornecido é inválido.")
        c = Cliente(id, nome, email, telefone, senha)
        ClienteDAO.atualizar(c)
        
    def cliente_excluir(id, nome, email, telefone, senha):
        c = Cliente(id, nome, email, telefone, senha)
        CarrinhoDAO.excluir_lote_idCliente(id)
        vendas : list[Venda] = VendaDAO.listar_meus(id)
        for venda in vendas:
            VendaItemDAO.excluir_lote_idVenda(venda.get_idCompra())
        VendaDAO.excluir_lote_idCliente(id)
        FavoritoDAO.excluir_lote_idCliente(id)
        ClienteDAO.excluir(c)

    def categoria_inserir(descricao):
        id = 0
        if descricao == "":
            raise ValueError("Erro! O preenchimento desse campo é obrigatório.")
        if "0" in descricao or "1" in descricao or "2" in descricao or "3" in descricao or "4" in descricao or "5" in descricao or "6" in descricao or "7" in descricao or "8" in descricao or "9" in descricao:
            raise ValueError("Erro! A descrição não pode conter números.")
        CategoriaDAO.inserir(Categoria(id, descricao))
    def categoria_listar():
        return CategoriaDAO.listar()
    def categoria_listar_id(id):
        return CategoriaDAO.listar_id(id)
    def categoria_atualizar(id, descricao):
        if descricao == "":
            raise ValueError("Erro! O preenchimento desse campo é obrigatório.")
        if descricao.isnumeric():
            raise ValueError("Erro! A descrição não pode ser numérica.")
        c = Categoria(id, descricao)
        CategoriaDAO.atualizar(c)
    def categoria_excluir(id, descricao):
        c = Categoria(id, descricao)
        CategoriaDAO.excluir(c)

    def produto_inserir(id, descricao, preco, estoque, idCategoria):
        id = 0
        if descricao == "":
            raise ValueError("Erro! O preenchimento de todos os campos é obrigatório.")
        if preco == 0.0 or preco < 0 or estoque == 0 or estoque < 0:
            raise ValueError("Erro! Nenhum dos valores podem ser menores ou iguais à 0.")
        c = Produto(id, descricao, preco, estoque, idCategoria)
        ProdutoDAO.inserir(c)
    def produto_listar():
        return ProdutoDAO.listar()
    def produto_listar_id(id):
        return ProdutoDAO.listar_id(id)
    def produto_atualizar(id, descricao, preco, estoque):
        if descricao == "" or preco == 0.0 or estoque == 0:
            raise ValueError("Erro! O preenchimento de todos os campos é obrigatório.")
        if preco == 0.0 or preco < 0 or estoque == 0 or estoque < 0:
            raise ValueError("Erro! Nenhum dos valores podem ser menores ou iguais à 0.")
        c = Produto(id, descricao, preco, estoque)
        ProdutoDAO.atualizar(c)
    def produto_excluir(id):
        c = Produto(id)
        ProdutoDAO.excluir(c)
    def produto_reajuste(percentual):
        for obj in ProdutoDAO.listar():
            reajuste = obj.get_preco() * (1 + percentual)
            obj.set_preco(reajuste)
            ProdutoDAO.atualizar(obj)
                

    def produto_atualizar(id, descricao, preco, estoque, idCategoria):
        if descricao == "" or preco == 0.0 or estoque == 0:
            raise ValueError("Erro! O preenchimento de todos os campos é obrigatório.")
        if preco == 0.0 or preco < 0 or estoque == 0 or estoque < 0:
            raise ValueError("Erro! Nenhum dos valores podem ser menores ou iguais à 0.")
        if "0" in descricao or "1" in descricao or "2" in descricao or "3" in descricao or "4" in descricao or "5" in descricao or "6" in descricao or "7" in descricao or "8" in descricao or "9" in descricao:
            raise ValueError("Erro! A descrição não pode conter números.")
        c = Produto(id, descricao, preco, estoque, idCategoria)
        ProdutoDAO.atualizar(c)
    def produto_excluir(id, descricao, preco, estoque, idCategoria):
        c = Produto(id, descricao, preco, estoque, idCategoria)
        ProdutoDAO.excluir(c)
        VendaItemDAO.excluir_lote_idProduto(id)
        CarrinhoDAO.excluir_lote_idProduto(id)
        FavoritoDAO.excluir_lote_idProduto(id)


    def listar_produtos(descricao):
        for obj in ProdutoDAO.listar():
            if obj.get_descricao() == descricao:
                return obj
        return f"Produto não encontrado!"
    def inserir_produto(obj):
        p = ProdutoDAO.listar()
        produto = ProdutoDAO.listar_id(obj.get_idProduto())
        if obj.get_qtd() <= 0: # validar pro estoque tbm. se a qtd for maior que o estoque, não deixa adicionar
            raise ValueError("Quantidade inválida.")
        if produto.get_estoque() < obj.get_qtd():
            raise ValueError("Erro! Estoque insuficiente.")
        if produto != None:
                CarrinhoDAO.inserir(obj)
        return None
    def visualizar_carrinho(idCliente):
        carrinho = []
        total = 0
        for obj in CarrinhoDAO.listar(idCliente):
            produto = ProdutoDAO.listar_id(obj.get_idProduto())
            preco = float(produto.get_preco())
            qtd = int(obj.get_qtd())
            subtotal = preco * qtd
            total += subtotal
            carrinho.append({
                "Produto": produto.get_descricao(),
                "Preço (R$)": f"{preco:.2f}",
                "Quantidade": qtd,
                "Subtotal (R$)": f"{subtotal:.2f}"
            })
        carrinho.append({
            "Produto": "TOTAL",
            "Preço (R$)": "",
            "Quantidade": "",
            "Subtotal (R$)": f"{total:.2f}"
        })
        return carrinho

    def total(idCliente):
        total = 0
        for obj in CarrinhoDAO.listar(idCliente):
            produto = ProdutoDAO.listar_id(obj.get_idProduto())
            preco = float(produto.get_preco())
            qtd = int(obj.get_qtd())
            subtotal = preco * qtd
            total += subtotal
        return total

    
    def finalizar_compra_antigo(idCliente):
        v = Venda(0, idCliente, 0)
        idVenda = VendaDAO.inserir(v)
        total = 0
        for carrinho in CarrinhoDAO.listar(idCliente):
            c : Carrinho = carrinho
            qtd = int(c.get_qtd())
            produto : Produto = ProdutoDAO.listar_id(c.get_idProduto())
            preco = float(produto.get_preco())
            total += (qtd * preco)
            vi = VendaItem(0, c.get_qtd(), c.get_qtd() * produto.get_preco(), idVenda, c.get_idProduto())
            VendaItemDAO.inserir(vi)
        v = VendaDAO.listar_idCliente(idVenda, idCliente)
        v.set_total(total)
        VendaDAO.atualizar(v)
        for carrinho in CarrinhoDAO.listar(idCliente): CarrinhoDAO.excluir(carrinho)
    
    def finalizar_compra(idCliente):
        itens = CarrinhoDAO.listar(idCliente)
        if len(itens) > 0:
            v = Venda(0, idCliente, 0)
            idVenda = VendaDAO.inserir(v)
            total = 0
            for carrinho in itens:
                c : Carrinho = carrinho
                produto : Produto = ProdutoDAO.listar_id(c.get_idProduto())
                total += c.get_qtd() * produto.get_preco()
                vi = VendaItem(0, c.get_qtd(), c.get_qtd() * produto.get_preco(), idVenda, c.get_idProduto())
                VendaItemDAO.inserir(vi)
            v = VendaDAO.listar_idCliente(idVenda, idCliente)
            v.set_total(total)
            VendaDAO.atualizar(v)
            for carrinho in CarrinhoDAO.listar(idCliente): 
                CarrinhoDAO.excluir(carrinho)

    def listar_compras(idCliente):
        vendas = VendaDAO.listar_meus(idCliente)
        conteudo = []
        total_geral = 0

        for venda in vendas:
            total_geral += venda.get_total()
            vis = VendaItemDAO.listar_idVenda(venda.get_idCompra())
            for vi in vis:
                produto = ProdutoDAO.listar_id(vi.get_idProduto())
                conteudo.append({
                        "idVenda": venda.get_idCompra(),
                        "descricao": produto.get_descricao(),
                        "unitario": produto.get_preco(),
                        "quantidade": vi.get_quantidade(),
                        "preco_total": vi.get_preco(),
                        "total_venda": venda.get_total()
                    })       
        return conteudo, total_geral

    
    def listar_compras_admin():
        vendas: list[Venda] = VendaDAO.listar()
        conteudo = []
        for venda in vendas:
            cliente: Cliente = ClienteDAO.listar_id(venda.get_idCliente())
            vis: list[VendaItem] = VendaItemDAO.listar_idVenda(venda.get_idCompra())
            for vi in vis:
                produto: Produto = ProdutoDAO.listar_id(vi.get_idProduto())
                conteudo.append({
                    "idVenda": venda.get_idCompra(),
                    "cliente": cliente.get_nome(),
                    "produto": produto.get_descricao(),
                    "unitario": produto.get_preco(),
                    "quantidade": vi.get_quantidade(),
                    "preco_item": vi.get_preco(),
                    "total_venda": venda.get_total()
                })
        return conteudo

    
    def listar_compras_admin_agrupado():
        clientes : list[Cliente] = ClienteDAO.listar()
        conteudo = []
        for c in clientes:
            cliente : Cliente = ClienteDAO.listar_id(c.get_idCliente())
            vendas : list[Venda] = VendaDAO.listar_meus(cliente.get_idCliente())
            total = 0
            conteudo.append(cliente.get_nome())
            for venda in vendas:
                total += venda.get_total()
                vis : list[VendaItem] = VendaItemDAO.listar_idVenda(venda.get_idCompra())
                for vi in vis:
                    produto : Produto = ProdutoDAO.listar_id(vi.get_idProduto())
                    conteudo.append(produto.get_descricao() + " - Unitario: "  + str(produto.get_preco()) + " - " + str(vi.get_quantidade()) + " - " + str(vi.get_preco()))
                conteudo.append("Total Venda " + str(venda.get_idCompra()) + ":" + str(venda.get_total())) 
            conteudo.append("Total todas vendas do cliente " + cliente.get_nome() + ": " + str(total) )    
        return conteudo
    
    def favoritar(obj):
        f = ProdutoDAO.listar_id(obj.get_idProduto())
        if f != None:
            FavoritoDAO.favoritar(obj)

    def desfavoritar(obj):
        f = ProdutoDAO.listar_id(obj.get_idProduto())
        if f != None:
            FavoritoDAO.desfavoritar(obj)

    def produtos_favoritos(idCliente):
        fav = []
        favoritos = FavoritoDAO.favoritos(idCliente)
        for f in favoritos:
            produto = ProdutoDAO.listar_id(f.get_idProduto())
            fav.append({
            "idProduto": produto.get_idProduto(),
            "Produto": produto.get_descricao(),
            "Preço": produto.get_preco()
        })
        if len(fav) == 0:
            return None 
        return fav
    
    def lista_favoritados(idCliente):
        fav = []
        favoritos = FavoritoDAO.favoritos(idCliente)
        for f in favoritos:
            produto = ProdutoDAO.listar_id(f.get_idProduto())
            fav.append([produto.get_idProduto(), produto.get_descricao(), produto.get_preco()])
        return fav