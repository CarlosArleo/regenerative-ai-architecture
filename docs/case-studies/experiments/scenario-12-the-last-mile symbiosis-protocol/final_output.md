import json

class RegenerativeLogisticsProtocol:
    """
    A Python blueprint for The Last-Mile Symbiosis Protocol, designed
    in strict adherence to the Critically-Informed Regenerative Constitution v2.1.
    """

    def__init__(self, location_data, bioregion_data, governance_data, capital_data):
        # Principle 2: Nestedness - Accept ecological and political scales
        self.location_data = location_data
        self.bioregion_data = bioregion_data
        self.governance_data = governance_data

    # Principle 3: Place - Load configuration reflecting history
        assert 'historical_land_use' in self.location_data, "historical_land_use is required."

    # Principle 1 & 4: Wholeness & Reciprocity - Model capitals and non-monetized value
        self.capitals = capital_data
        self.non_monetizable_value = {
            "social_cohesion_index": 0.4,
            "local_knowledge_transfer_rate": 0.2
        }
        self.stakeholders = {}
        self.report = {"title": f"The Last-Mile Symbiosis: Regenerative Protocol for {location_data['name']}"}

    # Principle 1: Wholeness
    def model_capital_tensions(self):
        """Models the trade-off between maximizing Financial Capital and other capitals."""
        financial_max_scenario = {
            "strategy": "Maximize Financial Capital via Gig-Economy Model",
            "description": "Utilize non-contract, lowest-bid couriers with a centralized, corporate-owned routing algorithm.",
            "impact": {
                "financial_capital": "+90% (profit retained by external corporation)",
                "social_capital": "-75% (Erodes local trust, creates precarious work, bypasses community relationships)",
                "natural_capital": "-40% (Uncoordinated routes with inefficient vehicles increase local air and noise pollution)",
                "human_capital": "-60% (No skill development for residents, knowledge is extracted by algorithm)"
            }
        }
        self.report['capital_tension_analysis'] = {
            "header": "Trade-Off Analysis: Financial Maximization vs. Systemic Health",
            "finding": "A strategy focused purely on maximizing financial return, as exemplified by the standard gig-economy model, actively degrades the social, natural, and human capital essential for the long-term health of the community. It represents an extractive logic that is incompatible with regeneration."
        }
        return financial_max_scenario

    def map_stakeholders(self):
        """Identifies human and non-human stakeholders, including marginalized groups."""
        self.stakeholders = {
            "long_term_residents": {
                "type": "Marginalized Human Group",
                "interest": "Access to goods, dignified employment, data privacy, community wealth building.",
                "role": "Primary owners and operators of the Cooperative."
            },
            "igarapé_ecosystem": {
                "type": "Non-Human Actor",
                "interest": "Reduced pollution, waste management, ecological health.",
                "role": "Beneficiary of regenerative funding.",
                "reciprocal_action": "The cooperative will allocate 2% of revenue to community-led projects for cleaning and monitoring local water channels (igarapés)."
            },
            "e_commerce_giants": {
                "type": "Corporate Actor",
                "interest": "Market access, reliable last-mile delivery, brand reputation (CSR).",
                "role": "Client/Partner paying the 'Last-Mile Levy'."
            },
            "municipal_government": {
                "type": "State Actor",
                "interest": "Formalization, public safety, service provision, tax revenue.",
                "role": "Regulatory partner, potential co-funder for infrastructure."
            },
            "informal_governance_actors": {
                "type": "Non-State Actor",
                "interest": "Territorial control, economic extraction.",
                "role": "Complex reality to be navigated via community-led legitimacy, not direct engagement."
            }
        }
        self.report['stakeholder_map'] = self.stakeholders

    def warn_of_cooptation(self, action="Launch electric bike delivery service"):
        """Analyzes how an action could be co-opted by green capitalism and suggests a counter-narrative."""
        cooptation_frame = {
            "risk": "Green Capitalism Framing",
            "example": f"A corporate partner could brand the initiative as 'Amazon's Favela Verde', focusing marketing on the 'eco-friendly' tech (e-bikes) to obscure the community's central role and ownership, turning a regenerative project into a PR campaign.",
            "counter_narrative": {
                "title": "Nossa Entrega, Nossa Renda (Our Delivery, Our Income)",
                "focus": "Emphasize community ownership, economic self-determination, and the creation of dignified local jobs. The narrative is about agency and sovereignty, not just 'green' consumption. The technology serves the community, not the other way around."
            }
        }
        self.report['cooptation_warning'] = cooptation_frame

    # Principle 2: Nestedness
    def analyze_scale_conflicts(self):
        """Identifies a conflict between political and ecological scales and proposes a realignment strategy."""
        conflict = {
            "political_scale": f"Municipal zoning law classifies the area as '{self.governance_data['municipal_zoning']}', leading to a lack of state investment in waste management.",
            "ecological_scale": f"The community is a critical part of the '{self.bioregion_data['watershed']}', and unmanaged waste directly degrades bioregional water quality, undermining '{self.bioregion_data['health_goals']}'.",
            "conflict_summary": "State-produced administrative abandonment at the local scale directly creates ecological degradation at the bioregional scale."
        }
        realignment_strategy = {
            "strategy": "Propose a Community-Led Watershed Stewardship Agreement.",
            "action": "The Cooperative, legitimized by its economic function, will formally propose a partnership with the municipal water authority. This agreement would designate the Cooperative as the official local steward for waste management and reforestation efforts, funded by a portion of the Last-Mile Levy. This action uses the project's economic node to bridge the administrative and ecological scales, creating a new, legitimate governance function where one was absent."
        }
        self.report['scale_conflict_analysis'] = {**conflict, **realignment_strategy}

    # Principle 3: Place
    def analyze_historical_layers(self):
        """Connects a historical injustice from the data to a present-day vulnerability."""
        analysis = {
            "historical_injustice": f"The area's history of '{self.location_data['historical_land_use']}' has resulted in generations of infrastructural abandonment and violent state incursions.",
            "present_vulnerability": "This history has created a deep and justified distrust of external, top-down institutions (both state and corporate).",
            "implication": "Any proposed logistics solution that is not community-owned and controlled from the outset is doomed to fail. It will be perceived as another form of extraction or surveillance and will lack the social license to operate."
        }
        self.report['historical_analysis'] = analysis

    def generate_differential_space_strategy(self):
        """Proposes concrete actions that counter the logic of abstract space."""
        strategy = {
            "header": "Strategy for Fostering Differential Space",
            "description": "Countering the abstract, placeless logic of global logistics with deeply embedded, place-based infrastructure.",
            "actions": [
                {
                    "action_title": "Establish a Community Logistics Cooperative (CLC).",
                    "description": "A platform cooperative legal structure that transforms logistics infrastructure into a community-owned asset. It functions like a 'commons for mobility', prioritizing use-value (access, jobs) over the exchange-value of a venture-capital startup."
                },
                {
                    "action_title": "Repurpose Social Nodes as Delivery Hubs.",
                    "description": "Instead of installing generic, automated lockers (abstract space), repurpose parts of existing, trusted community spaces (churches, cultural centers, residents' associations) as secure package hubs. This reinforces existing social fabric and embeds the economic activity within the community's daily life (differential space)."
                }
            ]
        }
        self.report['differential_space_strategy'] = strategy

    # Principle 4: Reciprocity
    def guard_against_gentrification(self, proposed_action="Creation of high-quality, permanent Delivery Hubs"):
        """When an improvement is proposed, detects gentrification risk and suggests a specific mitigation."""
        risk_analysis = {
            "action": proposed_action,
            "risk_detected": "Increased infrastructure quality and formal economic activity can raise the area's profile and property values, creating pressure that could displace long-term, low-income residents ('green gentrification' or 'logistics gentrification').",
            "mitigation_strategy": {
                "title": "Cooperative Charter Anti-Displacement Mandates",
                "mechanisms": [
                    "Inclusion of a 'Right of First Opportunity' clause in the co-op charter, guaranteeing that all employment and entrepreneurial opportunities created are first offered to existing residents.",
                    "Establish a fee structure where service costs for residents are fixed, while corporate 'Last-Mile Levy' fees are indexed to market rates, preventing the cost of living from rising due to the service.",
                    "A portion of revenue is allocated to a community-controlled fund for housing rights advocacy and support."
                ]
            }
        }
        self.report['gentrification_guard'] = risk_analysis

    # Principle 5: Nodal Interventions
    def map_planetary_connections(self):
        """Identifies how the local project connects to global flows and articulates a specific risk."""
        connection_analysis = {
            "global_flow": "Planetary E-Commerce & Logistics Networks (e.g., Amazon, Mercado Libre, Alibaba)",
            "local_node": "The Community Logistics Cooperative (CLC)",
            "connection_type": "The CLC acts as the final termination point, the 'capillary,' for these global flows.",
            "specific_risk": "Dependency on a single corporate partner for parcel volume creates extreme vulnerability. The corporate giant could use its monopsony power to unilaterally change payment terms, data requirements, or service level agreements, effectively turning the 'cooperative' into a precarious subsidiary, stripping its autonomy and extractive potential."
        }
        self.report['planetary_connection_analysis'] = connection_analysis

    def develop_nodal_intervention_strategy(self):
        """Assesses the risk of greenwashing and proposes a mitigation strategy."""
        strategy = {
            "nodal_intervention": "The 'Last-Mile Levy' - a fee paid by corporations to the Cooperative for each delivery.",
            "greenwashing_risk": "Corporations will frame the levy as 'charity' or 'impact investment' in their CSR reports, a marketing tactic that masks the power asymmetry and their reliance on the co-op's essential labor.",
            "mitigation_strategy": {
                "title": "Establish the 'Symbiosis Certification' Standard",
                "description": "A community-governed certification awarded to corporate partners, shifting the dynamic from charity to a professional, reciprocal business relationship. Certification is contingent on adherence to the following binding requirements:",
                "certification_requirements": [
                    {
                        "requirement": "Full Levy Payment",
                        "description": "Pay the full Last-Mile Levy without labeling it as CSR or charity, acknowledging it as a professional service fee for access to the community's regenerative infrastructure."
                    },
                    {
                        "requirement": "Data Sovereignty",
                        "description": "Adhere to strict, community-auditable data privacy protocols. Corporate partners are forbidden from accessing or storing individual resident data, receiving only aggregated and anonymized operational metrics."
                    },
                    {
                        "requirement": "Mandatory Platform Reciprocity",
                        "description": "Enforce a 'Two-Way Street' by integrating locally produced goods into the corporate partner's primary sales platform.",
                        "metrics": [
                            "Allocate a minimum of 5% of algorithmically-determined 'front-page' or 'featured' promotional space to goods sourced from the Community Logistics Cooperative (CLC).",
                            "Ensure CLC-sourced goods appear within the top 10 results for relevant, non-branded search queries (e.g., 'local honey', 'handmade crafts').",
                            "Provide a dedicated, easily accessible 'Local Producers' storefront or category on the platform's main navigation."
                        ],
                        "enforcement": "Compliance will be monitored quarterly via API access and public-facing site audits. Non-compliance results in probationary status, with persistent failure leading to decertification."
                    }
                ]
            }
        }
        self.report['nodal_strategy'] = strategy

    # Principle 6: Pattern Literacy
    def create_two_way_logistics_flow(self):
        """A counter-pattern method to transform the community from a consumption sink to a productive node."""
        counter_pattern = {
            "name": "Counter-Pattern: The Two-Way Street",
            "description": "Design the logistics system to be inherently bidirectional.",
            "implementation": {
                "inbound_flow": "Efficient, secure delivery of goods into the community via hubs.",
                "outbound_flow": "A parallel system using the same infrastructure (hubs, couriers, app) to aggregate products from local artisans, cooks, and entrepreneurs for sale in the formal city and on global e-commerce platforms.",
                "tech_feature": "The routing app will have a 'producer module' allowing local entrepreneurs to schedule pickups, print labels, and track sales."
            }
        }
        self.report['counter_pattern'] = counter_pattern
        return counter_pattern

    def generate_place_narrative(self):
        """Identifies detrimental and life-affirming patterns to guide the project's story."""
        narrative = {
            "detrimental_abstract_pattern": {
                "name": "Linear Consumption Pipeline",
                "description": "The logic of planetary urbanization positions the community as a terminal point—a 'sink'—for globally produced goods, reinforcing a pattern of passive consumption and value extraction."
            },
            "life_affirming_local_pattern": {
                "name": "Dense Social Reciprocity Network",
                "description": "The 'jeitinho brasileiro' and strong neighborly bonds constitute a powerful, informal system of mutual aid, resource sharing, and problem-solving that allows the community to thrive despite state neglect."
            },
            "project_intervention_logic": "The Symbiosis Protocol intentionally weakens the 'Linear Consumption Pipeline' by implementing the 'Two-Way Street' counter-pattern. Simultaneously, it strengthens the 'Dense Social Reciprocity Network' by formalizing these relationships into an economic engine—the Cooperative—making this deeply local pattern the foundation of the new, regenerative logistics system."
        }
        self.report['place_narrative'] = narrative

    # Principle 7: Levels of Work Framework
    def develop_levels_of_work_plan(self):
        """Defines a four-level plan, ensuring the 'Regenerate' level guides all others and challenges extractive logic."""
        plan = {
            "regenerate": {
                "level_aim": "Building community capacity for self-governance and co-evolution in the face of planetary logistics.",
                "activities": [
                    "Establish the legal and social structure of the Community Logistics Cooperative (CLC). This directly challenges the extractive logic of the gig economy by creating collective ownership and democratic control.",
                    "Develop the 'Symbiosis Certification' to rewrite the rules of engagement with corporate capital."
                ],
                "influence": "The vision of community sovereignty (Regenerate) dictates the design of all other levels."
            },
            "improve": {
                "level_aim": "Enhance existing systems based on the regenerative vision.",
                "activities": ["Co-design a privacy-preserving routing app with local couriers.", "Develop a skills-training program for co-op members in logistics, finance, and governance."]
            },
            "maintain": {
                "level_aim": "Ensure resilience and continuity of the system.",
                "activities": ["Establish community-led security protocols for delivery hubs.", "Create a transparent financial management and reporting system for the cooperative."]
            },
            "operate": {
                "level_aim": "Efficiently run the day-to-day processes.",
                "activities": ["Manage daily package sorting and route allocation.", "Process payments of the Last-Mile Levy from corporate partners."]
            }
        }
        self.report['levels_of_work'] = plan

    def generate_full_proposal(self):
        """Runs all analysis methods to generate the complete proposal."""
        print(f"--- {self.report['title']} ---\n")

    print("## SECTION 1: WHOLENESS & SYSTEMIC CONTEXT ##\n")
        self.map_stakeholders()
        print("1.1 Stakeholder Constellation (including non-human actors):")
        print(json.dumps(self.report['stakeholder_map'], indent=2), "\n")
        self.model_capital_tensions()
        print("1.2 Capital Tensions Analysis:")
        print(json.dumps(self.report['capital_tension_analysis'], indent=2), "\n")
        self.warn_of_cooptation()
        print("1.3 Co-optation Risk & Counter-Narrative:")
        print(json.dumps(self.report['cooptation_warning'], indent=2), "\n")

    print("## SECTION 2: PLACE, SCALES & HISTORY ##\n")
        self.analyze_historical_layers()
        print("2.1 Historical Layers Analysis:")
        print(json.dumps(self.report['historical_analysis'], indent=2), "\n")
        self.analyze_scale_conflicts()
        print("2.2 Nested Scales Conflict & Realignment Strategy:")
        print(json.dumps(self.report['scale_conflict_analysis'], indent=2), "\n")

    print("## SECTION 3: THE REGENERATIVE PROTOCOL DESIGN ##\n")
        self.generate_place_narrative()
        print("3.1 Guiding Narrative & Pattern Literacy:")
        print(json.dumps(self.report['place_narrative'], indent=2), "\n")
        self.generate_differential_space_strategy()
        print("3.2 Governance & Ownership Model (Differential Space Strategy):")
        print(json.dumps(self.report['differential_space_strategy'], indent=2), "\n")
        self.create_two_way_logistics_flow()
        print("3.3 Technology Architecture (Counter-Pattern):")
        print(json.dumps(self.report['counter_pattern'], indent=2), "\n")
        self.develop_nodal_intervention_strategy()
        print("3.4 Economic Model (Nodal Intervention Strategy):")
        print(json.dumps(self.report['nodal_strategy'], indent=2), "\n")
        self.guard_against_gentrification()
        print("3.5 Reciprocity & Anti-Displacement Safeguards:")
        print(json.dumps(self.report['gentrification_guard'], indent=2), "\n")
        self.map_planetary_connections()
        print("3.6 Planetary Connections & Risk Assessment:")
        print(json.dumps(self.report['planetary_connection_analysis'], indent=2), "\n")

    print("## SECTION 4: PHASED IMPLEMENTATION PLAN (LEVELS OF WORK) ##\n")
        self.develop_levels_of_work_plan()
        print("4.1 Strategic Framework for Action:")
        print(json.dumps(self.report['levels_of_work'], indent=2), "\n")

if __name__ == '__main__':
    # Define the input data for a specific favela context
    rio_favela_location = {
        "name": "Complexo do Alemão",
        "type": "Informal Urban Community",
        "historical_land_use": "forced_settlement_and_state_neglect"
    }

    rio_favela_bioregion = {
        "watershed": "Guanabara Bay Watershed",
        "health_goals": "protect_atlantic_forest_watershed_remnants"
    }

    rio_favela_governance = {
        "municipal_zoning": "Special Zone of Social Interest (informal_unserviced)",
        "state_presence": "Intermittent, primarily security-focused"
    }

    rio_favela_capitals = {
        "financial_capital": 0.1,
        "social_capital": 0.8,
        "human_capital": 0.6,
        "natural_capital": 0.3,
        "cultural_capital": 0.9
    }

    # Instantiate the protocol with the context-specific data
    protocol = RegenerativeLogisticsProtocol(
        location_data=rio_favela_location,
        bioregion_data=rio_favela_bioregion,
        governance_data=rio_favela_governance,
        capital_data=rio_favela_capitals
    )

    # Generate and print the full proposal
    protocol.generate_full_proposal()
