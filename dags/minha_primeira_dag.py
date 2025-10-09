import datetime
from airflow import DAG
from airflow.operators.empty import EmptyOperator


# Forma mais antiga de criar uma DAG

with DAG(
    dag_id="meu_nome_de_dag",
    start_date=datetime.datetime(2021, 1, 1),
    schedule="@daily",
    # Backfill comeca a rodar o código a partir da start_date dia por dia.
    catchup=False
):
    EmptyOperator(task_id="tarefa")
