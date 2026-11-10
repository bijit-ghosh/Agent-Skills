---
name: software-factory-interfaces
description: "Design or validate API and user-interface boundaries, including compatibility, accessibility, browser behavior, and failure states."
---

# Software Factory Interfaces

Validate what a caller or user can observe, including failure and recovery.

## Workflow

1. Identify consumers, supported versions/devices, existing design conventions, and the interaction contract. Preserve established patterns unless the requested change requires a break.
2. For APIs, define input validation, authorization, error semantics, pagination, ordering, idempotency, and compatibility as applicable. Derive a contract test from a real consumer path rather than only server internals.
3. For UI, cover loading, empty, success, invalid input, partial failure, and retry states relevant to the task. Preserve entered data through recoverable failures and provide an actionable error.
4. Verify keyboard navigation, focus movement, labels, status announcements, and contrast with appropriate tools. Semantic HTML and automated checks do not replace a relevant keyboard/browser check.
5. Exercise the real integration in an available browser or client with representative viewport/data states. Inspect console/network errors. Use synthetic data and do not submit an external transaction unless it is in the authorized scope.
6. Report which browser/API paths were actually exercised, their build identity, and any accessibility or compatibility checks left untested.

## Deliverable

The interface change or contract, exercised consumer paths, and evidence of observable behavior. Screenshots support visual review but do not prove interactive correctness.

