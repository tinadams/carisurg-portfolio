# Risk Register: AI-Assisted ED Triage for High-Risk Patient Identification

This risk register identifies the main technical, operational, ethical, and equity risks that could affect safe implementation of an AI tool, along with practical mitigations and measurable signals of success.

## Risk Register

| Risk Name                                     | Category     | Likelihood | Impact | Mitigation                                                                                                                                                                  | Signal-of-Success                                                                                       |
| --------------------------------------------- | ------------ | ---------: | -----: | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| Poor Local Model Performance            | AI-Technical |          M |      H | Test the AI with Caribbean ED data before using it with real patients, including different shifts, cultural seasons, and patient-volume periods.                                    | The AI correctly flags high-risk patients during testing.   |
| AI Misses a High-Risk Patient      | AI-Technical |          M |      H | Test how often the AI fails to flag patients who later need urgent care, admission, ICU review, or escalation. Use the tool only if the missed-case rate stays very low | Missed high-risk cases are reviewed during the pilot and stay within the accepted safety limit.            |
| AI Output Is Hard to Understand by Clinical Staff              | AI-Technical |          M |      H | Make the AI give a short, clear reason for each alert. e.g “high risk because of low blood pressure 70/40 mmHg and high heart rate 145 bpm.”                    | Nurses can clearly understand and communicate the reason for each AI alert.                           |
| Alert Fatigue (Too Many Alerts)                                 | Operational  |          H |      H | Only send alerts for serious cases that need attention. Allow nurses to preset their alert preferences e.g audio/visual alerts.                                              | Nurses set alert preferences and do not experience alert fatigue during the testing period.  |
| Workflow Disruption (Triage Takes Longer)                          | Operational  |          M |      H | The AI flag appears automatically, without requiring extra steps from nurses.                                    | Average triage time does not increase after the tool is introduced. Idealy, triage time decreases.                                     |
| Bed Shortages      | Operational  |          H |      M | Frame the tool as an early-warning and planning system, not to solve bed shortages. Link high-risk flags to earlier communication with the ED team and bed management.     | High-risk flags lead to earlier escalation or planning, even when no bed is immediately available.      |
| Over-Reliance on AI Output (Nurses Trust the AI Too Much)                    | Ethical      |          M |      H | Train staff that the AI is decision support only. Nurses must remain responsible for final triage decisions and can override the AI.                                        | Nurses still use their own judgment and override the AI when needed. Track ovveride rate, sudden drop in rate indicates over-reliance |
| No Clear Person Responsible                  | Ethical      |          M |      H | Decide and define who is responsible for model approval, monitoring, clinical use, and response to harm before deployment.                                                             | A A named clinical lead and technical lead are listed.                    |
| Patient Awareness and Consent (Patients May Not Know AI Is Used)          | Ethical      |          M |      M | Explain that AI may help with triage, but clinicians still make the final decision.                                  | Staff can explain the AI’s role if patients ask.              |
| Unequal Performance Across Patient Groups (AI Works Better for Some Patients)    | Equity       |          M |      H | Test if the AI works differently for different groups of patients, including age, sex, arrival mode, symptom type, triage category, etc.                                                     | FWe can clearly see that the AI performs equally well across patient groups, with no group having more missed cases or false alerts.           |
| Incomplete Records Cause Problems| Equity       |          H |      M | Design the tool to work with basic triage information, even when records are incomplete. Highlight missing fields instead of silently excluding patients.                                                 | Even if some patient information is missing the AI can still give a useful alert for patients during testing.     |
| One Hospital’s Data May Not Fit Another                             | Equity       |          M |      M | Don't assume that one hospital’s data represents all Caribbean EDs. Check that the AI works with the new hospital’s patient data and workflow before using it there.                               | Before the AI is used at another hospital compare its predictions with real patient outcomes from that hospital.                           |

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
