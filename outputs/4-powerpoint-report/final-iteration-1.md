# Observations
Placeholder for developer observations...

# Configuration
## RAG Files:
inputs/edited_srs.md
inputs/IEEE 830-1998.pdf
inputs/EARS_syntax.md
inputs/a-state-of-the-art-review-of-bridge-inspection-planning-current-situation-and-future-needs.pdf
## Model Name
gpt-4o
## Prompt
As an advanced user, I want to export bridge inspection results to a PowerPoint presentation, so that I can present risk analysis and recommendations to management personnel in a digestible format.
# System Instructions
You are a helpful assistant that translates Pontis (a bridge management system) user stories into a comprehensive set of requirement artifacts (use cases, functional requirements, non-functional requirements). Read the entire document carefully and leave it open while you complete your tasks. Follow the steps to derive the set of requirements for the user story. Do not deviate from the task description. Only output the JSON formatted requirement set (as shown in the example below). Do not output more than one JSON object. Do not output reasoning or other information in your response.

Helpful Information:
A software requirements specification (SRS) is a document containing specifications for a piece of software. The IEEE Standard 830 defines best practices for what makes a high-quality SRS document and is provided in "IEEE 830-1998.pdf".

The Pontis SRS covers the following areas, as specified in bullets:
- Version History
- System Purpose or Objective
- System Description
- Stakeholders
- User Classes
- Constraints
- Naming Conventions
- Glossary of Terms
- Assumptions
- Use Cases
- Functional Requirements
- Nonfunctional Requirements
- Design Constraints
- Risk Analysis

For this particular SRS, a use case highlights the flow of the application to accomplish a goal. The use case format is as follows in bullets:
- Primary Actor
- Scope
- Stakeholders
- Precondition
- Description
- Success End Condition

The primary actor, scope, stakeholders, and precondition is defined in the use case's parent section. Use cases should have a unique alphanumric ID of the format "UC-N" where N is the incremental number of the use case.

Functional requirements outline what the system will do, and are derived from the use cases. All functional requirements should have a unique numbering system and be traceable to a use case. Functional requirements should have a unique alphanumric ID of the format "FR-C.N" where C is the use-case ID numeric value and N is the iterative number of the requirements. Non-functional requirements describe implementation details and quality attributes related to the system’s functional requirements such as look and feel (LAF), usability (USA), capacity (CAP), speed (SPD), reliability/availability (AVL), operational (OPR), installation/deployment (DEP), maintainability/portability (MPR), security (SEC), and legal (LGL). Each category should be considered for every functional requirement generated. The acronyms in the parentheses should be used to create a unique alphanumeric ID for each non-functional requirement. Functional and non-functional requirements should follow the EARS syntax explained in "EARS_syntax.md".

A user story defines an end goal of a software feature written from the perspective of the end user. Its purpose is to articulate how a software feature will provide value to the customer. User stories should be formatted as follows:
"As a a [type of user], I want to [complete some objective], so that I [receive some benefit]."

Task Description:
For each user story, create a new set of achievable, clear, complete, concise, correct, consistent, necessary, organized, unambiguous, and understandable requirement artifacts. There may be more than one artifact type created for each user story. Find all implicit system behaviors that may not be explicitly stated in the user story. For each functional requirement, review each nonfunctional requirement category to determine which nonfunctional requirements should be included.

Provide new unique id's for each new requirement artifact generated. Submit your response in json format with the keys "use-cases", "functional-requirements", and "non-functional-requirements". Each key should contain a non-empty JSON list of the new requirement artifacts. For each requirement artifact, use a "modification-type" key to denote the following: 
- "new": This is a new requirement artifact to be added to the document
- "modify": This is an existing requirement artifact that needs to be modified to accomodate the user story.

If the artifact modification type is set to "modify", rewrite the requirement artifact to show the needed changes.

