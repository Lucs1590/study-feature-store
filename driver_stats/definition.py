from datetime import timedelta

from feast import (
    Entity,
    FeatureView,
    Field,
    FileSource,
    ValueType
)
from feast.types import Float32, Int64

driver_entity = Entity(
    name="driver_id",
    join_keys=["driver_id"],
    value_type=ValueType.INT64,
    description="The ID of the driver"
)

file_source = FileSource(
    path="data/driver_stats_with_string.parquet",
    timestamp_field="event_timestamp",
    created_timestamp_column="created"
)
driver_stats_fv = FeatureView(
    name="driver_stats_fv",
    entities=[driver_entity],
    ttl=timedelta(days=3),
    schema=[
        Field(name="conv_rate", dtype=Float32),
        Field(name="acc_rate", dtype=Float32),
        Field(name="avg_daily_trips", dtype=Float32)
    ],
    source=file_source,
    description="This feature view contains the statistics of the drivers",
)
