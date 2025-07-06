from feast import FeatureStore
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from joblib import dump


store = FeatureStore(repo_path="breast_cancer/")

training_df = store.get_saved_dataset(name="breast_cancer_dataset").to_df()

labels = training_df['target']
features = training_df.drop(
    labels=['target', 'event_timestamp', "patient_id"],
    axis=1
)

X_train, X_test, y_train, y_test = train_test_split(
    features,
    labels,
    stratify=labels
)

reg = LogisticRegression(solver='liblinear', max_iter=1000)
reg.fit(
    X=X_train[sorted(X_train)],
    y=y_train
)
dump(value=reg, filename="model.joblib")
