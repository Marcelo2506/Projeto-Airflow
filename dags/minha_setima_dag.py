from time import sleep

from airflow.decorators import dag, task
from airflow.models.baseoperator import chain

from datetime import datetime

# Manipulação de tasks com chain


@dag(
    dag_id="setima_pipeline",
    description="minha etl 7",
    schedule="* * * * *",
    start_date=datetime(2025, 10, 8),
    catchup=False  # backfill,
)
def minha_setima_pipeline():

    @task
    def primeira_atividade():
        print("minha primeira atividade - Hello World")
        sleep(2)

    @task
    def segunda_atividade(response):
        print("minha segunda atividade - Hello World 2")
        sleep(2)

    @task
    def terceira_atividade():
        print("minha terceira atividade - Hello World 3")
        sleep(2)

    @task
    def quarta_atividade():
        print("pipeline finalizou")

    t1 = primeira_atividade()
    t2 = segunda_atividade(t1)
    t3 = terceira_atividade()
    t4 = quarta_atividade()

    chain(t1, t2, t3, t4)


minha_setima_pipeline()
