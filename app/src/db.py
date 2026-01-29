import os
from sqlalchemy import create_engine

def load_geojson_to_db(gdf):
    db_url = os.getenv("DATABASE_URL")
    engine = create_engine(db_url)
    gdf.to_postgis("geo_data", engine, if_exists="append")
