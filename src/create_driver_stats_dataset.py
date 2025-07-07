import pandas as pd
import numpy as np
from feast import FeatureStore
from feast.infra.offline_stores.file_source import SavedDatasetFileStorage

store = FeatureStore(repo_path="driver_stats/")

timestamps = pd.date_range(
    start="2021-08-31",
    end="2021-09-04",
    freq='H'
).to_frame(name="event_timestamp", index=False)

# Dropping the first 17 hours of the day
timestamps = timestamps.drop(labels=np.arange(18), axis=0)
driver_ids = pd.DataFrame(
    data=[1001, 1002, 1003, 1004, 1005],
    columns=["driver_id"]
)

entity_df = timestamps.merge(
    right=driver_ids,
    how="cross"
)

data_job = store.get_historical_features(
    entity_df=entity_df,
    features=[
        "driver_stats_fv:conv_rate",
        "driver_stats_fv:acc_rate",
        "driver_stats_fv:avg_daily_trips",
    ]
)

dataset = store.create_saved_dataset(
    from_=data_job,
    name="driver_stats",
    storage=SavedDatasetFileStorage(
        path="../driver_stats/data/driver_stats.parquet"
    )
)

driver_id = pd.DataFrame(
    data=[1001],
    columns=["driver_id"]
)

entity_df_1001 = timestamps.merge(
    right=driver_id,
    how="cross"
)

data_job_1001 = store.get_historical_features(
    entity_df=entity_df_1001,
    features=[
        "driver_stats_fv:conv_rate",
        "driver_stats_fv:acc_rate",
        "driver_stats_fv:avg_daily_trips",
    ]
)

dataset_1001 = store.create_saved_dataset(
    from_=data_job_1001,
    name="driver_stats_1001",
    storage=SavedDatasetFileStorage(
        path="../driver_stats/data/driver_stats_1001.parquet"
    )
)
