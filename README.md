# CodeAgent

> A lightweight CLI Coding Agent for local repositories.

CodeAgent 是一个基于 Python + Ollama 的本地代码辅助 Agent，能够理解、搜索、修改和分析代码，并通过多步推理（ReAct）完成复杂任务。

## Features

* 🔍 Code Search
* 📖 Read File
* ✏️ Write File
* 📂 List Workspace Files
* 🤖 JSON Tool Calling
* 🧠 Multi-step Reasoning
* 💾 Conversation Memory
* ▶️ Run Python Scripts
* 📝 Automatic Code Editing
* 🔧 Modular Tool System

## Project Structure

```text
CodeAgent/
│
├── README.md
├── requirements.txt
├── main.py
├── config.py
│
├── prompts/
├── agent/
├── tools/
├── workspace/
├── memory/
└── logs/
```

## Requirements

* Python 3.10+
* Ollama
* Hermes3 / Qwen2.5 等兼容模型

## Install

```bash
git clone <your_repo>
cd CodeAgent

pip install -r requirements.txt
```

确保 Ollama 已启动：

```bash
ollama serve
```

拉取模型（以 Hermes3 为例）：

```bash
ollama pull hermes3
```

## Run

```bash
python main.py
```

示例：

```text
User > login函数在哪里

Agent >
auth.py:12

def login(username, password):
    ...
```

或者：

```text
User > 给 auth.py 增加 logout 函数

Agent >
✓ Read auth.py
✓ Generate new code
✓ Write auth.py

Done.
```

## Design

CodeAgent 采用模块化架构：

```
User
 │
 ▼
CLI
 │
 ▼
Planner
 │
 ▼
LLM
 │
 ▼
JSON Action
 │
 ▼
Executor
 │
 ▼
Tools
 │
 ▼
Workspace
```

LLM 负责推理，Executor 负责执行，Tools 负责实际操作文件系统，使模型与执行逻辑解耦。

## Planned Features

* Project Index
* Semantic Search
* Diff Preview
* Auto Bug Fix
* Git Integration
* Test Runner
* RAG for Repository
* Multi-file Refactoring

## License

MIT
