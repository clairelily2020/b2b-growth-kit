---
name: send-preflight
description: Gate any outbound send (cold email batch, LinkedIn connections or messages, partner or creator outreach, newsletter to a cold list) with a pass/fail checklist - mailbox and domain readiness, authentication, warm-up, caps, suppression, copy and list approval, rendered preview and final decision - and report exactly what blocks sending. Use before launching or resuming outreach, when auditing why an outbound engine sent nothing, or to produce a no-send approval pack.
---

# Send preflight

The last check before anything reaches a stranger's inbox. It produces one of three answers: ready for the approver's decision, blocked (with the exact blockers), or waiting on someone.

## When to use

- Before the first send of any sequence or batch, and before resuming a paused one.
- When an outbound process sent fewer messages than planned and someone asks why.
- To prepare an approval pack for the person who signs off sends.

## Inputs

- Profile: `outreach` (domains, caps, suppression source), `approvals.send`, `voice.personas`.
- The batch: list file, copy version, sending tool, sender accounts.
- The newest reports, logs and state files from the sending tool. Current files win over memory; if files disagree, use the newest coherent set and label the rest stale.

## Process

Check each gate and record pass, fail or unknown. Unknown counts as fail.

| Gate | Pass means |
|---|---|
| Sender inventory | The mailboxes or accounts exist, belong to the sending domain, and match the persona |
| Authentication | SPF, DKIM and DMARC pass for each sending domain |
| Warm-up | Inboxes finished warm-up; health scores are acceptable in the tool |
| Caps | Planned volume per inbox and per domain is within the profile caps |
| Domain health | Recent bounce rate under 3%, complaints under 0.1%, no blocklist listing |
| Suppression | Every row checked against do-not-contact, unsubscribes, bounces, customers in active deals, competitors |
| List approval | The exact list (file or batch ID) is approved |
| Copy approval | The exact copy version is approved; merge fields fill for every row |
| Rendered preview | The sending tool's preview shows paragraphs, lists, links and signature as approved |
| Compliance | Opt-out present; identity and address requirements of the recipient's region met |
| Final decision | The `approvals.send` role made an explicit send decision for this batch |

For an audit of a process that sent too little: count rows per blocker category from the newest batch files, and report the categories with counts rather than a single guess.

## Output

```markdown
Batch / tool / senders / planned volume
| Gate | Status | Evidence (file, setting, screenshot) | Fix |
Status: ready for decision / blocked / waiting on {role}
Blocker counts (for audits)
Smallest next action
```

## Gates

- This skill never sends, connects, uploads or activates anything. It reports.
- One failing or unknown gate means not ready; partial readiness is never described as ready. Rules from [outreach-compliance](../b2b-growth-kit/policies/outreach-compliance.md) and [approval-gates](../b2b-growth-kit/policies/approval-gates.md).

## References

- Copy and sequences: [cold-email](../cold-email/SKILL.md), [linkedin-outbound](../linkedin-outbound/SKILL.md)
