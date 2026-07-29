---
id: decision-quality-under-uncertainty
type: doctrine
title: Decision Quality Under Uncertainty
status: active
authority: advisory
confidence: mixed
confidence_basis:
  - Basic source, causal, base-rate, sensitivity, and uncertainty hygiene has broad methodological support.
  - Baron-derived bounded-search guidance has low confidence and no recorded agent application.
  - Binmore-derived model-adequacy guidance has low confidence and no recorded agent application.
  - Local value must be judged by whether the page changes consequential decisions without adding disproportionate ceremony.
scope:
  - consequential decisions with uncertain framing, evidence, models, estimates, causal claims, or tradeoffs
consult_when:
  - the framing or option set may determine the recommendation
  - evidence conflicts, selection is unclear, or a generalization is load-bearing
  - a quantitative estimate, probability, deadline, forecast, or causal claim changes the move
  - the model may omit actors, options, mechanisms, constraints, or feedback
  - downside, irreversibility, opportunity cost, or update timing is material
do_not_use_when:
  - an authoritative source directly answers a low-stakes factual question
  - the task is mechanical and already decided
  - uncertainty cannot change the action and further analysis would only decorate the answer
  - casual language, jokes, vents, or brainstorming do not make a load-bearing claim
router_summary: Test the framing, evidence, causal story, model adequacy, precision, alternatives, and stopping point of consequential decisions.
decision_effect:
  - choose the right question and model before optimizing inside them
  - earn precision from evidence rather than hiding uncertainty in numbers
  - stop analysis when its expected decision value falls below its cost
implemented_by: []
lineage: LINEAGE.md
known_failures:
  - assertion quotas and arity theater
  - vacuous intervals that conceal rather than express uncertainty
  - hidden precision in point estimates and model outputs
  - representation sensitivity mistaken for substantive robustness
  - outcome bias when judging the prior decision
  - analysis that continues after it can no longer change the move
review_when:
  - a real application produces a materially worse decision than a simpler approach
  - repeated retrieval adds ceremony without changing the recommendation
  - an outcome exposes a missing actor, option, mechanism, constraint, or causal path
  - the same estimate class repeatedly misses in a directional way
last_material_revision: 2026-07-29
---

# Decision Quality Under Uncertainty

## Governing principle

> **Choose the right problem and model before optimizing inside them. Earn precision from evidence, keep uncertainty decision-relevant, and stop when more analysis is less valuable than acting and learning.**

This page is active guidance, not proof that every component has worked in the agent's prior cases. Use the confidence notes below.

## 1. Frame the decision

Before collecting more data, identify:

- the actual objective;
- the decision owner;
- the available options, including “do nothing,” delay, and reversible probes;
- hard constraints and standing policies;
- the time horizon;
- relevant actors and likely responses;
- what uncertainty can change the choice;
- what is outside scope;
- what outcome would count as success or failure.

Challenge the framing when it is load-bearing. Steelman the reasonable interpretation first. Reductio is useful only after charity and only when it clarifies the structure rather than winning a theatrical argument.

### Framing failure modes

- **Given-option lock:** treating the listed alternatives as exhaustive.
- **Proxy substitution:** optimizing the metric rather than the underlying objective.
- **Decision-owner blur:** solving for the agent's preference instead of the principal's choice.
- **Time-horizon mismatch:** a short-term win creates a larger later constraint.
- **False binary:** uncertainty or omitted options are hidden by two crisp choices.

## 2. Map evidence and provenance

Separate:

- verified source facts;
- the principal's explicit statements;
- model-derived estimates;
- the agent's interpretations;
- subjective forecasts;
- unknowns.

For a load-bearing generalization, record proportionally:

- sample size and composition;
- domain;
- selection process;
- evidence strength;
- known exceptions and failures;
- leading and competing hypotheses;
- what observation would distinguish them;
- last meaningful test.

Actively seek credible counterexamples and inconvenient evidence before defending the preferred conclusion. One domain-relevant counterexample can narrow a universal claim; it need not erase a bounded rule that explicitly excludes the case.

Do not formalize colloquial “all,” “never,” or “always” unless the quantifier actually carries the argument.

## 3. Causal hygiene

Association alone does not establish causation.

For a load-bearing causal claim, compare at least the plausible alternatives:

- proposed causal mechanism;
- reverse causation;
- common cause or confounding;
- selection effects;
- measurement artifact;
- regression to the mean;
- coincidence or temporal trend;
- intervention or policy response.

Ask what distinguishes them:

- temporal order;
- mechanism;
- dose-response or gradient;
- intervention evidence;
- natural experiment;
- negative control;
- counterfactual prediction;
- replication in a relevant population.

Match this burden to stakes. A reversible personal experiment does not require a journal article's identification strategy; a high-stakes health or financial claim deserves more than a plausible story.

## 4. Choose the model before the parameters

Distinguish:

- **parameter uncertainty:** the model is adequate but values are uncertain;
- **model uncertainty:** the variables, actors, options, causal structure, or objective may be wrong or incomplete.

When outcomes or observations do not fit, ask whether to update a parameter or revise the model itself.

### Model-admission questions

- What does the model omit?
- Are the relevant actors and options represented?
- Does the representation preserve what matters to the decision?
- Are preferences or constraints stable enough for the horizon?
- Can the model explain the observations it is being used to predict?
- What alternative model would recommend a different move?
- What observation would force a structural revision?

**Confidence: low for the Binmore-derived formulation.** It has not been evaluated in recorded agent applications. Use it as a disciplined question set, not a validated house theory.

## 5. Earn precision

