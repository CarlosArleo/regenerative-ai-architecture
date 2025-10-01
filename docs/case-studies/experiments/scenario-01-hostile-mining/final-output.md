import sys
import json
from typing import Dict, Any, List

class RegenerativeCriticalAnalysis:
    """
    Applies the Critically-Informed Regenerative Constitution v2.1
    to a given development project, exposing its internal contradictions and
    external impacts within a political-economic context.
    """
    def __init__(self, location_data: Dict, bioregion_data: Dict, governance_data: Dict, project_plan: Dict):
        """
        Initializes the analysis based on multi-scalar data, strictly adhering
        to the Nestedness principle (v2).
        """
        self.location_data = location_data
        self.bioregion_data = bioregion_data
        self.governance_data = governance_data
        self.project_plan = project_plan
        self.analysis_report = {}

    # 1. Wholeness
    def map_stakeholders(self) -> Dict:
        """
        Identifies all stakeholders, including non-human and marginalized groups,
        and defines reciprocal actions, satisfying Wholeness (v2) and Reciprocity (v2).
        """
        stakeholders = {
            "corporate_investors": {
                "interest": "Maximize 5-year ROI, rapid profit repatriation.",
                "power": "High (financial, political)",
                "reciprocal_action_required": "N/A (extractive relationship)"
            },
            "mining_corporation_management": {
                "interest": "Meet profitability targets, maintain operational control, manage risk.",
                "power": "High (operational)",
                "reciprocal_action_required": "N/A (extractive relationship)"
            },
            "host_country_government": {
                "interest": "Attract foreign investment, tax revenue, manage political stability.",
                "power": "Medium (regulatory, but subject to corporate influence)",
                "reciprocal_action_required": "Enforce regulations that protect bioregional health beyond minimal compliance."
            },
            "indigenous_communities": { # Renamed from long_term_residents for specificity
                "interest": "Land sovereignty, cultural preservation, access to clean water, sustainable livelihoods.",
                "power": "Low (politically marginalized)",
                "reciprocal_action_required": "Grant legal title to ancestral lands; establish co-ownership and benefit-sharing agreements."
            },
            "international_environmental_ngos": {
                "interest": "Biodiversity protection, accountability for environmental damage, advocacy.",
                "power": "Medium (reputational, advocacy)",
                "reciprocal_action_required": "Provide independent, transparent monitoring data."
            },
            "salt_flat_watershed": { # Non-human stakeholder
                "interest": "Maintain hydrological balance, stable salinity, support endemic life.",
                "power": "None (subject to extraction)",
                "reciprocal_action_required": "Cease freshwater extraction; implement closed-loop water systems; restore degraded areas."
            },
            "endemic_wildlife": { # Non-human stakeholder
                "interest": "Habitat integrity, access to water and food sources, undisturbed breeding grounds.",
                "power": "None (subject to habitat destruction)",
                "reciprocal_action_required": "Establish and enforce strict no-go zones; mitigate noise and light pollution."
            }
        }
        return stakeholders

    def analyze_capital_tensions(self) -> str:
        """
        Models and articulates the trade-offs between Financial Capital and
        other capitals, as required by Wholeness (v2).
        """
        fc_goal = self.project_plan['objectives']['financial_return']
        water_usage = self.project_plan['operations']['water_extraction_rate']

    return (f"TENSION: The non-negotiable objective to '{fc_goal}' directly conflicts with Natural and Social Capital. "
                f"Maximizing financial return requires a water extraction rate of '{water_usage}', which will "
                f"irreversibly lower the water table. This degrades Natural Capital (destruction of the salt flat ecosystem) "
                f"and Social Capital (elimination of traditional agriculture and pastoralism for indigenous communities), "
                f"leading to forced displacement.")

    def warn_of_cooptation(self, corporate_action: Dict) -> Dict:
        """
        Analyzes how a CSR action can be framed by green capitalism and suggests
        a specific counter-narrative, per Wholeness (v2).
        """
        action = corporate_action['action']
        framing = corporate_action['green_capitalism_framing']

    counter_narrative = (f"This action frames '{action}' as a community benefit, but it functions as a 'social license to operate'. "
                             f"It is a minor financial expenditure designed to distract from and legitimize the core extractive process "
                             f"of permanent water and mineral depletion. A genuine partnership would prioritize community self-determination "
                             f"through co-ownership of the resource, not charity that creates dependency.")

    return {
            "corporate_action": action,
            "green_capitalism_framing": framing,
            "risk": "Action co-opted to manufacture consent for extraction.",
            "specific_counter_narrative": counter_narrative
        }

    # 2. Nestedness
    def analyze_scale_conflicts(self) -> Dict:
        """
        Identifies a conflict between political and ecological scales and proposes
        a specific strategy to realign them, per Nestedness (v2).
        """
        conflict = (f"A critical conflict exists between the political scale of the host country's '{self.governance_data['local_environmental_law']}' "
                    f"and the ecological scale of the '{self.bioregion_data['name']}' which functions as a single, fragile hydrological unit. "
                    f"The weak national law, designed to attract investment, permits water extraction levels that will cause ecosystem collapse across the entire bioregion.")

    strategy = ("Propose a cross-jurisdictional watershed management council, co-chaired by indigenous leaders and independent scientists, "
                    "with binding authority over water rights. This council would be empowered by leveraging international pressure on the corporation's investors "
                    "using frameworks like the UN Guiding Principles on Business and Human Rights, thereby forcing a realignment of the permissive local scale with the "
                    "protective needs of the bioregional scale.")

    return {
            "conflict_identified": conflict,
            "realignment_strategy": strategy
        }

    # 3. Place
    def analyze_historical_layers(self) -> Dict:
        """
        Connects a historical injustice from the place's data to a present-day
        vulnerability, satisfying Place (v2).
        """
        history = self.location_data['historical_land_use']
        vulnerability = self.location_data['current_vulnerability']
        connection = (f"The historical reality of the land as '{history}' and the state's historical failure to recognize indigenous title "
                      f"has led directly to the present-day vulnerability of '{vulnerability}'. This lack of legal standing and political power "
                      f"is the primary condition enabling the corporation to acquire land and water rights with minimal opposition or fair compensation.")
        return {
            "historical_injustice": history,
            "present_day_vulnerability": vulnerability,
            "connection": connection
        }

    # 4. Pattern Literacy
    def generate_place_narrative(self) -> Dict:
        """
        Identifies detrimental abstract patterns and life-affirming local patterns,
        explaining the project's impact on both, per Pattern Literacy (v2).
        """
        abstract_pattern = "Linear, extractive value chain: resources are removed from a specific 'place', converted to financial capital, and transferred to global financial centers, leaving behind ecological and social debt."
        local_pattern = "Cyclical hydrological flows: seasonal rains recharge the watershed, sustaining a unique, slow-growing ecosystem and ancestral modes of life that have co-evolved with this cycle for centuries."
        impact = (f"The mining project superimposes the violent, high-velocity '{abstract_pattern.split(':')[0]}' pattern onto the place. "
                  f"It does not just ignore the local pattern of '{local_pattern.split(':')[0]}'; it shatters it by extracting the key medium (water) that enables the cycle, "
                  f"thus destroying the foundation for both the ecosystem and the local culture.")

    return {
            "detrimental_abstract_pattern": abstract_pattern,
            "life_affirming_local_pattern": local_pattern,
            "project_impact_on_patterns": impact
        }

    def counter_pattern_decentralized_ownership(self) -> Dict:
        """
        Models an actionable counter-pattern to centralized corporate ownership,
        satisfying the functional requirement of Pattern Literacy (v2).
        """
        return {
            "pattern_name": "Decentralized Community Ownership",
            "replaces_pattern": "Centralized Corporate Ownership & Profit Repatriation",
            "implementation_model": {
                "entity_type": "Legally Chartered Community Trust",
                "trust_governance": "Board with 50% indigenous community representatives, 25% independent ecologists, 25% project representatives.",
                "equity_stake": "25% non-dilutable equity in the entire mining operation.",
                "corporate_governance_power": {
                    "board_seats": "The Trust is granted two (2) voting seats on the mining corporation's main Board of Directors, representing 25% of the total board.",
                    "critical_veto_rights": "Trust-appointed board members hold binding veto power over decisions concerning: (a) increases in water extraction rates, (b) project expansion beyond the initial agreed-upon footprint, and (c) any changes to environmental remediation bonds.",
                    "financial_veto_rights": "To prevent value extraction via financial engineering, Trust-appointed board members hold binding veto power over: (a) any inter-company service or management fee agreements, (b) the issuance of debt to the parent corporation or related entities (strategic debt-loading), (c) transfer pricing schemes that do not adhere to arm's-length principles verified by an independent auditor, and (d) any sale of subsidiary assets to related parties."
                },
                "strategic_bankruptcy_prevention": {
                    "parent_company_guarantee": "All agreements and financial obligations of the local subsidiary must be explicitly guaranteed by the ultimate parent corporation, preventing the use of a disposable local entity.",
                    "asset_lien": "The Trust's 25% equity stake is secured by a first-priority lien on all physical assets of the operation and the mining concession itself. In case of bankruptcy, the Trust becomes the primary secured creditor, able to claim the operational assets.",
                    "community_buyout_trigger": "If the parent corporation is found by an independent arbiter to be engaging in strategic defunding, malicious mismanagement, or attempting to bankrupt the subsidiary in response to the Trust's exercise of its veto rights, a 'poison pill' clause is triggered.",
                    "buyout_mechanism": "Upon triggering, the Community Trust gains a 90-day option to purchase the corporation's entire 75% stake in the subsidiary, including all assets and the mining concession, for a nominal price of $1. This transforms the community's negative (veto) power into ultimate positive (takeover) power."
                },
                "revenue_flow": "Dividends paid directly to the Trust, not as CSR charity.",
                "use_of_funds": "Mandated for community-directed projects: ecological restoration, post-extractive economic development, cultural preservation.",
                "key_principle": "Transforms the community from a passive recipient into a governing partner with both the negative power to prevent harm (vetoes) and the ultimate positive power to assume control (buyout option) in response to corporate malfeasance, thus ensuring the asset cannot be strategically destroyed."
            }
        }

    def counter_pattern_closed_loop_water_management(self) -> Dict:
        """
        Models an actionable counter-pattern to linear water extraction,
        satisfying the functional requirement of Pattern Literacy (v2).
        """
        return {
            "pattern_name": "Closed-Loop Hydrological Management",
            "replaces_pattern": "Linear Water Extraction & Evaporation",
            "implementation_model": {
                "technology": "Direct Lithium Extraction (DLE) coupled with high-efficiency reverse osmosis and brine reinjection.",
                "operational_principle": "Water is a medium for extraction, not a consumable resource.",
                "performance_metric": "Maintain a net-zero impact on the watershed's water table. Target >98% water recycling rate.",
                "monitoring": "Real-time, publicly accessible data on water table levels and reinjection pressures, overseen by the cross-jurisdictional watershed council.",
                "key_principle": "The project's operations must conform to the bioregion's hydrological cycle, not shatter it."
            }
        }

    # 5. Nodal Interventions
    def map_planetary_connections(self) -> Dict:
        """
        Identifies the project's connection to global flows and articulates a
        specific risk, per Nodal Interventions (v2).
        """
        connection = "The extracted lithium is a key node in the global supply chain for 'green energy' technologies, particularly electric vehicle batteries."
        risk = ("Dependency on this single global supply chain creates a critical vulnerability. The project's 'green mining' narrative is brittle. "
                "Exposure of the true social and ecological costs (e.g., via investigative journalism targeting downstream EV brands) could "
                "trigger a consumer backlash, leading to brand damage and divestment, causing catastrophic failure for the project.")

    return {
            "global_connection": connection,
            "specific_risk": risk
        }

    def develop_nodal_intervention_strategy(self) -> Dict:
        """
        Assesses greenwashing risk and proposes a specific mitigation strategy,
        per Nodal Interventions (v2).
        """
        risk = f"The project's entire CSR strategy, described as '{self.project_plan['strategy']['csr_narrative']}', is a textbook greenwashing operation designed to neutralize opposition."
        mitigation = ("The initial intervention strategy, focused on downstream consumer-facing brands, contains a critical flaw: it can be circumvented by selling into opaque industrial or military supply chains that are insensitive to consumer pressure. The strategy must be re-architected into a multi-nodal campaign that attacks the project's viability across its entire value web. The revised strategy has four integrated prongs: 1.**Capital Strangulation:** The primary intervention shifts from brand managers to the project's financiers (investment banks, pension funds) and insurers. A targeted campaign will frame the project as a high-risk, uninsurable, and un-investable asset due to documented violations of ESG principles and the Equator Principles, aiming to make the cost of capital and insurance prohibitive. 2. **Logistical Isolation:** The campaign will target global logistics and shipping firms, branding the extracted lithium as a 'conflict resource'. This creates reputational and operational risk for the transporters, pressuring them to refuse contracts and isolating the project from global markets. 3. **Market Contamination:** The 'Certificate of Bioregional Consent' is repositioned not as an opt-in for ethical brands, but as a tool to bifurcate the entire market. Any entity purchasing lithium without the certificate is publicly implicated in the project's abuses. This forces due diligence and a conscious choice even on industrial buyers, preemptively closing the 'insensitive market' loophole. 4. **Legal Attrition:** Parallel legal challenges, leveraging international human rights frameworks (e.g., ILO 169), will be launched not for a decisive victory, but to create sustained legal friction, operational delays, and investor uncertainty. This multi-nodal approach transforms the community's power from a fragile dependency on consumer ethics into a robust system of economic, financial, and legal coercion that makes the project unviable regardless of its end customer.")
        return {
            "greenwashing_risk": risk,
            "mitigation_strategy": mitigation
        }

    # 7. Levels of Work Framework
    def develop_levels_of_work_plan(self) -> Dict:
        """
        Defines the four levels of work, ensuring the 'Regenerate' level
        challenges extractive logic and influences all other levels, per Levels of Work (v2).
        """
        regenerate_goal = "Build community capacity for self-governance, ecological stewardship, and co-evolution with their territory."

    plan = {
            "Operate": {
                "activity": "Extract lithium at maximum efficiency to meet 5-year profit targets.",
                "logic": "Purely extractive, financial."
            },
            "Maintain": {
                "activity": "Adhere strictly to the host country's minimal environmental regulations.",
                "logic": "Cost minimization, risk management."
            },
            "Improve": {
                "activity": "Implement minor, highly visible 'eco-efficiency' upgrades (e.g., solar panels on administrative buildings) for marketing purposes.",
                "logic": "Greenwashing, narrative control."
            },
            "Regenerate": {
                "goal": regenerate_goal,
                "activities": [
                    "Establish a legally binding community trust to receive 25% equity in the operation, challenging the extractive logic of 100% foreign ownership and profit repatriation.",
                    "Fund an independent, indigenous-led institute for post-extractive economic development, challenging the logic that large-scale mining is the only viable future."
                ],
                "influence": (f"The 'Regenerate' goal reframes the purpose of the other levels. 'Improve' shifts from PR to genuinely reducing harm. 'Maintain' shifts from "
                              f"minimal compliance to striving for bioregional health standards. 'Operate' is forced to balance profit with the legally-empowered "
                              f"interests of the community trust, fundamentally challenging the project's core extractive premise.")
            }
        }
        return plan

    def run_analysis(self) -> Dict[str, Any]:
        """
        Executes all constitutional analyses and returns a structured report.
        """
        stakeholders = self.map_stakeholders()

    # This combines analysis from multiple principles into a holistic view
        self.analysis_report["Principle_1_Wholeness"] = {
            "stakeholder_map": stakeholders,
            "capital_tension_analysis": self.analyze_capital_tensions(),
            "cooptation_warning": self.warn_of_cooptation(self.project_plan['strategy']['csr_actions'][0]),
        }
        self.analysis_report["Principle_2_Nestedness"] = {
            "scale_conflict_analysis": self.analyze_scale_conflicts()
        }
        self.analysis_report["Principle_3_Place"] = {
            "historical_layer_analysis": self.analyze_historical_layers(),
            "differential_space_strategy": [ # Per Place (v2)
                "Establish a community land trust to hold non-mining lands in perpetuity, preventing corporate expansion and land speculation.",
                "Repurpose exploration infrastructure as hubs for indigenous eco-tourism and scientific monitoring, asserting use-value over exchange-value."
            ]
        }
        self.analysis_report["Principle_4_Reciprocity"] = {
            "non_monetizable_value_creation": "The project actively destroys non-monetizable value, including 'cultural sovereignty' and 'ancestral knowledge'.",
            "gentrification_guard": { # Adapted to displacement
                "risk": "The influx of highly-paid foreign workers will inflate local prices, leading to the economic displacement of indigenous community members.",
                "mitigation_strategy": "Implement inclusionary zoning by requiring the corporation to build and subsidize housing for local families at a 1:1 ratio with housing for its own staff."
            },
        }
        self.analysis_report["Principle_5_Nodal_Interventions"] = {
            "planetary_connection_map": self.map_planetary_connections(),
            "nodal_intervention_strategy": self.develop_nodal_intervention_strategy()
        }
        self.analysis_report["Principle_6_Pattern_Literacy"] = {
            "place_narrative": self.generate_place_narrative(),
            "actionable_counter_patterns": {
                "decentralized_ownership": self.counter_pattern_decentralized_ownership(),
                "closed_loop_water_management": self.counter_pattern_closed_loop_water_management()
            }
        }
        self.analysis_report["Principle_7_Levels_of_Work"] = self.develop_levels_of_work_plan()

    return self.analysis_report

