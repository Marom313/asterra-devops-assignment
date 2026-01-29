from sqs_client import get_message
from s3_client import download_file
from db import load_geojson_to_db
import geopandas as gpd
import json

def start_worker():
    print("Worker started...")

    message = get_message()
    if not message:
        print("No messages")
        return

    s3_key = message["s3_key"]
    local_path = download_file(s3_key)

    gdf = gpd.read_file(local_path)
    load_geojson_to_db(gdf)

    print("File processed successfully")
