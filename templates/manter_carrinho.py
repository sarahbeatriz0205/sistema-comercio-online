import streamlit as st
from views import View
import pandas as pd
from models.carrinho import Carrinho

class ManterCarrinhoUI:
    def main():

        st.header("Venha fazer suas compras aqui!")

        tab1, tab2, tab3 = st.tabs(["Colocar produtos no meu carrinho", "Visualizar meu carrinho", "Finalizar compra"])
        with tab1: ManterCarrinhoUI.inserir()
        with tab2: ManterCarrinhoUI.visualizar()
        with tab3: ManterCarrinhoUI.comprar()

    def inserir():
        idCliente = st.session_state["cliente_id"]
        op = st.selectbox("Selecione o produto que você deseja", View.produto_listar())
        if op: 
            idProduto = op.get_idProduto()
            qtd = st.number_input("Qual a quantidade desse produto que você quer?", value=0)
            if st.button("Adicionar no carrinho"):
                try:
                    c = Carrinho(idProduto, qtd, idCliente)
                    View.inserir_produto(c)
                    st.success("Item adicionado com sucesso!")
                except Exception as erro:
                    st.error(f"{erro}")
    
    def visualizar():
        idCliente = st.session_state["cliente_id"]
        carrinho = View.visualizar_carrinho(idCliente)
        df = pd.DataFrame(carrinho)
        st.dataframe(
        df, use_container_width=True, hide_index=True, column_order=["Produto", "Preço (R$)", "Quantidade", "Subtotal (R$)"])

    def comprar():
        idCliente = st.session_state["cliente_id"]
        vendas_cliente = View.listar_compras(idCliente)
        st.write("Total: ", View.total(idCliente))
        if st.button("Finalizar compra"):
            st.success("Compra finalizada com sucesso!")
            View.finalizar_compra(idCliente)
            View.produto_reajuste_estoque()