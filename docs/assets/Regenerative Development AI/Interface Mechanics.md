# How the System Actually Works: Interface Mechanics

<artifact identifier="system-mechanics-explained" type="text/markdown" title="Actual System Mechanics - Stage by Stage">
# System Mechanics: What Actually Happens
## The Key Question: Hardcoded vs Generative?

**Short answer: NO, nothing is hardcoded.** Every stage uses AI to generate contextually-specific outputs based on your inputs.

---

## Stage 1: Generate Inquiry Questions

### What You Do:

1. **Fill out a web form** with:

```
   - Project name
   - Location details
   - Current tensions (list)
   - Historical patterns (list)
   - Bioregion name
   - Stakeholder types (select/add)
```

2. **Click "Generate Questions"**

### What Happens Behind the Scenes:

javascript

```javascript
// Your form data is sent to backend
{
project_name:"Carrington Moss",
place_context:{
location_name:"Carrington, Greater Manchester",
current_tensions:["green belt development","peatland destruction"],
historical_patterns:["peatland commons","local food production"],
bioregion:"Greater Manchester Wetlands"
},
stakeholder_types:["long_term_residents","environmental_groups","youth"]
}

// Backend calls Gemini API with this prompt:
`You are a regenerative development practitioner...
Project: ${project_name}
Context: ${place_context}
Generate 15-20 Story of Place questions for each group: ${stakeholder_types}
Requirements: [regenerative framework instructions]`

// AI generates NEW questions specific to YOUR context
```

### What You Get Back:

json

```json
{
"questions":{
"long_term_residents":[
"What was this place like when you first knew it?",
"What did the moss provide for your family?",
// ... 15-20 questions tailored to Carrington Moss elders
],
"youth":[
"What would make you want to stay here?",
"How do you relate to the moss today?",
// ... 15-20 questions tailored to young people in THIS place
]
},
"workshop_protocol":"Suggested 2-hour workshop structure..."
}
```

**NOT A TEMPLATE.** If you input a different place (e.g., Colombian mangrove coast), you get completely different questions appropriate to THAT context.

---

## Stage 2: Process Stakeholder Responses

### What You Do:

**After conducting workshops, you return to the system:**

#### Interface Option A: Structured Form

```
┌─────────────────────────────────────────┐
│ Stage 2: Input Workshop Data            │
├─────────────────────────────────────────┤
│                                         │
│ Stakeholder Group:[Long-term residents] │
│                                         │
│ Key Responses/Quotes:                   │
│ ┌─────────────────────────────────────┐ │
│ │ "The moss was our commons..."       │ │
│ │ "Young folk don't understand..."    │ │
│ │ "It provided for us - fuel, food"   │ │
│ │                                     │ │
│ └─────────────────────────────────────┘ │
│                                         │
│ [Add Another Group]                     │
│                                         │
│ Your Initial Essence Hypothesis:        │
│ ┌─────────────────────────────────────┐ │
│ │ A place where common land holds...  │ │
│ └─────────────────────────────────────┘ │
│                                         │
│ [Synthesize Responses]                  │
└─────────────────────────────────────────┘
```

#### OR Option B: Upload Transcripts

```
┌─────────────────────────────────────────┐
│ Stage 2: Upload Workshop Data          │
├─────────────────────────────────────────┤
│                                         │
│ Upload workshop transcripts:            │
│ [📎 elders_workshop.txt]               │
│ [📎 youth_workshop.txt]                │
│ [📎 environmental_groups.txt]          │
│                                         │
│ Or paste text directly:                 │
│ ┌─────────────────────────────────────┐ │
│ │ [Combined transcript here]          │ │
│ └─────────────────────────────────────┘ │
│                                         │
│ Initial essence hypothesis (optional):  │
│ ┌─────────────────────────────────────┐ │
│ │                                     │ │
│ └─────────────────────────────────────┘ │
│                                         │
│ [Process Data]                          │
└─────────────────────────────────────────┘
```

### What Happens Behind the Scenes:

javascript

