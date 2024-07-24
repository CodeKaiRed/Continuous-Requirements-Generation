### Generic requirements syntax
The generic requirement syntax adopted during this
study is as follows:

[optional preconditions] [optional trigger] the [system name] shall [system response]

This simple structure forces the requirement author to separate the conditions in which the requirement can be invoked (preconditions), the event that initiates the requirement (trigger) and the necessary system behaviour (system response). Both preconditions and trigger are optional, depending on the requirement type, as described
later in this section. The order of the clauses in this syntax is also significant, since it follows temporal logic:
- Any preconditions must be satisfied otherwise the requirement cannot ever be activated.
- The trigger must be true for the requirement to be “fired”, but only if the preconditions were already satisfied.
- The system is required to achieve the stated system response if and only if the preconditions and trigger are true.

The generic requirement syntax is specialised into five types of requirement (Ubiquitous, Event-driven, Unwanted behaviours, State-driven and Optional features), which are described in more detail below.

### 4.2 Ubiquitous requirements
A ubiquitous requirement has no preconditions or trigger. It is not invoked by an event detected at the system boundary or in response to a defined system state, but is
always active. The general form of a ubiquitous requirement is:

The [system name] shall [system response]

For example: “The control system shall prevent engine overspeed”. This is a system behaviour that must be active at all times; hence this is a ubiquitous requirement.

### 4.3 Event-driven requirements
An event-driven requirement is initiated only when a triggering event is detected at the system boundary. The keyword When is used for event-driven requirements. The
general form of an event-driven requirement is:

WHEN [optional preconditions] [trigger] the [system name] shall [system response]

For example: “When continuous ignition is commanded by the aircraft, the control system shall switch on continuous ignition”. This system response is required when and only when the stated event is detected at the boundary of the system.

### 4.4 Unwanted behaviours
Requirements to handle unwanted behaviour are defined using a syntax derived from event-driven requirements. “Unwanted behaviour” is a general term used to cover all situations that are undesirable. This includes failures, disturbances, deviations from desired user behaviour and any unexpected behaviour of interacting systems. The authors’ experiences suggest that unwanted behaviour is a major source of omissions in early requirements, necessitating costly rework. Consequently, these requirements were given their own syntax, so that they could be easily identified throughout the lifecycle. 

Requirements for unwanted behaviour are designated using the keywords If and Then. The general form of a requirement for unwanted behaviour is:

IF [optional preconditions] [trigger], THEN the [system name] shall [system response]

For example “If the computed airspeed fault flag is set, then the control system shall use modelled airspeed”. In this example, the unwanted event (computed air speed fault flag is set) triggers the system response, which allows continued safe operation of the system. 

Using the If-Then structure explicitly differentiates the requirements that handle unwanted behaviour. In such requirements the system response mitigates the impact of
the unwanted event, or prevents the system from entering an unwanted state.

Note: The distinction between wanted and unwanted behaviour is not always clear. For example, due to the safety-critical nature of aero engine control systems, many subsystems employ multiple redundant components. This allows the system to accommodate unwanted events whilst continuing to satisfy operational requirements. In such cases, the system is behaving “normally”, but the requirements would be considered as describing “unwanted behaviours” using the classification described here. Hence the distinction between wanted and unwanted behaviour is a matter of viewpoint, or even a matter of “style”. Another perspective on the distinction between wanted and unwanted
behaviours is provided by the concept of Misuse Cases. Misuse Cases describe users with hostile intent who are likely to have wants that are in direct opposition to the wants of other system stakeholders. 

### 4.5 State-driven requirements
A state-driven requirement is active while the system is in a defined state. The keyword While is used to denote state-driven requirements. The general form of a statedriven requirement is:

WHILE [in a specific state] the [system name] shall [system response]

For example: “While the aircraft is in-flight, the control system shall maintain engine fuel flow above XXlbs/sec”. The system response is required at all times
whilst the system is in the defined state. 

To make requirements easier to read, the keyword During can be used instead of While for state-driven requirements. For example: “During thrust reverser door translation, the control system shall limit thrust to minimum idle”. In this context, the meaning of During is identical to While, and this alternative keyword is used purely to aid readability.

### 4.6 Optional features
An optional feature requirement is applicable only in systems that include a particular feature. An optional feature requirement is designated with the keyword Where. The general form of an optional feature requirement is:

WHERE [feature is included] the [system name] shall [system response]

For example, “Where the control system includes an overspeed protection function, the control system shall test the availability of the overspeed protection function
prior to aircraft dispatch”. This functionality only makes sense (and therefore is only required) for a system that includes the specified feature.

### 4.7 Complex requirement syntax
For requirements with complex conditional clauses, combinations of the keywords When, While and Where may be required. The keywords can be built into more complex expressions to specify richer system behaviours. For instance, the same event may trigger different system behaviour depending on the state of the system when the
event is detected. 

For example: “While the aircraft is on-ground, when reverse thrust is commanded, the control system shall enable deployment of the thrust reverser”. The triggering event (reverse thrust command) triggers the system response only when the system is in a particular state (aircraft on-ground).

The keywords When, While and Where can also be used within If-Then statements to handle unwanted behaviour with more complex conditional clauses. For example the requirement to handle thrust reverser commands during the in-flight state (an unwanted and potentially catastrophic event) is handled as follows: “While the aircraft is in-flight, if reverse thrust is commanded, then the control system shall inhibit thrust reverser deployment”. In this situation the trigger (reverse thrust command) is
unwanted whilst in-flight and the required system response prevents the system from entering an unwanted state.

Similarly, in the requirement “When selecting idle setting, if aircraft data is unavailable, then the control system shall select Approach Idle”, the unwanted behaviour (aircraft data is unavailable) should result in the stated system response only when the triggering event (selecting idle) is satisfied.