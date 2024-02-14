from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {
    'owner': 'shiv',
    'retries': 5,
    'retry_delay': timedelta(minutes=5)
}

with DAG(
    default_args=default_args,
    dag_id='dag_with_catchup_backfill_v1',
    description='DAG with catchup & backfill',
    start_date=datetime(2024, 5, 1),
    schedule_interval ='@daily',
    catchup=True
    ) as dag:
    task1 = BashOperator(
        task_id = 'task1',
        bash_command='echo This is bash command'
    )