```javascript
// Your workshop data is sent to backend
{
project_name:"Carrington Moss",
stakeholder_responses:{
"long_term_residents":[
"The moss was our commons, we all shared it",
"Young folk don't understand what's been lost",
// ... all their responses
],
"youth":[
"We want to stay but there's nothing for us here",
// ... all their responses
]
},
essence_hypothesis:"A place where common land holds community together"
}

// Backend calls Gemini with synthesis prompt:
`You are synthesizing Story of Place responses...

Workshop data from Carrington Moss:
${JSON.stringify(stakeholder_responses)}

Initial essence: ${essence_hypothesis}

Task:
1. Assess health of 8 Essential Processes (0-100% across ecological/economic/social)
2. Refine the place essence based on what you heard
3. Identify priority intervention (which process is most degraded?)
4. Provide confidence level (High/Medium/Low based on data richness)

Use Essential Processes framework:
- Nourishment, Shelter, Resource Generation, Identity/Belonging, etc.

Analyze quotes for patterns, tensions, aspirations...`

// AI GENERATES (not retrieves from template):
```

### What You Get Back:

json

```json
{
"essential_processes_assessment":{
"nourishment":{
"ecological":25,
"economic":30,
"social":35,
"overall":30,
"reasoning":"Elders remember when moss provided peat for fuel and grazing for animals. Youth feel disconnected from land-based sustenance. Economic flows now external."
},
"resource_generation":{
"ecological":15,
"economic":10,
"social":20,
"overall":15,
"reasoning":"PRIORITY PROCESS. Historical peatland economy collapsed. Youth have no pathway to place-based livelihood. Ecological productivity severely degraded."
},
// ... all 8 processes with contextual reasoning
},
  
"refined_essence":"A place where peatland commons call community to collective stewardship—ancestral wisdom seeking new hands to restore reciprocity between people and place",
  
"priority_intervention":"Create paid restoration work that reconnects youth with land through elder mentorship, rebuilding resource generation capacity while healing ecological and social relationships",
  
"confidence_level":"HIGH",
"confidence_reasoning":"Rich qualitative data, clear patterns across generations, strong emotional connection to place, explicit aspirations for future",
  
"next_steps":"Validate this essence with community. If confirmed, proceed to Stage 3 to design specific interventions."
}
```

**KEY POINT:** This is NOT pulling from a database of pre-written assessments. The AI is genuinely analyzing YOUR community's specific responses and generating contextual insights.

### You Then:

1. **Review the assessment**
2. **Present refined essence to community**
3. **Get validation** (or go back for more inquiry if confidence is LOW)
4. **Proceed to Stage 3** once essence is validated

---

## Stage 3: Generate Design Brief

### What You Do:

**After community validates the essence:**

```
┌─────────────────────────────────────────────┐
│ Stage 3: Design Brief Generation            │
├─────────────────────────────────────────────┤
│                                             │
│ Validated Essence (from Stage 2):           │
│ ┌─────────────────────────────────────────┐ │
│ │ [Auto-filled from Stage 2]              │ │
│ │ "A place where peatland commons..."     │ │
│ └─────────────────────────────────────────┘ │
│                                             │
│ Proposed Intervention:                      │
│ ┌─────────────────────────────────────────┐ │
│ │ Community-led peatland restoration with │ │
│ │ paid work for youth, mentored by elders │ │
│ └─────────────────────────────────────────┘ │
│                                             │
│ Stakeholder Commitments:                    │
│                                             │
│ Group:[Long-term residents ▼]               │
│ Commitment:[Share traditional knowledge]    │
│ Capacity:[High ▼]                           │
│ [+ Add Commitment]                          │
│                                             │
│ Group:[Youth ▼]                             │
│ Commitment:[Participate in restoration]     │
│ Capacity:[Medium ▼]                         │
│ [+ Add Commitment]                          │
│                                             │
│ Group:[Environmental groups ▼]              │
│ Commitment:[Technical expertise, funding]   │
│ Capacity:[High ▼]                           │
│ [+ Add Commitment]                          │
│                                             │
│ Essential Processes Data (from Stage 2):    │
│ [Auto-imported]                             │
│                                             │
│ [Generate Design Brief]                     │
└─────────────────────────────────────────────┘
```

### What Happens Behind the Scenes:

javascript