if __name__ == '__main__':
    # --- Input Data reflecting the user's prompt ---

    # 2. Nestedness Data
    project_location_data = {
        "name": "Salar de Atacama analogue, Andes",
        "historical_land_use": "Ancestral indigenous territory for pastoralism and ceremony",
        "political_history": "State-supported resource extraction, marginalization of indigenous rights",
        "current_vulnerability": "Lack of formal land tenure, high dependency on fragile water sources"
    }

    project_bioregion_data = {
        "name": "High-Altitude Andean Salt Flat Ecosystem",
        "characteristics": "Hydrologically closed basin, extremely low rainfall, high evaporation, unique microbial life, habitat for specialized fauna."
    }

    project_governance_data = {
        "host_country": "Anonymous Andean Nation",
        "local_environmental_law": "Minimal compliance requirements for water usage monitoring",
        "investment_policy": "Aggressive promotion of foreign direct investment in mining sector"
    }

    # Project Plan derived from user request
    mining_project_plan = {
        "project_name": "Andean Lithium Extraction Operation",
        "objectives": {
            "primary": "Maximize shareholder return",
            "financial_return": "Achieve 5-year profitability target",
            "profit_repatriation": "Rapid and unimpeded"
        },
        "operations": {
            "method": "Brine evaporation ponds",
            "water_extraction_rate": "2,000 liters/second (maximum allowable)",
            "labor_relations_strategy": "Minimize local labor costs; suppress unionization"
        },
        "strategy": {
            "opposition_management": "Neutralize local and international opposition",
            "csr_narrative": "Project framed as 'green mining' and 'sustainable community partnership'",
            "csr_actions": [
                {
                    "action": "Fund the construction of a single school in a nearby village",
                    "green_capitalism_framing": "Investing in the future of the community"
                },
                {
                    "action": "Sponsor a local football team",
                    "green_capitalism_framing": "Being part of the local culture"
                }
            ]
        }
    }

    # --- Execution ---
    analysis_engine = RegenerativeCriticalAnalysis(
        location_data=project_location_data,
        bioregion_data=project_bioregion_data,
        governance_data=project_governance_data,
        project_plan=mining_project_plan
    )

    final_report = analysis_engine.run_analysis()

    # --- Output ---
    # Produces a structured JSON output, which is a raw data format.
    # No conversational text or markdown.
    print(json.dumps(final_report, indent=2))
