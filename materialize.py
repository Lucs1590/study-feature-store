from feast import FeatureStore
from datetime import datetime, timedelta

store = FeatureStore(repo_path="breast_cancer/")
store.materialize_incremental(end_date=datetime.now())
