from templates.manter_cliente import ManterClienteUI
from templates.manter_categoria import ManterCategoriaUI
from templates.listar_vendas_admin import ListarVendasUI
from templates.manter_produto import ManterProdutoUI
from templates.login import LoginUI
from templates.criar_conta import CriarContaUI
from templates.listar_produtos import ListarProdutosUI
from templates.manter_carrinho import ManterCarrinhoUI
from templates.favoritar import ManterFavoritoUI
from templates.listar_compras import ListarMinhasComprasUI
from views import View
import streamlit as st

class IndexUI:
        def menu_visitante():
                op = st.selectbox("Entre no sistema ou crie sua conta", ["Entrar no sistema", 
                                                                        "Criar Conta"])
                if op == "Entrar no sistema": LoginUI.main()
                if op == "Criar Conta": CriarContaUI.main()
        def menu_admin():
                # st.sidebar.selectbox: caixa de seleção
                op = st.sidebar.selectbox("Menu", ["Cadastro de Categorias", 
                                        "Cadastro de Clientes", 
                                        "Cadastro de Produtos", 
                                        "Listar todas as vendas"])
                
                # ao clicar, direciono o usuário para a página correspode àquela opção
                if op == "Cadastro de Categorias": ManterCategoriaUI.main()
                if op == "Cadastro de Clientes": ManterClienteUI.main()
                if op == "Cadastro de Produtos": ManterProdutoUI.main()
                if op == "Listar todas as vendas": ListarVendasUI.main()
        
        def menu_cliente():
                op = st.sidebar.selectbox("Menu", ["Listar produtos",
                                        "Quero comprar",
                                        "Listar minhas compras",
                                        "Favoritar produtos"])
                if op == "Listar produtos": ListarProdutosUI.main()
                if op == "Quero comprar": ManterCarrinhoUI.main()
                if op == "Favoritar produtos": ManterFavoritoUI.main()
                if op == "Listar minhas compras": ListarMinhasComprasUI.main()

        def sidebar():
                if "cliente_id" not in st.session_state: IndexUI.menu_visitante()
                else:
                        st.sidebar.write("Bem-vindo(a), " + st.session_state["cliente_nome"])
                        admin = st.session_state["cliente_email"] == "admin@"
                        if admin: IndexUI.menu_admin()
                        else: IndexUI.menu_cliente()
                        IndexUI.sair_do_sistema() 

        def sair_do_sistema():
                if st.sidebar.button("Sair"):
                        del st.session_state["cliente_id"]
                        del st.session_state["cliente_nome"]
                        st.rerun()
                
        def main():
                View.cliente_criar_admin("admin@", "admin")
                IndexUI.sidebar() 


IndexUI.main()