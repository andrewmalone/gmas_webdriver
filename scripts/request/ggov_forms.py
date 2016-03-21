empty = {
    "name": "",
    "attachments": {
        "minimal": {

        },
        "full": {

        }
    },
    "questions": {
        "minimal": {

        },
        "full": {

        }
    }
}

formlist = {
    "minimal": [
        ("sf424", "minimal")
    ],
    "r01_d_minimal": [
        ("sf424", "minimal"),
        ("rr_other", "minimal"),
        ("performance_site", "minimal"),
        ("key_person", "minimal"),
        ("cover_page_supplement", "minimal"),
        ("research_plan", "minimal")
    ],
    "r01_d_validate": [
        ("sf424", "validate"),
        ("rr_other", "validate"),
        ("performance_site", "validate"),
        ("key_person", "validate"),
        ("cover_page_supplement", "validate"),
        ("research_plan", "validate")
    ]
}

sf424 = {
    "name": "SF424 Research & Related",
    "attachments": {
        "full": {
            "Pre-application": "Preapplication.pdf",
            "SFLLL or other Explanatory Documentation": "SFLLL.pdf",
            "Cover Letter": "Mandatory_Cover_Letter.pdf"
        }
    },
    "questions": {
        "minimal": {
            "sf424_3": 2,
            "sf424_4": 2,
            "sf424_5b": "0",
            "sf424_6": 2
        },
        "full": {
            "sf424_1": "FEDID",
            "sf424_2": "AGENCY",
            "sf424_3": 2,
            "sf424_4": 1,
            "sf424_4a": "other agency",
            "sf424_5b": "0",
            "sf424_6": 1,
            "sf424_6a": "1/1/08"
        }
    }
}

rr_other = {
    "name": "Research & Related Other Project Info",
    "attachments": {
        "minimal": {
            "Project Summary/Abstract": "Project_Summary_Abstract.pdf",
            "Project Narrative": "Project_Narrative.pdf",
        },
        "full": {
            "Project Summary/Abstract": "Project_Summary_Abstract.pdf",
            "Project Narrative": "Project_Narrative.pdf",
            "Bibliography & References Cited": "Bibliography.pdf",
            "Facilities & Other Resources": "Facilities.pdf",
            "Equipment": "Equipment.pdf",
            "Other Attachments": "Other_Attach_1.pdf",
        }
    },
    "questions": {
        "minimal": {
            "rr_other_1": 2,
            "rr_other_2": 2,
            "rr_other_3": 2,
            "rr_other_4": 2,
        },
        "full": {
            "rr_other_1": 1,
            "rr_other_2": 1,
            "rr_other_2a": "environmental explanation",
            "rr_other_2b": 1,
            "rr_other_2c": "environmental exemption explanation",
            "rr_other_3": 1,
            "rr_other_3a": "historic site explanation",
            "rr_other_4": 1,
            "rr_other_4a": "other countries",
            "rr_other_4b": "other country explanation",
        }
    }
}

performance_site = {
    "name": "Performance Site",
    "questions": {
        "minimal": {
            "ps_organization": "Harvard University",
            "ps_duns": "000000000",
            "ps_street1": "12 Oxford Street",
            "ps_city": "Cambridge",
            "ps_state": "Massachusetts",
            "ps_zip": "02138-0000",
            "ps_country": "United States",
            "ps_district": "MA-008",
        },
        "full": {
            "ps_organization": "Harvard University",
            "ps_duns": "000000000",
            "ps_street1": "12 Oxford Street",
            "ps_city": "Cambridge",
            "ps_state": "Massachusetts",
            "ps_zip": "02138-0000",
            "ps_country": "United States",
            "ps_district": "MA-008",
        }
    }
}

key_person = {
    "name": "Research & Related Key Person Expanded",
    "attachments": {
        "minimal": {
            "Biographical Sketch": "Biosketch_PI.pdf"
        },
        "full": {
            "Biographical Sketch": "Biosketch_PI.pdf",
            "Current and Pending Support": "Current_Pending_Support_PI.pdf"
        }
    }
}

