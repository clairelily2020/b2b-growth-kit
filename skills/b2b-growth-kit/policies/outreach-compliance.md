# Outreach compliance

Applies to cold email, LinkedIn connection requests and messages, DMs on any platform, and partner or creator outreach. Sending also requires approval under [approval-gates.md](approval-gates.md).

## Before anyone is contacted

1. **Suppression first.** Check the profile's `outreach.suppression_source` (do-not-contact flags, unsubscribes, bounces, existing customers in an active deal, competitors). Unknown suppression status is a fail, not a pass.
2. **Lawful basis.** Follow the rules of the recipient's region (for example CAN-SPAM, GDPR/PECR, CASL). Business email to a role relevant to the offer is the minimum; personal email addresses are excluded.
3. **No scraped private data.** Use public professional information only. Do not buy or enrich lists from sources whose terms forbid it.
4. **Real sender.** Messages come from a real person or the company, using a persona from the profile. No fake identities, no pretending to be a customer or a peer.

## Email deliverability

- Send from the profile's `outreach.sending_domains`, not the main corporate domain.
- SPF, DKIM and DMARC pass on the sending domain before the first send.
- New inboxes warm up before cold volume; respect `outreach.daily_cap_email_per_inbox`.
- Every message has a working opt-out and a physical or company identifier where the law requires it.
- Stop a domain when bounce rate exceeds 3% or spam complaints exceed 0.1%, and investigate before resuming.
- Check the rendered preview in the actual sending tool. Line breaks, merge fields and links must look right there, not only in the draft.

## LinkedIn and other platforms

- Respect the platform's terms and the profile's daily caps. Automation that violates platform terms is out of scope.
- Space actions out; no bursts.
- A connection request is not consent to a sales sequence. Earn the reply first.

## Message content

- One clear reason for reaching out that is specific to the recipient, and checkable.
- No false urgency, fake "Re:" or "Fwd:" subjects, or implied prior relationship.
- Claims follow [evidence-and-claims.md](evidence-and-claims.md).
- Stop the sequence on any reply, including a negative one. A "not interested" ends outreach to that person.

## Records

Log who was contacted, when, through which channel, with which version, and the outcome. This log is what makes suppression work next time.
