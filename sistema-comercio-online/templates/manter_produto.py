import streamlit as st
import pandas as pd
from views import View

class ManterProdutoUI:
    def main():
        st.header("Cadastro de produtos")

        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1: ManterProdutoUI.listar()
        with tab2: ManterProdutoUI.inserir()
        with tab3: ManterProdutoUI.atualizar()
        with tab4: ManterProdutoUI.excluir()

    def listar():
        produtos = View.produto_listar()
        if len(produtos) == 0: st.write("Nenhum produto até o momento")
        else:
            list_dic = []
            for produto in produtos: list_dic.append(produto.to_json())
            df = pd.DataFrame(list_dic)
            st.dataframe(df, hide_index=True, column_order=["id", "descricao", "preco", "estoque", "idCategoria"])     

    def inserir():
        id = 0
        descricao = st.text_input("Descrição do produto")
        preco = st.number_input("Preço")
        estoque = st.number_input("Estoque atual", value=0)
        categoria = st.selectbox("Categoria", View.categoria_listar())
        if len(View.categoria_listar()) > 0 and st.button("Inserir"): 
            View.produto_inserir(id, descricao, preco, estoque, categoria.get_id())
            st.success("Produto adicionado com sucesso!")

    def atualizar():
        produtos = View.produto_listar()
        if len(produtos) == 0: st.write("Nenhum produto até o momento")
        else:
            op = st.selectbox("Atualizar Produtos", produtos)
            descricao = st.text_input("Nova descrição",  op.get_descricao())
            preco = st.number_input("Novo preço", min_value=0.0, value=op.get_preco())
            estoque = st.number_input("Novo estoque", min_value=0, value=op.get_estoque())
            categorias = st.selectbox("Nova categoria", View.categoria_listar())
            if len(View.categoria_listar()) > 0 and  st.button("Atualizar"):
                id = op.get_idProduto()
                View.produto_atualizar(id, descricao, preco, estoque, categorias.get_id())
                st.success("Produto atualizado com sucesso!")
                st.rerun()
    
    def excluir():
        produtos = View.produto_listar()
        if len(produtos) == 0: st.write("Nenhum produto até o momento")
        else:
            op = st.selectbox("Excluir Produtos", produtos)
            if op:
                if st.button("Excluir"):
                    id = op.get_idProduto()
                    descricao = op.get_descricao()
                    preco = op.get_preco()
                    estoque = op.get_estoque()
                    idCategoria = op.get_idCategoria()
                    View.produto_excluir(id, descricao, preco, estoque, idCategoria)
                    st.success("Produto excluído com sucesso!")
                    st.rerun()
    
    #def reajustar_preco():
        #produtos = View.produto_listar()
