
# Anti-Fraud Transaction Pipeline 

O repositório mais simples e rápido para entender um pipeline de dados com arquitetura de medalhão (Raw -> Silver -> Gold). Este projeto demonstra a ingestão, processamento e detecção de fraudes em transações financeiras utilizando **DuckDB**, **Parquet** e **Streamlit**.

O código é plano e legível: `processamento.py` faz a limpeza dos dados e `analise_fraudes.py` utiliza SQL analítico de alta performance para filtrar anomalias.

## Instalação

```bash
pip install requirements.txt

Início Rápido

Se você quer apenas sentir a "mágica" e ver o pipeline funcionando, siga estes passos:

    Gerar os dados brutos (Raw):
    Bash

    python gerador_transacoes.py

    Isso cria um arquivo transacoes_raw.csv com registros sintéticos (incluindo transações suspeitas de alto valor).

    Processar para Silver (Parquet):
    Bash

    python processamento.py

    O script limpa os dados, trata tipagens de data e converte o CSV para o formato binário otimizado .parquet.

    Executar análise de fraude (Gold):
    Bash

    python analise_fraudes.py

    Utiliza o DuckDB para ler o arquivo Parquet via SQL e isolar transações acima de R$ 3.000, salvando o resultado em fraudes_gold.parquet.

    Visualizar o Dashboard:
    Bash

    streamlit run dashboard.py

Camadas de Dados (Medallion Architecture)

O projeto segue a arquitetura de medalhão para garantir a qualidade e linhagem do dado:

    Raw (Bronze): Dados brutos em CSV exatamente como gerados pela fonte.

    Processed (Silver): Dados em Parquet, com tipos corrigidos (datetime) e sem valores nulos.

    Gold: O "filé mignon" dos dados. Contém apenas transações filtradas pela regra de negócio (Potenciais Fraudes).

Eficiência com DuckDB

Diferente de bancos de dados tradicionais, o uso de DuckDB permite processar arquivos Parquet quase instantaneamente no seu computador, sem a necessidade de instalar servidores pesados. É a stack moderna para Engenharia de Dados local.
Todos

    [ ] Implementar um modelo de Machine Learning para detecção de anomalias.

    [ ] Adicionar testes unitários com pytest.

    [ ] Criar automação do pipeline com Airflow ou Prefect.
    
contact

 linkedin: https://www.linkedin.com/in/thalison-dev
