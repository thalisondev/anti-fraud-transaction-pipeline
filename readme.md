
# Anti-Fraud Transaction Pipeline 

The simplest and fastest repository to understand a data pipeline using the Medallion Architecture (Raw -> Silver -> Gold). This project demonstrates data ingestion, processing, and fraud detection using **DuckDB**, **Parquet**, and **Streamlit**.

The code is plain and readable: `processamento.py` handles data cleaning and `analise_fraudes.py` uses high-performance analytical SQL to filter anomalies.

## Install

```bash
pip install -r requirements.txt
```
## Quick Start

If you want to feel the "magic" and see the pipeline in action, follow these steps:

   Generate Raw Data:
    
    python gerador_transacoes.py

   This creates a transacoes_raw.csv file with synthetic records (including high-value suspicious transactions).

   Process to Silver (Parquet):

    python processamento.py

   The script cleans the data, fixes datetime types, and converts the CSV into the optimized binary .parquet format.

   Run Fraud Analysis (Gold):
    
    python analise_fraudes.py

   Uses DuckDB to read the Parquet file via SQL and isolate transactions above R$ 3,000, saving the result to fraudes_gold.parquet.

   Launch the Dashboard:
    
    streamlit run dashboard.py

Data Layers (Medallion Architecture)

The project follows the medallion architecture to ensure data quality and lineage:

    Raw (Bronze): Crude CSV data exactly as it comes from the source.

    Processed (Silver): Cleaned Parquet data with corrected types (datetime) and no null values.

    Gold: The "best" data. Contains only transactions filtered by the business rule (Potential Frauds).

Efficiency with DuckDB

Unlike traditional databases, using DuckDB allows you to process Parquet files almost instantly on your machine without the need for heavy server installations. It is the modern stack for local Data Engineering.
Todos

    [ ] Implement a Machine Learning model for anomaly detection.

    [ ] Add unit tests with pytest.

    [ ] Automate the pipeline using Airflow or Prefect.
    other languages

🇧🇷 Portuguese: README.pt-br.md

contact:

 linkedin: https://www.linkedin.com/in/thalison-dev
