from airflow.decorators import task, dag

from include.controller import gerar_numero_aletorio, fetch_pokemon_data, add_pokemon_to_db

from airflow.models.baseoperator import chain

from datetime import datetime


@dag(dag_id="api_postgres",
     description="pipeline_capturar_pokemon",
     start_date=datetime(2025, 10, 13),
     schedule="* * * * *",
     catchup=False
     )
def api_postgres():

    @task(task_id='gerar_numero_aletorio')
    def task_gerar_numero_aletorio():
        return gerar_numero_aletorio()

    @task(task_id='fetch_pokemon_data')
    def task_fetch_pokemon_data(numero_aletorio):
        return fetch_pokemon_data(numero_aletorio)

    @task(task_id="add_pokemon_to_db")
    def task_add_pokemon_to_db(pokemon_data):
        add_pokemon_to_db(pokemon_data)

    @task
    def print_de_sucesso(response):
        print(response)

    t1 = task_gerar_numero_aletorio()
    t2 = task_fetch_pokemon_data(t1)
    t3 = task_add_pokemon_to_db(t2)
    t4 = print_de_sucesso(t3)

    t1 >> t2 >> t3 >> t4


api_postgres()
