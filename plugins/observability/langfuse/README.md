# Langfuse Observability Plugin

This plugin ships bundled with Doppel but is **opt-in** — it only loads when
you explicitly enable it.

## Enable

```bash
pip install langfuse
doppel plugins enable observability/langfuse
```

Or check the box in the interactive `doppel plugins` UI.

## Required credentials

Set these in `~/.doppel/.env`:

```bash
DOPPEL_LANGFUSE_PUBLIC_KEY=pk-lf-...
DOPPEL_LANGFUSE_SECRET_KEY=sk-lf-...
DOPPEL_LANGFUSE_BASE_URL=https://cloud.langfuse.com   # or your self-hosted URL
```

Without the SDK or credentials the hooks no-op silently — the plugin fails
open.

Legacy `HERMES_LANGFUSE_*` and bare `LANGFUSE_*` env vars still work, but the
Doppel-prefixed names are preferred when more than one value is set.

## Verify

```bash
doppel plugins list                 # observability/langfuse should show "enabled"
doppel chat -q "hello"              # then check Langfuse for a "Doppel turn" trace
```

## Optional tuning

```bash
DOPPEL_LANGFUSE_ENV=production       # environment tag
DOPPEL_LANGFUSE_RELEASE=v1.0.0       # release tag
DOPPEL_LANGFUSE_SAMPLE_RATE=0.5      # sample 50% of traces
DOPPEL_LANGFUSE_MAX_CHARS=12000      # max chars per field (default: 12000)
DOPPEL_LANGFUSE_DEBUG=true           # verbose plugin logging
```

## Disable

```bash
doppel plugins disable observability/langfuse
```
