import streamlit as st
from views import View

class CriarContaUI:
    def main():
        st.header("Criar Conta")

        nome = st.text_input("Nome completo")
        email = st.text_input("E-mail")
        telefone = st.text_input("Número de telefone")
        senha = st.text_input("Senha", type="password")
        if st.button("Criar Conta"):
            try:
                View.cliente_inserir(nome, email, telefone, senha)
                st.success("Conta criada com sucesso!", icon="✅")
            except Exception as erro:
                st.error(f"{erro}")