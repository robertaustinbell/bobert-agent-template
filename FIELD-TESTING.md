# Field-testing the concepts

This starter contains active but revisable operating doctrine. Real work—not repository coherence—reveals whether a concept improves an agent's observation, recommendation, action, verification, or repair.

Field reports are welcome for useful results, null results, failures, excess ceremony, and cases where another explanation fits better.

## Choose a bounded test

1. Name the doctrine section or claim being tested.
2. Use a real task where the concept could materially change a decision. Do not manufacture risk or broaden an agent's authority merely to create a test.
3. Prefer a prospective test: record the prediction, expected decision effect, success or failure signal, stop condition, and review point before acting.
4. Use the smallest safe action that can expose useful feedback.
5. Afterward, distinguish what happened from what the concept changed.

A retrospective can still identify a plausible failure layer or missing control, but hindsight is weaker evidence than a prediction recorded before the result.

## Situational-understanding starter test

For a consequential task where relevant state can change:

1. **Perception:** record the material verified current state and important unobserved state.
2. **Comprehension:** state what those observations mean relative to the objective, decision owner, constraints, dependencies, and feedback loops.
3. **Projection:** identify the near-future transition or response most likely to change the move.
4. Record the expected observable result, a disconfirming signal, the authorization boundary, and the feedback path.
5. Take only an already-authorized action.
6. After a surprise or failure, identify the earliest supported layer: perception, comprehension, projection, decision, execution, or feedback. Preserve ambiguity when the evidence cannot distinguish them.

A test becomes informative when it shows a material decision effect, a useful failure, or a clean null result against a prior prediction—not merely when the vocabulary can be applied after the fact.

## Critical-capability mapping candidate test

For a consequential task where the objective may depend on a concentrated capability or enabling condition:

1. State the objective, decision owner, and time horizon.
2. Name the capability or jointly necessary set of capabilities that must exist for the objective to remain achievable. Do not begin with the most visible component or actor.
3. Identify the process, component, or role that performs the capability.
4. Map the capability's critical requirements: resources, information, authority, coordination, infrastructure, and feedback it depends on.
5. Identify conditional vulnerabilities: requirements whose deficiency or loss would materially impair the capability in this context.
6. Challenge concentration before acting. Look for substitutes, redundancy, jointly necessary elements, adaptation, and changes in the objective or horizon. Do not force one decisive centre.
7. Record what the map is expected to change—protection, strengthening, simplification, redundancy, bypass, instrumentation, sequencing, or explicit risk acceptance—and what result would disconfirm the map.
8. Compare the result with ordinary critical-path or bottleneck analysis. A clean null result includes finding that the map only renamed an already-known dependency.

Importance is not vulnerability, and vulnerability does not establish causal sufficiency. Do not label a person as a vulnerability or convert the analysis into attack-first framing; describe the capability, role, dependency, and rights-preserving intervention instead.

This candidate adapts critical-factor analysis discussed in Eystein L. Meyer, [“The Centre of Gravity Concept: Contemporary Theories, Comparison, and Implications”](https://doi.org/10.1080/14702436.2022.2030715) (2022). Meyer concludes that “centre of gravity” is terminologically polluted across competing theories. The candidate therefore retains the capability–requirement–vulnerability map without presuming a universal, singular, or decisive centre. Its usefulness for agents is unestablished.

## Report the result

A useful report includes:

- concept and exact repository path or heading;
- prospective or retrospective design;
- task context at the minimum safe granularity;
- prediction and expected decision effect;
- observation and evidence quality;
- what changed in the decision, action, verification, or repair;
- strongest alternative explanation or confound;
- failure, null result, or cost imposed by the concept;
- proposed narrowing, revision, or follow-up, if any.

Do not use a report count as a promotion threshold. Repeated applications can share the same blind spot. Evidence should update confidence and scope according to independence, consequence, source quality, and whether the concept changed the work.

## Privacy and authority boundary

Publish only sanitized, minimum-necessary evidence. Never include:

- credentials, tokens, keys, passwords, or connection strings;
- personal, household, health, financial, client, employee, or location records;
- private messages, transcripts, screenshots, runtime dumps, or proprietary source code;
- machine paths, account identifiers, infrastructure details, or authorization state;
- actions taken outside the authority already granted by the system owner.

If sanitization would make the report misleading, keep the evidence private and submit only the general lesson—or do not submit it.

## Submit feedback

Open the repository’s **Issues** tab, choose **New issue**, and select **Concept field test**. A pull request is appropriate when the evidence supports a concrete public change; follow [CONTRIBUTING.md](CONTRIBUTING.md) and explain the decision effect, scope, strongest objection, known failure, and reversal evidence.
