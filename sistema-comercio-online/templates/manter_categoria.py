import streamlit as st
import pandas as pd
from views import View

class ManterCategoriaUI:
    def main():
        st.header("Cadastro de categorias")

        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1: ManterCategoriaUI.listar()
        with tab2: ManterCategoriaUI.inserir()
        with tab3: ManterCategoriaUI.atualizar()
        with tab4: ManterCategoriaUI.excluir()

    def listar():
        categorias = View.categoria_listar()
        if len(categorias) == 0: st.write("Nenhum categoria até o momento")
        else:
            list_dic = []
            for categoria in categorias: list_dic.append(categoria.to_json())
            df = pd.DataFrame(list_dic)
            st.dataframe(df, hide_index=True, column_order=["id", "descricao"]) 

    def inserir():
        id = 0
        descricao = st.text_input("Descrição")
        if st.button("Inserir"): 
            View.categoria_inserir(descricao)
            st.success("Categoria adicionado com sucesso!")
            st.rerun()

    def atualizar():
        categorias = View.categoria_listar()
        if len(categorias) == 0: st.write("Nenhum categoria cadastrada até o momento")
        else:
            op = st.selectbox("Atualizar categorias", categorias)
            descricao = st.text_input("Nova descrição",  op.get_descricao())
            if st.button("Atualizar"):
                id = op.get_id()
                View.categoria_atualizar(id, descricao)
                st.success("Categoria atualizada com sucesso!")
                st.rerun()
    
    def excluir():
        # selecionar um produto já existente e excluir
        categorias = View.categoria_listar()
        if len(categorias) == 0: st.write("Nenhum categoria cadastrada até o momento")
        else:
            op = st.selectbox("Excluir Categorias", categorias)
            if op:
                if st.button("Excluir"):
                    id = op.get_id()
                    descricao = op.get_descricao()
                    View.categoria_excluir(id, descricao)
                    st.success("Categoria excluído com sucesso!")
                    st.rerun()