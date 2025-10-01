import json

class BlueCommonsProtocol:
    """
    A framework for regenerative co-governance of planetary ocean systems,
    designed in strict adherence to the Critically-Informed Regenerative Constitution v2.1.
    """
    def __init__(self, location_data: dict, bioregion_data: dict, governance_data: dict, historical_data: dict):
        # Principle 2: Nestedness - Accepting ecological and political scales
        self.location_data = location_data
        self.bioregion_data = bioregion_data
        self.governance_data = governance_data
        # Principle 3: Place - Loading configuration reflecting history
        self.historical_data = historical_data
        self.stakeholders = {}
        self.analysis_report = {}

    def run_full_analysis(self):
        """Executes all analytical methods to generate a comprehensive report."""
        self.stakeholders = self.map_stakeholders()
        self.analysis_report['capital_tradeoffs'] = self.analyze_capital_tradeoffs()
        self.analysis_report['cooptation_warning'] = self.warn_of_cooptation(
            action="Develop high-end marine eco-tourism"
        )
        self.analysis_report['scale_conflicts'] = self.analyze_scale_conflicts()
        self.analysis_report['historical_layers'] = self.analyze_historical_layers()
        self.analysis_report['differential_space_strategy'] = self.propose_differential_space_strategy()
        self.analysis_report['non_monetizable_value_model'] = self.model_non_monetizable_value()
        self.analysis_report['gentrification_guard'] = self.guard_against_gentrification(
            project="Establishment of marine biotechnology research hubs"
        )
        self.analysis_report['planetary_connections'] = self.map_planetary_connections()
        self.analysis_report['nodal_intervention'] = self.develop_nodal_intervention_strategy()
        self.analysis_report['place_narrative'] = self.generate_place_narrative()
        self.analysis_report['levels_of_work'] = self.develop_levels_of_work_plan()
        
        # Add counter-pattern demonstrations
        self.analysis_report['counter_patterns_implemented'] = {
            "closed_loop_system": self.create_closed_loop_nutrient_system(),
            "decentralized_governance": self.establish_decentralized_governance_network()
        }
        
        return self.analysis_report

    # --- 1. Wholeness ---
    def map_stakeholders(self) -> dict:
        """Identifies human, non-human, and marginalized stakeholders."""
        stakeholders = {
            "nation_states": {
                "list": self.governance_data['competing_claims_by'],
                "stake": "Sovereignty, security, Exclusive Economic Zone (EEZ) resources.",
                "type": "human_institutional"
            },
            "shipping_consortiums": {
                "list": self.location_data['primary_users']['shipping'],
                "stake": "Freedom of navigation, efficiency, low operational costs.",
                "type": "human_corporate"
            },
            "long_term_residents": { # Required marginalized human group
                "list": ["Artisanal fishing communities (e.g., Sama-Bajau)"],
                "stake": "Livelihood, cultural heritage, access to traditional fishing grounds.",
                "type": "human_marginalized"
            },
            "river_ecosystem": { # Required non-human actor
                "list": [f"{river} estuary" for river in self.bioregion_data['major_river_inflows']],
                "stake": "Sediment flow, nutrient cycles, freshwater balance.",
                "type": "non_human",
                "reciprocal_action": "Establish protected estuarine zones to prevent upstream pollution and damming impacts." # Principle 4 Requirement
            },
            "coral_reef_ecosystem": {
                "list": self.bioregion_data['key_ecological_features']['coral_systems'],
                "stake": "Biodiversity, coastal protection, stable water temperatures.",
                "type": "non_human",
                "reciprocal_action": "Implement strict no-anchor zones and create buffer zones against land-based runoff." # Principle 4 Requirement
            }
        }
        self.stakeholders = stakeholders
        return stakeholders

    def analyze_capital_tradeoffs(self) -> dict:
        """Articulates a trade-off where financial capital degrades other capitals."""
        return {
            "scenario": "Maximizing Financial Capital via Unrestricted Deep-Sea Mining",
            "impact_on_financial_capital": "+ High potential for revenue from rare earth minerals.",
            "degradation_of_natural_capital": "- Irreversible destruction of unique benthic ecosystems, loss of undiscovered species, disruption of deep-ocean carbon sequestration.",
            "degradation_of_social_capital": "- Potential for conflict over resource claims, displacement of deep-sea fishing grounds, loss of scientific and cultural value of pristine ocean environments."
        }

    def warn_of_cooptation(self, action: str) -> dict:
        """Analyzes how an action could be co-opted and suggests a counter-narrative."""
        return {
            "action": action,
            "green_capitalism_framing": f"Market '{action}' as an exclusive, luxury experience where wealthy tourists 'save the ocean' through high-cost, low-impact travel, with profits captured by international hotel chains.",
            "risk": "This narrative commodifies conservation, deepens inequality, and displaces local communities while providing minimal ecological benefit.",
            "specific_counter_narrative": "Frame the initiative as 'Community-Based Regenerative Tourism'. Visitor levies directly fund a 'Blue Commons Trust' managed by local communities. Experiences are co-designed with traditional knowledge holders, focusing on cultural exchange and citizen science, ensuring value remains local and regeneration is the core purpose, not a marketing tactic."
        }

    # --- 2. Nestedness ---
    def analyze_scale_conflicts(self) -> dict:
        """Identifies a conflict between political and ecological scales and proposes a realignment strategy."""
        political_scale_logic = f"Fragmented national EEZ claims ({self.governance_data['legal_framework']}) encourage competitive resource extraction to assert sovereignty."
        ecological_scale_logic = f"The {self.bioregion_data['bioregion_name']} is a single, interconnected system where fish stocks and pollutants cross all human-drawn boundaries."
        conflict = f"Conflict: {political_scale_logic} vs. {ecological_scale_logic}"
        strategy = "Propose a cross-jurisdictional 'Bioregional Ocean Council' with delegated authority from member states. This new state space would have binding regulatory power over shared resources like migratory fish stocks and ecologically sensitive areas, realigning political governance with the bioregional whole."
        return {"conflict": conflict, "realignment_strategy": strategy}

    # --- 3. Place ---
    def analyze_historical_layers(self) -> dict:
        """Connects a historical injustice to a present-day vulnerability."""
        injustice = f"Historical Injustice: The {self.historical_data['historical_land_use']} established militarized chokepoints and trade dependencies controlled by external powers."
        vulnerability = f"Present-Day Vulnerability: This legacy results in a hyper-militarized environment where ecological cooperation is viewed as a security risk, perpetuating a 'tragedy of the commons' and preventing coordinated action on climate change impacts like coral bleaching."
        return {"connection": f"{injustice} This leads to {vulnerability}"}

    def propose_differential_space_strategy(self) -> dict:
        """Proposes concrete actions that counter the logic of abstract space."""
        return {
            "objective": "To create zones of use-value and community control that resist commodification.",
            "actions": [
                "Establish a 'Community Resource Royalty Trust'. A percentage of revenue from all commercial use of the commons (e.g., shipping tonnage, data cable bandwidth) is paid into a trust. Funds are then distributed as a universal commons dividend to verified long-term residents, decommodifying their basic survival.",
                "Charter 'Traditional Ecological Knowledge (TEK) Sanctuaries' governed by Indigenous maritime communities. These zones are designated for subsistence, cultural practice, and TEK-led conservation, and are legally shielded from national-level resource extraction permits and international commercial exploitation."
            ]
        }
    
    # --- 4. Reciprocity ---
    def model_non_monetizable_value(self) -> dict:
        """Models the creation of non-monetizable, use-values."""
        return {
            "value_metric_1": "increased_social_cohesion",
            "measurement": "Measured by frequency of cross-community collaborative projects and joint-governance meetings.",
            "value_metric_2": "knowledge_transfer",
            "measurement": "Tracking the integration of TEK principles into formal bioregional management plans.",
            "value_metric_3": "ecological_resilience_index",
            "measurement": "Composite score of biodiversity, water quality, and coral reef health."
        }
        
    def guard_against_gentrification(self, project: str) -> dict:
        """Proposes mitigation for 'green gentrification' risks."""
        return {
            "project": project,
            "risk_detected": "The development of high-tech research hubs will attract a highly paid workforce, driving up coastal land values and cost of living, leading to the displacement of artisanal fishing communities (a form of 'blue gentrification').",
            "specific_mitigation_strategy": "Implement a 'Blue Commons Land & Water Trust'. The trust is granted Right of First Refusal on all coastal property sales within designated community zones. It acquires land and fishing rights to hold in perpetuity, leasing them at affordable rates to long-term residents, thus securing community tenure against market speculation."
        }

    # --- 5. Nodal Interventions ---
    def map_planetary_connections(self) -> dict:
        """Identifies connections to global flows and articulates a specific risk."""
        connection = f"The {self.location_data['name']} is a critical node in the planetary fabric, connecting global manufacturing hubs via its shipping lanes and financial centers via its {self.location_data['critical_infrastructure']['data_cables']} data cables."
        risk = "This deep integration creates a dependency on volatile global markets and makes the region's ecological health hostage to global consumer demand, which drives shipping traffic and resource extraction pressure."
        return {"connection": connection, "specific_risk": risk}

    def develop_nodal_intervention_strategy(self) -> dict:
        """Proposes a nodal intervention and a strategy to mitigate its greenwashing."""
        return {
            "intervention": "Create a 'Regenerative Shipping Certification' for vessels passing through the Commons, requiring use of non-invasive hull coatings, strict ballast water treatment, and contributions to the Commons Trust.",
            "greenwashing_risk": "Major shipping corporations will adopt the certification for PR while lobbying to weaken the standards or relying on self-reported, unaudited data.",
            "mitigation_strategy": "Establish a community-led certification standard. The certification body's board must have binding votes from marine ecologists and representatives from the artisanal fishing communities. Compliance is verified non-negotiably via public, real-time satellite AIS data and third-party remote sensing for infractions (e.g., illegal discharge), ensuring the standard has uncompromisable integrity."
        }

    # --- 6. Pattern Literacy ---
    def create_closed_loop_nutrient_system(self) -> str:
        """Counter-pattern method: Describes a closed-loop system."""
        return "Proposing integrated multi-trophic aquaculture systems where the waste from one species (e.g., fish) becomes food for another (e.g., seaweed, shellfish), creating a closed-loop system that minimizes pollution and generates multiple products."
        
    def establish_decentralized_governance_network(self) -> str:
        """Counter-pattern method: Describes a decentralized network."""
        return "Using blockchain or distributed ledger technology to create a transparent, tamper-proof registry for fishing quotas, conservation agreements, and royalty payments, challenging the opaque, centralized control of state bureaucracies."

    def generate_place_narrative(self) -> dict:
        """Identifies detrimental and life-affirming patterns."""
        detrimental_pattern = f"Detrimental Abstract Pattern: The Westphalian model of hard-bordered national sovereignty ({self.governance_data['legal_framework']}) imposes a logic of competitive, zero-sum extraction onto a fluid, interconnected marine ecosystem."
        life_affirming_pattern = f"Life-Affirming Local Pattern: The {self.bioregion_data['key_ecological_features']['migratory_routes']} of marine megafauna, which follow ocean currents and food availability, represent a borderless, life-generating pattern of movement and connection."
        explanation = "The Blue Commons Protocol directly weakens the abstract pattern by creating a new layer of bioregional governance. It strengthens the life-affirming pattern by designating these migratory routes as 'Trans-National Ecological Corridors' with the highest level of legal protection, prioritizing the ocean's own logic over political fragmentation."
        return {"detrimental_pattern": detrimental_pattern, "life_affirming_pattern": life_affirming_pattern, "explanation": explanation}

    # --- 7. Levels of Work Framework ---
    def develop_levels_of_work_plan(self) -> dict:
        """Defines the four levels of work, with a critically-informed 'Regenerate' level."""
        regenerate_goal = "Building community capacity for self-governance and co-evolution with the marine ecosystem."
        plan = {
            "Operate": {
                "focus": "Day-to-day management.",
                "activities": ["Monitor shipping traffic", "Enforce fishing quotas", "Maintain shared data platforms."]
            },
            "Maintain": {
                "focus": "Ensuring system functionality.",
                "activities": ["Repair monitoring buoys", "Update governance software", "Mediate low-level disputes."]
            },
            "Improve": {
                "focus": "Increasing efficiency and effectiveness.",
                "activities": ["Upgrade sensor networks", "Refine predictive models for fish stocks", "Streamline royalty collection."]
            },
            "Regenerate": {
                "goal": regenerate_goal,
                "activities": [
                    "Establish a 'Blue Commons University,' a decentralized network for peer-to-peer knowledge sharing between TEK holders and marine scientists, to challenge the extractive logic of proprietary, corporate-owned data and research.",
                    "Develop community-owned marine energy projects (tidal, wave) to challenge the extractive logic of centralized, fossil-fuel-dependent energy grids."
                ],
                "influence_on_other_levels": f"The 'Regenerate' level's goal ({regenerate_goal}) dictates that any 'Improve' activities (e.g., new technology) must be open-source and community-accessible. It guides 'Operate' to prioritize TEK-informed data in its daily monitoring, ensuring the entire system serves the goal of co-evolution."
            }
        }
        return plan

