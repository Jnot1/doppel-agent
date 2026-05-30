<p align="center">
  <img src="assets/banner.png" alt="Doppel Agent" width="100%">
</p>

# Doppel Agent ☤

<p align="center">
  <a href="website/docs/index.mdx"><img src="https://img.shields.io/badge/Docs-Doppel%20Agent-FFD700?style=for-the-badge" alt="Documentation"></a>
  <a href="https://github.com/Jnot1/doppel-agent"><img src="https://img.shields.io/badge/GitHub-Jnot1%2Fdoppel--agent-111827?style=for-the-badge&logo=github" alt="GitHub repository"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" alt="License: MIT"></a>
  <a href="NOTICE.md"><img src="https://img.shields.io/badge/Notice-Hermes%20fork-blue?style=for-the-badge" alt="Fork notice"></a>
  <a href="README.md"><img src="https://img.shields.io/badge/Lang-English-lightgrey?style=for-the-badge" alt="English"></a>
</p>

**Doppel Agent 是你的日常个人 AI 助手。** 它是基于 Nous Research 的 Hermes Agent 修改而来的分叉版本，由 Doppelme 维护，适合处理邮件分拣、日历整理、购物清单、待办事项、健身陪练、烹饪辅助，以及需要记忆、工具和自动化能力的复杂技术工作流。

