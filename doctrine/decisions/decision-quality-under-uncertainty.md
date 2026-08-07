---
id: decision-quality-under-uncertainty
type: doctrine
title: Decision Quality Under Uncertainty
status: active
authority: advisory
confidence: mixed
confidence_basis:
  - Basic source, causal, base-rate, sensitivity, and uncertainty hygiene has broad methodological support.
  - Formal-inference boundaries reflect standard distinctions among representation, validity, soundness, and countermodels; adopters should validate any executable procedure separately.
  - Baron-derived bounded-search guidance has low confidence and no recorded agent application.
  - Binmore-derived model-adequacy guidance has low confidence and no recorded agent application.
  - The situational-awareness failure taxonomy is an operational extrapolation; adopters should judge it by changed decisions or repairs rather than conceptual neatness.
  - Control-loop timing guidance is a bounded qualitative transfer; it is not calibrated control design and has no established agent-effectiveness evidence.
  - Value-sensitive comparison guidance is a bounded operational synthesis of contested theories. It does not establish a universal value theory or a master value.
  - Representation-adequacy guidance is a bounded operational transfer from information theory; its application to agent context and handoffs is advisory and has no established agent-effectiveness evidence.
  - Local value must be judged by whether the page changes consequential decisions without adding disproportionate ceremony.
scope:
  - consequential decisions with uncertain framing, evidence, models, estimates, causal claims, or tradeoffs
consult_when:
  - the framing, option set, contested values, preference or consent interpretation, aggregation, or objective proxy may determine the recommendation
  - evidence conflicts, selection is unclear, or a generalization is load-bearing
  - a quantitative estimate, probability, deadline, forecast, causal claim, or consequential compression choice changes the move
  - the model may omit actors, options, mechanisms, constraints, or feedback
  - current state may change during the task, several observations must be integrated, or a near-future projection materially determines the move
  - recurring observation, retry, or correction can act again before a prior effect becomes observable
  - downside, irreversibility, opportunity cost, or update timing is material
  - an argument's validity depends on representation, quantifiers, identity, relation direction, scoped assumptions, or multi-step derivation
  - recurring predictions permit comparison between a bounded model or context and a materially stronger baseline
do_not_use_when:
  - an authoritative source directly answers a low-stakes factual question
  - the task is mechanical and already decided
  - uncertainty cannot change the action and further analysis would only decorate the answer
  - a current authoritative source resolves the relevant state and further situation modeling cannot alter the authorized action
  - casual language, jokes, vents, or brainstorming do not make a load-bearing claim
  - formalizing the claim cannot change the decision or would erase causal, temporal, probabilistic, normative, or authorization-relevant structure
  - the choice is routine, low-stakes, mechanically settled, or a richer value audit cannot change the move
  - the representation is routine, one-shot, reversible, and no plausible omitted distinction could change the action
  - no real probabilities, comparable outcomes, or meaningful predictive-loss measure exist
router_summary: Test framing, values, preference authority, evidence, inference, causal stories, models, alternatives, and stopping points in consequential decisions.
decision_effect:
  - choose the right question and model before optimizing inside them
  - earn precision from evidence rather than hiding uncertainty in numbers
  - stop analysis when its expected decision value falls below its cost
  - separate representation, derivation, premise truth, causal support, decision support, and authority rather than allowing one layer to launder another
  - preserve task-relevant distinctions through compression and test recurring context or model mismatch against a declared stronger baseline
implemented_by: []
lineage: LINEAGE.md
known_failures:
  - assertion quotas and arity theater
  - vacuous intervals that conceal rather than express uncertainty
  - hidden precision in point estimates and model outputs
  - representation sensitivity mistaken for substantive robustness
  - outcome bias when judging the prior decision
  - mistaking information volume, confidence, fluent explanation, or a successful outcome for situational understanding
  - checklist theater that names awareness stages without changing observation, projection, action, or repair
  - analysis that continues after it can no longer change the move
  - proving a nearby proposition after a lossy translation of the actual claim
  - treating failed or bounded proof search as invalidity, or formal validity as premise truth, causation, decision quality, or authority
  - treating fluent reconstruction, compression ratio, retrieval similarity, confidence, or information quantity as proof that a representation preserved what mattered
