# Add case-insensitive task search

## Problem

`GET /tasks` can filter by completion state but cannot search task titles.

## Requested behavior

Add an optional `q` query parameter to `GET /tasks`.

## Acceptance criteria

- Matching is case-insensitive.
- A task matches when `q` appears anywhere in its title.
- Leading and trailing whitespace in `q` is ignored.
- An omitted or blank `q` preserves the current list behavior.
- `q` composes with the existing `completed` filter.
- Tests cover matching, no matches, blank search, and combined filters.
- Existing API behavior remains backward compatible.

## Validation

```bash
pytest
```
