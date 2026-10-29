import streamlit as st
from calculadora import Calculadora

st.set_page_config(
    page_title="Calculadora em Python",
    page_icon="🧮",
    layout="centered"
)

if "calculadora" not in st.session_state:
    st.session_state.calculadora = Calculadora(persistir=False)

if "resultado" not in st.session_state:
    st.session_state.resultado = None

if "mensagem_erro" not in st.session_state:
    st.session_state.mensagem_erro = None

calc = st.session_state.calculadora

st.markdown("""
<style>
    .stApp {
        background: linear-gradient(135deg, #0f172a, #1e293b);
    }

    .main-title {
        text-align: center;
        color: white;
        font-size: 2.2rem;
        font-weight: 700;
        margin-bottom: 0.2rem;
    }

    .subtitle {
        text-align: center;
        color: #cbd5e1;
        margin-bottom: 2rem;
    }

    .card {
        background: rgba(255,255,255,0.08);
        padding: 24px;
        border-radius: 20px;
        box-shadow: 0 8px 30px rgba(0,0,0,0.25);
        backdrop-filter: blur(8px);
        border: 1px solid rgba(255,255,255,0.08);
        margin-bottom: 20px;
    }

    .result-box {
        background: #111827;
        color: #22c55e;
        font-size: 1.8rem;
        font-weight: bold;
        text-align: center;
        padding: 18px;
        border-radius: 14px;
        margin-top: 12px;
        border: 1px solid #334155;
    }

    .history-item {
        background: rgba(255,255,255,0.05);
        color: white;
        padding: 12px 14px;
        border-radius: 12px;
        margin-bottom: 10px;
        border: 1px solid rgba(255,255,255,0.06);
    }

    div[data-testid="stNumberInput"] label,
    div[data-testid="stSelectbox"] label {
        color: #e2e8f0 !important;
        font-weight: 600;
    }

    .section-title {
        color: white;
        font-size: 1.1rem;
        font-weight: 700;
        margin-bottom: 10px;
    }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">🧮 Calculadora em Python</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Desafio 01 • Imersão Alura • Engenharia de Software na Era da IA</div>', unsafe_allow_html=True)

st.markdown('<div class="card">', unsafe_allow_html=True)
st.markdown('<div class="section-title">Digite os valores</div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    numero1 = st.number_input("Primeiro número", value=0.0, step=1.0)
with col2:
    numero2 = st.number_input("Segundo número", value=0.0, step=1.0)

st.markdown('<div class="section-title">Escolha a operação</div>', unsafe_allow_html=True)

b1, b2, b3, b4 = st.columns(4)

def executar(operador):
    resultado = calc.calcular(numero1, operador, numero2)
    if resultado["sucesso"]:
        st.session_state.resultado = f"{resultado['expressao']} = {resultado['resultado']}"
        st.session_state.mensagem_erro = None
    else:
        st.session_state.resultado = None
        st.session_state.mensagem_erro = resultado["erro"]

with b1:
    if st.button("＋", use_container_width=True):
        executar("+")
with b2:
    if st.button("－", use_container_width=True):
        executar("-")
with b3:
    if st.button("×", use_container_width=True):
        executar("*")
with b4:
    if st.button("÷", use_container_width=True):
        executar("/")

if st.session_state.resultado:
    st.markdown(f'<div class="result-box">{st.session_state.resultado}</div>', unsafe_allow_html=True)

if st.session_state.mensagem_erro:
    st.error(st.session_state.mensagem_erro)

st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="card">', unsafe_allow_html=True)
st.markdown('<div class="section-title">Histórico</div>', unsafe_allow_html=True)

if calc.historico:
    historico_invertido = list(reversed(calc.historico))
    for item in historico_invertido:
        st.markdown(
            f'<div class="history-item">{item["expressao"]} = <strong>{item["resultado"]}</strong></div>',
            unsafe_allow_html=True
        )

    if st.button("Limpar histórico", use_container_width=True):
        calc.limpar_historico()
        st.session_state.resultado = None
        st.session_state.mensagem_erro = None
        st.rerun()
else:
    st.info("Nenhum cálculo realizado ainda.")

st.markdown('</div>', unsafe_allow_html=True)
