from datetime import timedelta
from feast.types import Float32, Int64
from feast import Entity, Field, FeatureView, FileSource, ValueType
patient = Entity(
    name="patient_id",
    join_keys=["patient_id"],
    value_type=ValueType.INT64,
    description="The ID of the patient"
)

f_source1 = FileSource(
    path="data/data_df1.parquet",
    event_timestamp_column="event_timestamp"
)

df1_fv = FeatureView(
    name="df1_feature_view",
    ttl=timedelta(days=3),
    description="This feature view contains the mean features of the breast cancer dataset",
    entities=[patient],
    schema=[
        Field(name="mean radius", dtype=Float32),
        Field(name="mean texture", dtype=Float32),
        Field(name="mean perimeter", dtype=Float32),
        Field(name="mean area", dtype=Float32),
        Field(name="mean smoothness", dtype=Float32)
    ],
    source=f_source1
)

f_source2 = FileSource(
    path="data/data_df2.parquet",
    event_timestamp_column="event_timestamp"
)

df2_fv = FeatureView(
    name="df2_feature_view",
    ttl=timedelta(days=3),
    description="This feature view contains the mean features of the breast cancer dataset",
    entities=[patient],
    schema=[
        Field(name="mean compactness", dtype=Float32),
        Field(name="mean concavity", dtype=Float32),
        Field(name="mean concave points", dtype=Float32),
        Field(name="mean symmetry", dtype=Float32),
        Field(name="mean fractal dimension", dtype=Float32)
    ],
    source=f_source2
)

f_source3 = FileSource(
    path="data/data_df3.parquet",
    event_timestamp_column="event_timestamp"
)

df3_fv = FeatureView(
    name="df3_feature_view",
    ttl=timedelta(days=3),
    description="This feature view contains the error features of the breast cancer dataset",
    entities=[patient],
    schema=[
        Field(name="radius error", dtype=Float32),
        Field(name="texture error", dtype=Float32),
        Field(name="perimeter error", dtype=Float32),
        Field(name="area error", dtype=Float32),
        Field(name="smoothness error", dtype=Float32),
        Field(name="compactness error", dtype=Float32),
        Field(name="concavity error", dtype=Float32)
    ],
    source=f_source3
)

f_source4 = FileSource(
    path="data/data_df4.parquet",
    event_timestamp_column="event_timestamp"
)

df4_fv = FeatureView(
    name="df4_feature_view",
    ttl=timedelta(days=3),
    description="This feature view contains the worst features of the breast cancer dataset",
    entities=[patient],
    schema=[
        Field(name="concave points error", dtype=Float32),
        Field(name="symmetry error", dtype=Float32),
        Field(name="fractal dimension error", dtype=Float32),
        Field(name="worst radius", dtype=Float32),
        Field(name="worst texture", dtype=Float32),
        Field(name="worst perimeter", dtype=Float32),
        Field(name="worst area", dtype=Float32),
        Field(name="worst smoothness", dtype=Float32),
        Field(name="worst compactness", dtype=Float32),
        Field(name="worst concavity", dtype=Float32),
        Field(name="worst concave points", dtype=Float32),
        Field(name="worst symmetry", dtype=Float32),
        Field(name="worst fractal dimension", dtype=Float32),
    ],
    source=f_source4
)

target_source = FileSource(
    path="data/target_df.parquet",
    timestamp_field="event_timestamp"
)

target_fv = FeatureView(
    name="target_feature_view",
    entities=[patient],
    ttl=timedelta(days=3),
    description="This feature view contains the target variable of the breast cancer dataset",
    schema=[
        Field(name="target", dtype=Int64)
    ],
    source=target_source
)
