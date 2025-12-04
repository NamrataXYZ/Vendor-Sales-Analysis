import pandas as pd
import os
from sqlalchemy import create_engine
import logging
import time

logging.basicConfig(
    filename="logs/ingestion_db.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filemode="a"
)

engine = create_engine('sqlite:///inventory.db')

def load_raw_data():
    start = time.time()
    for file in os.listdir('data'):
        if file.endswith('.csv'):
            path = os.path.join('data', file)
            df = pd.read_csv(path)
            logging.info(f"Ingesting {file} in db")
            ingest_db(df, file[:-4], engine)
    end = time.time()
    total_time = (end-start)/60
    logging.info('------------------Ingestion Complete-------------------')  
    logging.info(f'\nTotal_time_taken: {total_time} minutes')

def ingest_db(df, table_name, engine):
    try:
        df.to_sql(
            table_name,
            con=engine,
            if_exists='replace',  # or 'append' if you want to keep previous tables
            index=False,
            chunksize=50000  # write 50K rows at a time
        )
        print(f"Successfully ingested {table_name} ({len(df)} rows)")
    except MemoryError:
        print(f"MemoryError on {table_name}. Try smaller chunks.")
    except Exception as e:
        print(f"Error ingesting {table_name}: {e}")

if __name__ == '__main__':
    load_raw_data()