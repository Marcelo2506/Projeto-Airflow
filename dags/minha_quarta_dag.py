from time import sleep
from airflow.decorators import dag, task
from datetime import datetime

# Neste código variamos o fluxo de tasks


@dag(
    dag_id="quarta_pipeline",
    description="ETL",
    schedule="* * * * *",
    start_date=datetime(2025, 10, 8),
    catchup=False
)
def quarta_pipeline():

    @task
    def primeira_atividade():
        print("primeira atividade! - Hello World")
        sleep(2)

    @task
    def segunda_atividade():
        print("segunda atividade! - Olá Mundo!")
        sleep(2)

    @task
    def terceira_atividade():
        print("terceira atividade! - ¡Hola, mundo!")
        sleep(2)

    @task
    def quarta_atividade():
        print("quarta atividade! - Bonjour, le monde !")
        sleep(2)

    t1 = primeira_atividade()
    t2 = segunda_atividade()
    t3 = terceira_atividade()
    t4 = quarta_atividade()

    t1 >> [t2, t3]  # t1 aciona t2 e t3
    t3 << t4  # t4 aciona t3


quarta_pipeline()