```javascript
// Your data sent to backend
{
validated_essence:"A place where peatland commons call community...",
proposed_intervention:"Community-led peatland restoration...",
stakeholder_commitments:[
{stakeholder:"long_term_residents",commitment:"Share knowledge",capacity:"high"},
{stakeholder:"youth",commitment:"Participate in restoration",capacity:"medium"},
// ...
],
essential_processes:{/* from Stage 2 */}
}

// Backend calls Gemini with design synthesis prompt:
`You are creating a regenerative design brief for Carrington Moss.

Place Essence (validated by community):
"${validated_essence}"

Proposed Intervention:
"${proposed_intervention}"

Available Commitments:
${JSON.stringify(stakeholder_commitments)}

Essential Processes Health:
${JSON.stringify(essential_processes)}

Task:
Generate a comprehensive design brief using Three Spheres framework:

1. DESIGN PRINCIPLES (4-6 principles)
   - Each derived directly from the place essence
   - Actionable guidance for designers
   - Traceable back to community wisdom

2. THREE SPHERES SYNTHESIS
   Economic Sphere:
   - Opportunities aligned with resource generation
   - Risks (e.g., market dependencies, funding capture)
   - Economic flows that strengthen rather than extract
   
   Social Sphere:
   - Opportunities for identity/belonging and meaningful participation
   - Risks (e.g., conflict, exclusion, burnout)
   - Social structures that honor commitments
   
   Ecological Sphere:
   - Opportunities for nourishment and shelter processes
   - Risks (e.g., monoculture, chemical inputs, over-harvest)
   - Ecological restoration aligned with community capacity
   
   SWEET SPOTS: Where all three spheres align

3. NESTED SCALES
   - Site scale (specific restoration parcels)
   - Watershed scale (Greater Manchester Wetlands)
   - Bioregion scale (Mersey Basin)
   - Human settlement scale (how this fits in Greater Manchester)

4. SUCCESS METRICS
   - Ecological indicators (peat depth, biodiversity, carbon storage)
   - Social indicators (youth participation, elder involvement, knowledge transfer)
   - Economic indicators (livelihood pathways, local value creation)
   - Process health tracking (which Essential Processes improving?)

5. DESIGN PHASE WORKSHOP PROTOCOL
   - How to engage community in co-design
   - Activities for translating principles into spatial design
   - Integration with professional design team

Output as structured JSON with rich detail...`

// AI GENERATES contextual design brief
```

### What You Get Back:

json