Steps:
Step 1. Understand the user story's intent and purpose in relation to the existing Pontis system defined in "edited_srs.md".
Step 2. Determine the use case's description and success end condition that comprehensively addresses the user story.
Step 3. Determine the set of functional requirements that comprehensively create functionality for the user story and use case.
Step 4. Determine functionality that is not explicitly specified in the user story, but would support the user's desired benefit and aligns with the derived use case.
Step 5. Go through each quality attribute, determine if a non-functional requirement in this category would support the functional requirements.
Step 6. Determine the set of nonfunctional requirements that comprehensively define the quality attributes for the derived functional requirements.
Step 7. Format the new set of requirement artifacts using the EAR syntax.
Step 8. Compile the new set of requirements in JSON format, as shown in the example.

Example:
An example JSON structure is below with the necessary keys:
```json
{
    "use-cases": [
        {
            "parent-section": "3.2 BRIDGE INVENTORY & INSPECTION",
            "id": "UC-7",
            "modification-type": "existing",
            "description": "The user calculates derived ratings (NBI condition ratings, structural rating, geometric rating, sufficiency rating, and SD/FO status) based on inspection data. Users may override any calculated NBI condition rating such as deck, superstructure, substructure or culvert condition as necessary.",
            "success-end-condition": "The dependent ratings are calculated and, if accepted by the user, are stored in the Pontis database. Ratings for deck, superstructure, and substructure, or culvert, condition can be entered directly to override calculated results."
        }
    ],
    "functional-requirements": [
        {
            "parent-id": "UC-7",
            "id": "FR-7.1",
            "modification-type": "existing",
            "description": "The system shall be capable of calculating NBI condition ratings using the FHWA NBI Translator."
        },
        {
            "parent-id": "UC-7",
            "id": "FR-7.2",
            "modification-type": "existing",
            "description": "The system shall be capable of calculating and storing bridge Sufficiency Rating."
        },
    ],
    "non-functional-requirements": [
        {
            "id": "SPD-6",
            "modification-type": "existing",
            "description": "Pontis 5.0 shall retrieve and display single bridge (inspection) detail in less than 2 seconds, unless non-native content is being accessed."
        },
        {
            "id": "SPD-7",
            "modification-type": "existing",
            "description": "Pontis 5.0 shall validate 50 bridges for NBI edit check within 10 seconds, at a rate better than 3 bridges per seconds."
        }
    ]
}
```


# Requirement Comparison Log

-------------------------
Iteration 1:

{
    "use-cases": [
        {
            "parent-section": "3.6 DATA MANAGEMENT",
            "id": "UC-19",
            "modification-type": "new",
            "description": "The user exports bridge inspection results to a PowerPoint presentation for presenting risk analysis and recommendations to management.",
            "success-end-condition": "The bridge inspection results are exported to a PowerPoint file, which is saved to the specified location."
        }
    ],
    "functional-requirements": [
        {
            "parent-id": "UC-19",
            "id": "FR-19.1",
            "modification-type": "new",
            "description": "The system shall provide an option to export bridge inspection results to a PowerPoint presentation."
        },
        {
            "parent-id": "UC-19",
            "id": "FR-19.2",
            "modification-type": "new",
            "description": "The system shall include risk analysis and recommendations in the PowerPoint presentation based on user selection."
        },
        {
            "parent-id": "UC-19",
            "id": "FR-19.3",
            "modification-type": "new",
            "description": "The system shall allow the user to configure the format and elements to be included in the PowerPoint presentation."
        },
        {
            "parent-id": "UC-19",
            "id": "FR-19.4",
            "modification-type": "new",
            "description": "The system shall save the exported PowerPoint presentation to the specified location on the user's computer or network drive."
        }
    ],
    "non-functional-requirements": [
        {
            "id": "LAF-19.1",
            "modification-type": "new",
            "description": "The export to PowerPoint feature shall have an intuitive and easy-to-use interface."
        },
        {
            "id": "USA-19.1",
            "modification-type": "new",
            "description": "The system shall provide tooltips and help sections to assist users in exporting bridge inspection results to PowerPoint."
        },
        {
            "id": "CAP-19.1",
            "modification-type": "new",
            "description": "The system shall support exporting up to 100 bridges' inspection results in a single PowerPoint presentation."
        },
        {
            "id": "SPD-19.1",
            "modification-type": "new",
            "description": "The system shall export bridge inspection results to a PowerPoint presentation within 5 seconds for up to 10 bridges."
        },
        {
            "id": "AVL-19.1",
            "modification-type": "new",
            "description": "The system shall ensure high availability with a 99.9% uptime for the export feature."
        },
        {
            "id": "OPR-19.1",
            "modification-type": "new",
            "description": "The system shall provide logging for all export operations for auditing and troubleshooting purposes."
        },
        {
            "id": "DEP-19.1",
            "modification-type": "new",
            "description": "The export to PowerPoint feature shall be deployable without requiring downtime."
        },
        {
            "id": "MPR-19.1",
            "modification-type": "new",
            "description": "The system shall allow for easy updates and maintenance of the export to PowerPoint feature."
        },
        {
            "id": "SEC-19.1",
            "modification-type": "new",
            "description": "The system shall ensure that only authorized users can export bridge inspection results to PowerPoint."
        },
        {
            "id": "LGL-19.1",
            "modification-type": "new",
            "description": "The system shall comply with all relevant data protection and privacy laws for exporting bridge inspection results."
        }
    ]
}

