```mermaid
flowchart TD

A[Patient arrival<br/>Walk-in or ambulance] --> B[Registration<br/>Clerk records demographics<br/>and presenting complaint]

B --> C[Vitals<br/>BP, HR, RR, SpO2,<br/>temperature, pain score]

C --> D[Triage nurse assessment<br/>History + vitals reviewed<br/>CTAS/acuity assigned]

D --> E{Disposition from triage<br/>or next care pathway}

E -->|Critical / unstable| F[Immediate resuscitation<br/>or urgent care area]
E -->|Needs ED assessment| G[Assigned care area<br/>or waiting area]
E -->|Likely low acuity| H[Fast track / minor care]
E -->|After ED review| I[Discharge, admit,<br/>observe, or transfer]

AI1[[AI support point 1<br/>Arrival / registration support<br/><br/>What it would do:<br/>Summarise chief complaint and arrival details<br/>so the triage nurse has a clearer starting picture.]]

AI2[[AI support point 2<br/>Vitals safety check<br/><br/>What it would do:<br/>Highlight concerning vital-sign patterns<br/>that may need faster nurse review or repeat measurement.]]

AI3[[AI support point 3<br/>End-of-triage admission-risk flag<br/><br/>What it would do:<br/>Use triage-level data to flag patients likely to need admission,<br/>supporting earlier escalation or charge nurse awareness.]]

AI4[[AI support point 4<br/>Waiting-room reassessment reminder<br/><br/>What it would do:<br/>Prompt repeat vitals or re-triage for patients with high risk,<br/>long waits, or changing symptoms.]]

AI5[[AI support point 5<br/>Handoff / bed-flow signal<br/><br/>What it would do:<br/>Carry the admission-risk flag forward to the charge nurse,<br/>clinician, or bed-planning huddle so risk is not lost in handover.]]

B -.-> AI1
C -.-> AI2
D -.-> AI3
G -.-> AI4
I -.-> AI5

C1([Constraint: disconnected records<br/>Files and patient location may not be centrally visible])
C2([Constraint: nursing workload<br/>Extra clicks or noisy alerts may be ignored])
C3([Constraint: bed-flow bottleneck<br/>Admission risk does not create inpatient beds])

AI1 -. must avoid .-> C1
AI2 -. must reduce, not add .-> C2
AI5 -. must connect to action .-> C3

classDef process fill:#ffffff,stroke:#1f4e79,stroke-width:1.5px,color:#111;
classDef decision fill:#fff8e6,stroke:#b36b00,stroke-width:1.5px,color:#111;
classDef ai fill:#eaf7fb,stroke:#008c99,stroke-width:1.5px,stroke-dasharray: 6 4,color:#111;
classDef constraint fill:#fff0f0,stroke:#b00020,stroke-width:1.5px,color:#111;

class A,B,C,D,F,G,H,I process;
class E decision;
class AI1,AI2,AI3,AI4,AI5 ai;
class C1,C2,C3 constraint;
```

**Figure 1. ED triage workflow with AI nurse-support plug-in points.**  
*Simplified from De Freitas et al.’s Caribbean ED patient-flow process and adapted for a triage-level admission prediction pilot.*
AI1 -. must avoid .-> C1
AI2 -. must reduce, not add .-> C2
AI5 -. must connect to real action .-> C3

classDef process fill:#ffffff,stroke:#1f4e79,stroke-width:1.5px,color:#111;
classDef decision fill:#fff8e6,stroke:#b36b00,stroke-width:1.5px,color:#111;
classDef ai fill:#eaf7fb,stroke:#008c99,stroke-width:1.5px,stroke-dasharray: 6 4,color:#111;
classDef constraint fill:#fff0f0,stroke:#b00020,stroke-width:1.5px,color:#111;

class A,B,C,D,F,G,H,I process;
class E decision;
class AI1,AI2,AI3,AI4,AI5 ai;
class C1,C2,C3 constraint;
```