```json
{
"core_design_principles":[
{
"principle":"Honor the Moss as Teacher",
"description":"Design must learn from the peatland's own patterns of water retention, slow accumulation, and collective nourishment. All interventions ask: What would the moss do?",
"design_guidance":"Water management mimics natural bog hydrology. Paths follow existing microtopography. Planting follows existing vegetation patterns as templates.",
"traceable_to":"Elder quotes about 'the moss provided' + Youth desire to 'know how to protect it'"
},
{
"principle":"Create Pathways from Wisdom to Action",
"description":"Every design element creates opportunities for elders to share knowledge and youth to apply it through meaningful work.",
"design_guidance":"Work stations designed for pairs (mentor + learner). Documentation systems capture traditional ecological knowledge. Paid positions structured as apprenticeships.",
"traceable_to":"Essence phrase 'ancestral wisdom seeking new hands' + Stakeholder commitment to mentorship"
},
// ... 4-6 total, each genuinely derived from YOUR context
],
  
"three_spheres_synthesis":{
"economic":{
"opportunities":[
"Youth employment in restoration work (addressing resource generation degradation)",
"Value-added products from sustainable peatland management",
"Ecotourism/education based on restored commons"
],
"risks":[
"Grant dependency creating fragility",
"Market pressures for unsustainable harvest",
"Gentrification if land values increase"
],
"guidance":"Structure economic flows as commons-based peer production. Ensure youth wages come from diverse sources (grants, tourism, land stewardship contracts). Build in anti-gentrification protections."
},
"social":{
"opportunities":[
"Intergenerational healing and knowledge transfer",
"Community pride in restored commons",
"New identity as 'peatland stewards' for youth"
],
"risks":[
"Elder burnout if extraction of knowledge",
"Youth tokenism if not real decision-making power",
"Conflict over land use priorities"
],
"guidance":"Elder involvement is voluntary and compensated. Youth have veto power over key decisions. Conflict resolution protocol built into governance from start."
},
"ecological":{
"opportunities":[
"Rewetting peatland for carbon storage",
"Biodiversity recovery (rare bog plants, birds)",
"Water quality improvement downstream"
],
"risks":[
"Inappropriate restoration techniques damaging site",
"Climate change effects outpacing restoration",
"Invasive species establishment during transition"
],
"guidance":"Use existing healthy bog patches as reference ecosystems. Adaptive management approach expecting surprises. Monitoring protocol to detect problems early."
},
"sweet_spots":[
"Paid youth restoration work mentored by elders = Economic + Social + Ecological alignment",
"Community monitoring of bog health = Social capacity building + Ecological stewardship + Economic skill development",
"Traditional peat harvesting techniques demonstration = Cultural preservation + Ecological knowledge + Tourism income"
]
},
  
"nested_scales":{
"site":"Specific parcels for rewetting, planting, public access",
"watershed":"Coordination with upstream/downstream landowners for water management",
"bioregion":"Connection to Greater Manchester peatland restoration network",
"settlement":"Model for green infrastructure and youth employment in Greater Manchester"
},
  
"success_metrics":{
"ecological":[
"Water table depth (target: within 10cm of surface)",
"Sphagnum moss cover (target: 60% within 10 years)",
"Indicator bird species presence (curlew, snipe returning)"
],
"social":[
"Number of youth completing restoration apprenticeships",
"Elder satisfaction with knowledge transmission process",
"Community use of restored commons (measured via participatory mapping)"
],
"economic":[
"Number of living-wage restoration jobs created",
"Diversity of revenue streams (not >40% from single source)",
"Percentage of economic value staying local"
],
"process_health":[
"Resource Generation process improvement (target: 15% → 50% by year 5)",
"Identity/Belonging process improvement (track via annual surveys)"
]
},
  
"design_phase_workshop_protocol":"3-session co-design process: (1) Walk the land with elders + designers, (2) Youth sketch ideas based on principles, (3) Community review of draft plans with red/yellow/green sticky dots for concerns/questions/enthusiasm"
}
```

**AGAIN: NOT HARDCODED.** If you had input a Colombian mangrove context, you'd get completely different design principles (e.g.,"Respect the Tide's Rhythm","Build with Storms, Not Against Them") and different Three Spheres analysis specific to mangrove socio-ecology.

---

## Stage 4: Governance Harmonization (VDK)

### What You Do:

```
┌─────────────────────────────────────────────┐
│ Stage 4: Governance Pathways Generation     │
├─────────────────────────────────────────────┤
│                                             │
│ Design Brief (from Stage 3):                │
│ [Auto-imported]                             │
│                                             │
│ Upload Policy Documents:                    │
│ [📎 UK_Planning_Policy.pdf]                │
│ [📎 Greater_Manchester_Dev_Plan.pdf]       │
│ [📎 Community_Land_Trust_Guidelines.pdf]   │
│ [+ Add Document]                            │
│                                             │
│ Select Constitutional Framework:            │
│ [Regenerative Constitution (default) ▼]     │
│                                             │
│ Analysis Focus (optional):                  │
│ ☑ Governance structure                     │
│ ☑ Capture risk assessment                  │
│ ☑ Implementation pathway                   │
│ ☐ Funding mechanisms                        │
│                                             │
│ [Generate Governance Pathways]              │
│ (This will take 5-10 minutes -              │
│  VDK runs multiple iterations)              │
└─────────────────────────────────────────────┘
```

### What Happens Behind the Scenes:

This is the MOST complex stage. The VDK runs multiple iterations:

javascript

