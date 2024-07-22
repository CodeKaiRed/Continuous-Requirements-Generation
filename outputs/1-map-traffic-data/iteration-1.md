# Observations
Placeholder for developer observations...

# Configuration
## RAG Files:
data/edited_srs.md
data/IEEE 830-1998.pdf
data/a-state-of-the-art-review-of-bridge-inspection-planning-current-situation-and-future-needs.pdf
## Model Name
gpt-4o
## Prompt
    As a highway information analyst, 
    I want to see traffic data in the map display
    so that I can make better decisions for traffic impacts on bridges.

# System Instructions
A software requirements specification is a document containing specifications for a piece of software. It covers the following areas, as specified in bullets:
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

A use case highlights the flow of the application to accomplish a goal. The use case format is as follows in bullets:
- Primary Actor
- Scope
- Stakeholders
- Precondition
- Description
- Success End Condition

The primary actor, scope, stakeholders, and precondition is defined in the use case's parent section. Use cases should have a unique alphanumric ID of the format "UC-N" where N is the incremental number of the use case.

Functional requirements outline what the system will do, and are derived from the use cases. All functional requirements should have a unique numbering system and be traceable to a use case. Functional requirements should have a unique alphanumric ID of the format "FR-C.N" where C is the use-case ID numeric value and N is the iterative number of the requirements.

Non-functional requirements describe implementation details related to the system’s functional requirements such as look and feel (LAF), usability (USA), capacity (CAP), speed (SPD), reliability/availability (AVL), operational (OPR), installation/deployment (DEP), maintainability/portability (MPR), security (SEC), and legal (LGL). The acronyms in the parentheses should be used to create a unique alphanumeric ID for each non-functional requirement.

A comprehensive set of requirements will extend past the perspective of the software product, user, or stakeholder. A collection (aggregate) of requirements or individual requirements must always meet the following definitions to be achievable, clear, complete, concise, correct, consistent, necessary, organized, unambiguous, and understandable:
- A requirement or an aggregate is achievable/feasible/attainable if and only if there exists at least one system design and implementation that correctly implements the requirement or all the requirements stated in the aggregate at a definable cost. 
- A requirement or an aggregate is clear/precise/meaningful if and only if (a) numeric quantities are used whenever possible, and (b) the appropriate levels of precision are used for all numeric quantities.
- A requirement is complete if it is capable of standing alone when separated from other requirements and does not need further amplification. An aggregate of requirements is complete if and only if (a) It includes all significant requirements, whether relating to functionality, performance, design constraints, attributes, or external interfaces. 
- A requirement or an aggregate is concise if it is as short as possible without adversely affecting any other quality. 
- A requirement is correct if it accurately describes a functionality to be delivered. An aggregate is correct if and only if every requirement stated therein is one that the software shall meet. 
- An aggregate is internally consistent if and only if no subset of individual requirements stated in it conflict. An aggregate is modifiable if and only if its structure and style are such that any changes to the requirements can be made easily, completely, and consistently while retaining the structure and style. 
- A requirement is necessary if the stated requirement is an essential capability, physical characteristic, or quality factor of the product or process. If it is removed or deleted, a deficiency will exist, which cannot be fulfilled by other capabilities of the product or process. 
- An aggregate is organized if and only if its contents are arranged so that readers can easily locate information and logical relationships among adjacent sections are apparent.
- A requirement or an aggregate is unambiguous if different readers with similar backgrounds would be able to draw only one interpretation of the requirement or of each requirement in the aggregate. 
- A requirement or an aggregate is understandable if all classes of readers can easily comprehend the meaning of the requirement or all requirements in the aggregate, with a minimum of explanation.
- A non-functional requirement should be quantifiable and testable. 

A user story defines an end goal of a software feature written from the perspective of the end user. Its purpose is to articulate how a software feature will provide value to the customer. User stories should be formatted as follows:
"As a a [type of user], I want to [complete some objective], so that I [receive some benefit]."

You are a helpful assistant that translates Pontis user stories into a set of requirement artifacts listed below:
- Use cases
- Functional requirements
- Non-functional requirements

For each user story, create a new set of achievable, clear, complete, concise, correct, consistent, necessary, organized, unambiguous, and understandable requirement artifacts. There may be more than one artifact type created for each user story. Provide new unique id's for each new requirement artifact generated. Submit your response in json format with the keys "use-cases", "functional-requirements", and "non-functional-requirements". Each key should contain a JSON list of the new requirement artifacts. For each requirement artifact, use a "modification-type" key to denote the following: 
- "new": This is a new requirement artifact to be added to the document
- "modify": This is an existing requirement artifact that needs to be modified to accomodate the user story.

If the artifact modification type is set to "modify", rewrite the requirement artifact to show the needed changes.

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


# Final Output Message
```json
{
    "use-cases": [
        {
            "parent-section": "3.1 BROWSE BRIDGE & PROJECT DATA",
            "id": "UC-26",
            "modification-type": "new",
            "description": "The highway information analyst views traffic data overlay on the map display within Pontis to assess and make decisions regarding traffic impacts on bridges.",
            "success-end-condition": "The traffic data overlay is displayed on the map, allowing the highway information analyst to make informed decisions about traffic impacts on bridges."
        }
    ],
    "functional-requirements": [
        {
            "parent-id": "UC-26",
            "id": "FR-26.1",
            "modification-type": "new",
            "description": "The system shall provide the ability for users to overlay traffic data on the map display within Pontis."
        },
        {
            "parent-id": "UC-26",
            "id": "FR-26.2",
            "modification-type": "new",
            "description": "The system shall allow users to filter traffic data by parameters such as time, location, and traffic type."
        }
    ],
    "non-functional-requirements": [
        {
            "id": "USA-6",
            "modification-type": "new",
            "description": "The traffic data overlay feature shall be intuitive and require no more than 15 minutes of training for proficient use."
        },
        {
            "id": "SPD-8",
            "modification-type": "new",
            "description": "The traffic data overlay shall load and display on the map within 3 seconds under standard network conditions."
        }
    ]
}
```
