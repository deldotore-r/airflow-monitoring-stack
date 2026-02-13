from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
import requests
import pandas as pd
from pathlib import Path
import pendulum

# Configuração de Fuso Horário (Lisboa coincide com UTC no inverno, mas pendulum evita erros no verão)
local_tz = pendulum.timezone("Europe/Lisbon")

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2026, 2, 9, tzinfo=local_tz),
    'retries': 1,
    'retry_delay': timedelta(minutes=1),
}

def coletar_cotacao(**context):
    """Extrai dados da API e salva no CSV"""
    url = "https://economia.awesomeapi.com.br/json/last/EUR-BRL"
    response = requests.get(url)
    response.raise_for_status()
    
    data = response.json()['EURBRL']
    
    resultado = {
        'timestamp': datetime.now(local_tz).strftime('%Y-%m-%d %H:%M:%S'),
        'cotacao': float(data['bid']),
        'variacao': float(data['pctChange']),
        'maxima': float(data['high']),
        'minima': float(data['low'])
    }
    
    data_path = Path('/opt/airflow/data')
    data_path.mkdir(exist_ok=True)
    csv_file = data_path / 'cotacoes_eur_brl.csv'
    
    df = pd.DataFrame([resultado])
    df.to_csv(csv_file, mode='a', header=not csv_file.exists(), index=False)
    
    print(f"Coleta realizada com sucesso: {resultado['cotacao']}")

with DAG(
    'cambio_brl_eur_coleta',
    default_args=default_args,
    description='Ingestão de câmbio EUR/BRL (Janela PT-BR)',
    # AJUSTE: O intervalo 9-20 garante que a última execução seja às 20:55.
    # Se fosse 9-21, o Airflow continuaria coletando até as 21:55.
    schedule_interval='*/5 9-20 * * 1-5',
    catchup=False,
    tags=['ingestao', 'cambio'],
) as dag:

    task_coletar = PythonOperator(
        task_id='coletar_cotacao_eur_brl',
        python_callable=coletar_cotacao,
    )