# Project Handover

## 1. Project Summary

This project evaluates machine-learning models for predicting Emergency
Severity Index, or ESI, levels using information available at emergency
department triage.

The model uses structured triage information, including vital signs and
chief-complaint indicators. Post-triage information was excluded to reduce
the risk of data leakage.

The purpose of the project is to compare several classification models and
select one model that offers a suitable balance of predictive performance,
interpretability, computational efficiency, and reproducibility.

## 2. Final Model Decision

**Selected model:** Logistic Regression

Logistic Regression was selected as the final Phase 3 model because it achieved
the highest Week 7 macro-F1 score while remaining easier to interpret, maintain,
audit, and deploy than the more complex models tested.

**Week 7 headline results:**

- Accuracy: 0.667
- Macro precision: 0.582
- Macro recall: 0.463
- Macro-F1: 0.492
- Training time: approximately 0.10 minutes

The exact final hyperparameters will be recorded in `config.yaml`.

## 3. How to Run

The intended command for training the final model is:

```bash
python scripts/train.py --config config.yaml
