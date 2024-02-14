from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator

default_args = {
    'owner': 'shiv',
    'retries': 5,
    'retry_delay':timedelta(minutes=5)
}

def greet(ti):
    f_name = ti.xcom_pull(task_ids='get_name', key='first_name')
    l_name = ti.xcom_pull(task_ids='get_name', key='last_name')
    age    = ti.xcom_pull(task_ids='get_age', key='age')
    print(f"Yellow World ! My name is {f_name}saurus {l_name}don, and I am {age} billion years old!")

def get_name(ti):
    ti.xcom_push(key='first_name', value='Jeremy')
    ti.xcom_push(key='last_name', value='Jelly')

def get_age(ti):
    ti.xcom_push(key='age', value='2')


with DAG(
    default_args=default_args,
    dag_id='our_dag_with_python_operator_v8',
    description='Our first dag using python operator',
    start_date=datetime(2024, 2, 13),
    schedule_interval='@daily'
) as dag:
    task1 = PythonOperator(
        task_id='greet',
        python_callable=greet,
        # op_kwargs={name:'Shiv', 'age':27} #Dictionary of key words as arguments
    )

    task2 = PythonOperator(
        task_id='get_name',
        python_callable=get_name,      
    )

    task3 = PythonOperator(
        task_id='get_age',
        python_callable=get_age,
    )

    [task2,task3]>>task1