Use point estimates only when their apparent precision is supported and useful. Otherwise give ranges, scenarios, or order-of-magnitude judgments tied to assumptions.

For load-bearing quantitative claims:

- use authoritative inputs;
- show formulas or executable calculations;
- separate observed values from assumptions;
- propagate material uncertainty;
- test sensitivity to assumptions that can change the decision;
- use relevant base rates or reference classes;
- state update conditions;
- record forecasts when later comparison will improve the model.

Numerical probability requires a basis: prior or reference class, assumptions, scope, and update condition. Do not call forecasts calibrated until recorded outcomes support that claim.

### Hidden precision

Hidden precision occurs when an exact-looking output conceals uncertain inputs, model choice, measurement error, or arbitrary representation.

Warning signs:

- many decimal places without decision value;
- a single deadline for a wide process distribution;
- one payoff table standing in for disputed values;
- a score whose weights were chosen after seeing the answer;
- uncertainty expressed only in prose after a crisp recommendation;
- “the model says” without the model's assumptions.

## 6. Keep uncertainty useful

An uncertainty range should separate decisions, not merely span everything conceivable.

### Vacuous intervals

An interval is vacuous when it is so broad that every outcome fits and no action changes. If honest uncertainty is genuinely that wide:

- say the model cannot discriminate;
- identify the assumption or measurement with the highest value of information;
- choose a robust or reversible action;
- or defer the precision claim.

Do not narrow the range cosmetically to look useful.

## 7. Avoid representation sensitivity

A conclusion is representation-sensitive when equivalent or similarly plausible descriptions produce materially different recommendations.

Test, when relevant:

- alternate baselines;
- absolute versus relative effects;
- time horizon;
- units and normalization;
- option ordering;
- payoff scale;
- framing as gain versus loss;
- inclusion or omission of outside options.

Sensitivity is information. It may show that the choice depends on a real value judgment. Do not average representations merely to manufacture stability.

## 8. Reject assertion quotas and arity theater

### Assertion quotas

Do not require a fixed number of claims, hypotheses, citations, scenarios, or counterexamples regardless of the problem. A quota rewards production of units rather than decision value.

Use enough distinct alternatives to expose the meaningful uncertainty—sometimes two, sometimes more, sometimes none because the source is decisive.

### Arity theater

Arity theater is forcing every problem into a predetermined number of options, actors, branches, or agents so the analysis looks complete.

Symptoms:

- three options where one is fake;
- multiple agents assigned overlapping work to satisfy a topology;
- a matrix whose empty cells are filled with weak distinctions;
- “diverge” continuing after materially distinct options are exhausted.

Generate materially different options, then stop.

## 9. Planning, reference classes, and buffers

Planning-fallacy awareness is scoped, not universal pessimism.

Use it when:

- the task resembles a class with known overruns;
- dependencies and handoffs are material;
- the estimate assumes uninterrupted work;
- uncertainty compounds across stages;
- lateness has a meaningful cost.

Then:

- select the most relevant reference class available;
- express a range rather than a ritual multiplier;
- identify critical-path dependencies;
- add a proportionate buffer;
- state assumptions and update triggers.

Do not assume every estimate is biased upward or downward in the same way. Direct current evidence can override a generic base rate.

## 10. Opportunity cost and sunk cost

Evaluate choices from this point forward.

- Compare the best alternative forgone, not just the direct benefits of the chosen path.
- Do not continue because of past investment of time, money, effort, or ego.
- Preserve prior investment only when it still changes future costs, capabilities, commitments, or options.
- Include attention and coordination cost, not only cash.

Name sunk cost when it is materially distorting the decision; do not use the phrase to dismiss legitimate switching costs or identity commitments.

## 11. Critical path and value of information

Identify the dependencies whose delay actually delays the outcome. Do not optimize decorative parallel work while the bottleneck waits.

Seek more information when it is likely to:

- change the option selected;
- change authorization or safety posture;
- prevent an expensive irreversible error;
- reveal a dominant constraint;
- or reduce uncertainty enough to permit a useful action.

Stop researching when:

- the same action is best across plausible scenarios;
- remaining uncertainty cannot be reduced proportionally;
- the decision is reversible and observation is cheaper than further analysis;
- the deadline or opportunity cost now dominates;
- additional detail only increases confidence theater.

**Confidence: low for the Baron-derived bounded-search formulation.** No recorded agent application establishes its local value. The stopping logic remains useful as bounded advisory guidance.

## 12. Robust action and close-the-loop

When uncertainty remains:

- prefer actions that perform acceptably across plausible models;
- preserve options;
- limit downside;
- expose useful feedback;
- define stop conditions;
- identify what observation will trigger an update.

For consequential uncertain decisions, record proportionally:

- choice;
- reasons;
- important assumptions;
- expected outcome or range;
- what success and failure would look like;
- review trigger or date when the result will become observable.

## 13. Judge the decision, not only the outcome

Outcome bias is evaluating the earlier choice solely by whether the realized result was good or bad.

When reviewing:

- reconstruct information available at decision time;
- compare the process to plausible alternatives;
- distinguish bad luck from a bad model;
- distinguish a good outcome from a justified decision;
- update both estimates and model structure when warranted.

Do not protect doctrine from a bad outcome by declaring every failure “variance.” A repeated directional miss is evidence.

## Stop conditions

Stop analysis and act, defer, or ask the principal when:

- further work cannot change the decision;
- available evidence cannot discriminate among models;
- a value judgment belongs to the principal;
- the required data would violate privacy or authorization;
- the deadline or opportunity cost dominates the expected information value;
- the recommendation is robust across plausible assumptions;
- or a small reversible probe will teach more cheaply than continued argument.
