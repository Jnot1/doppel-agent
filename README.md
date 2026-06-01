<p align="center">
  <img src="assets/banner.png" alt="Doppel Agent" width="100%">
</p>

# Doppel Agent ☤

<p align="center">
  <a href="website/docs/index.mdx"><img src="https://img.shields.io/badge/Docs-Doppel%20Agent-FFD700?style=for-the-badge" alt="Documentation"></a>
  <a href="https://github.com/Jnot1/doppel-agent"><img src="https://img.shields.io/badge/GitHub-Jnot1%2Fdoppel--agent-111827?style=for-the-badge&logo=github" alt="GitHub repository"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" alt="License: MIT"></a>
  <a href="NOTICE.md"><img src="https://img.shields.io/badge/Notice-Upstream%20notice-blue?style=for-the-badge" alt="Upstream notice"></a>
  <a href="README.zh-CN.md"><img src="https://img.shields.io/badge/Lang-中文-red?style=for-the-badge" alt="中文"></a>
</p>

**Doppel Agent is Your Everyday Personal AI Assistant.** Maintained by Doppelme for everyday life assistance and serious technical work. Original upstream attribution is preserved in [NOTICE.md]. Use it for email triage, calendar organization, grocery planning, to-do management, personal training support, cooking help, and deep multi-step workflows that benefit from memory, tools, and automation.

