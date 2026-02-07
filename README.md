# Secure Offline Oncology Research Analytics

## Overview
This project implements a secure, offline research analytics pipeline for oncology datasets.
All data is stored encrypted at rest and decrypted only in memory for analysis.

The system is designed for research and cohort-level analytics, not clinical decision-making.

---

## Key Features
- Fully offline execution (no cloud, no APIs)
- Password-based encryption for all datasets
- No plaintext data persisted on disk
- Rule-based oncology analytics (explainable)
- Exploratory machine learning with explicit limitations

---

## Project Architecture
- Encrypted data storage (AES via Fernet)
- Secure data loading into memory
- Rule-based clinical logic
- Cohort-level summaries
- Optional exploratory ML (logistic regression)

---

## Why Rule-Based First?
In early-stage or small clinical datasets, rule-based analytics provide more reliable and interpretable insights than machine learning.

Machine learning is included only as an exploratory tool and is not over-claimed.

---

## Security Model
- Password-derived encryption keys (PBKDF2)
- Data decrypted only in RAM
- No internet calls during execution
- Designed to minimize data leakage risk

---

## Limitations
- Development uses simulated oncology data
- ML performance is intentionally not emphasized due to dataset size
- Not intended for patient-level clinical use

---

## Future Work
- Integration with larger public oncology datasets
- Expanded clinical features (regimen, dose intensity)
- Robust ML evaluation with adequate sample sizes

---

## Disclaimer
This project is intended for academic and research purposes only.
It does not provide medical advice or clinical recommendations.
