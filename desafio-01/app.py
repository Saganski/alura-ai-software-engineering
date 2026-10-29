
import streamlit as st
from calculadora import Calculadora

st.set_page_config(
    page_title="Calculadora em Python",
    page_icon="🧮",
    layout="centered"
)

if "calculadora" not in st.session_state:
    st.session_state.calculadora = Calculadora(persistir=False)

calc = st.session_state.calculadora

st.title("🧮 Calculadora em Python")
st.caption("Desafio 01 — Imersão Alura | Engenharia de Software com IA")

st.subheader("Realize seu cálculo")

col1, col2 = st.columns(2)

with col1:
    numero1 = st.number_input("Primeiro número", value=0.0)

with col2:
    numero2 = st.number_input("Segundo número", value=0.0)

operacoes = {
    "Somar (+)": "+",
    "Subtrair (-)": "-",
    "Multiplicar (×)": "*",
    "Dividir (÷)": "/"
}

operacao = st.selectbox(
    "Escolha a operação",
    list(operacoes.keys())
)

if st.button("Calcular", type="primary", use_container_width=True):
    resultado = calc.calcular(
        numero1,
        operacoes[operacao],
        numero2
    )

    if resultado["sucesso"]:
        st.success(f"Resultado: {resultado['resultado']}")
    else:
        st.error(resultado["erro"])

st.divider()

st.subheader("Histórico de cálculos")

if calc.historico:
    for item in calc.historico:
        st.write(f"{item['expressao']} = **{item['resultado']}**")

    if st.button("Limpar histórico"):
        calc.limpar_historico()
        st.rerun()
else:
    st.info("Nenhum cálculo realizado ainda.")
