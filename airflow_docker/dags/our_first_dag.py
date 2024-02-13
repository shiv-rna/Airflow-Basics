from datetime  import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator

#Default Args is dictionary variable containing the default values
default_args={
        'owner':'shiv',
        'retries':5,
        'retry_delay': timedelta(minutes=2)
}

#Defining the DAG
with DAG(
    dag_id='our_first_dag_v5',
    default_args=default_args,
    description='This our first dag that we write',
    start_date=datetime(2024, 2, 12, 8),
    schedule_interval='@daily'
    ) as dag:
        task1 = BashOperator(
                task_id='first_task',
                bash_command="echo hellow world, this is the first task!"
        )

        task2 = BashOperator(
                task_id='second_task',
                bash_command="echo I am the second one here!"
        )

        task3 = BashOperator(
                task_id='third_task',
                bash_command="echo Yo-yo! I am the amazing third one here!" 
        )

        task1 >> [task2, task3]
        
        # task1 >> task2
        # task1 >> task3

        # task1.set_downstream(task2)
        # task1.set_downstream(task3)