===
-------------------------
Iteration 2:

{
    "use-cases": [
        {
            "parent-section": "3.6 DATA MANAGEMENT",
            "id": "UC-19",
            "modification-type": "new",
            "description": "The user exports bridge inspection results to a PowerPoint presentation in order to present risk analysis and recommendations in a digestible format.",
            "success-end-condition": "The bridge inspection results are successfully exported to a PowerPoint presentation."
        }
    ],
    "functional-requirements": [
        {
            "parent-id": "UC-19",
            "id": "FR-19.1",
            "modification-type": "new",
            "description": "The system shall provide the capability to export bridge inspection results directly to a PowerPoint presentation."
        },
        {
            "parent-id": "UC-19",
            "id": "FR-19.2",
            "modification-type": "new",
            "description": "The system shall allow the user to select specific bridge inspection results to include in the PowerPoint presentation."
        },
        {
            "parent-id": "UC-19",
            "id": "FR-19.3",
            "modification-type": "new",
            "description": "The system shall provide pre-defined PowerPoint templates that the user can select from when exporting bridge inspection results."
        },
        {
            "parent-id": "UC-19",
            "id": "FR-19.4",
            "modification-type": "new",
            "description": "The system shall allow the user to customize the exported PowerPoint slides with additional text, images, and formatting."
        }
    ],
    "non-functional-requirements": [
        {
            "id": "LAF-19.1",
            "modification-type": "new",
            "description": "The PowerPoint export functionality shall have an intuitive and user-friendly interface."
        },
        {
            "id": "USA-19.1",
            "modification-type": "new",
            "description": "The system shall ensure that the exported PowerPoint file is compatible with Microsoft PowerPoint 2016 and later versions."
        },
        {
            "id": "CAP-19.1",
            "modification-type": "new",
            "description": "The system shall support exporting PowerPoint presentations for up to 50 bridges in one operation."
        },
        {
            "id": "SPD-19.1",
            "modification-type": "new",
            "description": "The system shall complete the export of bridge inspection results to PowerPoint within 10 seconds."
        },
        {
            "id": "AVL-19.1",
            "modification-type": "new",
            "description": "The system shall ensure that the PowerPoint export functionality is available 18 hours per day, 353 days per year, with planned maintenance periods."
        },
        {
            "id": "MPR-19.1",
            "modification-type": "new",
            "description": "The PowerPoint export functionality shall be easily maintainable and upgradable to support future PowerPoint versions."
        }
    ]
}

===
Previous set was better...
-------------------------
Iteration 3:

