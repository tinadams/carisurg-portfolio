# Model-Selection Results

This table records the models evaluated during Weeks 6 and 7. Models were
compared using overall predictive performance, macro-averaged metrics,
clinically important class recall, computational cost, interpretability,
and suitability for deployment.

| Selected   | Model                          |  Accuracy | Macro precision | Macro recall |  Macro F1 |  Weighted F1 | ESI 1 recall | ESI 2 recall | Training time | Inference time per prediction |
| ---------- | ------------------------------ | --------: | --------------: | -----------: | --------: | -----------: | -----------: | -----------: | ------------: | ----------------------------: |
|            | Dummy Classifier               |     0.375 |    Not recorded | Not recorded |     0.204 |        0.375 |         0.00 | Not recorded |  Not recorded |                  Not recorded |
|            | Decision Tree                  |     0.547 |    Not recorded | Not recorded |     0.207 |        0.449 |         0.00 | Not recorded |  Not recorded |                  Not recorded |
|            | Week 6 Logistic Regression     |     0.683 |           0.607 |        0.476 |     0.508 |        0.677 |         0.25 |        0.626 |  Not recorded |                  Not recorded |
| **Winner** | **Week 7 Logistic Regression** | **0.667** |       **0.582** |    **0.463** | **0.492** |    **0.665** |     **0.25** |    **0.608** |  **0.10 min** |                **0.00351 ms** |
|            | Tuned Random Forest            |     0.605 |           0.449 |        0.517 |     0.471 | Not recorded | Not recorded | Not recorded |      5.56 min |                    0.05637 ms |
|            | Small Multi-Layer Perceptron   |     0.642 |           0.518 |        0.442 |     0.467 | Not recorded | Not recorded | Not recorded |      4.15 min |                    0.00710 ms |
|            | Gradient Boosting              |     0.556 |           0.423 |        0.559 |     0.432 | Not recorded | Not recorded | Not recorded |      0.21 min |                    0.02107 ms |
|            | Untuned Random Forest          |     0.638 |           0.468 |        0.363 |     0.383 | Not recorded | Not recorded | Not recorded |      1.08 min |                    0.23852 ms |

## Final Decision

The selected Phase 3 model is **Logistic Regression**.

It was selected because it achieved the highest Week 7 macro-F1 score while
also offering the strongest balance of predictive performance,
interpretability, computational efficiency, maintainability, and ease of
deployment.

The Week 7 Logistic Regression achieved a macro-F1 score of 0.492 and trained
in approximately 0.10 minutes. Although Gradient Boosting achieved the highest
macro recall, its macro-F1 and accuracy were lower. The tuned Random Forest
also required substantially more training time without outperforming Logistic
Regression.

See the Week 7 Cost-Benefit Memo for the full decision rationale.
