---
name: software-factory-operations
description: "Investigate runtime incidents and improve observability around software-factory outcomes, retries, reconciliation, and recovery."
---

# Software Factory Operations

Use telemetry to distinguish a failed action from an unknown outcome.

## Workflow

1. Establish the affected outcome, time window, deployment/config identity, and impact. Separate observed evidence from suspected cause.
2. Correlate request, workflow, tool, and durable-effect IDs. Examine retries, queue state, partial completion, cancellation, and external service acknowledgments where relevant.
3. Contain ongoing harm using authorized reversible controls. Before replaying a job or retrying a write, check the authoritative durable state and idempotency record.
4. Add telemetry at decision boundaries: intent, authorization result, attempt ID, observed effect, reconciliation status, and terminal outcome. Avoid credentials and unnecessary personal data; define retention and sampling.
5. Test the recovery path in an appropriate environment. Validate both restored service and absence of duplicate or unauthorized effects.
6. Convert the demonstrated failure into a regression fixture, alert with an actionable condition, and a concise recovery note. Track impact and unresolved risk without claiming root cause from correlation alone.

## Deliverable

An evidence-backed incident timeline, verified recovery state, and targeted prevention changes. Alerts should indicate an actionable outcome or invariant violation.