cover_page_supplement = {
    "name": "PHS398 Cover Page Supplement",
    "questions": {
        "minimal": {
            "phs_cover_4": 2,
            "phs_cover_5": 2,
            "phs_cover_6": 2,
        },
        "minimal_hs": {
            "phs_cover_1a1": 2
        },
        "full": {
            "phs_cover_1a1": 1,
            "phs_cover_1a2": 1,
            "phs_cover_2a1": 1,
            "phs_cover_2a2": 2,
            "phs_cover_2a3": "scientific justification",
            "phs_cover_cell_line": "1234",
            "phs_cover_4": 1,
            "phs_cover_4a": 1,
            "phs_cover_5": 1,
            "phs_cover_5a_prefix": "Dr.",
            "phs_cover_5a_firstname": "Firstname",
            "phs_cover_5a_middlename": "Middlename",
            "phs_cover_5a_lastname": "Lastname",
            "phs_cover_5a_suffix": "Sr.",
            "phs_cover_6": 1,
            "phs_cover_6a": "former"
        }
    }
}

research_plan = {
    "name": "PHS398 Research Plan",
    "attachments": {
        "minimal": {
            "Research Strategy": "Research_Strategy.pdf",
        },
        "minimal_hs": {
            "Research Strategy": "Research_Strategy.pdf",
            "Specific Aims": "Specific_Aims.pdf",
            "Inclusion of Children": "Inclusion_of_Children.pdf",
            "Inclusion of Women and Minorities": "Inclusion_of_Women_and_Minorities.pdf",
            "Protection of Human Subjects": "Protection_of_Human_Subjects.pdf",
        },
        "full": {
            "Research Strategy": "Research_Strategy.pdf",
            "Introduction to Application": "Introduction_to_Application.pdf",
            "Specific Aims": "Specific_Aims.pdf",
            "Progress Report Publication List": "Progress_Report_Publication_List.pdf",
            "Protection of Human Subjects": "Protection_of_Human_Subjects.pdf",
            "Inclusion of Women and Minorities": "Inclusion_of_Women_and_Minorities.pdf",
            "Appendix": "Appendix_1.pdf",
            "Vertebrate Animals": "Vertebrate_Animals.pdf",
            "Select Agent Research": "Select_Agent_Research.pdf",
            "Multiple PD/PI Leadership Plan": "Multiple_PDPI_Leadership_Plan.pdf",
            "Consortium/Contractual Arrangements": "Consortium_Contractual.pdf",
            "Letters of Support": "Letters_of_Support.pdf",
            "Resource Sharing Plan(s)": "Resource_Sharing_Plan.pdf",
            "Inclusion of Children": "Inclusion_of_Children.pdf",
            "Data Safety Monitoring Plan": "data_safety_monitoring.pdf",
            "Authentication of Key Biological and/or Chemical Resources": "authentication_biological.pdf"
        },
        "validate": {
            "Specific Aims": "Specific_Aims.pdf",
            "Research Strategy": "Research_Strategy.pdf",
        }
    }
}

modular_budget = {
    "name": "PHS398 Modular Budget",
    "attachments": {
        "full": {
            "Personnel Justification": "Personnel_Justification.pdf",
            "Consortium Justification": "Consortium_Justification.pdf",
            "Additional Narrative Justification": "Additional_Narrative_Justification.pdf"
        },
        "validate": {
            "Personnel Justification": "Personnel_Justification.pdf",
        }
    }
}

budget = {
    "name": "Research & Related Budget",
    "attachments": {
        "minimal": {
            "Budget Justification": "Budget_Justification.pdf"
        }
    }
}

assignment_request = {
    "name": "PHS Assignment Request Form",
    "questions": {
        "full": {
            "assign_award1": "NCI",
            "assign_award2": "NEI",
            "assign_award3": "NHLBI",
            "assign_award4": "NHGRI",
            "assign_award5": "NIA",
            "assign_award6": "NIAAA",
            "assign_study1": "ACE",
            "assign_study2": "ACTS",
            "assign_study3": "ADDT",
            "assign_study4": "AICS",
            "assign_study5": "AIP",
            "assign_study6": "AMCB",
            "assign_individuals": "List of individuals",
            "assign_expertise1": "Expertise 1",
            "assign_expertise2": "Expertise 2",
            "assign_expertise3": "Expertise 3",
            "assign_expertise4": "Expertise 4",
            "assign_expertise5": "Expertise 5"
        }
    }
}

inclusion_enrollment = {
    "name": "PHS Inclusion Enrollment Report"
}

sub_budget = {
    "name": "Research & Related Subaward Budget Attachment(s) Form",
    "attachments": {
        "validate": {
            "Subaward Budget": "sub_budget.pdf"
        }
    }
}