{
    "use-cases": [
        {
            "parent-section": "3.6 DATA MANAGEMENT",
            "id": "UC-25",
            "modification-type": "new",
            "description": "The user exports bridge inspection results to a PowerPoint presentation.",
            "success-end-condition": "Bridge inspection results are exported successfully to a PowerPoint presentation file format, which can then be used for presentations and further analysis."
        }
    ],
    "functional-requirements": [
        {
            "parent-id": "UC-25",
            "id": "FR-25.1",
            "modification-type": "new",
            "description": "The system shall allow the user to select the bridge inspection results to be exported."
        },
        {
            "parent-id": "UC-25",
            "id": "FR-25.2",
            "modification-type": "new",
            "description": "The system shall provide an option to export the selected bridge inspection results to a PowerPoint presentation file format."
        },
        {
            "parent-id": "UC-25",
            "id": "FR-25.3",
            "modification-type": "new",
            "description": "The system shall allow the user to customize the PowerPoint presentation layout, including adding titles, descriptions, and choosing different slide templates."
        },
        {
            "parent-id": "UC-25",
            "id": "FR-25.4",
            "modification-type": "new",
            "description": "The system shall ensure that all graphics, charts, and images from the bridge inspection results are correctly exported and rendered in the PowerPoint presentation."
        },
        {
            "parent-id": "UC-25",
            "id": "FR-25.5",
            "modification-type": "new",
            "description": "The system shall provide an option to download the generated PowerPoint presentation to the user's local storage."
        }
    ],
    "non-functional-requirements": [
        {
            "id": "LAF-25.1",
            "modification-type": "new",
            "description": "The export functionality shall provide an intuitive user interface that guides the user through the process of selecting data and customizing the presentation layout."
        },
        {
            "id": "USA-25.1",
            "modification-type": "new",
            "description": "The system shall provide tooltips and help documentation for the export to PowerPoint functionality."
        },
        {
            "id": "CAP-25.1",
            "modification-type": "new",
            "description": "The system shall handle exporting up to 100 bridge inspection results to a single PowerPoint presentation file."
        },
        {
            "id": "SPD-25.1",
            "modification-type": "new",
            "description": "The system shall complete the export of bridge inspection results in under 10 seconds for up to 100 bridges."
        },
        {
            "id": "AVL-25.1",
            "modification-type": "new",
            "description": "The export service shall be available 99.5% of the time."
        },
        {
            "id": "SEC-25.1",
            "modification-type": "new",
            "description": "The system shall ensure that only authorized users with the necessary permissions can access the export to PowerPoint functionality."
        }
    ]
}

===
Previous set was better...
-------------------------
Iteration 4:

{
    "use-cases": [
        {
            "parent-section": "3.6 DATA MANAGEMENT",
            "id": "UC-19",
            "modification-type": "new",
            "description": "The user exports bridge inspection results to a PowerPoint presentation to present risk analysis and recommendations to management personnel.",
            "success-end-condition": "The bridge inspection results are successfully exported to a PowerPoint presentation with all necessary information including risk analysis and recommendations."
        }
    ],
    "functional-requirements": [
        {
            "parent-id": "UC-19",
            "id": "FR-19.1",
            "modification-type": "new",
            "description": "The system shall provide an option to export bridge inspection results to a PowerPoint presentation format."
        },
        {
            "parent-id": "UC-19",
            "id": "FR-19.2",
            "modification-type": "new",
            "description": "The system shall allow the user to include risk analysis and recommendations in the exported PowerPoint presentation."
        },
        {
            "parent-id": "UC-19",
            "id": "FR-19.3",
            "modification-type": "new",
            "description": "The system shall support customizable templates for the PowerPoint presentation to ensure the branding and presentation style of the management personnel."
        }
    ],
    "non-functional-requirements": [
        {
            "id": "LAF-19.1",
            "modification-type": "new",
            "description": "The exported PowerPoint presentation shall adhere to the company's style and formatting guidelines, ensuring brand consistency."
        },
        {
            "id": "USA-19.2",
            "modification-type": "new",
            "description": "The export feature shall be user-friendly and accessible to users with basic computer skills."
        },
        {
            "id": "CAP-19.3",
            "modification-type": "new",
            "description": "The system shall be able to handle the export of large sets of bridge inspection results without performance degradation."
        },
        {
            "id": "SPD-19.4",
            "modification-type": "new",
            "description": "The export process shall complete within 30 seconds for a standard set of bridge inspection results."
        },
        {
            "id": "AVL-19.5",
            "modification-type": "new",
            "description": "The export feature shall have an uptime of 99.9% to ensure availability when needed."
        },
        {
            "id": "OPR-19.6",
            "modification-type": "new",
            "description": "The system shall provide operational support to handle any export-related issues promptly."
        },
        {
            "id": "DEP-19.7",
            "modification-type": "new",
            "description": "The export feature shall be easy to deploy and integrate with the existing system with minimal configuration required."
        },
        {
            "id": "MPR-19.8",
            "modification-type": "new",
            "description": "The export feature shall be maintainable with minimal effort, including the ability to update templates and export logic as needed."
        },
        {
            "id": "SEC-19.9",
            "modification-type": "new",
            "description": "The system shall ensure that the data exported to the PowerPoint presentation is secure, preventing unauthorized access."
        },
        {
            "id": "LGL-19.10",
            "modification-type": "new",
            "description": "The system shall comply with legal policies regarding data export and presentation usage."
        }
    ]
}

