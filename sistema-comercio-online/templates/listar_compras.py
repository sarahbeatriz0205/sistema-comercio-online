import streamlit as st
import pandas as pd
from views import View

class ListarMinhasComprasUI:
    def main():
        idCliente = st.session_state["cliente_id"]
        compras, total_geral = View.listar_compras(idCliente)

        if not compras:
            st.write("Nenhuma compra até o momento")
        else:
            df = pd.DataFrame(compras)
            st.dataframe(df, hide_index=True, column_order=["idVenda", "descricao", "unitario", "quantidade", "preco_total"])
            st.write(f"**Total todas vendas: R$ {total_geral:,.2f}**")