支持任意模型——[Nous Portal](https://portal.nousresearch.com)、[OpenRouter](https://openrouter.ai)（200+ 模型）、[NVIDIA NIM](https://build.nvidia.com)（Nemotron）、[小米 MiMo](https://platform.xiaomimimo.com)、[z.ai/GLM](https://z.ai)、[Kimi/Moonshot](https://platform.moonshot.ai)、[MiniMax](https://www.minimax.io)、[Hugging Face](https://huggingface.co)、OpenAI，或自定义端点。使用 `doppel model` 即可切换——无需改代码，无锁定。过渡期间仍兼容旧的 `hermes` 命令。

<table>
<tr><td><b>真正的终端界面</b></td><td>完整的 TUI，支持多行编辑、斜杠命令自动补全、对话历史、中断重定向和流式工具输出。</td></tr>
<tr><td><b>随你所在</b></td><td>Telegram、Discord、Slack、WhatsApp、Signal 和 CLI——全部从单个网关进程运行。语音备忘录转写、跨平台对话连续性。</td></tr>
<tr><td><b>闭环学习</b></td><td>代理管理记忆并定期自我提醒。复杂任务后自动创建技能。技能在使用中自我改进。FTS5 会话搜索配合 LLM 摘要实现跨会话回溯。<a href="https://github.com/plastic-labs/honcho">Honcho</a> 辩证式用户建模。兼容 <a href="https://agentskills.io">agentskills.io</a> 开放标准。</td></tr>
<tr><td><b>定时自动化</b></td><td>内置 cron 调度器，支持向任何平台投递。日报、夜间备份、周审计——全部用自然语言描述，无人值守运行。</td></tr>
<tr><td><b>委派与并行</b></td><td>生成隔离子代理处理并行工作流。编写 Python 脚本通过 RPC 调用工具，将多步管道压缩为零上下文开销的轮次。</td></tr>
<tr><td><b>随处运行</b></td><td>六种终端后端——本地、Docker、SSH、Daytona、Singularity 和 Modal。Daytona 和 Modal 提供 Serverless 持久化——代理环境空闲时休眠、按需唤醒，空闲期间几乎零成本。$5 VPS 或 GPU 集群都能跑。</td></tr>
<tr><td><b>研究就绪</b></td><td>批量轨迹生成、轨迹压缩——用于训练下一代工具调用模型。</td></tr>
</table>

---

## 快速安装

```bash
curl -fsSL https://raw.githubusercontent.com/Jnot1/doppel-agent/main/scripts/install.sh | bash
```

支持 Linux、macOS、WSL2 和 Android (Termux)。安装程序会自动处理平台特定的配置。

> **Android / Termux：** 已测试的手动安装路径请参考 [Termux 指南](website/docs/getting-started/termux.md)。在 Termux 上，Doppel 会安装精选的 `.[termux]` 扩展，因为完整的 `.[all]` 扩展会拉取 Android 不兼容的语音依赖。
>
> **Windows：** 原生 Windows 目前属于**早期 Beta**。PowerShell 一键安装已经可用，但稳定性仍不如 Linux/macOS/WSL2 路径；如果遇到问题，请优先在 [Jnot1/doppel-agent issues](https://github.com/Jnot1/doppel-agent/issues) 反馈。若你更看重稳定性，仍建议在 [WSL2](https://learn.microsoft.com/zh-cn/windows/wsl/install) 中运行上面的 Linux 安装命令。

安装后：

```bash
source ~/.bashrc    # 重新加载 shell（或: source ~/.zshrc）
doppel              # 开始对话！
```

---

## 快速入门

```bash
doppel              # 交互式 CLI — 开始对话
doppel model        # 选择 LLM 提供商和模型
doppel tools        # 配置启用的工具
doppel config set   # 设置单个配置项
doppel gateway      # 启动消息网关（Telegram、Discord 等）
doppel setup        # 运行完整设置向导（一次性配置所有内容）
doppel claw migrate # 从 OpenClaw 迁移（如果来自 OpenClaw）
doppel update       # 更新到最新版本
doppel doctor       # 诊断问题
```

📖 **[仓库内文档 →](website/docs/index.mdx)**

---

## 省去到处收集 API Key — Nous Portal

Doppel Agent 始终允许你使用任意服务商，这点不会改变。但如果你不想为模型、网页搜索、图像生成、TTS、云浏览器分别去申请五个不同的 API Key，**[Nous Portal](https://portal.nousresearch.com)** 用一个订阅就能覆盖全部：

- **300+ 模型** — 用 `/model <name>` 随时切换
- **Tool Gateway** — 网页搜索（Firecrawl）、图像生成（FAL）、文本转语音（OpenAI）、云浏览器（Browser Use），全部通过订阅托管。无需额外注册任何账户。

全新安装时一条命令即可：

```bash
doppel setup --portal
```

它会通过 OAuth 登录、把 Nous 设为推理服务商，并启用 Tool Gateway。随时用 `doppel portal status` 查看路由状态。完整说明见 [Tool Gateway 文档](website/docs/user-guide/features/tool-gateway.md)。

你随时可以按工具单独切回自己的 API Key — Gateway 是按工具粒度生效的，不是一刀切。

---

## CLI 与消息平台 快速对照

Doppel 有两种入口：用 `doppel` 启动终端 UI，或运行网关从 Telegram、Discord、Slack、WhatsApp、Signal 或 Email 与之对话。进入对话后，许多斜杠命令在两种界面中通用。

| 操作 | CLI | 消息平台 |
|------|-----|----------|
| 开始对话 | `doppel` | 运行 `doppel gateway setup` + `doppel gateway start`，然后给机器人发消息 |
| 开始新对话 | `/new` 或 `/reset` | `/new` 或 `/reset` |
| 更换模型 | `/model [provider:model]` | `/model [provider:model]` |
| 设置人格 | `/personality [name]` | `/personality [name]` |
| 重试或撤销上一轮 | `/retry`、`/undo` | `/retry`、`/undo` |
| 压缩上下文 / 查看用量 | `/compress`、`/usage`、`/insights [--days N]` | `/compress`、`/usage`、`/insights [days]` |
| 浏览技能 | `/skills` 或 `/<skill-name>` | `/skills` 或 `/<skill-name>` |
| 中断当前工作 | `Ctrl+C` 或发送新消息 | `/stop` 或发送新消息 |
| 平台特定状态 | `/platforms` | `/status`、`/sethome` |

完整命令列表请参阅 [CLI 指南](website/docs/user-guide/cli.md) 和 [消息网关指南](website/docs/user-guide/messaging/index.md)。

---

## 文档

主要文档位于仓库内的 **[website/docs](website/docs/index.mdx)**：

| 章节 | 内容 |
|------|------|
| [快速开始](website/docs/getting-started/quickstart.md) | 安装 → 设置 → 2 分钟内开始首次对话 |
| [CLI 使用](website/docs/user-guide/cli.md) | 命令、快捷键、人格、会话 |
| [配置](website/docs/user-guide/configuration.md) | 配置文件、提供商、模型、所有选项 |
| [消息网关](website/docs/user-guide/messaging/index.md) | Telegram、Discord、Slack、WhatsApp、Signal、Home Assistant |
| [安全](website/docs/user-guide/security.md) | 命令审批、DM 配对、容器隔离 |
| [工具与工具集](website/docs/user-guide/features/tools.md) | 40+ 工具、工具集系统、终端后端 |
| [技能系统](website/docs/user-guide/features/skills.md) | 过程记忆、技能中心、创建技能 |
| [记忆](website/docs/user-guide/features/memory.md) | 持久记忆、用户画像、最佳实践 |
| [MCP 集成](website/docs/user-guide/features/mcp.md) | 连接任意 MCP 服务器扩展能力 |
| [定时调度](website/docs/user-guide/features/cron.md) | 定时任务与平台投递 |
| [上下文文件](website/docs/user-guide/features/context-files.md) | 影响每次对话的项目上下文 |
| [架构](website/docs/developer-guide/architecture.md) | 项目结构、代理循环、关键类 |
| [贡献](website/docs/developer-guide/contributing.md) | 开发设置、PR 流程、代码风格 |
| [CLI 参考](website/docs/reference/cli-commands.md) | 所有命令和标志 |
| [环境变量](website/docs/reference/environment-variables.md) | 完整环境变量参考 |

---

## 从 OpenClaw 迁移

如果你来自 OpenClaw，Doppel 可以自动导入你的设置、记忆、技能和 API 密钥。

**首次安装时：** 安装向导（`doppel setup`）会自动检测 `~/.openclaw` 并在配置开始前提供迁移选项。

**安装后任意时间：**

```bash
doppel claw migrate              # 交互式迁移（完整预设）
doppel claw migrate --dry-run    # 预览将要迁移的内容
doppel claw migrate --preset user-data   # 仅迁移用户数据，不含密钥
doppel claw migrate --overwrite  # 覆盖已有冲突
```

导入内容：
- **SOUL.md** — 人格文件
- **记忆** — MEMORY.md 和 USER.md 条目
- **技能** — 用户创建的技能 → `~/.doppel/skills/openclaw-imports/`
- **命令白名单** — 审批模式
- **消息设置** — 平台配置、允许用户、工作目录
- **API 密钥** — 白名单中的密钥（Telegram、OpenRouter、OpenAI、Anthropic、ElevenLabs）
- **TTS 资产** — 工作区音频文件
- **工作区指令** — AGENTS.md（使用 `--workspace-target`）

使用 `doppel claw migrate --help` 查看所有选项，或使用 `openclaw-migration` 技能进行交互式代理引导迁移（含干运行预览）。

---

## 贡献

欢迎贡献！请参阅 [贡献指南](website/docs/developer-guide/contributing.md) 了解开发设置、代码风格和 PR 流程。

贡献者快速开始——克隆并使用 `setup-hermes.sh`：

```bash
git clone https://github.com/Jnot1/doppel-agent.git
cd doppel-agent
./setup-hermes.sh     # 安装 uv、创建 venv、安装 .[all]，并同时暴露 doppel / hermes 启动器
./doppel              # 自动检测 venv，无需先 source
```

手动安装（等效于上述命令）：

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
uv venv venv --python 3.11
source venv/bin/activate
uv pip install -e ".[all,dev]"
python -m pytest tests/ -q
```

---

## 社区

- 💬 [Discord](https://discord.gg/NousResearch)
- 📚 [技能中心](https://agentskills.io)
- 🐛 [问题反馈](https://github.com/Jnot1/doppel-agent/issues)
- 💡 [讨论区](https://github.com/Jnot1/doppel-agent/discussions)
- 🔌 [HermesClaw](https://github.com/AaronWong1999/hermesclaw) — 社区微信桥接：在同一微信账号上运行 Doppel Agent 和 OpenClaw。

---

## 许可证

MIT — 详见 [LICENSE](LICENSE)。

Doppel Agent 由 Doppelme 维护，并作为 Nous Research 的 Hermes Agent 修改分叉发布。所需归属说明请参阅 [NOTICE.md](NOTICE.md)。