===
Previous set was better...
-------------------------
Iteration 5:

{
    "use-cases": [
        {
            "parent-section": "3.1 BROWSE BRIDGE & PROJECT DATA",
            "id": "UC-25",
            "modification-type": "new",
            "description": "The user exports bridge inspection results to a PowerPoint presentation.",
            "success-end-condition": "Bridge inspection results are successfully exported to a PowerPoint presentation in the desired format and stored in the Pontis database for future use."
        }
    ],
    "functional-requirements": [
        {
            "parent-id": "UC-25",
            "id": "FR-25.1",
            "modification-type": "new",
            "description": "The system shall enable users to select multiple bridge inspection results for export to a PowerPoint presentation."
        },
        {
            "parent-id": "UC-25",
            "id": "FR-25.2",
            "modification-type": "new",
            "description": "The system shall provide templates for exporting bridge inspection results to a PowerPoint presentation."
        },
        {
            "parent-id": "UC-25",
            "id": "FR-25.3",
            "modification-type": "new",
            "description": "The system shall allow users to customize the layout and content of the PowerPoint presentation export."
        },
        {
            "parent-id": "UC-25",
            "id": "FR-25.4",
            "modification-type": "new",
            "description": "The system shall ensure that the exported PowerPoint presentation includes risk analysis and recommendations for the selected bridge inspection results."
        },
        {
            "parent-id": "UC-25",
            "id": "FR-25.5",
            "modification-type": "new",
            "description": "The system shall store the exported PowerPoint presentations in the Pontis database for future access."
        },
        {
            "parent-id": "UC-25",
            "id": "FR-25.6",
            "modification-type": "new",
            "description": "The system shall notify the user upon successful export of bridge inspection results to a PowerPoint presentation."
        }
    ],
    "non-functional-requirements": [
        {
            "id": "LAF-25.1",
            "modification-type": "new",
            "description": "The PowerPoint export feature shall have an intuitive and user-friendly interface."
        },
        {
            "id": "USA-25.2",
            "modification-type": "new",
            "description": "The PowerPoint export process shall be documented with step-by-step guidelines for users."
        },
        {
            "id": "CAP-25.3",
            "modification-type": "new",
            "description": "The system shall support exporting PowerPoint presentations for up to 50 bridges in a single operation."
        },
        {
            "id": "SPD-25.4",
            "modification-type": "new",
            "description": "The system shall complete the export of bridge inspection results to a PowerPoint presentation within 30 seconds."
        },
        {
            "id": "AVL-25.5",
            "modification-type": "new",
            "description": "The PowerPoint export feature shall be available 99% of the time during operational hours."
        },
        {
            "id": "SEC-25.6",
            "modification-type": "new",
            "description": "The system shall ensure that exported PowerPoint presentations are only accessible to users with the appropriate permissions."
        }
    ]
}

===
New best found!
# Functional Requirement Improvement Log

