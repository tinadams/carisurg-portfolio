# Risk Register: AI-Assisted ED Triage / Admission-Risk Tool

## Project Context

This project proposes an AI-assisted emergency department triage tool that flags patients who may be at higher risk of admission or clinical deterioration. The tool is intended to support triage nurses, not replace their clinical judgment.

## Risk Register

| Risk Name                                     | Category     | Likelihood | Impact | Mitigation                                                                                                                                                                  | Signal-of-Success                                                                                       |
| --------------------------------------------- | ------------ | ---------: | -----: | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| Distribution Shift in Caribbean ED            | AI-Technical |          M |      H | Validate the model on local or locally similar ED data before live use, including different shifts, seasons, and patient-volume periods.                                    | Model recall and false-negative rate remain within the accepted safety threshold on local pilot data.   |
| Data Leakage from Post-Triage Features        | AI-Technical |          M |      H | Audit all model inputs before training and remove variables only available after triage, such as admission status, length of stay, final disposition, or treatment outcome. | Pre-deployment feature audit confirms that every input is available at the moment of triage.            |
| Poor Explainability of AI Output              | AI-Technical |          M |      H | Use an interpretable model where possible and show a short reason for each alert, such as “high risk because of low blood pressure and high heart rate.”                    | Triage nurses can explain the alert reason in plain language during testing.                            |
| Alert Fatigue                                 | Operational  |          H |      H | Limit alerts to high-risk cases, avoid repeated pop-ups, and review alert thresholds with triage nurses during the pilot.                                                   | Percentage of alerts followed by a clinical action is reviewed weekly and does not steadily decline.    |
| Workflow Disruption                           | Operational  |          M |      H | Embed the AI output into the existing triage workflow as a simple support flag without requiring extra clicks or separate documentation.                                    | Average triage time does not increase after the tool is introduced.                                     |
| Limited Actionability from Bed Shortages      | Operational  |          H |      M | Frame the tool as an early-warning and planning aid, not a solution to bed capacity. Link high-risk flags to earlier communication with the ED team and bed management.     | High-risk flags lead to earlier escalation or planning, even when no bed is immediately available.      |
| Over-Reliance on AI Output                    | Ethical      |          M |      H | Train staff that the AI is decision support only. Nurses must remain responsible for final triage decisions and can override the AI.                                        | Override rate remains within an expected range; sudden drops trigger review for possible over-reliance. |
| Unclear Accountability Chain                  | Ethical      |          M |      H | Define who is responsible for model approval, monitoring, clinical use, and response to harm before deployment.                                                             | Governance document names the clinical lead, technical lead, and escalation pathway.                    |
| Patient Awareness and Consent Gap             | Ethical      |          M |      M | Provide clear hospital-level communication that AI may support triage decisions and explain that clinicians remain responsible for care.                                    | Patient-facing information is available and staff can explain the role of the AI if asked.              |
| Unequal Performance Across Patient Groups     | Equity       |          M |      H | Test model performance across available subgroups, including age, sex, arrival mode, symptom type, and triage category.                                                     | False-negative and false-positive rates are reviewed by subgroup before and during pilot use.           |
| Exclusion of Patients with Incomplete Records | Equity       |          H |      M | Design the tool to work with routinely available triage fields and flag missingness instead of silently excluding patients.                                                 | Percentage of patients receiving a usable prediction is tracked across shifts and patient groups.       |
| Single-Site Bias                              | Equity       |          M |      M | Avoid assuming that one hospital’s data represents all Caribbean EDs. Use external validation before applying the tool to another site.                                     | Performance at any new site is checked against local outcomes before rollout.                           |

## Risk Memo: Top 3 Risks

### 1. Distribution Shift in Caribbean ED

The biggest risk is that the model may perform differently in a Caribbean emergency department than it did in the setting where it was trained. In simple terms, the model may not fully understand the local patient population, staffing patterns, documentation habits, seasonal surges, or bed constraints.

This matters because triage is high-stakes. If the model misses a high-risk patient, that patient may wait too long before reassessment. The mitigation is to test the model on local or locally similar ED data before live use. The signal of success is that the model continues to catch high-risk patients at an acceptable rate during the pilot.

### 2. Alert Fatigue

The second major risk is alert fatigue. If the system sends too many warnings, triage nurses may start ignoring them, including alerts that are actually important. This could make the ED less safe instead of safer.

The mitigation is to keep alerts limited, clear, and actionable. The tool should only flag cases where early attention could realistically change the next step in care. The signal of success is that alerts continue to lead to real clinical actions, such as reassessment, escalation, or earlier communication with the ED team.

### 3. Unequal Performance Across Patient Groups

The third major risk is that the AI may work better for some patients than others. For example, it may perform differently based on age, sex, arrival mode, symptom type, or whether the patient has a complete record.

This matters because an AI tool could unintentionally widen existing health inequalities. The mitigation is to test performance across patient groups before and during the pilot. The signal of success is that false-negative and false-positive rates are reviewed by subgroup, and any major gap is corrected before wider rollout.
