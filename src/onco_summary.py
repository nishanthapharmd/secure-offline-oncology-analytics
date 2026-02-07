import pandas as pd
from onco_loader import load_encrypted_csv
from onco_rules import apply_onco_rules

def summarize_onco_data(df: pd.DataFrame):
    summaries = {}

    # Overall anemia prevalence
    summaries["anemia_prevalence"] = (
        df["anemia_flag"].mean() * 100
    )

    # Anemia by stage
    summaries["anemia_by_stage"] = (
        df.groupby("stage")["anemia_flag"]
        .mean()
        .mul(100)
        .round(1)
    )

    # Anemia by treatment group
    summaries["anemia_by_treatment"] = (
        df.groupby("treatment_group")["anemia_flag"]
        .mean()
        .mul(100)
        .round(1)
    )

    # High-risk cohort count
    summaries["high_risk_count"] = df["high_risk"].sum()

    return summaries

if __name__ == "__main__":
    password = "strong_test_password"

    df = load_encrypted_csv(password, "onco_sample.csv.enc")
    df = apply_onco_rules(df)

    summaries = summarize_onco_data(df)

    print("\n=== Oncology Research Summaries ===\n")

    print(f"Overall anemia prevalence: {summaries['anemia_prevalence']:.1f}%\n")

    print("Anemia prevalence by cancer stage (%):")
    print(summaries["anemia_by_stage"], "\n")

    print("Anemia prevalence by treatment group (%):")
    print(summaries["anemia_by_treatment"], "\n")

    print(f"High-risk patient count: {summaries['high_risk_count']}")