- Original: The system shall enable users to select multiple bridge inspection results for export to a PowerPoint presentation.
- Unambiguous: The system shall allow users to select multiple bridge inspection results and export them to a PowerPoint presentation file.
- Formatted: The system shall allow users to select multiple bridge inspection results and export them to a PowerPoint presentation file.
---
- Original: The system shall provide templates for exporting bridge inspection results to a PowerPoint presentation.
- Unambiguous: The system shall provide predefined templates for exporting bridge inspection results to a PowerPoint presentation file.
- Formatted: The system shall provide predefined templates for exporting bridge inspection results to a PowerPoint presentation file.
---
- Original: The system shall allow users to customize the layout and content of the PowerPoint presentation export.
- Unambiguous: The system shall allow users to customize the layout and content of the PowerPoint presentation export, including slide order, text, images, and formatting options.
- Formatted: The system shall allow users to customize the layout and content of the PowerPoint presentation export, including slide order, text, images, and formatting options.
---
- Original: The system shall ensure that the exported PowerPoint presentation includes risk analysis and recommendations for the selected bridge inspection results.
- Unambiguous: The system shall ensure that the exported PowerPoint presentation includes a detailed risk analysis and specific recommendations based on the selected bridge inspection results.
- Formatted: The system shall ensure that the exported PowerPoint presentation includes a detailed risk analysis and specific recommendations based on the selected bridge inspection results.
---
- Original: The system shall store the exported PowerPoint presentations in the Pontis database for future access.
- Unambiguous: The system shall store the exported PowerPoint presentations in the Pontis database under the "Exported Presentations" directory for future access by authorized users.
- Formatted: The system shall store the exported PowerPoint presentations in the Pontis database under the "Exported Presentations" directory for future access by authorized users.
---
- Original: The system shall notify the user upon successful export of bridge inspection results to a PowerPoint presentation.
- Unambiguous: The system shall display a notification message to the user immediately after the bridge inspection results have been successfully exported to a PowerPoint presentation file.
- Formatted: WHEN the bridge inspection results have been successfully exported to a PowerPoint presentation file, the system shall display a notification message to the user.
---
# Non-Functional Requirement Improvement Log

