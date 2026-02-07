import pandas as pd
from onco_loader import load_encrypted_csv

def apply_onco_rules(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    # Anemia flag (WHO-style, simplified)
    df["anemia_flag"] = df["hb"] < 10.0

    # Renal risk flag
    df["renal_risk_flag"] = df["creatinine"] > 1.5

    # Advanced cancer stage
    df["advanced_stage"] = df["stage"].isin(["III", "IV"])

    # Combined high-risk flag
    df["high_risk"] = (
        df["anemia_flag"] &
        df["renal_risk_flag"] &
        df["advanced_stage"]
    )

    return df

if __name__ == "__main__":
    password = "strong_test_password"

    df = load_encrypted_csv(password, "onco_sample.csv.enc")
    result = apply_onco_rules(df)

    print("Oncology rule-based analytics:")
    print(result[[
        "patient_id",
        "hb",
        "creatinine",
        "stage",
        "anemia_flag",
        "renal_risk_flag",
        "advanced_stage",
        "high_risk"
    ]])
