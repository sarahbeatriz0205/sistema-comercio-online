import streamlit as st
import pandas as pd
from views import View

class ListarVendasUI:
    def main():
        st.header("Todas as vendas")
        vendas = View.listar_compras_admin()
        if len(vendas) == 0:
            st.write("Nenhuma venda até agora.")
        else:
            df = pd.DataFrame(vendas)
            st.dataframe(
                df,
                hide_index=True,
                column_order=["idVenda", "cliente", "produto", "unitario", "quantidade", "preco_item", "total_venda"])