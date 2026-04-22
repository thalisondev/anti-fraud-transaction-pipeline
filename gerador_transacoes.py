import pandas as pd
from faker import Faker
import random

# Configurando pro Brasil
fake = Faker('pt_BR')

def gerar_transacoes(num_registros=800):
    dados = []
    categorias = ['Apple', 'Samsung', 'Google', 'Amazon', 'Microsoft', 'Nike', 'Coca-Cola', "McDonald's", 'Brahma']
    
    for _ in range(num_registros):
        # Sorteio: 5% de chance de criarmos uma transação "criminosa"
        is_fraude_obvia = random.random() < 0.05 
        
        # Se for normal, valor até 500 reais. Se for fraude, de 5 mil a 20 mil!
        valor = round(random.uniform(5000.0, 20000.0), 2) if is_fraude_obvia else round(random.uniform(10.0, 800.0), 2)
        categoria = 'fonte do sabor' if is_fraude_obvia else random.choice(categorias)
        
        registro = {
            'id_transacao': fake.uuid4(),
            'id_cliente': random.randint(1000, 1050), # 50 clientes recorrentes pra gente ver o histórico depois
            'data_transacao': fake.date_time_between(start_date='-30d', end_date='now').strftime("%Y-%m-%d %H:%M:%S"),
            'valor_brl': valor,
            'categoria': categoria,
            'cidade_transacao': fake.city(),
            'metodo_pagamento': random.choice(['Cartão de Crédito', 'Pix', 'Cartão de Débito'])
        }
        dados.append(registro)
        
    return dados

# Gerando e salvando
df = pd.DataFrame(gerar_transacoes(800))
df.to_csv('transacoes_raw.csv', index=False)
print("🚨 Arquivo transacoes_raw.csv gerado com sucesso! Contém transações normais e tentativas de fraude.")