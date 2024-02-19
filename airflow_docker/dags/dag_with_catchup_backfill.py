from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {
    'owner':'Shiv',
    'retries': 5,
    'retry_delay': timedelta(minutes=5)
}

with DAG(
    dag_id='dag_with_catchup_backup_v3',
    default_args =default_args,
    start_date=datetime(2024,2,1),
    schedule_interval='@daily',
    catchup=False
) as dag:
    task1 = BashOperator(
        task_id='task1',
        bash_command='echo Yellow, this is bash command being bashing around'
    )