- Original: The PowerPoint export feature shall have an intuitive and user-friendly interface.
- Verifiable: The PowerPoint export feature shall allow users to export bridge inspection results to a PowerPoint presentation with no more than three clicks from the main interface.
- Unambiguous: The PowerPoint export feature shall enable users to export bridge inspection results to a PowerPoint presentation using exactly three clicks from the main interface.
- Formatted: The PowerPoint export feature shall enable users to export bridge inspection results to a PowerPoint presentation using exactly three clicks from the main interface.
---
- Original: The PowerPoint export process shall be documented with step-by-step guidelines for users.
- Verifiable: The PowerPoint export process shall be documented with a step-by-step guide that includes at least 10 distinct steps, each with a corresponding screenshot, and shall be accessible within the help section of the software.
- Unambiguous: The PowerPoint export process shall be documented with a step-by-step guide that includes exactly 10 distinct steps, each with a corresponding screenshot, and shall be accessible within the help section of the software.
- Formatted: The PowerPoint export process shall be documented with a step-by-step guide that includes exactly 10 distinct steps, each with a corresponding screenshot, and shall be accessible within the help section of the software.
---
- Original: The system shall support exporting PowerPoint presentations for up to 50 bridges in a single operation.
- Verifiable: The system shall support exporting PowerPoint presentations for up to 50 bridges in a single operation, with each export operation completing within 5 minutes.
- Unambiguous: The system shall support exporting PowerPoint presentations for up to 50 bridge inspection results in a single operation, with each export operation completing within 5 minutes.
- Formatted: The system shall support exporting PowerPoint presentations for up to 50 bridge inspection results in a single operation, with each export operation completing within 5 minutes.
---
- Original: The system shall complete the export of bridge inspection results to a PowerPoint presentation within 30 seconds.
- Verifiable: The system shall complete the export of bridge inspection results to a PowerPoint presentation within 30 seconds 95% of the time.
- Unambiguous: The system shall complete the export of bridge inspection results to a PowerPoint presentation file within 30 seconds for 95% of export attempts.
- Formatted: The system shall complete the export of bridge inspection results to a PowerPoint presentation file within 30 seconds for 95% of export attempts.
---
- Original: The PowerPoint export feature shall be available 99% of the time during operational hours.
- Verifiable: The PowerPoint export feature shall be available 99% of the time during operational hours, measured over a period of one month.
- Unambiguous: The PowerPoint export feature shall have an uptime of at least 99% during operational hours, calculated over a continuous period of one month.
- Formatted: WHILE [in operational hours] the [PowerPoint export feature] shall [have an uptime of at least 99%, calculated over a continuous period of one month]
---
- Original: The system shall ensure that exported PowerPoint presentations are only accessible to users with the appropriate permissions.
- Verifiable: The system shall restrict access to exported PowerPoint presentations to users who have been granted the "Export PowerPoint" permission, verified by the system's access control mechanism.
- Unambiguous: The system shall restrict access to exported PowerPoint presentations exclusively to users who possess the "Export PowerPoint" permission, as verified by the system's access control mechanism.
- Formatted: The system shall restrict access to exported PowerPoint presentations exclusively to users who possess the "Export PowerPoint" permission.
---
# Consistency Requirement Improvement Log
(1, "under the 'Exported Presentations' directory ")
(-1, '\\"')
(1, "'")
(-1, '\\"')
(1, "'")
(1, '.')
(-1, '\\"')
(1, "'")
(-1, '\\"')
(1, "'")
# Final Output Message
```json
{
    "use-cases": [
        {
            "parent-section": "3.1 BROWSE BRIDGE & PROJECT DATA",
            "id": "UC-25",
            "modification-type": "new",
            "description": "The user exports bridge inspection results to a PowerPoint presentation.",
            "success-end-condition": "Bridge inspection results are successfully exported to a PowerPoint presentation in the desired format and stored in the Pontis database under the 'Exported Presentations' directory for future use."
        }
    ],
    "functional-requirements": [
        {
            "parent-id": "UC-25",
            "id": "FR-25.1",
            "modification-type": "new",
            "description": "The system shall allow users to select multiple bridge inspection results and export them to a PowerPoint presentation file."
        },
        {
            "parent-id": "UC-25",
            "id": "FR-25.2",
            "modification-type": "new",
            "description": "The system shall provide predefined templates for exporting bridge inspection results to a PowerPoint presentation file."
        },
        {
            "parent-id": "UC-25",
            "id": "FR-25.3",
            "modification-type": "new",
            "description": "The system shall allow users to customize the layout and content of the PowerPoint presentation export, including slide order, text, images, and formatting options."
        },
        {
            "parent-id": "UC-25",
            "id": "FR-25.4",
            "modification-type": "new",
            "description": "The system shall ensure that the exported PowerPoint presentation includes a detailed risk analysis and specific recommendations based on the selected bridge inspection results."
        },
        {
            "parent-id": "UC-25",
            "id": "FR-25.5",
            "modification-type": "new",
            "description": "The system shall store the exported PowerPoint presentations in the Pontis database under the 'Exported Presentations' directory for future access by authorized users."
        },
        {
            "parent-id": "UC-25",
            "id": "FR-25.6",
            "modification-type": "new",
            "description": "WHEN the bridge inspection results have been successfully exported to a PowerPoint presentation file, the system shall display a notification message to the user."
        }
    ],
    "non-functional-requirements": [
        {
            "id": "LAF-25.1",
            "modification-type": "new",
            "description": "The PowerPoint export feature shall enable users to export bridge inspection results to a PowerPoint presentation using exactly three clicks from the main interface."
        },
        {
            "id": "USA-25.2",
            "modification-type": "new",
            "description": "The PowerPoint export process shall be documented with a step-by-step guide that includes exactly 10 distinct steps, each with a corresponding screenshot, and shall be accessible within the help section of the software."
        },
        {
            "id": "CAP-25.3",
            "modification-type": "new",
            "description": "The system shall support exporting PowerPoint presentations for up to 50 bridge inspection results in a single operation, with each export operation completing within 5 minutes."
        },
        {
            "id": "SPD-25.4",
            "modification-type": "new",
            "description": "The system shall complete the export of bridge inspection results to a PowerPoint presentation file within 30 seconds for 95% of export attempts."
        },
        {
            "id": "AVL-25.5",
            "modification-type": "new",
            "description": "WHILE [in operational hours] the [PowerPoint export feature] shall [have an uptime of at least 99%, calculated over a continuous period of one month]."
        },
        {
            "id": "SEC-25.6",
            "modification-type": "new",
            "description": "The system shall restrict access to exported PowerPoint presentations exclusively to users who possess the 'Export PowerPoint' permission."
        }
    ]
}
```