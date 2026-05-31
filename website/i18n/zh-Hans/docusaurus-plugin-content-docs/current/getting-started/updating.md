---
sidebar_position: 3
title: "更新与卸载"
description: "如何将 Doppel Agent 更新到最新版本或卸载"
---

# 更新与卸载

## 更新

### Git 安装方式

使用单条命令更新至最新版本：

```bash
doppel update
```

该命令会从 `main` 拉取最新代码、更新依赖项，并提示你配置自上次更新以来新增的选项。

### pip 安装方式

PyPI 发布版本跟踪**带标签的版本**（主版本和次版本发布），而非 `main` 上的每次提交。检查更新并升级：

```bash
doppel update --check    # 查看 PyPI 上是否有更新的版本
doppel update            # 执行 pip install --upgrade doppel-agent
```

或手动执行：

```bash
pip install --upgrade doppel-agent    # 或：uv pip install --upgrade doppel-agent
```

:::tip
`doppel update` 会自动检测新的配置选项并提示你添加。如果跳过了该提示，可手动运行 `doppel config check` 查看缺失的选项，再运行 `doppel config migrate` 以交互方式添加。
:::

### 更新过程（Git 安装方式）

运行 `doppel update` 时，将依次执行以下步骤：

1. **配对数据快照** — 保存一份轻量级的更新前状态快照（涵盖 `~/.doppel/pairing/`、飞书评论规则及其他运行时修改的状态文件）。可通过 [快照与回滚](../user-guide/checkpoints-and-rollback.md) 中描述的快照恢复流程进行恢复，或从 Doppel 写入 `~/.doppel/` 目录旁的最新快速快照 zip 文件中提取。
2. **Git pull** — 从 `main` 分支拉取最新代码并更新子模块
3. **拉取后语法校验 + 自动回滚** — 在拉取后，Doppel 会在启动时编译每次启动都要导入的 8 个关键文件。如果解析失败（例如遗留的冲突标记、文件被意外截断），Doppel 会执行 `git reset --hard <pre-pull-sha>` 将安装回退到更新前状态。待上游修复后，重新运行 `doppel update` 即可继续。
4. **依赖安装** — 运行 `uv pip install -e ".[all]"` 以获取新增或变更的依赖项
5. **配置迁移** — 检测自当前版本以来新增的配置选项并提示设置
6. **Gateway 自动重启** — 更新完成后刷新正在运行的 gateway，使新代码立即生效。由服务管理的 gateway（Linux 上的 systemd、macOS 上的 launchd）通过服务管理器重启；手动启动的 gateway 在 Doppel 能将运行中的 PID 映射回某个 profile 时会自动重新启动。

### 更新到非默认分支：`--branch`

默认情况下，`doppel update` 追踪 `origin/main`。使用 `--branch <name>` 可切换到其他分支（例如 QA 通道、特性分支或候选发布测试）：

```bash
doppel update --branch release-candidate
doppel update --check --branch experimental   # 仅预览是否落后
```

如果你本地当前检出的是其他分支，Doppel 会先自动 stash 所有未提交修改，再切换 HEAD 到目标分支并执行拉取。不存在于本地的分支会自动从 `origin/<name>` 建立跟踪分支（`git checkout -B <name> origin/<name>`）；不存在的分支会干净失败，并在退出前恢复你之前 stash 的改动。`main` 专用的 fork-upstream 同步逻辑会在非 `main` 分支下自动跳过。

### 仅预览：`doppel update --check`

想在拉取前确认是否有更新？运行 `doppel update --check` — 对于 Git 安装方式，它会获取并与 `origin/main` 比较提交；对于 pip 安装方式，它会查询 PyPI 上的最新版本。不修改任何文件，不重启 gateway。适合在以“是否有更新”为条件的脚本和 cron 任务中使用。

### 完整更新前备份：`--backup`

对于高价值 profile（生产环境 gateway、团队共享安装），可选择在拉取前对 `HERMES_HOME`（配置、认证、会话、技能、配对数据）进行完整备份：

```bash
doppel update --backup
```

或将其设为每次运行的默认行为：

```yaml
# ~/.doppel/config.yaml
updates:
  pre_update_backup: true
```

`--backup` 在早期版本中是始终开启的行为，但在大型 home 目录上会给每次更新增加数分钟时间，因此现已改为按需启用。上述轻量级配对数据快照仍会无条件执行。

### Windows：另一个 `doppel.exe` 正在运行

在 Windows 上，如果 `doppel update` 检测到另一个 `doppel.exe` 进程持有 venv 入口点可执行文件的句柄，它将拒绝运行 — 最常见的情况是 Doppel Desktop 应用启动的后端进程、另一个终端中打开的 `doppel` REPL，或正在运行的 gateway：

```
$ doppel update
✗ Another doppel.exe is running:
    PID 12345  doppel.exe

  Updating now would fail to overwrite ...\venv\Scripts\doppel.exe because
  Windows blocks REPLACE on a running executable.

  Close Doppel Desktop, exit any open `doppel` REPLs, and
  stop the gateway (`doppel gateway stop`) before retrying.
  Override with `doppel update --force` if you've already
  confirmed those processes will not write to the venv.
```

关闭列出的进程后重试。如果你确定并发进程不会造成干扰（极少见 — 通常仅在杀毒软件 shim 被误判时有用），可传入 `--force` 跳过检查。此时更新程序仍会以指数退避方式重试 `.exe` 重命名操作，对于顽固的文件锁，会通过 `MoveFileEx(MOVEFILE_DELAY_UNTIL_REBOOT)` 将替换操作安排在下次重启时执行，以确保更新能够完成。

预期输出如下：

