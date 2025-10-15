FROM astrocrpublic.azurecr.io/runtime:3.1-2

#ADICIONAR AS BIBLIOTECAS EXTRA AIRFLOW NO REQUIREMENTS
RUN pip install -r requirements.txt 