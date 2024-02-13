from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator

default_args = {
    'owner': 'shiv',
    'retries': 5,
    'retry_delay':timedelta(minutes=5)
}

def greet(name, age):
    print(f"Yellow World ! My name is {name}saurus, and I am {age} billion years old!")

with DAG(
    default_args=default_args,
    dag_id='our_dag_with_python_operator_v2',
    description='Our first dag using python operator',
    start_date=datetime(2024, 2, 13),
    schedule_interval='@daily'
) as dag:
    task1 = PythonOperator(
        task_id='greet',
        python_callable=greet,
        op_kwargs={'name':'Shiv', 'age':27} #Dictionary of key words as arguments
    )
