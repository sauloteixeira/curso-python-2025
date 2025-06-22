import streamlit as st
import requests
import pandas as pd
# Define a função para buscar o CEP
def buscar_cep(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    resposta = requests.get(url)
    
    if resposta.status_code == 200:
        dados = resposta.json()
        if "erro" not in dados:
            return dados
        else:
            st.error("CEP não encontrado.")
            return None
    else:
        st.error("Erro ao consultar o CEP. Verifique se o CEP está correto.")
        return None
# Configuração do Streamlit
st.title("Consulta de CEP")
cep_input = st.text_input("Digite o CEP (somente números):", "")
if st.button("Buscar"):
    if cep_input:
        dados_cep = buscar_cep(cep_input)
        if dados_cep:
            st.subheader("Dados do CEP")
            st.write(f"CEP: {dados_cep['cep']}")
            st.write(f"Logradouro: {dados_cep['logradouro']}")
            st.write(f"Bairro: {dados_cep['bairro']}")
            st.write(f"Cidade: {dados_cep['localidade']}")
            st.write(f"Estado: {dados_cep['uf']}")
    else:
        st.warning("Por favor, insira um CEP válido.")
# Exibir o DataFrame com os dados do CEP
if 'dados_cep' in locals():
    df = pd.DataFrame([dados_cep])
    st.subheader("Dados em formato de tabela")
    st.dataframe(df)

