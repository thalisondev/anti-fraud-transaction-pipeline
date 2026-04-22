import streamlit as st
import pandas as pd

# Configuração da página para ficar larga e com título bonito
st.set_page_config(page_title="Monitor de Fraudes", page_icon="🚨", layout="wide")

st.title( "Painel de Prevenção a Fraudes")
st.markdown("Monitoramento em tempo real de transações suspeitas bloqueadas pelo sistema.")

# Carregando a nossa Camada Gold
try:
    df_gold = pd.read_parquet('fraudes_gold.parquet')
    # Criando os "Cards" (KPIs) com os resumos lá no topo
    col1, col2, col3 = st.columns(3)
    col1.metric("Total de Fraudes Bloqueadas", len(df_gold))
    col2.metric("Valor Total Salvo (R$)", f"R$ {df_gold['valor_brl'].sum():,.2f}")
    col3.metric("Maior Tentativa de Golpe (R$)", f"R$ {df_gold['valor_brl'].max():,.2f}")
    
    st.divider()

    # Dividindo a tela em duas colunas para os gráficos
    grafico_col, tabela_col = st.columns([1, 1])

    with grafico_col:
        st.subheader("📍 Cidades Alvo dos Golpistas")
        # Conta quantas fraudes teve por cidade e gera um gráfico de barras
        cidades_afetadas = df_gold['cidade_transacao'].value_counts()
        st.bar_chart(cidades_afetadas)

    with tabela_col:
        st.subheader("📋 Relatório Detalhado")
        st.dataframe(df_gold, use_container_width=True)

except FileNotFoundError:
    st.error("Arquivo da Camada Gold não encontrado. Rode o pipeline de análise primeiro!")