import datetime
from airflow import DAG
from airflow.operators.empty import EmptyOperator

# Outro modo de criar uma dag, criando variavel e executando.

minha_dag = DAG(
    dag_id="minha_segunda_dag",
    start_date=datetime.datetime(2025, 10, 8),
    schedule="@daily",
    catchup=False
)

EmptyOperator(task_id="tarefa", dag=minha_dag)
