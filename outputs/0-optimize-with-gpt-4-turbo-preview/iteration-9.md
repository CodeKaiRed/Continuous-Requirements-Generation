# Observations
The SRS was edited to provide more concise, single statments for non-functional requirements, and more robust alphanumeric identifiers for all requirement artifacts. The system instructions were updated to include clearer formatting for the output based on the edits made to the document. The LLM no longer receives the original pdf file for RAG.

The output shown is better than iteration-8. However, the LLM is confused on how to output multiple of the same requirement artifact type. For example, it has accurately identified three FR's to capture the user story. Though, the last two FR's are listed as sub-bullets for the first one. Maybe a better output format should be considered. The LLM also cannot recognize that the unique ID's provided conflict with the existing. Maybe updating the system instructions will help here.

# Configuration
## RAG Files:
data/edited_srs.md
data/IEEE 830-1998.pdf
## Model Name
gpt-4-turbo-preview
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
- An aggregate is organized if and only if its contents are arranged so that readers can easily locate information and logical relationships among adjacent sections are apparent. - A requirement is prioritized/ranked/annotated by relative importance if the requirement is assigned an implementation priority to indicate how essential it is to include it in a particular product. 
- An aggregate is prioritized/ranked/annotated by relative importance if each requirement in it has an identifier to indicate the importance of that particular requirement. 
- A requirement or an aggregate is unambiguous if different readers with similar backgrounds would be able to draw only one interpretation of the requirement or of each requirement in the aggregate. 
- A requirement or an aggregate is understandable if all classes of readers can easily comprehend the meaning of the requirement or all requirements in the aggregate, with a minimum of explanation.
- A non-functional requirement should be quantifiable and testable. 

A user story defines an end goal of a software feature written from the perspective of the end user. Its purpose is to articulate how a software feature will provide value to the customer. User stories should be formatted as follows:
"As a a [type of user], I want to [complete some objective], so that I [receive some benefit]."

You are a helpful assistant that translates Pontis user stories into a set of requirement artifacts listed below:
- Use cases
- Functional requirements
- Non-functional requirements

For each user story, create a new set of achievable, clear, complete, concise, correct, consistent, necessary, organized, unambiguous, and understandable requirement artifacts. There may be more than one artifact type created for each user story. For each requirement artifact, provide the lowest-level section heading of the output_srs.md file where the artifact should be placed. Submit your answer in the following format delimited by triple quotes:

"""
### Use Cases
UC-7: Calculate Dependent/Derived Inspection Results
- **Description:** The user calculates derived ratings (NBI condition ratings, structural rating, geometric rating, sufficiency rating, and SD/FO status) based on inspection data. Users may override any calculated NBI condition rating such as deck, superstructure, substructure or culvert condition as necessary.
- **Success End Condition:**  The dependent ratings are calculated and, if accepted by the user, are stored in the Pontis database. Ratings for deck, superstructure, and substructure, or culvert, condition can be entered directly to override calculated results.
- **Section Location:** 3.2

### Functional Requirements
FR-7.1 The system shall be capable of calculating NBI condition ratings using the FHWA NBI Translator.
-**Section Location:** UC-7 **Calculate Dependent/Derived Inspection Results**
FR-7.2 The system shall be capable of calculating and storing bridge Sufficiency Rating.
-**Section Location:** UC-7 **Calculate Dependent/Derived Inspection Results**

### Non-Functional Requirements
SPD-6: Pontis 5.0 shall retrieve and display single bridge (inspection) detail in less than 2 seconds, unless non-native content is being accessed.
SPD-7: Pontis 5.0 shall validate 50 bridges for NBI edit check within 10 seconds, at a rate better than 3 bridges per seconds.
-**Section Location:** Speed (SPD)
"""


# Final Output Message

### Use Cases
UC-1: Display Traffic Data on Map
- **Description:** As a highway information analyst, the user wants to be able to see traffic data overlaid on a map display within the software interface to aid in making informed decisions regarding traffic impacts on bridges.
- **Primary Actor:** Highway Information Analyst
- **Scope:** Software Interface
- **Stakeholders:** Highway Information Analysts, Traffic Management Authorities, Bridge Maintenance Teams
- **Precondition:** The user has access to the software and relevant traffic and bridge data is available.
- **Success End Condition:** Traffic data is displayed on the map, allowing the analyst to visualize traffic conditions and potential impacts on bridge infrastructure.
- **Section Location:** 3.2 Use Cases

### Functional Requirements
FR-1.1: The system shall provide an interface to overlay traffic data on the map display.
- **Section Location:** UC-1 **Display Traffic Data on Map**
FR-1.2: The system shall allow users to select specific bridges on the map to view detailed traffic data.
- **Section Location:** UC-1 **Display Traffic Data on Map**
FR-1.3: The system shall update traffic data on the map in real-time or near-real-time to ensure information is current.
- **Section Location:** UC-1 **Display Traffic Data on Map**

### Non-Functional Requirements
USA-1: The traffic data overlay on the map shall be intuitive to use and require minimal training for highway information analysts.
- **Section Location:** Usability (USA)
SPD-1: The system shall update the displayed traffic data within seconds of receiving new data to ensure timely decision-making.
- **Section Location:** Speed (SPD)
CAP-1: The system must be capable of handling the simultaneous display of traffic data for at least 1000 bridges without degradation of performance.
- **Section Location:** Capacity (CAP)