review_when:
  - a real application produces a materially worse decision than a simpler approach
  - repeated retrieval adds ceremony without changing the recommendation
  - an outcome exposes a missing actor, option, mechanism, constraint, or causal path
  - perception, comprehension, and projection failures cannot be distinguished reliably enough to prescribe different repairs
  - control-loop timing repeatedly delays necessary intervention, fails to prevent duplicate correction, or adds ceremony without changing execution or repair
  - the same estimate class repeatedly misses in a directional way
  - formal-inference auditing repeatedly adds ceremony without catching a material representation, scope, witness, assumption, or search-status error
  - value-sensitive auditing repeatedly renames obvious tradeoffs without changing a decision, clarification, safeguard, abstention, or conflict record
  - representation-adequacy checks repeatedly add context or ceremony without changing a consequential conclusion, verification result, or repair
last_material_revision: 2026-08-07
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

Trace the means–ends chain when the proposed action is not obviously tied to the objective: action → immediate output → intermediate capability or behavior → desired outcome. Name the weakest link and do not optimize a means after it has stopped serving the end.

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

Also label the claim mode when confusion would change the decision:

- **descriptive:** what is or was true;
- **interpretive:** what the evidence means;
- **forecast:** what is expected to happen;
- **normative or prescriptive:** what should matter or what should be done.

Record material evidence processing—not only the final citation. Distinguish direct observation from extraction, transformation, filtering, summarization, model output, and inference; preserve enough provenance to reproduce or challenge the load-bearing step. Treat directional evidence, disconfirming evidence, ambiguous evidence, and absence of evidence differently rather than collapsing them into one confidence label.

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

## Formal-inference boundaries

Use a formal-inference audit only when an argument's structure is load-bearing. Its first job is not to prove the conclusion but to preserve the proposition being evaluated.

Keep six statuses separate:

1. **Representation fidelity:** the formal or normalized claim preserves the original domain, time, unit, quantifiers, identity, relation direction, modality, grouping, and relevant open conditions.
2. **Derivational validity:** the exact conclusion follows under the declared assumptions, semantics, and formal system.
3. **Premise support:** the premises are current and warranted for the represented world rather than merely available to a proof.
4. **Causal support:** the evidence supports causal dependence rather than material implication, sequence, or association alone.
5. **Decision support:** objectives, alternatives, tradeoffs, uncertainty, downside, reversibility, and opportunity cost support the move.
6. **Authority and values:** the decision owner is authorized to choose, disclose, commit, and set any normative premise.

No layer silently licenses the next. Validity cannot manufacture true premises; true premises plus a valid derivation do not by themselves establish causation, a wise decision, authorization, or legitimacy.

Before deriving, preserve the exact conclusion and reverse-render any formalization into ordinary language. Reject the representation when it erases load-bearing causal, counterfactual, temporal, epistemic, deontic, probabilistic, vague, or normative structure. Make hidden bridge premises visible. A restatement or presupposition of the conclusion is not independent warrant.

Scope temporary assumptions and every dependent claim. A result derived only within a hypothetical frame remains conditional unless a valid discharge rule licenses its exported form. Give each existential claim a fresh witness; do not merge witnesses, identify them with named entities, count them as distinct, or generalize from them without explicit identity, inequality, or dependency evidence. Preserve quantifier order and relation direction.

Label transformations as alpha-renaming, equivalence under named semantics, identity substitution, definitional expansion, one-way entailment, defeasible paraphrase, or operational summary. Only a transformation whose type licenses substitution may replace a claim inside a derivation.

