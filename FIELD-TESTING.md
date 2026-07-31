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

The test succeeds as evidence only when it shows a material decision effect or useful failure—not when the vocabulary can be applied after the fact.

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
