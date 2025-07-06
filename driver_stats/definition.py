from datetime import timedelta
from feast.types import Float32
from feast import Entity, Field, FeatureView, FileSource, ValueType

driver_entity = Entity(
    name="driver_id",
    join_keys=["driver_id"],
    value_type=ValueType.INT64,
    description="The ID of the driver"
)

file_source = FileSource(
    path="data/driver_stats_with_string.parquet",
    event_timestamp_column="event_timestamp",
    created_timestamp_column="created"
)

driver_stats_fv = FeatureView(
    name="driver_stats_fv",
    ttl=timedelta(days=3),
    description="This feature view contains the statistics of the drivers",
    entities=[driver_entity],
    schema=[
        Field(name="conv_rate", dtype=Float32),
        Field(name="acc_rate", dtype=Float32),
        Field(name="avg_daily_trips", dtype=Float32)
    ],
    source=file_source
)
