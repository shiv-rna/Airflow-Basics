from datetime import datetime, timedelta

from airflow.decorators import dag, task

default_args = {
    'owner': 'Shiv',
    'retries': 5,
    'retry_delay': timedelta(minutes=5)
}

@dag(dag_id='dag_with_taskflow_api_v02',
     default_args=default_args,
     start_date=datetime(2021, 10, 26),
     schedule_interval='@daily')
def hello_world_etl():


    @task(multiple_outputs=True)
    def get_name():
        return {
            'first_name': 'Jerry',
            'last_name':'Jello'
        }
    
    @task()
    def get_age():
        return "21"
    
    @task()
    def greet(f_name, l_name, age):
        print(f"Yellow, I am {f_name} {l_name} & I am {age} years")

    name_dict = get_name()
    age = get_age()
    greet(f_name= name_dict['first_name'], 
          l_name = name_dict['last_name'], 
          age=age)

# Creating an instance of the DAG
# Taskflow API automatically calculates the dependencies
greet_dag = hello_world_etl()

# Note : Something is weird happening, instead of running just once, this DAG is running 
# running multiple times, when triggered --> Check if there is issue with Code
    