# Task API Product Contract

The service provides a small in-memory task API for deterministic E2E testing.

## Current behavior

- Create a task with a non-empty title.
- List all tasks or filter by completion state.
- Update a task's completion state.
- Return `404` when updating a missing task.

Product specifications in this directory belong to the consumer repository and
must survive AEW installation and synchronization.