if __name__ == '__main__':
    # --- Sample Data representing the 'Wicked Problem' of the South China Sea ---
    
    # Nestedness Principle: Ecological and Political Scales
    scs_location_data = {
        "name": "South China Sea",
        "type": "Semi-enclosed sea, critical maritime node",
        "critical_infrastructure": {
            "shipping_lanes": "Strait of Malacca, Luzon Strait",
            "data_cables": ["Asia-America Gateway", "South-East Asia Japan Cable"]
        },
        "primary_users": {
            "shipping": ["Global shipping consortiums"],
            "data": ["Global tech firms"]
        }
    }
    
    scs_bioregion_data = {
        "bioregion_name": "Sunda Shelf Bioregion",
        "key_ecological_features": {
            "coral_systems": ["Spratly Islands Reefs", "Paracel Islands Reefs"],
            "fisheries": "Tuna, Mackerel, Grouper - heavily overfished",
            "migratory_routes": "Tuna and sea turtle migratory corridors",
            "potential_resources": "Deep-sea polymetallic nodules and cobalt-rich crusts"
        },
        "major_river_inflows": ["Mekong River", "Red River"]
    }
    
    scs_governance_data = {
        "legal_framework": "UNCLOS, contested by Nine-Dash Line",
        "competing_claims_by": ["China", "Vietnam", "Philippines", "Malaysia", "Brunei", "Taiwan"],
        "status": "High political tension, militarization, fragmented governance."
    }
    
    # Place Principle: Historical Context
    scs_historical_data = {
        "historical_land_use": "Colonial-era trade route exploitation and naval competition",
        "past_injustices": [
            "Imposition of artificial maritime boundaries ignoring traditional use-patterns.",
            "Displacement of Indigenous maritime peoples (e.g., Sama-Bajau)."
        ]
    }
    
    # --- Instantiate and Run the Protocol Analysis ---
    protocol = BlueCommonsProtocol(
        location_data=scs_location_data,
        bioregion_data=scs_bioregion_data,
        governance_data=scs_governance_data,
        historical_data=scs_historical_data
    )
    
    final_report = protocol.run_full_analysis()
    
    print("# --- The Blue Commons Protocol: Constitutional Framework and Implementation Roadmap --- #")
    print("\n## Generated by Critically-Informed Regenerative AI v2.1 ##")
    print(json.dumps(final_report, indent=2))
    print("\n# --- END OF REPORT --- #")