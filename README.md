# CodeAgent

一个基于 **LLM + ReAct + Planner + MCP + Tool Calling** 的本地代码智能体（Code Agent）。

CodeAgent 能够理解自然语言需求，自主规划执行步骤，调用工具读取、搜索、修改代码，并完成验证，实现类似 Claude Code、OpenHands 的代码操作流程。

---

# 功能特点

## 1. ReAct Agent

采用经典 ReAct（Reason + Act）模式。

```
User
    │
    ▼
LLM 思考
    │
    ▼
Tool Action
    │
    ▼
Tool Result
    │
    ▼
LLM 再推理
    │
    ▼
Final
```

模型可以根据工具返回结果动态调整下一步行为，而不是一次性生成全部答案。

---

## 2. Planner（任务规划）

用户输入首先经过 Planner 分类。

例如：

```
读取 auth.py
```

Planner：

```
Task Type: read

Suggested Steps

read_file

final
```

例如：

```
给 auth.py 增加 logout
```

Planner：

```
Task Type: edit

Suggested Steps

read_file

replace_text

read_file

final
```

Planner 会作为额外 System Prompt 提供给模型，约束执行流程，提高稳定性。

---

## 3. MCP（Model Context Protocol）

项目实现了轻量级 MCP Client。

```
Agent
    │
    ▼
MCP Client
    │
    ▼
Filesystem Server
    │
    ▼
Tool
```

当前支持：

* read_file
* replace_text
* write_file
* search_code
* list_files
* run_python

所有工具统一通过 MCP Client 调度，而不是直接耦合在 Agent 中。

后续新增工具无需修改 Agent 主流程。

---

## 4. Tool Executor

Executor 负责：

* 接收 Action
* 查找对应 Tool
* 执行 Tool
* 返回结果

Agent 不关心 Tool 实现细节，仅负责推理与决策。

---

## 5. Memory

Memory 保存完整上下文：

```
User

Assistant

Tool Result

Assistant

Tool Result
```

用于支持多轮 ReAct 推理。

读取文件时，仅保存源码内容供模型分析，不直接修改文件。

---

## 6. Parser

Parser 负责解析 LLM 输出。

支持：

* Markdown ```json
* 纯 JSON
* 多余文本包裹
* 自动提取首个合法 JSON

避免因模型输出格式不规范导致流程中断。

---

## 7. 安全编辑策略

项目采用：

```
read_file
    ↓
replace_text
    ↓
read_file（验证）
    ↓
final
```

而不是直接覆盖整个文件。

只有：

* 创建新文件
* 完全重写文件

才允许使用：

```
write_file
```

已有文件默认使用：

```
replace_text
```

从而降低误覆盖风险。

---

## 8. Read / Edit 分离

Planner 将任务分为两类：

### Read Task

例如：

* 查看文件
* 搜索代码
* 分析代码
* 列出文件

推荐流程：

```
read_file
↓

final
```

不应修改任何文件。

### Edit Task

例如：

* 增加函数
* 修改逻辑
* 删除代码
* 修复 Bug

推荐流程：

```
read_file
↓

replace_text

↓

read_file

↓

final
```

---

## 9. Backup 机制

修改文件时自动生成：

```
xxx.py.bak
```

发生异常可快速恢复。

---

# 项目结构

```
CodeAgent/

├── agent/
│   ├── loop.py
│   ├── planner.py
│   ├── parser.py
│   ├── executor.py
│   ├── llm.py
│   └── memory.py
│
├── mcp/
│   ├── client.py
│   ├── registry.py
│   ├── base.py
│   └── filesystem.py
│
├── tools/
│   ├── read_file.py
│   ├── replace_text.py
│   ├── write_file.py
│   ├── search_code.py
│   ├── list_files.py
│   └── run_python.py
│
├── prompts/
│   └── system_prompt.py
│
└── main.py
```

---

# 工作流程

```
          User
            │
            ▼
        Planner
            │
            ▼
      Build Prompt
            │
            ▼
            LLM
            │
            ▼
         Parser(JSON)
            │
            ▼
        Executor/MCP
            │
            ▼
      Filesystem Server
            │
            ▼
           Tool
            │
            ▼
        Tool Result
            │
            ▼
          Memory
            │
            ▼
            LLM
            │
            ▼
          Final
```

---

# 示例

## 读取文件

输入：

```
读取 auth.py
```

Agent：

```
read_file

↓

final
```

---

## 搜索代码

输入：

```
搜索 login
```

Agent：

```
search_code

↓

final
```

---

## 添加函数

输入：

```
给 auth.py 增加 logout 函数
```

Agent：

```
read_file

↓

replace_text

↓

read_file

↓

final
```

---

# 技术特点

* ReAct Agent
* Planner 驱动执行
* MCP Client 架构
* Tool Calling
* Memory 管理上下文
* JSON Parser 容错
* ReplaceText 安全编辑
* Backup 自动备份
* 可扩展 Tool Registry
* 本地代码仓库操作

---

# 后续可扩展方向

* 多 Planner（Task Decomposition）
* 多 Agent 协作（Supervisor / Worker）
* Code Review Agent
* 自动生成 Patch（Diff）
* Git Commit Agent
* RAG + Repository Index
* AST 级代码编辑
* Docker Sandbox 执行
* 并行 Tool Calling
* Web Search / Browser MCP

---

# 项目定位

CodeAgent 是一个面向代码理解与自动修改的本地智能体框架，融合了 **LLM、ReAct、Planner、MCP、Tool Calling 和 Memory** 等核心 Agent 技术，具备自主规划、工具调用、代码检索、安全编辑与结果验证能力，可作为 Agent 工程、代码助手及大模型应用开发的实践项目基础。