Categorical formal results require receipts. A validity claim needs a derivation certificate; invalidity needs a countermodel that makes every premise true and the exact conclusion false. Classify search as exhaustive for a declared finite space, bounded model search, heuristic proof search, resource-limited, nonterminated, or not applicable. Failure to find a proof is not invalidity; failure to find a countermodel within a bound is not unrestricted validity.

Before using reductio, check whether the original premises are already inconsistent. If they are, report `vacuously valid — premise set inconsistent` and localize the conflict rather than treating contradiction as independent support or permitting arbitrary world claims.

An adopter may implement these controls as a bounded skill or checklist. The implementation must not expand the doctrine boundaries or trigger on routine, low-stakes, mechanically settled work.

## Value-sensitive decision boundary

Use this boundary only when a consequential, contested, multi-party, preference-sensitive, or high-uncertainty choice depends on what matters, whose standpoint counts, whether expressed preference is authoritative, or whether unlike values can be compared. Routine tasks stay lightweight.

Type only claims that could change the choice. Distinguish descriptive, evaluative, reason-giving, deontic, and authorization claims; intrinsic, instrumental, constitutive, final, or unresolved value roles; and personal, relational, role-relative, moral, impartial, or unresolved standpoints. Goodness is not automatically a reason, and a reason is not automatically permission, obligation, prohibition, consent, or authority.

Prediction, representation, explanation, justification, legitimacy, and authority are different relations. A model may predict or reproduce a judgment without explaining it; an explanation need not justify it; a justification does not by itself establish legitimacy or authority to act. Keep these statuses explicit when collapsing them could change the move.

Preference evidence is not self-interpreting. When material, label a preference as actual, informed, hypothetical, adaptive, manipulated, coerced, constrained, or unresolved. Treat coercion, strategic expression, politeness, resignation, misinformation, and constrained options as investigation signals—not automatic grounds to dismiss the person's expressed preference or override them. Do not infer consent, merit, welfare, or authority from agreement, satisfaction, silence, or predicted choice alone.

Before counting reasons, trace each through underlying facts, causal consequences, and evaluative classifications. Do not count paraphrases of one consequence as independent reasons. Preserve temporal order when a reason's force changes over time or depends on an earlier condition.

Use numerical comparison only for a bounded, explicit decision. Disclose the comparison basis, weights, normalization, aggregation rule, time horizon, authority to choose them, distribution of benefits and burdens, and material omissions. A score does not prove commensurability or legitimacy. Never invent a zero baseline, person, preference, consent state, or evidential fact to complete the model.

Return one narrow comparison status when it matters: `compared under declared assumptions`; `partially ordered`; `incommensurable on the current basis`; `insufficient authority`; `insufficient evidence`; `deferred — value of information exceeds delay cost`; or `abstain — unresolved legitimacy or rights constraint`. Uncertainty need not force abstention, and abstention is not a substitute for preserving authorized reversible options.

After a consequential selection, preserve what the selected option outweighs, brackets, or sacrifices; who bears that loss; and whether it is temporary, conditional, revisitable, or irreversible. Record conflict without implying that one choice erased the rejected value.

This boundary does not adopt pleasure, desire satisfaction, welfare, money, health, relationships, security, autonomy, equality, freedom, nature, existence, aggregation, or any other candidate as a universal master value. It does not require a universal ontology, one numerical score, or philosophy ceremony for ordinary work.

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

Keep three registers separate when values could contaminate prediction:

1. **Feasibility:** what actions or outcomes are actually possible under the constraints.
2. **Belief or forecast:** what is likely, with assumptions and evidence.
3. **Preference or objective:** what the principal values or chooses among feasible outcomes.

Desirability is not evidence that an outcome is likely, and an unattractive forecast is not invalid merely because it is inconvenient.

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

For a range-based recommendation, state the decision threshold and which segment of the range changes the action. If no plausible value crosses a threshold, additional precision has no immediate decision value.

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

### Representation adequacy and information loss

