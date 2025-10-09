from time import sleep
from airflow.decorators import dag, task
from datetime import datetime

# Neste Código Utilizo a técnica de decoradores para executar


@dag(
    dag_id="minha_terceira_dag",
    description="ETL",
    schedule="* * * * *",  # roda o código de 1 em 1 minuto
    start_date=datetime(2025, 10, 8),
    catchup=False
)
def minha_terceira_dag():

    @task
    def primeira_atividade():
        print("Primeira atividade, Realizada!")
        sleep(2)

    @task
    def segunda_atividade():
        print("Segunda Atividade, Realizada!")
        sleep(2)

    @task
    def terceira_atividade():
        print("Terceira Atividade, Realizada!")
        sleep(2)

    @task
    def quarta_atividade():
        print("Quarta Atividade, Realizada!")

    t1 = primeira_atividade()
    t2 = segunda_atividade()
    t3 = terceira_atividade()
    t4 = quarta_atividade()

    t1 >> t2 >> t3 >> t4  # Com isso, determinamos a ordem das tasks


minha_terceira_dag()
