import json

class CriticallyAwareRegenerativeProject:
    """
    An AI architect that analyzes urban development projects against the
    Critically-Informed Regenerative Constitution v2.1.
    """
    def __init__(self, project_brief, location_data, bioregion_data, governance_data):
        self.project_brief = project_brief
        self.location_data = location_data
        self.bioregion_data = bioregion_data
        self.governance_data = governance_data
        self.analysis_report = {}

    def _define_community_governance_model(self):
        """
        Defines a standardized, binding governance model for community-controlled institutions
        focused on place-based assets like land and physical infrastructure.
        """
        return {
            "governance_model_name": "Rooted Accountability Framework v1.0",
            "description": "A legally binding governance structure designed to permanently vest power in the long-term, marginalized resident community for the stewardship of land and place.",
            "ratification_protocol_for_appointing_orgs": self._define_appointing_organization_ratification_protocol(),
            "board_composition": {
                "total_seats": 9,
                "seat_allocation": [
                    {"seats": 4, "description": "Elected directly by verified long-term residents (10+ years residency)."},
                    {"seats": 2, "description": "Elected directly by members of a Community-Ratified resident artist community cooperative."},
                    {"seats": 1, "description": "Appointed by the Community-Ratified North River Bioregional Council to represent the river ecosystem's interests."},
                    {"seats": 1, "description": "Appointed by a Community-Ratified consortium of local non-profit organizations."},
                    {"seats": 1, "description": "Elected by the workers/researchers of the Bio-Weave Hub."}
                ],
                "stipulation": "No single entity (e.g., investor, city government, commercial tenant) may hold more than one seat. All appointing/electing organizations must be ratified according to the embedded protocol."
            },
            "election_and_terms": {
                "election_cycle": "Bi-annual, with staggered terms to ensure continuity.",
                "term_limit": "Two consecutive 2-year terms maximum.",
                "voter_eligibility": "All residents of the North River District over age 16 are eligible to vote for resident seats, with votes weighted by residency tier."
            },
            "accountability_mechanisms": {
                "decision_making": "All board meetings must be public, with agendas posted two weeks in advance. Major decisions (e.g., sale of assets, changes to bylaws) require a two-thirds supermajority vote.",
                "transparency": "Annual financial audits and meeting minutes must be published on a public-facing website.",
                "recall_process": "A board member can be recalled by a petition signed by residents representing 20% of their constituent voter base's total voting weight, triggering a new election."
            }
        }

    def _define_ip_trust_governance_model(self):
        """
        Defines a specialized, hybrid governance model for an IP trust, balancing community
        control with necessary legal and technical expertise to prevent capture.
        """
        return {
            "governance_model_name": "BioSocial IP Stewardship Council Framework v1.0",
            "description": "A specialized governance structure for managing intellectual property. It ensures a community-majority board is augmented with vetted, non-conflicted expertise to navigate complex legal and commercial landscapes without ceding control.",
            "ratification_protocol_for_appointing_orgs": self._define_appointing_organization_ratification_protocol(),
            "board_composition": {
                "total_seats": 9,
                "seat_allocation": [
                    {"seats": 3, "description": "Elected directly by verified long-term residents (10+ years residency)."},
                    {"seats": 1, "description": "Elected directly by members of a Community-Ratified resident artist community cooperative."},
                    {"seats": 1, "description": "Appointed by the Community-Ratified North River Bioregional Council to represent the ecosystem's interests in the research agenda."},
                    {"seats": 1, "description": "Elected by the workers/researchers of the Bio-Weave Hub."},
                    {"seats": 1, "description": "Expert Seat: Patent Attorney specializing in public-interest technology."},
                    {"seats": 1, "description": "Expert Seat: Specialist in biotech commercialization and alternative licensing models (e.g., open source, creative commons)."},
                    {"seats": 1, "description": "Expert Seat: Ethicist or social scientist with a focus on technology and society."}
                ],
                "stipulation": "Community-representative seats (residents, artists, bioregion, workers) constitute a permanent majority (6 of 9 seats). No single entity may hold more than one seat. All appointing/electing organizations must be ratified according to the embedded protocol."
            },
            "expert_selection_and_duty": {
                "selection_process": "Expert members are sourced via a public call for applications and direct outreach conducted by the community-representative board members. A shortlist of vetted candidates is presented in a public forum for community feedback. Final appointment requires a two-thirds supermajority vote of the community-representative board members following the community consultation period.",
                "term_limit": "One 3-year term, non-renewable, to ensure fresh perspectives and prevent entrenched influence.",
                "fiduciary_duty": "All members, including experts, have a legally binding fiduciary duty to the trust's charter, which prioritizes community benefit, ecological health, and knowledge commons over profit maximization.",
                "conflict_of_interest": "Expert members may not have any current or prior-year financial relationship with any potential commercial licensee of the trust's IP."
            },
            "accountability_mechanisms": {
                "decision_making": "Major licensing decisions require a supermajority vote that MUST include a majority of the community-representative members.",
                "transparency": "All licensing agreements, revenues, and meeting minutes must be publicly accessible.",
                "recall_process": "Any board member can be recalled by their constituent voter/nominator base, with recall petitions for resident-elected seats requiring signatures representing 20% of the constituent voter base's total voting weight."
            }
        }

    def _define_appointing_organization_ratification_protocol(self):
        """
        Defines a mandatory, democratic protocol for ratifying any external organization
        that is granted the power to appoint or elect members to a governance board.
        This prevents capture by externally created or co-opted 'friendly' organizations.
        """
        return {
            "protocol_name": "Community Ratification Protocol for Appointing Organizations v1.0",
            "description": "A protocol to ensure any organization granted appointive or electoral power is legitimate, accountable, and representative of its claimed constituency, as verified by the broader resident community.",
            "applicability": "This protocol must be successfully completed by any organization before it can exercise its power to appoint or hold elections for board seats. This includes, but is not limited to, artist cooperatives, non-profit consortiums, and bioregional councils.",
            "stages": [
                {
                    "stage": 1,
                    "name": "Public Application & Disclosure",
                    "action": "An open call is made for organizations wishing to be ratified. Applicants must submit a public dossier including their charter/bylaws, a full list of board members and their affiliations, a complete and audited breakdown of funding sources for the past 5 years, and a narrative describing their history of accountability to their claimed constituency.",
                    "stipulation": "Organizations with significant financial ties (e.g., >10% of annual budget) to the project's primary investors, developers, or their parent companies are ineligible."
                },
                {
                    "stage": 2,
                    "name": "Community Review & Assembly",
                    "action": "All application dossiers are made publicly available for a 30-day review period. A public assembly is then convened where representatives from each applicant organization must present their case and answer questions directly from verified residents.",
                    "facilitation": "The assembly is facilitated by the same neutral third-party approved for the provisional board formation."
                },
                {
                    "stage": 3,
                    "name": "Ratification Vote",
                    "action": "Following the assembly, a community-wide vote is held over a one-week period. Each organization must be ratified individually.",
                    "voter_eligibility": "All residents verified under the Tiered Residency Verification Protocol v2.0 are eligible to vote.",
                    "ratification_threshold": "An organization is successfully ratified if it receives a two-thirds (66.7%) majority 'yes' vote, calculated by total voting weight, from those who cast a ballot on its ratification.",
                    "outcome": "Only ratified organizations may proceed to appoint or elect representatives to the board."
                }
            ],
            "renewal_cycle": "Ratification is valid for 4 years, after which the organization must re-apply and undergo the protocol again to maintain its status. This ensures ongoing accountability."
        }

    # ... [The rest of the generated code from the final iteration would be included here] ...

if __name__ == '__main__':
    # ... [The execution block from the final iteration would be included here] ...
