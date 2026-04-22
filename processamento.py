import pandas as pd

print("⏳ Lendo o arquivo CSV bruto (Camada Raw)...")
df = pd.read_csv('transacoes_raw.csv')

# Simulando uma limpeza básica: garantindo que a data seja reconhecida como data de verdade
df['data_transacao'] = pd.to_datetime(df['data_transacao'])

# Removendo qualquer linha que tenha vindo em branco (nula) por erro do sistema
df = df.dropna()

print("🔄 Convertendo e comprimindo os dados...")
# Salvando no formato otimizado Parquet (Camada Processed)
df.to_parquet('transacoes_processed.parquet', engine='pyarrow', index=False)

print("✅ Sucesso! Arquivo transacoes_processed.parquet gerado e pronto para o Banco de Dados.")