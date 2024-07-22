# Observations
After updating the system instructions to match the use case format to the provided SRS, the outputs are more seamless. The LLM chooses to place the edits at the end of each relevant section, instead of choosing a location that is more appropriate. It also chose to use N as a variable numeric indicator instead of coming up with an appropriate value for the numbering scheme.

# Configuration
## RAG Files:
data/2005 - pontis.pdf
data/output_srs.md
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

Functional requirements outline what the system will do, and are derived from the use cases. All functional requirements should have a unique numbering system and be traceable to a use case.

Non-functional requirements describe implementation details related to the system’s functional requirements such as performance, security, safety, reliability, availability, modularity, legality, maintability, portability, supportability, scalability, and/or usability. 

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

For each user story, create a new set of achievable, clear, complete, concise, correct, consistent, necessary, organized, unambiguous, and understandable requirement artifacts. There may be more than one artifact type created for each user story. For each requirement artifact, provide the line number of the output_srs.md file where the artifact should be placed.

# Final Output Message
To fulfill the requirement based on the provided user story, we will translate the user story into a set of requirement artifacts including Use Cases, Functional Requirements, and Non-Functional Requirements. These will be organized based on the appropriate sections within the "output_srs.md" file. Let's begin:

### Use Case

**Primary Actor:** Highway Information Analyst

**Scope:** Pontis Application
  
**Stakeholders:** Highway Information Analysts
  
**Precondition:** The user is logged into the Pontis application.
  
**Description:** The analyst wants to view traffic data overlayed or incorporated within the map display provided by the application.
  
**Success End Condition:** Traffic data is accurately displayed within the map view, allowing the analyst to make informed decisions regarding traffic impacts on bridges.

**Line for Placement in output_srs.md:** Post Use Case 24 administration functionalities .

### Functional Requirements

1. **FR-N**: The system shall provide the capability for highway information analysts to view traffic data within the map display.
   
2. **FR-N+1**: The system shall allow filtering and selection of traffic data based on specific bridge-related criteria within the map display.
   
3. **FR-N+2**: Traffic data displayed shall be updated in real-time to ensure decision-making is based on the most current information available.

**Line for Placement in output_srs.md:** After the last detailed functional requirement for Create/Edit Inspection .

### Non-Functional Requirements

1. **NF-N**: The system shall ensure traffic data is displayed on the map within X seconds of the user's request, ensuring timely access to information.
   
2. **NF-N+1**: The system's map display component shall be capable of handling simultaneous traffic data requests from multiple users without significant performance degradation.

**Line for Placement in output_srs.md:** After the last detailed non-functional requirement regarding saving reports in different formats including PDF, HTML, and XML .

---
**Note:** "N" denotes the next available sequential number following the latest requirement listed in the provided "output_srs.md" document for each type of requirement. Please adjust the "N" accordingly based on the current document state to maintain a proper and unique numbering sequence for easy tracking and referencing.
