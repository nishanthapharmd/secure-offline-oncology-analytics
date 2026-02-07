import pandas as pd
from onco_loader import load_encrypted_csv
from onco_rules import apply_onco_rules

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report

def run_ml_pipeline(df: pd.DataFrame):
    X = df[
        ["age", "stage", "wbc", "creatinine", "treatment_group"]
    ]
    y = df["anemia_flag"]

    categorical_features = ["stage", "treatment_group"]
    numeric_features = ["age", "wbc", "creatinine"]

    preprocessor = ColumnTransformer(
        transformers=[
            ("cat", OneHotEncoder(drop="first", handle_unknown="ignore"), categorical_features),
            ("num", "passthrough", numeric_features),
        ]
    )

    model = LogisticRegression(max_iter=1000)

    pipeline = Pipeline(
        steps=[
            ("preprocess", preprocessor),
            ("model", model),
        ]
    )

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.4, random_state=42
    )

    pipeline.fit(X_train, y_train)
    y_pred = pipeline.predict(X_test)

    print("\n=== ML Classification Report ===\n")
    print(classification_report(y_test, y_pred))

    return pipeline

if __name__ == "__main__":
    password = "strong_test_password"

    df = load_encrypted_csv(password, "onco_sample.csv.enc")
    df = apply_onco_rules(df)

    run_ml_pipeline(df)
