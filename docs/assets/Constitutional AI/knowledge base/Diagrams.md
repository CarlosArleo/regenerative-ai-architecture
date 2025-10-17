# Constitutional AI Framework - Minimalist Diagrams

## Diagram 1: Dialectical Forcing Function (Core Mechanism)

```mermaid
graph TB
    P[Proposed Policy P]
    NL[Natural Law Constraints]
    SL[Social Law Constraints]
    CHECK{P ∈ NL ∩ SL?}
    VIABLE[Constitutional]
    REJECT[Rejected]
    ITERATE[Iterate]
  
    P --> CHECK
    NL -.-> CHECK
    SL -.-> CHECK
    CHECK -->|Yes| VIABLE
    CHECK -->|No| REJECT
    REJECT --> ITERATE
    ITERATE --> P
```

---

## Diagram 2: Domain Constraint Architecture

```mermaid
graph LR
    GOV_NL[Cognitive Limits] --> GOV_RF[Biopolitics]
    GOV_SL[Legitimacy] --> GOV_RF
  
    ECON_NL[Entropy] --> ECON_RF[Ecological Economics]
    ECON_SL[Sustainability] --> ECON_RF
  
    URBAN_NL[Socio-Ecological] --> URBAN_RF[Regenerative Design]
    URBAN_SL[Spatial Justice] --> URBAN_RF
  
    HEALTH_NL[Biological Variability] --> HEALTH_RF[Biophilosophy]
    HEALTH_SL[Autonomy] --> HEALTH_RF
  
    EDU_NL[Neurobiology] --> EDU_RF[Science of Learning]
    EDU_SL[Equity] --> EDU_RF
  
    FOOD_NL[Planetary Boundaries] --> FOOD_RF[Agroecology]
    FOOD_SL[Labor Justice] --> FOOD_RF
  
    ENERGY_NL[Grid Physics] --> ENERGY_RF[Energy Justice]
    ENERGY_SL[Access] --> ENERGY_RF
  
    CRIM_NL[Determinism] --> CRIM_RF[Restorative Justice]
    CRIM_SL[Free Will] --> CRIM_RF
```

---

## Diagram 3: Three Fundamental Dialectical Tensions

```mermaid
graph TB
    subgraph T1[Tension 1]
        T1_NL[Efficiency] 
        T1_SL[Equity]
        T1_RES[Equity Primary<br/>Efficiency Secondary]
    end
  
    subgraph T2[Tension 2]
        T2_NL[Determinism]
        T2_SL[Autonomy]
        T2_RES[Acknowledge Both<br/>Preserve Dignity]
    end
  
    subgraph T3[Tension 3]
        T3_NL[Flow]
        T3_SL[Stock]
        T3_RES[Steady State<br/>Regulated Flow]
    end
  
    T1_NL & T1_SL --> T1_RES
    T2_NL & T2_SL --> T2_RES
    T3_NL & T3_SL --> T3_RES
```

---

## Diagram 4: Optimization Failure Modes

```mermaid
graph TD
    POLICY[Policy Design]
  
    F1[Optimize NL Only]
    F1_R[Technocratic Determinism → Social Alienation]
  
    F2[Optimize SL Only]
    F2_R[Aspirational Idealism → Entropic Decay]
  
    SUCCESS[Balance Both]
    S_R[Viable and Just → Long-term Stability]
  
    POLICY --> F1 --> F1_R
    POLICY --> F2 --> F2_R
    POLICY --> SUCCESS --> S_R
```

---

## Diagram 5: Domain Maturity & Implementation Readiness

```mermaid
graph TB
    START[CAI Implementation]
  
    HIGH[High Maturity<br/>Economic Systems<br/>Urban Planning]
  
    MEDIUM[Medium Maturity<br/>Healthcare<br/>Food Systems<br/>Energy]
  
    LOW[Low Maturity<br/>Governance<br/>Education<br/>Criminal Justice]
  
    START --> HIGH
    HIGH -.-> MEDIUM
    MEDIUM -.-> LOW
```

---

## Diagram 6: Meta-Constitutional Principles

```mermaid
graph TB
    META[Meta-Constitution]
  
    A1[Entropy Constraint<br/>Minimize Exergy Loss]
    A2[Equity Distribution<br/>Restorative Justice]
    A3[Irreversibility Principle<br/>Preserve Capital]
  
    DOMAINS[All 8 Domains]
  
    META --> A1
    META --> A2
    META --> A3
  
    A1 --> DOMAINS
    A2 --> DOMAINS
    A3 --> DOMAINS
```

---

