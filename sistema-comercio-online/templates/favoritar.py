import streamlit as st
from views import View
import pandas as pd
from models.favorito import Favorito

class ManterFavoritoUI:
    def main():

        st.header("Favoritar produtos")

        tab1, tab2, tab3 = st.tabs(["Favoritar", "Desfavoritar", "Ver meus favoritos"])
        with tab1: ManterFavoritoUI.favoritar()
        with tab2: ManterFavoritoUI.desfavoritar()
        with tab3: ManterFavoritoUI.meus_favoritos()

    def favoritar():
        idCliente = st.session_state["cliente_id"]
        op = st.selectbox("Selecione o produto que você deseja favoritar", View.produto_listar())
        if op: 
            idProduto = op.get_idProduto()
            if st.button("Curtir"):
                c = Favorito(idProduto, idCliente)
                View.favoritar(c)
                st.success("Item favoritado com sucesso!")

    def desfavoritar(): # na teoria, tá funcionando kkkkk
        idCliente = st.session_state["cliente_id"]
        produtos_fav = View.produtos_favoritos(idCliente)
        if produtos_fav == None:
            st.write("Nenhum produto favoritado até o momento.")
        else:
            if produtos_fav: 
                op = st.selectbox("Selecione o produto que você deseja desfavoritar", produtos_fav, format_func=lambda p: f"Id: {p['idProduto']} / Produto: {p['Produto']} / Preço: {p['Preço']}")
                idProduto = op["idProduto"]
                c = Favorito(idProduto, idCliente)
                if op and st.button("Desfavoritar"):
                    View.desfavoritar(c)
                    st.success("Item desfavoritado com sucesso!")
                    st.rerun()
        
    def meus_favoritos():
        idCliente = st.session_state["cliente_id"]
        favoritos = View.produtos_favoritos(idCliente)
        if favoritos == None:
            st.write("Nenhum produto favoritado até o momento.")
        else:
            df = pd.DataFrame(favoritos)
            st.dataframe(df, hide_index=True, column_order=["idProduto", "Produto", "Preço"])