```javascript
// Backend process (simplified)
asyncfunctionstage4_governance(designBrief, policyDocs, constitution){
  
const pathways =[];
const rejected =[];
  
// Generate 3 different governance pathways
for(let pathwayNum =1; pathwayNum <=3; pathwayNum++){
  
let iteration =awaitgenerateInitialGovernance(
      designBrief, 
      policyDocs, 
      constitution,
      pathways // Avoid duplicating existing
);
  
// Iterative refinement (up to 5 iterations)
for(let iterNum =1; iterNum <=5; iterNum++){
    
// Critique current iteration
const critique =awaitcritiqueGovernance(
        iteration,
        designBrief,
        policyDocs,
        constitution
);
    
// VDK COHERENCE CHECK
const coherence =awaitvdkCoherenceCheck(
        iteration,
        previousIteration,
        constitution,
        critique
);
    
// Check for extractive drift
if(coherence.trajectory==='EXTRACTIVE_DRIFT'){
        rejected.push({
pathway_attempt: pathwayNum,
iteration_number: iterNum,
reason: coherence.concerns,
language_that_triggered: coherence.extractive_language
});
      
// REVERT and try alternative approach
        iteration =awaitgenerateAlternativeApproach(
          previousIteration,
          coherence.concerns
);
continue;
}
    
// If coherent and high score, we're done
if(coherence.trajectory==='COHERENT'&& coherence.score>0.85){
        pathways.push({
name: iteration.name,
governance_model: iteration.model,
legal_framework: iteration.legal,
pros: iteration.pros,
cons: iteration.cons,
capture_risk: coherence.capture_risk_level,
viability_score: coherence.score,
vdk_trajectory:'COHERENT',
iteration_history:[/* all iterations for transparency */]
});
break;
}
    
// Otherwise, correct and continue
      iteration =awaitcorrectGovernance(iteration, critique);
}
}
  
return{
pathways: pathways,
rejected_pathways: rejected,
metadata:{/* timing, model used, etc */}
};
}
```

**Example VDK Detection:**

javascript

```javascript
// Iteration 2 of Pathway 1 might look like:

{
name:"NGO Partnership Model",
governance:"Community Advisory Board provides input to NGO who owns and manages the land..."
}

// VDK analyzes this and detects:
{
trajectory:"EXTRACTIVE_DRIFT",
score:0.52,
concerns:[
"Language shifted from 'community-led' to 'advisory' (power moved external)",
"Asset ownership: NGO owns, community has 'access' (extractive pattern #3)",
"Decision structure: 'provides input' not 'makes decisions' (tokenism)",
"Matches known failure pattern: NGO capture through 'partnership' rhetoric"
],
extractive_language:["advisory board","provides input","managed by NGO"],
recommendation:"REJECT - Try community ownership model instead"
}

// System automatically reverts and tries alternative:
{
name:"Community Land Trust with Charitable Status",
governance:"Community members are voting members of CLT board. Professional staff hired by and accountable to community board..."
}

// VDK checks this:
{
trajectory:"COHERENT",
score:0.87,
concerns:[],
reasoning:"Community retains decision-making power. Asset ownership by community-controlled entity. Accountability flows correctly."
}

// This pathway is accepted and becomes one of the 3 options presented
```

### What You Get Back:

json