## Diagram 7: Material Basis of Social Justice

```mermaid
graph TD
    UNJUST[Unjust System<br/>Unequal Distribution]
    JUST[Just System<br/>Equitable Distribution]
  
    SHOCK[Natural Law Shock]
  
    BRITTLE[Brittle Response<br/>System Collapse]
    RESILIENT[Resilient Response<br/>Adaptive Capacity]
  
    UNJUST --> SHOCK --> BRITTLE
    JUST --> SHOCK --> RESILIENT
  
    INSIGHT[Social Justice = Physical Precondition for Resilience]
  
    BRITTLE -.-> INSIGHT
    RESILIENT -.-> INSIGHT
```

---

## Diagram 8: Implementation Risks & Safeguards

```mermaid
graph TB
    CAI[Constitutional AI]
  
    R1[Loss of Context]
    R1S[Domain-Specific Firewalls]
  
    R2[Algorithmic Bias]
    R2S[Bias Auditing]
  
    R3[Lack of Interpretability]
    R3S[Mandatory XAI]
  
    SAFE[Safe Implementation]
  
    CAI --> R1 --> R1S
    CAI --> R2 --> R2S
    CAI --> R3 --> R3S
  
    R1S --> SAFE
    R2S --> SAFE
    R3S --> SAFE
```

---

## Diagram 9: Complete System Architecture

```mermaid
graph TB
    INPUT[Policy Input]
  
    NL_LAYER[NL Constraint Layer<br/>Thermodynamics | Ecology | Biology]
    SL_LAYER[SL Constraint Layer<br/>Justice | Legitimacy | Equity]
  
    DFF[Dialectical Forcing Function]
  
    VIABLE[Viable Space]
    JUST[Just Space]
  
    INTERSECTION[NL ∩ SL]
  
    OUTPUT_PASS[Policy Approved]
    OUTPUT_FAIL[Policy Rejected]
  
    INPUT --> NL_LAYER
    INPUT --> SL_LAYER
  
    NL_LAYER --> VIABLE
    SL_LAYER --> JUST
  
    VIABLE --> DFF
    JUST --> DFF
  
    DFF --> INTERSECTION
  
    INTERSECTION -->|Pass| OUTPUT_PASS
    INTERSECTION -->|Fail| OUTPUT_FAIL
    OUTPUT_FAIL -.-> INPUT
```

---

## Diagram 10: Eight Domains Flow

```mermaid
graph LR
    NL[Natural Law]
    SL[Social Law]
  
    GOV[Governance]
    ECON[Economic]
    URBAN[Urban]
    HEALTH[Healthcare]
    EDU[Education]
    FOOD[Food]
    ENERGY[Energy]
    CRIM[Criminal Justice]
  
    RF[Reconciliation Framework]
  
    NL --> GOV & ECON & URBAN & HEALTH & EDU & FOOD & ENERGY & CRIM
    SL --> GOV & ECON & URBAN & HEALTH & EDU & FOOD & ENERGY & CRIM
  
    GOV & ECON & URBAN & HEALTH & EDU & FOOD & ENERGY & CRIM --> RF
```

---

## Diagram 11: Constraint Hierarchy

```mermaid
graph TB
    ROOT[Constitutional AI]
  
    META[Meta-Constitutional Principles]
  
    NL[Natural Law Space]
    SL[Social Law Space]
  
    D1[Governance]
    D2[Economic]
    D3[Urban]
    D4[Healthcare]
    D5[Education]
    D6[Food]
    D7[Energy]
    D8[Criminal Justice]
  
    ROOT --> META
    META --> NL
    META --> SL
  
    NL --> D1 & D2 & D3 & D4 & D5 & D6 & D7 & D8
    SL --> D1 & D2 & D3 & D4 & D5 & D6 & D7 & D8
```

---

## Diagram 12: Policy Evaluation Process (Simplified)

```mermaid
graph LR
    P[Policy P]
    NL_CHECK{NL Valid?}
    SL_CHECK{SL Valid?}
    APPROVED[Approved]
    REJECTED[Rejected]
  
    P --> NL_CHECK
    NL_CHECK -->|Yes| SL_CHECK
    NL_CHECK -->|No| REJECTED
    SL_CHECK -->|Yes| APPROVED
    SL_CHECK -->|No| REJECTED
    REJECTED -.-> P
```

---

## Usage Instructions

These minimalist diagrams use:

- Simple lines and arrows only
- No color coding
- No background fills
- No boxes or borders
- Plain text labels
- Clear hierarchies

They'll render cleanly in any Mermaid viewer with a minimal aesthetic.
