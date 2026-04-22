import duckdb

print("🔌 Conectando ao Banco de Dados (DuckDB)...")
con = duckdb.connect('warehouse.db')

print("🥇 Gerando a Camada Gold (Isolando as fraudes)...")

# O comando COPY pega o resultado do SELECT e salva direto em um novo arquivo!
query_gold = """
    COPY (
        SELECT 
            id_cliente, 
            data_transacao, 
            categoria, 
            valor_brl, 
            cidade_transacao
        FROM 'transacoes_processed.parquet' -- Lendo da nossa camada Silver
        WHERE valor_brl > 3000              -- Nossa regra de negócio
        ORDER BY valor_brl DESC
    ) TO 'fraudes_gold.parquet' (FORMAT PARQUET);
"""

con.execute(query_gold)

print("✅ Sucesso! O arquivo 'fraudes_gold.parquet' (Camada Gold) foi gerado.")
print("Agora o sistema do banco já pode ler esse arquivo para bloquear os cartões e gerar os gráficos!")