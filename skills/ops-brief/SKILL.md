---
name: ops-brief
description: Answer "where is marketing stuck today?" for a founder or lead - read the newest reports, queues, approval items and run logs, classify every blocker (system failure, waiting for a decision, waiting for data, held by policy, ready to do locally), and turn many open inputs into three to six ranked actions with where to act, how, what it unlocks and what stays blocked. Use for a daily marketing status, unblock list, approval queue triage, or audit of automated marketing workflows.
---

# Ops brief

A short daily answer to two questions: what is blocked and why, and which few decisions would unblock the most. It replaces a long system report with a ranked to-do list for the person who decides.

## When to use

- Daily or weekly status of a marketing operation, especially one with automated jobs.
- Many open approvals and inputs, and the decider needs to know which first.
- Something "should have run" and did not.

## Inputs

- Profile: `approvals` (who decides what), `channels.active`.
- The newest reports, queues, approval items, logs and state files of your marketing workflows. Read the current date first; current files beat memory; if files disagree, use the newest coherent set and call the rest stale.

## Process

1. **Collect open items** from reports, queues and logs.
2. **Classify each blocker:**
   | Class | Means |
   |---|---|
   | System failure | A job, integration or script broke |
   | Waiting for a decision | A specific approval or choice from a role |
   | Waiting for data | An input, export or fact is missing |
   | Held by policy | Blocked on purpose by a gate (no send, no publish) |
   | Ready locally | Can be done now without anyone else |
3. **Rank by unlock impact:** decisions that unblock several lanes first; then send-safety gates (suppression, mailbox, list and copy approvals); then content facts (sources, CTA, claim boundary); then data source decisions; then vendor or spend approvals; long-term policy changes last. Ties go to whatever the decider can finish fastest.
4. **Write each action specifically:** where to act (the file, view or tool), how (exact field and value), what it unlocks, and what still stays blocked afterwards. Approvals asked for are specific ("approve these facts for a draft"), never blanket ("let the agent send").
5. **Collapse the rest** into categories; list one to three items not worth handling today.

## Output

```markdown
## Verdict (one sentence)
## Do these first
1. {action} - where / how / unlocks / still blocked
...(3-6)
## Not today (1-3, and why)
## System hygiene (failures and stale artifacts)
## Priority call (one line)
```

## Gates

- This skill reports and recommends. It does not fill decision files, mark approvals as given, or execute anything ([approval-gates](../b2b-growth-kit/policies/approval-gates.md)).
- Status claims cite the file and timestamp they came from; anything unverified is labelled ([evidence-and-claims](../b2b-growth-kit/policies/evidence-and-claims.md)).

## References

- Planning context: [growth-plan](../growth-plan/SKILL.md) · Send gates: [send-preflight](../send-preflight/SKILL.md)
