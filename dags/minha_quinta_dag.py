from time import sleep
from airflow.decorators import dag, task
from datetime import datetime

# Neste Código outra forma de manusear o fluxo de tasks, agora usando upstream e downstream


@dag(
    dag_id="quinta_pipeline",
    description="ETL",
    schedule="* * * * *",
    start_date=datetime(2025, 10, 9),
    catchup=False
)
def quinta_pipeline():
    @task
    def primeira_atividade():
        print("minha primeira atividade! - Hello World")
        sleep(2)

    @task
    def segunda_atividade():
        print("minha segunda atividade! - Hello World")
        sleep(2)

    @task
    def terceira_atividade():
        print("minha terceira atividade - Hello World")
        sleep(2)

    @task
    def quarta_atividade():
        print("pipeline finalizou")

    t1 = primeira_atividade()
    t2 = segunda_atividade()
    t3 = terceira_atividade()
    t4 = quarta_atividade()

    t1.set_downstream([t2, t3])  # T1 executa t2 e t3
    t3.set_upstream([t4])  # T4 executa t3


quinta_pipeline()
