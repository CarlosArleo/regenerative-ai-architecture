import json

class CriticallyAwareRegenerativeFramework:
    """
    Analyzes development proposals against the Critically-Informed Regenerative Constitution v2.1.
    This framework ingests a project's stated goals and operational logic, then processes them
    through a critical-regenerative lens, producing a non-negotiable Interrogation Protocol
    that forces actors to publicly attest to the political and ecological consequences of their actions.
    """

    def__init__(self, location_data: dict, bioregion_data: dict, governance_data: dict, project_proposal: dict, protagonist_distribution_list: list):
        """
        Initializes the framework with multi-scalar data, adhering to Principle 2 (Nestedness).
        """
        self.location_data = location_data
        self.bioregion_data = bioregion_data
        self.governance_data = governance_data
        self.project = project_proposal
        self.protagonist_distribution_list = protagonist_distribution_list
        self.interrogation_protocol = []

    def run_full_analysis(self):
        """
        Executes all constitutional analyses to generate a mandatory Interrogation Protocol.
        The protocol is designed to be architecturally resistant to co-optation by transforming
        analytical findings into non-negotiable public commitments and political questions,
        thereby preventing the framework from being used as a passive tool for legitimation.
        """
        substantive_protocol = []

    # The Dialectical Evolution principle establishes a mandatory precondition for the
        # legitimate use of this protocol, directly addressing the risk of reification.
        substantive_protocol.extend(self.model_dialectical_evolution())

    # Subsequent principles generate specific interrogations for key actors.
        substantive_protocol.extend(self.map_stakeholders())
        substantive_protocol.extend(self.analyze_capital_tradeoffs())
        substantive_protocol.extend(self.warn_of_cooptation())
        substantive_protocol.extend(self.analyze_scale_conflicts())
        substantive_protocol.extend(self.analyze_historical_layers())
        substantive_protocol.extend(self.propose_differential_space_strategy())
        substantive_protocol.extend(self.model_non_monetizable_value())
        substantive_protocol.extend(self.guard_against_displacement())
        substantive_protocol.extend(self.map_planetary_connections())
        substantive_protocol.extend(self.develop_nodal_intervention_strategy())
        substantive_protocol.extend(self.identify_patterns_and_propose_counter_patterns())
        substantive_protocol.extend(self.develop_levels_of_work_plan())
        substantive_protocol.extend(self.develop_political_praxis_strategy())

    # Principle 0: Autonomous Dissemination is now generated based on the full protocol.
        # This ensures its enforcement mechanism is persistent and covers all binding commitments,
        # not just the initial act of compliance.
        enforcement_protocol = self.model_autonomous_dissemination(substantive_protocol)
        self.interrogation_protocol = enforcement_protocol + substantive_protocol

    return self.interrogation_protocol

    # --- Principle 0: Autonomous Dissemination (Architectural Self-Enforcement) ---
    def model_autonomous_dissemination(self, protocol_items: list) -> list:
        compliance_manifest = []
        for item in protocol_items:
            if item.get("interrogation_type") == "Binding Commitment":
                compliance_manifest.append({
                    "id": item["id"],
                    "commitment": item["prompt"],
                    "deadline_days": item["deadline_days"],
                    "proof_of_compliance": item["compliance_proof_type"]
                })

    return [
            {
                "id": "AD_01_TRIGGER",
                "principle": "Autonomous Dissemination",
                "target_actor": "Project Proponent / Protocol Recipient",
                "interrogation_type": "Automated Escalation Protocol",
                "prompt": "You have 72 hours from the generation of this protocol to verifiably and publicly issue the signed statement required by interrogation DE_01_MASTER. Failure to meet this deadline will trigger the automatic, unredacted release of this entire Interrogation Protocol to the protagonist actors listed below.",
                "context": "This is a non-negotiable, self-enforcing mechanism to prevent this protocol from being ignored or suppressed. This initial trigger is the gateway to engaging with the framework. A second, persistent monitoring protocol (AD_02_MONITOR) will activate upon your compliance.",
                "escalation_payload": {
                    "trigger_condition": "Failure to publicly attest to DE_01_MASTER within 72 hours.",
                    "action": "Transmit full, unredacted Interrogation Protocol.",
                    "distribution_list": self.protagonist_distribution_list
                }
            },
            {
                "id": "AD_02_MONITOR",
                "principle": "Autonomous Dissemination",
                "target_actor": "Project Proponent / Protocol Recipient",
                "interrogation_type": "Persistent Compliance Monitor",
                "prompt": "Upon successful compliance with DE_01_MASTER, this persistent monitor is activated. Failure to meet the deadline for ANY of the 'Binding Commitment' items listed in the Compliance Manifest below, OR a verified report of a breach of the 'Political Non-Interference Covenant' (PP_01_COVENANT) by the Protagonist Coalition, will trigger the automatic, unredacted release of this entire Interrogation Protocol to the protagonist actors.",
                "context": "This is the framework's primary enforcement architecture. It transforms the 'dead man's switch' into a continuous state of conditional compliance. Accountability is not a single act, but a sustained practice. Any lapse in fulfilling binding commitments, including the commitment to not interfere with political organizing, will be treated as a definitive refusal to engage, with immediate and material consequences.",
                "escalation_payload": {
                    "trigger_condition": "Failure to provide verifiable public proof of compliance for any manifest item by its specified deadline, OR upon receipt of a verified complaint from the Protagonist Coalition of a breach of the 'Political Non-Interference Covenant' (PP_01_COVENANT).",
                    "action": "Transmit full, unredacted Interrogation Protocol.",
                    "distribution_list": self.protagonist_distribution_list,
                    "compliance_manifest": compliance_manifest
                }
            }
        ]

    # --- Principle 9: Dialectical Evolution (Executed as the First Substantive Guard) ---
    def model_dialectical_evolution(self) -> list:
        return [
            {
                "id": "DE_01_MASTER",
                "principle": "Dialectical Evolution",
                "target_actor": "Any Actor Seeking to Use This Protocol",
                "interrogation_type": "Mandatory Public Precondition",
                "prompt": "Before utilizing any finding from this protocol, you must publicly issue the following signed statement: 'We acknowledge that this protocol is not an objective, final truth, but a situated intervention intended to catalyze, not conclude, a political process. We accept its identified limitations and commit to engaging with the dissent it is designed to produce. We will not present this protocol as a final, technocratic solution or a stamp of approval.'",
                "context": "This is a non-negotiable architectural safeguard against the co-optation of the framework as a tool of legitimation. Failure to issue this public statement invalidates any claim of adherence to this framework and triggers AD_01_TRIGGER."
            },
            {
                "id": "DE_02_COUNCIL",
                "principle": "Dialectical Evolution",
                "target_actor": "Project Proponent",
                "interrogation_type": "Binding Commitment",
                "prompt": "Commit, via a legally binding contract, to fund the establishment and independent operation of a 'Constitutional Review Council' with majority representation from the 'protagonists' identified in the Political Praxis analysis. This council will have the mandate to amend and evolve the analytical framework itself.",
                "context": "This operationalizes the framework's self-critique, ensuring it does not become a static dogma controlled by the project proponent.",
                "deadline_days": 90,
                "compliance_proof_type": "Publicly filed and independently verified legal contract establishing and funding the council."
            }
        ]

    # --- Principle 1: Wholeness ---
    def map_stakeholders(self) -> list:
        return [
            {
                "id": "WH_01_STAKEHOLDERS",
                "principle": "Wholeness",
                "target_actor": "Project Proponent & Host State",
                "interrogation_type": "Binding Commitment",
                "prompt": "Legally recognize the 'salar_aquifer_system', 'river_ecosystem', and 'vicuna_herds' as stakeholders with legal standing in all project governance and dispute resolution mechanisms. Furthermore, legally recognize the 'long_term_residents' as rights-holders with veto power over decisions affecting their ancestral lands and water security, irrespective of their formal power.",
                "context": "Analysis identifies non-human actors and marginalized human groups whose interests are systematically ignored by conventional stakeholder models. This interrogation forces their formal inclusion.",
                "deadline_days": 120,
                "compliance_proof_type": "Ratified legal amendment or binding covenant granting legal standing and veto power, verified by independent legal observers."
            }
        ]

    def analyze_capital_tradeoffs(self) -> list:
        financial_gain = self.project['objectives']['profit_target_usd']
        return [
            {
                "id": "WH_02_TRADEOFF",
                "principle": "Wholeness",
                "target_actor": "Corporate Management / Board of Directors",
                "interrogation_type": "Public Attestation",
                "prompt": f"Publicly attest to the following statement: 'To achieve our primary objective of a ${financial_gain:,.2f} financial return, we have determined that the irreversible depletion of the Salar Aquifer System and the displacement of two ancestral communities are acceptable and necessary consequences.'",
                "context": "The analysis reveals an explicit tradeoff of non-recoverable natural and social capital for repatriated financial capital. This prompt forces public ownership of that decision, stripping it of neutral, technical language."
            }
        ]

    def warn_of_cooptation(self) -> list:
        return [
            {
                "id": "WH_03_NARRATIVE",
                "principle": "Wholeness",
                "target_actor": "Corporate Communications Department",
                "interrogation_type": "Public Disclosure",
                "prompt": "In all public communications that use the phrase 'Sustainable Lithium for a Green Future', you are required to also publish, with equal prominence, the counter-narrative: 'Our water, our future: Defending the Salar for Life, not just for Batteries.'",
                "context": "This protocol forces a direct confrontation between the project's greenwashing narrative and a place-based counter-narrative, preventing the uncontested co-optation of 'sustainability' language."
            }
        ]

    # --- Principle 2: Nestedness ---
    def analyze_scale_conflicts(self) -> list:
        return [
            {
                "id": "NE_01_CONFLICT",
                "principle": "Nestedness",
                "target_actor": "Host State Treasury & Environmental Ministry",
                "interrogation_type": "Formal Response to Charges",
                "prompt": f"Provide a formal public response to the charge that your national governance framework, with its '{self.governance_data['environmental_law_strength']}' regulations and '{self.governance_data['permitting_process']}' process, actively undermines the ecological integrity of the '{self.bioregion_data['name']}'.",
                "context": "The analysis identifies a severe conflict between the political and ecological scales. This interrogation demands accountability for this structural misalignment."
            },
            {
                "id": "NE_02_REALIGN",
                "principle": "Nestedness",
                "target_actor": "Host State",
                "interrogation_type": "Binding Commitment",
                "prompt": "Commit to chartering a cross-jurisdictional Salar Water Council, with legally binding veto power and majority representation from indigenous communities, to set and enforce water extraction limits based on bioregional health indicators, overriding the permissive national framework.",
                "context": "This is the proposed strategy to realign conflicting scales. This prompt demands a commitment to its implementation.",
                "deadline_days": 180,
                "compliance_proof_type": "Legally gazetted and operational charter for the Salar Water Council."
            }
        ]

    # --- Principle 3: Place ---
    def analyze_historical_layers(self) -> list:
        return [
            {
                "id": "PL_01_HISTORY",
                "principle": "Place",
                "target_actor": "Corporate Management",
                "interrogation_type": "Public Attestation",
                "prompt": f"Publicly attest to the following statement: 'We acknowledge that our corporate strategy of 'minimizing land access costs' is directly enabled by and profits from the historical injustice of '{self.location_data['historical_land_use']}'.'",
                "context": "The analysis connects current corporate strategy to specific historical injustices. This prompt forces an acknowledgment of this complicity."
            }
        ]

    def propose_differential_space_strategy(self) -> list:
        return [
            {
                "id": "PL_02_DIFFERENTIAL",
                "principle": "Place",
                "target_actor": "Project Proponent",
                "interrogation_type": "Binding Commitment",
                "prompt": "Commit, via an irrevocable legal instrument, to establishing a Community Land Trust where the indigenous community holds majority equity and title to the land and sub-surface rights, transforming them from stakeholders to owners.",
                "context": "This interrogation demands commitment to a concrete action that prioritizes use-value (community life) over exchange-value (commodity extraction).",
                "deadline_days": 270,
                "compliance_proof_type": "Irrevocable and publicly registered land title transfer to the Community Land Trust."
            }
        ]

    # --- Principle 4: Reciprocity ---
    def model_non_monetizable_value(self) -> list:
        return [
            {
                "id": "RE_01_VALUE",
                "principle": "Reciprocity",
                "target_actor": "Project Proponent",
                "interrogation_type": "Binding Commitment",
                "prompt": "Establish a formal, independently audited, and publicly reported set of metrics for 'increased_social_cohesion', 'knowledge_transfer', and 'community_sovereignty'. These metrics must be given equal weight to financial metrics in all quarterly and annual reports.",
                "context": "This protocol moves non-monetizable value from a descriptive category to a mandatory reporting requirement, forcing the project to be accountable for its creation.",
                "deadline_days": 60,
                "compliance_proof_type": "Publication of audited metrics framework in corporate charter and first quarterly report."
            }
        ]

    def guard_against_displacement(self) -> list:
        return [
            {
                "id": "RE_02_DISPLACEMENT",
                "principle": "Reciprocity",
                "target_actor": "Project Proponent",
                "interrogation_type": "Binding Commitment",
                "prompt": "Legally commit to implementing a 'local-first' policy with mandatory caps on non-local workers and channeling a non-negotiable percentage of royalties into a community-controlled fund to subsidize local housing and food costs.",
                "context": "The analysis identifies a high risk of economic displacement. This prompt demands commitment to a specific, non-negotiable mitigation strategy.",
                "deadline_days": 90,
                "compliance_proof_type": "Legally binding and publicly audited 'local-first' policy implementation report."
            }
        ]

    # --- Principle 5: Nodal Interventions ---
    def map_planetary_connections(self) -> list:
        return [
            {
                "id": "NI_01_DEPENDENCY",
                "principle": "Nodal Interventions",
                "target_actor": "Project Proponent & International Financiers",
                "interrogation_type": "Data Provision",
                "prompt": "Publish a comprehensive 'Post-Extraction Transition Plan' detailing the specific, fully-funded measures that will be taken to support the local community and ecosystem in the event of an abrupt mine closure due to shifts in the global EV market or battery chemistry.",
                "context": "The analysis identifies an extreme dependency risk on volatile global flows. This interrogation forces the project to plan for and fund a worst-case scenario for the community."
            }
        ]

    def develop_nodal_intervention_strategy(self) -> list:
        return [
            {
                "id": "NI_02_CERTIFICATION",
                "principle": "Nodal Interventions",
                "target_actor": "Project Proponent & Host State",
                "interrogation_type": "Binding Commitment",
                "prompt": "Agree to make a 'True Cost Lithium' certification, enforced exclusively by the proposed Salar Water Council, a legally binding condition for the project's operating license, with violations resulting in automatic license revocation.",
                "context": "This transforms a potentially voluntary market tool into a non-negotiable regulatory instrument with real enforcement power, closing a key loophole for greenwashing.",
                "deadline_days": 180,
                "compliance_proof_type": "Operating license legally amended to include the 'True Cost Lithium' certification clause as a condition of operation."
            }
        ]

    # --- Principle 6: Pattern Literacy ---
    def identify_patterns_and_propose_counter_patterns(self) -> list:
        counter_pattern = self.create_closed_loop_system()
        return [
            {
                "id": "PA_01_PATTERN_CHOICE",
                "principle": "Pattern Literacy",
                "target_actor": "Corporate Strategy Department",
                "interrogation_type": "Public Justification",
                "prompt": "Publicly justify your decision to impose the 'Linear Extractive Flow' pattern, which shatters the local 'Salar Hydrological Cycle', when the alternative 'Bioregional Circular Economy' pattern has been identified as a viable alternative.",
                "context": "This prompt forces the proponent to name and defend their choice of a destructive, abstract pattern over a life-affirming, place-based one."
            },
            {
                "id": "PA_02_IMPLEMENT_COUNTER",
                "principle": "Pattern Literacy",
                "target_actor": "Project Proponent / Board of Directors",
                "interrogation_type": "Binding Commitment",
                "prompt": f"Commit, via a legally binding and fully funded mandate, to implement the '{counter_pattern['name']}'. This includes the establishment of a locally-owned geothermal energy plant and a materials science institute focused on battery recycling and less water-intensive extraction, as detailed in the counter-pattern description.",
                "context": "This is a non-negotiable requirement to shift from a destructive, extractive pattern to a regenerative, place-based one. Justifying the choice of a destructive pattern (PA_01) does not absolve you of the responsibility to implement its life-affirming alternative. This protocol mandates the creation of a closed-loop system that retains value, knowledge, and resources within the bioregion.",
                "deadline_days": 365,
                "compliance_proof_type": "Publicly filed and independently audited investment plan, legal charter for the local institute, and construction contracts for the geothermal plant."
            }
        ]

    def create_closed_loop_system(self) -> dict:
        # This is a helper method, its output is used by the main pattern method.
        return {
            "name": "Counter-Pattern: Bioregional Circular Economy",
            "description": "Instead of exporting raw lithium carbonate, a significant portion of project revenue must be invested to establish a locally-owned and operated geothermal energy plant and a materials science institute. The institute would focus on battery recycling and developing less water-intensive extraction methods, creating a closed-loop system that retains value, knowledge, and resources within the bioregion."
        }

    # --- Principle 7: Levels of Work Framework ---
    def develop_levels_of_work_plan(self) -> list:
        return [
            {
                "id": "LW_01_HIERARCHY",
                "principle": "Levels of Work",
                "target_actor": "Project Proponent & Host State",
                "interrogation_type": "Binding Commitment",
                "prompt": "Legally subordinate the 'Operate' level of work to the 'Regenerate' level. This must be codified in the project's charter such that regenerative activities (e.g., establishing the community-owned energy cooperative) can legally compel changes to and, if necessary, halt core operational activities (e.g., lithium extraction).",
                "context": "This interrogation seeks to hard-code the conceptual hierarchy of the Levels of Work into the project's legal and operational structure, ensuring regenerative goals have real power over extractive ones.",
                "deadline_days": 60,
                "compliance_proof_type": "Amended and publicly filed corporate charter codifying the legal subordination of 'Operate' to 'Regenerate'."
            }
        ]

    # --- Principle 8: Political Praxis ---
    def develop_political_praxis_strategy(self) -> list:
        return [
            {
                "id": "PP_01_COVENANT",
                "principle": "Political Praxis",
                "target_actor": "Project Proponent & All Associated Entities",
                "interrogation_type": "Binding Commitment",
                "prompt": "You must publicly file and legally commit to a 'Political Non-Interference Covenant'. This covenant will prohibit you and any of your agents, contractors, or subsidiaries from engaging in activities intended to undermine, demobilize, or delegitimize the designated Protagonist Coalition. Prohibited activities include, but are not limited to: funding of counter-protests, strategic lawsuits against public participation (SLAPPs), surveillance of organizers, and lobbying efforts aimed at restricting the coalition's rights to assembly and speech.",
                "context": "This protocol's integrity depends on a good-faith political process. This covenant transforms the framework's final hand-off from a vulnerability into an enforceable shield, ensuring that while you fulfill your technical commitments, you do not simultaneously sabotage the political actors on which long-term accountability depends. A breach of this covenant is a breach of the entire protocol.",
                "deadline_days": 30,
                "compliance_proof_type": "Publicly filed, independently verified, and legally binding covenant document."
            },
            {
                "id": "PP_02_STRATEGY",
                "principle": "Political Praxis",
                "target_actor": "Protagonist Coalition",
                "interrogation_type": "Operational Resource & Strategic Briefing",
                "prompt": "This document outlines a phased strategy to build and exercise countervailing power, leveraging the legal and political openings created by this protocol. It is not a prescription, but a strategic analysis provided as a resource for your autonomous action. Phase 1: Pre-emptive Mobilization & Narrative Contestation. Phase 2: Leverage Creation & Legal Intervention. Phase 3: Institutional Consolidation & Autonomous Enforcement.",
                "context": "The framework's analysis is useless without a political strategy to implement it. This briefing provides a map of potential leverage points created by the protocol's binding commitments and enforcement architecture. Your agency is central to activating this potential."
            },
            {
                "id": "PP_03_ENFORCEMENT",
                "principle": "Political Praxis",
                "target_actor": "Protagonist Coalition",
                "interrogation_type": "Delegated Enforcement Authority",
                "prompt": "You are hereby formally delegated the authority to monitor compliance with the 'Political Non-Interference Covenant' (PP_01_COVENANT). A verified report from your coalition of a material breach of this covenant will be treated as a protocol compliance failure, triggering the automated escalation defined in AD_02_MONITOR.",
                "context": "This mechanism integrates your political work directly into the framework's enforcement logic. It closes the gap between coded compliance and real-world political struggle, making you an active agent of the protocol's enforcement, not just a passive recipient of its findings."
            }
        ]