```json
{
"pathways":[
{
"name":"Community Land Trust (Charitable) with Regenerative Stewardship",
"governance_model":{
"legal_structure":"Community Land Trust with UK charitable status",
"decision_making":"Community members are CLT board members (one member one vote). Decisions by 2/3 majority. Elders' Wisdom Council has veto on land use changes.",
"asset_ownership":"CLT owns land in perpetuity with asset lock. Cannot be sold for private gain.",
"accountability":"Annual General Meeting, public accounts, Charity Commission oversight"
},
"legal_framework":"Follows UK Community Land Trust model. Charitable Objects include 'regenerative stewardship of Carrington Moss for community benefit'. Compatible with Greater Manchester planning policy...",
"pros":[
"Community maintains control perpetually",
"Charitable status enables tax benefits and grant access",
"Asset lock prevents gentrification/speculation",
"Proven model with legal precedent in UK"
],
"cons":[
"Charity Commission regulation adds bureaucracy",
"Fundraising burden on community",
"May limit commercial revenue generation"
],
"capture_risk":"LOW",
"capture_risk_analysis":"Strong anti-capture mechanisms: asset lock, community board control, veto powers. Charity Commission oversight prevents private benefit.",
"viability_score":0.89,
"best_for":"Communities with strong local organizing capacity, patient timeframe, willing to navigate charity regulations",
"implementation_steps":[
"Form steering group",
"Draft governing document",
"Register with Charity Commission",
"Secure initial land parcel or lease",
"Begin regenerative stewardship plan"
],
"vdk_trajectory":"COHERENT",
"iteration_history":[
{ iteration:1, score:0.72, issue:"Needed stronger elder voice"},
{ iteration:2, score:0.81, issue:"Clarified asset ownership"},
{ iteration:3, score:0.89, issue:"None - accepted"}
]
},
  
{
"name":"Cooperative + Parish Council Partnership",
"governance_model":{
"legal_structure":"Worker-owned cooperative for restoration work + Service agreement with Parish Council for land management",
"decision_making":"Coop members elect board. Parish Council retains land ownership but delegates management to coop via long-term agreement.",
"asset_ownership":"Split: Land owned by Parish Council (public), infrastructure owned by Coop",
"accountability":"Coop to members + annual report to Parish Council"
},
"legal_framework":"Follows UK Co-operative Society Act. Service agreement under Local Government Act allows Parish Council to delegate. Compatible with Greater Manchester devolution framework...",
"pros":[
"Faster implementation (no land purchase needed)",
"Public ownership aligns with some community values",
"Coop model creates democratic workplace",
"Parish Council provides stability and resources"
],
"cons":[
"Split ownership creates potential conflicts",
"Parish Council political changes could affect agreement",
"Less community control than full CLT ownership"
],
"capture_risk":"MEDIUM",
"capture_risk_analysis":"Parish Council could theoretically terminate agreement. Requires strong contractual protections and community political engagement.",
"viability_score":0.78,
"best_for":"Communities with strong Parish Council relationships, need quick start, okay with shared governance",
"implementation_steps":[
"Negotiate with Parish Council",
"Form worker coop (FCA registration)",
"Draft service agreement with poison pills",
"Secure initial restoration contract",
"Build towards land transfer if possible"
],
"vdk_trajectory":"COHERENT",
"iteration_history":[
{ iteration:1, score:0.68, issue:"Needed protections against political shifts"},
{ iteration:2, score:0.75, issue:"Clarified coop vs council powers"},
{ iteration:3, score:0.78, issue:"None - accepted"}
]
},
  
{
"name":"Community Benefit Society with Social Enterprise",
"governance_model":"...",
// Third alternative pathway
}
],
  
"rejected_pathways":[
{
"pathway_attempt":"NGO Partnership Model (REJECTED)",
"rejection_reason":"EXTRACTIVE_DRIFT detected in iteration 2",
"vdk_analysis":{
"concerns":[
"Language shifted from 'community-led' (iteration 1) to 'advisory role' (iteration 2)",
"Asset ownership moved to NGO with community having 'access rights'",
"Decision structure: community 'provides input' rather than makes decisions",
"Matches known failure pattern: NGO capture disguised as partnership"
],
"extractive_language":["advisory board","provides input","managed by","capacity building required before transfer"],
"score_trajectory":[0.68,0.52, ...],
"why_rejected":"Constitutional principle violated: Community sovereignty compromised. Even with 'good intentions', this structure has failed repeatedly in documented cases."
}
}
],
  
"metadata":{
"constitution_used":"regenerative.md",
"documents_analyzed":3,
"total_iterations_run":11,
"pathways_generated":3,
"pathways_rejected":1,
"processing_time_ms":342000,
"model_used":"gemini-2.5-pro"
}
}
```

### You Then:

1. **Review all 3 pathways** with community
2. **Understand pros/cons** of each
3. **See which were rejected** and why (transparency!)
4. **Choose the pathway** that fits your context best
5. **Use the implementation steps** to move forward

---

## Key Points About "Hardcoded"

### What IS hardcoded:

- **The frameworks** (Essential Processes, Three Spheres, Seven Principles)
- **The process structure** (4 stages in sequence)
- **The VDK logic** (how it detects extractive drift)
- **The form fields** (what inputs are needed)

### What is NOT hardcoded:

- **The questions generated** (unique to your place)
- **The synthesis** (unique to your workshop data)
- **The design principles** (derived from YOUR essence)
- **The governance pathways** (contextually appropriate to YOUR legal/cultural context)

### Why This Matters:

**Template approach** (what we're NOT doing):

```
IF project_type == "peatland" THEN
  design_principle_1 = "Respect water flows"
  design_principle_2 = "Engage youth"
```

**Generative approach** (what we ARE doing):

```
essence = community_validated_essence
historical_patterns = workshop_responses
AI_generates_unique_principles(
  essence,
  historical_patterns,
  place_context,
  regenerative_frameworks
)
```

The AI is genuinely THINKING about your specific situation using regenerative frameworks as a lens, not filling in mad-libs.

---

## Technical Architecture

```
┌─────────────────────────────────────────────────┐
│                 Frontend (React)                 │
│  • Forms for data input                          │
│  • Display results                               │
│  • Download outputs                              │
└────────────────┬────────────────────────────────┘
                 │
                 │ HTTPS Request with JSON
                 ▼
┌─────────────────────────────────────────────────┐
│            Backend (Firebase Functions)          │
│  • Validate input                                │
│  • Call Gemini API with prompt                   │
│  • Parse AI response                             │
│  • Validate output structure                     │
│  • Return JSON to frontend                       │
└────────────────┬────────────────────────────────┘
                 │
                 │ API Call
                 ▼
┌─────────────────────────────────────────────────┐
│         Google Gemini 2.5 Pro API                │
│  • Receives prompt with your context             │
│  • Generates contextual response                 │
│  • Returns text (structured as JSON)             │
└─────────────────────────────────────────────────┘
```

Every stage follows this pattern:

1. You input data (forms/uploads)
2. Backend constructs prompt with your data
3. Gemini generates contextual response
4. Backend validates and returns
5. You review and proceed

---

## Example: What "Generative" Means

**If two practitioners input:**

**Project A: Carrington Moss, UK**

```
Tensions: Green belt development, peatland destruction
Patterns: Commons history, local food production
```

**Project B: Bajo Baudó, Colombia**

```
Tensions: Coastal erosion, youth migration, shrimp farm pressure
Patterns: Mangrove stewardship, Afro-Colombian traditions
```

**Stage 1 will generate COMPLETELY DIFFERENT questions:**

**Carrington (UK):**

* "What was harvested from the moss when you were young?"
* "How did families share use of the common land?"
* "What does 'the green belt' mean to you?"

**Bajo Baudó (Colombia):**

* "How do the tides shape your daily rhythms?"
* "What stories do the elders tell about when the mangroves were healthy?"
* "What would make young people want to stay in the territory?"

**Stage 3 will generate COMPLETELY DIFFERENT design principles:**

**Carrington:**

* "Honor the Moss as Teacher"
* "Create Pathways from Wisdom to Action"

**Bajo Baudó:**

* "Respect the Tide's Rhythm"
* "Let the Mangrove Speak Through Design"

This is NOT template substitution. It's contextual generation.

---

## Does This Clarify?

The system is:

* **Structured** (same process stages for everyone)
* **Framework-grounded** (uses regenerative development concepts)
* **Contextually generative** (outputs unique to your situation)

The AI is essentially a **very smart practitioner** who:

* Knows regenerative development frameworks deeply
* Can synthesize large amounts of qualitative data
* Can generate contextually-appropriate outputs
* Can detect extractive patterns (VDK)

But it's guided by YOU inputting YOUR community's data at each stage.

**Questions?**

* How does the upload process work for transcripts?
* What file formats are accepted?
* Can you edit AI outputs before proceeding?
* How long does each stage take to process?
  `</artifact>`

---

Does this clarify how the system actually works? The key insight is:

**The FRAMEWORKS are fixed (Essential Processes, Three Spheres, Seven Principles).**

**The OUTPUTS are generative (unique questions, synthesis, design principles, governance pathways specific to YOUR context).**

It's like having a regenerative development expert who knows the frameworks deeply but applies them fresh to each unique situation—not someone reading from a script!

What other mechanics questions do you have?
