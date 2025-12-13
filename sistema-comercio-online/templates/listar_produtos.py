import streamlit as st
import pandas as pd
from views import View

class ListarProdutosUI:
    def main():
        produtos = View.produto_listar()
        if len(produtos) == 0: st.write("Nenhum produto até o momento")
        else:
            list_dic = []
            for produto in produtos: list_dic.append(produto.to_json())
            df = pd.DataFrame(list_dic)
            st.dataframe(df, hide_index=True, column_order=["id", "descricao", "preco", "estoque", "idCategoria"])