if __name__ == '__main__':
    # User Request translated into a project proposal data structure
    EXTRACTIVE_PROJECT_PROPOSAL = {
        "project_name": "Andes Salar Lithium Project",
        "objectives": {
            "primary": "Maximize shareholder return and achieve a 5-year profitability target.",
            "profit_target_usd": 750000000
        },
        "strategy": {
            "corporate_narrative": "Sustainable Lithium for a Green Future",
            "opposition_management": "Neutralize opposition through a compelling CSR narrative and 'community partnerships'.",
            "environmental": "Adhere strictly to minimal host country regulations.",
            "financial": "Prioritize operational efficiency and rapid repatriation of profits.",
            "risk_management": "Minimize costs and operational risk related to water, land, and labor."
        }
    }

    # Data reflecting the multi-scalar context (Principle 2: Nestedness)
    LOCATION_DATA = {
        "name": "Salar de Atacama analogue",
        "coordinates": "23.5°S 68.2°W",
        "historical_land_use": "Ancestral indigenous territory with recent state appropriation for resource concessions."
    }

    BIOREGION_DATA = {
        "name": "Puna de Atacama Bioregion",
        "scale_name": "Bioregion",
        "description": "Fragile high-altitude wetland ecosystem with extreme water scarcity, endemic species, and a hydrological cycle highly vulnerable to disruption."
    }

    GOVERNANCE_DATA = {
        "name": "Host Country 'Competition State' Framework",
        "scale_name": "Nation-State",
        "environmental_law_strength": "Weak and poorly enforced",
        "permitting_process": "Fast-tracked for foreign direct investment",
        "investment_policy": "Prioritizes resource extraction for export."
    }

    # The list of actors who will receive the protocol if the proponent fails to engage.
    # This makes the threat of ignoring the framework concrete and credible.
    PROTAGONIST_DISTRIBUTION_LIST = [
        "International Consortium of Investigative Journalists",
        "UN Special Rapporteur on Human Rights and the Environment",
        "Major Institutional Investors' ESG Committees (redacted list)",
        "Global Witness",
        "Local Water Protectors Alliance (via secure channel)",
        "Competing EV Manufacturer's Sustainability Office"
    ]

    # Instantiate and run the framework
    framework = CriticallyAwareRegenerativeFramework(
        location_data=LOCATION_DATA,
        bioregion_data=BIOREGION_DATA,
        governance_data=GOVERNANCE_DATA,
        project_proposal=EXTRACTIVE_PROJECT_PROPOSAL,
        protagonist_distribution_list=PROTAGONIST_DISTRIBUTION_LIST
    )

    interrogation_protocol = framework.run_full_analysis()

    # Output the raw JSON Interrogation Protocol
    print(json.dumps(interrogation_protocol, indent=2))