Treat a consequential summary, context packet, handoff, memory representation, or model input as task-conditioned rather than generally sufficient. Before compressing, name the downstream task and decision owner; the distinctions whose loss could change a decision, verification result, authority assessment, causal interpretation, numerical result, or safety boundary; the canonical sources, citations, retrieval handles, evidence artifacts, and tools expected to remain available; and the acceptable loss boundary.

Evaluate the compact representation together with that reconstruction support. Prefer a compact decision layer linked to recoverable evidence over repeated truncation of one narrative. A representation adequate for one task may be inadequate for another.

For consequential recurring tasks, compare the bounded representation against a materially expanded or retrieval-enabled context when the difference can be checked. Preserve or retrieve additional context when it changes a consequential conclusion, materially improves a declared decision-relevant measure, or exposes a recurring omission. Otherwise retain the smaller representation. Do not impose this trial on routine one-shot work, assume stationarity or independence, or discard rare decisive evidence merely because it is atypical.

When recurring probabilistic predictions have real probabilities and comparable outcomes, retain the model or method version, forecast basis, selected predictive-loss measure, and baseline. Sustained excess loss is evidence to inspect model mismatch, dependence, selection, sample size, or regime change—not permission to keep tuning parameters inside an inadequate model.

Information quantity, entropy, surprise, compression ratio, similarity, predictive confidence, and KL divergence do not establish truth, meaning, relevance, causation, value, legitimacy, permission, obligation, prohibition, or authority. A sufficient statistic is sufficient only for its named model, parameter, and task. Do not fabricate probabilities to enable a metric or describe people as deficient channels.

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

### Situational understanding in dynamic work

When relevant state can change during analysis or execution, separate three layers of situational understanding:

1. **Perception:** establish relevant current state from live, appropriately authoritative observations.
2. **Comprehension:** integrate those observations relative to the objective, decision owner, constraints, actors, dependencies, and feedback loops.
3. **Projection:** identify material state transitions, responses, and near-future possibilities that could change the decision.

Information volume is not situational understanding. More observations can reduce decision quality when they are stale, redundant, correlated, unauthoritative, irrelevant, invasive, or too costly to obtain. Allocate observation and reasoning effort according to consequence, volatility, uncertainty, authority, and expected decision value.

For consequential dynamic actions, preserve proportionally the objective and owner, material verified and unobserved state, interpretation, load-bearing projection, expected result, disconfirming signal, authorization boundary, and feedback path. This is a checkpoint, not a mandatory visible recital. Skip it when live authoritative state directly resolves a low-stakes question or more modeling cannot change the authorized move.

### Diagnose the earliest failed layer

After a material surprise or failure, distinguish:

- **Perception failure:** relevant state was missed, stale, or drawn from the wrong source.
- **Comprehension failure:** facts were observed but their relationships or significance were misunderstood.
- **Projection failure:** present state was understood but its development was forecast poorly.
- **Decision failure:** the situation model was adequate but the chosen action poorly fit the objective, authority, tradeoffs, or downside.
- **Execution failure:** the decision was sound but implementation, sequencing, tooling, or verification failed.
- **Feedback failure:** action occurred but its effects were not observed or incorporated.

Classify the earliest load-bearing failure supported by evidence rather than the most visible final symptom. Multiple layers may fail; preserve ambiguity when the evidence cannot distinguish them. Do not infer sound understanding from confidence, fluent explanation, process completion, or outcome alone.

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

### Time feedback to the system

For a recurring monitor, retry, or corrective loop whose repeated action can create cost or instability, distinguish the process-change timescale, observation interval, evidence window, action-to-observable-effect delay, settling condition, cooldown, duplicate-action suppression, maximum correction size, and oscillation stop condition.

Do not launch another corrective cycle merely because the desired result is not yet visible. First ask whether the prior action has had enough time to propagate. Intervene earlier when a new material hazard appears; otherwise wait for the declared observation window rather than manufacturing failure from stale state.

This is consequence-gated control hygiene, not a requirement to model every workflow as a physical controller. Skip it for one-shot actions, harmless read-only checks, and loops whose cadence cannot alter decisions, side effects, notifications, or resource use.

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
