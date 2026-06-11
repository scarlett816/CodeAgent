"""
CodeAgent 全局配置文件

统一管理：
- 路径
- 模型
- Agent参数
- 日志
"""

from pathlib import Path

# =====================================================
# Project Root
# =====================================================

PROJECT_ROOT = Path(__file__).resolve().parent

# =====================================================
# Workspace
# Agent 只能修改这里面的代码
# =====================================================

WORKSPACE = PROJECT_ROOT / "workspace"

# =====================================================
# Memory
# =====================================================

MEMORY_DIR = PROJECT_ROOT / "memory"

# =====================================================
# Prompt
# =====================================================

PROMPT_DIR = PROJECT_ROOT / "prompts"

# =====================================================
# Log
# =====================================================

LOG_DIR = PROJECT_ROOT / "logs"

LOG_FILE = LOG_DIR / "agent.log"

# =====================================================
# Memory Files
# =====================================================

HISTORY_FILE = MEMORY_DIR / "history.json"

PROJECT_INDEX_FILE = MEMORY_DIR / "project_index.json"

# =====================================================
# Ollama
# =====================================================

OLLAMA_BASE_URL = "http://localhost:11434/api/chat"

OLLAMA_MODEL = "hermes3"

# 以后如果切换模型，只修改这里即可
# OLLAMA_MODEL = "qwen2.5:7b"
# OLLAMA_MODEL = "deepseek-r1:8b"

# =====================================================
# Agent Config
# =====================================================

MAX_STEPS = 10

TEMPERATURE = 0.2

# =====================================================
# 自动创建目录
# =====================================================

WORKSPACE.mkdir(exist_ok=True)

MEMORY_DIR.mkdir(exist_ok=True)

PROMPT_DIR.mkdir(exist_ok=True)

LOG_DIR.mkdir(exist_ok=True)