Use any model you want — [Nous Portal](https://portal.nousresearch.com), [OpenRouter](https://openrouter.ai) (200+ models), [NovitaAI](https://novita.ai) (AI-native cloud for Model API, Agent Sandbox, and GPU Cloud), [NVIDIA NIM](https://build.nvidia.com) (Nemotron), [Xiaomi MiMo](https://platform.xiaomimimo.com), [z.ai/GLM](https://z.ai), [Kimi/Moonshot](https://platform.moonshot.ai), [MiniMax](https://www.minimax.io), [Hugging Face](https://huggingface.co), OpenAI, or your own endpoint. Switch with `doppel model` — no code changes, no lock-in. Legacy compatibility aliases remain available during the transition.

<table>
<tr><td><b>A real terminal interface</b></td><td>Full TUI with multiline editing, slash-command autocomplete, conversation history, interrupt-and-redirect, and streaming tool output.</td></tr>
<tr><td><b>Lives where you do</b></td><td>Telegram, Discord, Slack, WhatsApp, Signal, and CLI — all from a single gateway process. Voice memo transcription, cross-platform conversation continuity.</td></tr>
<tr><td><b>A closed learning loop</b></td><td>Agent-curated memory with periodic nudges. Autonomous skill creation after complex tasks. Skills self-improve during use. FTS5 session search with LLM summarization for cross-session recall. <a href="https://github.com/plastic-labs/honcho">Honcho</a> dialectic user modeling. Compatible with the <a href="https://agentskills.io">agentskills.io</a> open standard.</td></tr>
<tr><td><b>Scheduled automations</b></td><td>Built-in cron scheduler with delivery to any platform. Daily reports, nightly backups, weekly audits — all in natural language, running unattended.</td></tr>
<tr><td><b>Delegates and parallelizes</b></td><td>Spawn isolated subagents for parallel workstreams. Write Python scripts that call tools via RPC, collapsing multi-step pipelines into zero-context-cost turns.</td></tr>
<tr><td><b>Runs anywhere, not just your laptop</b></td><td>Six terminal backends — local, Docker, SSH, Singularity, Modal, and Daytona. Daytona and Modal offer serverless persistence — your agent's environment hibernates when idle and wakes on demand, costing nearly nothing between sessions. Run it on a $5 VPS or a GPU cluster.</td></tr>
<tr><td><b>Research-ready</b></td><td>Batch trajectory generation, trajectory compression for training the next generation of tool-calling models.</td></tr>
</table>

---

## Quick Install

### Linux, macOS, WSL2, Termux

```bash
curl -fsSL https://raw.githubusercontent.com/Jnot1/doppel-agent/main/scripts/install.sh | bash
```

### Windows (native, PowerShell) — Early Beta

> **Heads up:** Native Windows support is **early beta**. It installs and runs, but hasn't been road-tested as broadly as our Linux/macOS/WSL2 paths. Please [file issues](https://github.com/Jnot1/doppel-agent/issues) when you hit rough edges. For the most battle-tested Windows setup today, run the Linux/macOS one-liner above inside **WSL2**.

Run this in PowerShell:

```powershell
iex (irm https://raw.githubusercontent.com/Jnot1/doppel-agent/main/scripts/install.ps1)
```

The installer handles everything: uv, Python 3.11, Node.js, ripgrep, ffmpeg, **and a portable Git Bash** (MinGit, unpacked to `%LOCALAPPDATA%\doppel\git` — no admin required, completely isolated from any system Git install). Doppel uses this bundled Git Bash to run shell commands.

If you already have Git installed, the installer detects it and uses that instead.  Otherwise a ~45MB MinGit download is all you need — it won't touch or interfere with any system Git.

> **Android / Termux:** The tested manual path is documented in the [Termux guide](website/docs/getting-started/termux.md). On Termux, Doppel installs a curated `.[termux]` extra because the full `.[all]` extra currently pulls Android-incompatible voice dependencies.
>
> **Windows:** Native Windows is supported as an **early beta** — the PowerShell one-liner above installs everything, but expect rough edges and please file issues when you hit them. If you'd rather use WSL2 (our most battle-tested Windows path), the Linux command works there too. Native Windows installs default to `%LOCALAPPDATA%\doppel`; WSL2 installs default to `~/.doppel`. The legacy `HERMES_HOME` path is still honored for compatibility. The only Doppel feature that currently needs WSL2 specifically is the browser-based dashboard chat pane (it uses a POSIX PTY — classic CLI and gateway both run natively).

After installation:

```bash
source ~/.bashrc    # reload shell (or: source ~/.zshrc)
doppel              # start chatting!
```

---

## Getting Started

```bash
doppel              # Interactive CLI — start a conversation
doppel model        # Choose your LLM provider and model
doppel tools        # Configure which tools are enabled
doppel config set   # Set individual config values
doppel gateway      # Start the messaging gateway (Telegram, Discord, etc.)
doppel setup        # Run the full setup wizard (configures everything at once)
doppel claw migrate # Migrate from OpenClaw (if coming from OpenClaw)
doppel update       # Update to the latest version
doppel doctor       # Diagnose any issues
```

📖 **[Documentation in this repo →](website/docs/index.mdx)**

---

## Skip the API-key collection — Nous Portal

Doppel Agent works with whatever provider you want — that's not changing. But if you'd rather not collect five separate API keys for the model, web search, image generation, TTS, and a cloud browser, **[Nous Portal](https://portal.nousresearch.com)** covers all of them under one subscription:

- **300+ models** — pick any of them with `/model <name>`
- **Tool Gateway** — web search (Firecrawl), image generation (FAL), text-to-speech (OpenAI), cloud browser (Browser Use), all routed through your sub. No extra accounts.

One command from a fresh install:

```bash
doppel setup --portal
```

That logs you in via OAuth, sets Nous as your provider, and turns on the Tool Gateway. Check what's wired up any time with `doppel portal status`. Full details are in the [Tool Gateway docs](website/docs/user-guide/features/tool-gateway.md).

You can still bring your own keys per-tool whenever you want — the gateway is per-backend, not all-or-nothing.

---

## CLI vs Messaging Quick Reference

Doppel has two entry points: start the terminal UI with `doppel`, or run the gateway and talk to it from Telegram, Discord, Slack, WhatsApp, Signal, or Email. Once you're in a conversation, many slash commands are shared across both interfaces.

| Action | CLI | Messaging platforms |
|---------|-----|---------------------|
| Start chatting | `doppel` | Run `doppel gateway setup` + `doppel gateway start`, then send the bot a message |
| Start fresh conversation | `/new` or `/reset` | `/new` or `/reset` |
| Change model | `/model [provider:model]` | `/model [provider:model]` |
| Set a personality | `/personality [name]` | `/personality [name]` |
| Retry or undo the last turn | `/retry`, `/undo` | `/retry`, `/undo` |
| Compress context / check usage | `/compress`, `/usage`, `/insights [--days N]` | `/compress`, `/usage`, `/insights [days]` |
| Browse skills | `/skills` or `/<skill-name>` | `/<skill-name>` |
| Interrupt current work | `Ctrl+C` or send a new message | `/stop` or send a new message |
| Platform-specific status | `/platforms` | `/status`, `/sethome` |

For the full command lists, see the [CLI guide](website/docs/user-guide/cli.md) and the [Messaging Gateway guide](website/docs/user-guide/messaging/index.md).

---

## Documentation

Primary docs live in **[website/docs](website/docs/index.mdx)**:

| Section | What's Covered |
|---------|---------------|
| [Quickstart](website/docs/getting-started/quickstart.md) | Install → setup → first conversation in 2 minutes |
| [CLI Usage](website/docs/user-guide/cli.md) | Commands, keybindings, personalities, sessions |
| [Configuration](website/docs/user-guide/configuration.md) | Config file, providers, models, all options |
| [Messaging Gateway](website/docs/user-guide/messaging/index.md) | Telegram, Discord, Slack, WhatsApp, Signal, Home Assistant |
| [Security](website/docs/user-guide/security.md) | Command approval, DM pairing, container isolation |
| [Tools & Toolsets](website/docs/user-guide/features/tools.md) | 40+ tools, toolset system, terminal backends |
| [Skills System](website/docs/user-guide/features/skills.md) | Procedural memory, Skills Hub, creating skills |
| [Memory](website/docs/user-guide/features/memory.md) | Persistent memory, user profiles, best practices |
| [MCP Integration](website/docs/user-guide/features/mcp.md) | Connect any MCP server for extended capabilities |
| [Cron Scheduling](website/docs/user-guide/features/cron.md) | Scheduled tasks with platform delivery |
| [Context Files](website/docs/user-guide/features/context-files.md) | Project context that shapes every conversation |
| [Architecture](website/docs/developer-guide/architecture.md) | Project structure, agent loop, key classes |
| [Contributing](website/docs/developer-guide/contributing.md) | Development setup, PR process, code style |
| [CLI Reference](website/docs/reference/cli-commands.md) | All commands and flags |
| [Environment Variables](website/docs/reference/environment-variables.md) | Complete env var reference |

---

## Migrating from OpenClaw

If you're coming from OpenClaw, Doppel can automatically import your settings, memories, skills, and API keys.

**During first-time setup:** The setup wizard (`doppel setup`) automatically detects `~/.openclaw` and offers to migrate before configuration begins.

**Anytime after install:**

```bash
doppel claw migrate              # Interactive migration (full preset)
doppel claw migrate --dry-run    # Preview what would be migrated
doppel claw migrate --preset user-data   # Migrate without secrets
doppel claw migrate --overwrite  # Overwrite existing conflicts
```

What gets imported:
- **SOUL.md** — persona file
- **Memories** — MEMORY.md and USER.md entries
- **Skills** — user-created skills → `~/.doppel/skills/openclaw-imports/`
- **Command allowlist** — approval patterns
- **Messaging settings** — platform configs, allowed users, working directory
- **API keys** — allowlisted secrets (Telegram, OpenRouter, OpenAI, Anthropic, ElevenLabs)
- **TTS assets** — workspace audio files
- **Workspace instructions** — AGENTS.md (with `--workspace-target`)

See `doppel claw migrate --help` for all options, or use the `openclaw-migration` skill for an interactive agent-guided migration with dry-run previews.

---

## Contributing

We welcome contributions! See the [Contributing Guide](website/docs/developer-guide/contributing.md) for development setup, code style, and PR process.

Quick start for contributors — clone and go with `setup-hermes.sh`:

```bash
git clone https://github.com/Jnot1/doppel-agent.git
cd doppel-agent
./setup-hermes.sh     # installs uv, creates venv, installs .[all], exposes doppel and keeps legacy launcher aliases available
./doppel              # auto-detects the venv, no need to `source` first
```

Manual path (equivalent to the above):

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
uv venv .venv --python 3.11
source .venv/bin/activate
uv pip install -e ".[all,dev]"
scripts/run_tests.sh
```

---

## Community

- 💬 [GitHub Discussions](https://github.com/Jnot1/doppel-agent/discussions)
- 📚 [Skills Hub](https://agentskills.io)
- 🐛 [Issues](https://github.com/Jnot1/doppel-agent/issues)
- 🔌 [computer-use-linux](https://github.com/avifenesh/computer-use-linux) — Linux desktop-control MCP server for Doppel and other MCP hosts, with AT-SPI accessibility trees, Wayland/X11 input, screenshots, and compositor window targeting.
- 🔌 [HermesClaw](https://github.com/AaronWong1999/hermesclaw) — Community WeChat bridge: Run Doppel Agent and OpenClaw on the same WeChat account.

---

## License

MIT — see [LICENSE](LICENSE).

Doppel Agent is maintained by Doppelme. Original upstream attribution is preserved in [NOTICE.md].
