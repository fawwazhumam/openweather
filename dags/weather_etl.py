from datetime import datetime, timezone

from airflow.providers.standard.operators.python import PythonOperator
from airflow.sdk import DAG


def extract():
    print("TODO: ambil data dari OpenWeather")


with DAG(
    dag_id="weather_etl",
    start_date=datetime(2026, 1, 1, tzinfo=timezone.utc),
    schedule="@daily",
    catchup=False,
) as dag:
    extract_task = PythonOperator(task_id="extract", python_callable=extract)
