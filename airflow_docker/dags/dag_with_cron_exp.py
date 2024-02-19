from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {
    'owner': 'Shiv',
    'retries': 5,
    'retry_delay':timedelta(minutes=5)
}

with DAG(
    default_args=default_args,
    dag_id="dag_with_cron_expression_v4",
    start_date=datetime(2024, 2, 10),
    schedule_interval='0 3 * * Tue-Fri'
    # Cron Expression: minute - hour - day(month) - month - day(week)
) as dag:
    task1 = BashOperator(
        task_id='task1',
        bash_command="echo dag with cron expression"
    )