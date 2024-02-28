from datetime import datetime, timedelta

from airflow import DAG
from airflow.providers.amazon.aws.sensors.s3 import S3KeySensor

default_args = {
    'owner':'Shiv',
    'retries': 5,
    'retry_delay': timedelta(minutes=5)
}

with DAG (
    default_args=default_args,
    start_date=datetime(2024, 2, 23),
    schedule_interval='@daily',
    dag_id='dag_with_minio_s3_v03'
) as dag:
    task1 = S3KeySensor(
        task_id='sensor_minio_s3',
        bucket_name='airflow',
        bucket_key='data.csv',
        aws_conn_id='minio_s3_conn'
    )

    # Error when running the Minio docker
    # When creating the connection in Airflow, the endpoint URL connection could not be setup as
    # host.docker.internal:9000 doesnt work
    # Tested with localhost as well