```
$ doppel update
Updating Doppel Agent...
📥 Pulling latest code...
Already up to date.  (or: Updating abc1234..def5678)
📦 Updating dependencies...
✅ Dependencies updated
🔍 Checking for new config options...
✅ Config is up to date  (or: Found 2 new options — running migration...)
🔄 Restarting gateways...
✅ Gateway restarted
✅ Doppel Agent updated successfully!
```

### 更新后建议的验证步骤

`doppel update` 处理主要的更新流程，但快速验证可确认一切正常落地：

1. `git status --short` — 若工作树出现意外的脏状态，请在继续前检查
2. `doppel doctor` — 检查配置、依赖项和服务健康状态
3. `doppel --version` — 确认版本已按预期更新
4. 如果使用 gateway：`doppel gateway status`
5. 如果 `doctor` 报告 npm audit 问题：在标记的目录中运行 `npm audit fix`

:::warning 更新后工作树出现脏状态
如果 `doppel update` 后 `git status --short` 显示意外变更，请在继续前停下来检查。这通常意味着本地修改被重新应用到了更新后的代码之上，或依赖步骤刷新了锁文件。
:::

### 终端在更新中途断开连接

`doppel update` 针对意外终端断开进行了保护：

- 更新会忽略 `SIGHUP`，因此关闭 SSH 会话或终端窗口不再会在安装中途终止它。`pip` 和 `git` 子进程继承此保护，因此 Python 环境不会因连接断开而处于半安装状态。
- 更新运行期间，所有输出会同步镜像到 `~/.doppel/logs/update.log`。如果终端消失，重新连接后检查日志，确认更新是否完成以及 gateway 重启是否成功：

```bash
tail -f ~/.doppel/logs/update.log
```

- `Ctrl-C`（SIGINT）和系统关机（SIGTERM）仍会被响应 — 这些是主动取消操作，而非意外中断。

你不再需要将 `doppel update` 包裹在 `screen` 或 `tmux` 中来应对终端断开。

### 查看当前版本

```bash
doppel version
```

与 [GitHub releases 页面](https://github.com/Jnot1/doppel-agent/releases) 上的最新版本进行比较。

### 从消息平台更新

你也可以直接从 Telegram、Discord、Slack、WhatsApp 或 Teams 发送以下命令进行更新：

```
/update
```

此命令会拉取最新代码、更新依赖项并重启正在运行的 gateway。Bot 在重启期间会短暂下线（通常为 5–15 秒），之后恢复服务。

### 手动更新

如果你是手动安装的（未使用快速安装脚本）：

```bash
cd /path/to/doppel-agent
export VIRTUAL_ENV="$(pwd)/venv"

# Pull latest code
git pull origin main

# Reinstall (picks up new dependencies)
uv pip install -e ".[all]"

# Check for new config options
doppel config check
doppel config migrate   # 交互式补齐缺失配置
```

### 回滚说明

如果更新引入了问题，可以回滚到之前的版本：

```bash
cd /path/to/doppel-agent

# List recent versions
git log --oneline -10

# Roll back to a specific commit
git checkout <commit-hash>
git submodule update --init --recursive
uv pip install -e ".[all]"

# Restart the gateway if running
doppel gateway restart
```

回滚到特定发布标签：

```bash
git checkout vX.Y.Z
git submodule update --init --recursive
uv pip install -e ".[all]"
```

:::warning
如果新增了配置选项，回滚可能导致配置不兼容。回滚后运行 `doppel config check`，如果遇到错误，请从 `config.yaml` 中删除无法识别的选项。
:::

### Nix 用户注意事项

如果你通过 Nix flake 安装，更新由 Nix 包管理器负责：

```bash
# Update the flake input（使用你自己的 flake input 名称）
nix flake update doppel-agent

# Or rebuild with the latest
nix profile upgrade doppel-agent
```

首选 flake 包别名和 derivation 契约现已使用 `doppel-agent`。如果某个旧安装最初是通过 `#hermes-agent` 添加的，仍可继续使用该兼容别名升级；packaged 安装仍然默认使用 `doppel` 入口点，并保留 `hermes` 作为兼容别名。NixOS 服务/模块命名空间仍保持 `services.hermes-agent`。

Nix 安装是不可变的 — 回滚由 Nix 的 generation 系统处理：

```bash
nix profile rollback
```

详情参见 [Nix 安装](./nix-setup.md)。

### Homebrew 用户注意事项

如果你的 tap 已暴露新的 Doppel 公式名，全新安装可以使用：

```bash
brew install doppel-agent
brew upgrade doppel-agent
```

仍在使用旧公式名的 Homebrew 旧安装，应继续通过以下命令升级：

```bash
brew upgrade hermes-agent
```

`doppel update` 现在会显示为该安装写入的确切 Homebrew 公式名，因此受 Homebrew 管理的安装会明确提示你应使用 `doppel-agent` 还是 `hermes-agent`。

---

## 卸载

### Git 安装方式

```bash
doppel uninstall
```

卸载程序会提供选项，让你保留配置文件（`~/.doppel/`）以便将来重新安装。

### pip 安装方式

```bash
pip uninstall hermes-agent
rm -rf ~/.doppel            # 可选 — 如计划重新安装则保留
```

### 手动卸载

```bash
rm -f ~/.local/bin/doppel ~/.local/bin/hermes
rm -rf /path/to/doppel-agent
rm -rf ~/.doppel            # 可选 — 如计划重新安装则保留
```

:::info
如果你将 gateway 安装为系统服务，请先停止并禁用它：
```bash
doppel gateway stop
# Linux: systemctl --user disable doppel-gateway
# macOS: launchctl remove ai.doppel.gateway
```
:::
