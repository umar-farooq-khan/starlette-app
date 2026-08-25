# How A2A, google-adk, and Starlette relate

From a conversation about the Antenna Lookup project's `agent-service`
(`E:\Personal Projects\Antenna-Lookup\agent-service\a2a_server.py`).

Not the protocol itself — the library, `google-adk`.

`to_a2a()` is a function from `google.adk.a2a.utils.agent_to_a2a`. You pass it
your agent, and it returns a ready-to-run ASGI app that already implements the
A2A protocol's HTTP routes (agent card endpoint, message-send endpoint, etc.) —
internally built with Starlette.

So the layering is:

- **A2A protocol** = a spec (what routes must exist, what JSON shapes go over
  the wire). Not code.
- **google-adk** = a library that implements that spec for you, as a function
  returning an app object.
- **Starlette** = what that returned app object happens to be built on, under
  the hood.

You never write `Route("/a2a/send", ...)` yourself. ADK already did it inside
`to_a2a`. In `a2a_server.py`, line 70 is the whole thing:

```python
_a2a_app = to_a2a(root_agent, host=A2A_HOST, port=A2A_PORT, runner=runner)
```

That's why swapping Starlette for FastAPI isn't something you can do in that
repo's own code — the app object already exists, built by ADK, before you ever
touch it. You only wrap it (`FlushTracesMiddleware`).
