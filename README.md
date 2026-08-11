# AEW E2E FastAPI Template

A small but realistic FastAPI product used to validate Agentic Engineering
Workflows (AEW) in a consumer repository. It intentionally owns `docs/`,
`specs/`, and repository instructions so installation and update tests can prove
that AEW does not overwrite product content.

## Run locally

```bash
python -m venv .venv
. .venv/bin/activate
pip install -e '.[test]'
pytest
uvicorn task_api.main:app --reload
```

Open <http://127.0.0.1:8000/docs> for the generated API documentation.

## Use as an AEW live-test repository

1. Select **Use this template** on GitHub and create a disposable repository
   under your own account.
2. Create an issue using
   [`fixtures/issues/001-task-search.md`](fixtures/issues/001-task-search.md).
3. Install the AEW `.agents/` payload into the disposable repository.
4. Invoke `@.agents/commands/gl-issue-to-pr.md` or the registered `/gl-issue-to-pr` command
   with the issue URL.
5. Review the spec PR, request changes or approve it, then resume `/gl-issue-to-pr`.
6. Verify the implementation PR and run `pytest`.

Do not run destructive E2E experiments directly against this template. Create
a repository from it first.
