import streamlit as st
from views import View

class LoginUI:
    def main():
        st.header("Entrar no sistema")
        email = st.text_input("E-mail")
        senha = st.text_input("Senha", type="password")
        if st.button("Entrar"):
            autenticacao = View.cliente_autenticar(email, senha)
            if autenticacao == None: st.write("E-mail ou senha inválidos")
            else:
                st.session_state["cliente_id"] = autenticacao["id"]
                st.session_state["cliente_nome"] = autenticacao["nome"]
                st.session_state["cliente_email"] = autenticacao["email"]
                st.rerun()