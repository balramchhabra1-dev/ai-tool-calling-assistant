# Local AI Tool Calling Assistant

A local AI-powered system monitoring assistant built using Python, Ollama, and Qwen 3 (0.6B). The assistant uses LLM-based tool calling to select and execute Python functions that collect CPU, memory, and disk usage.

## Project Overview

This project demonstrates how an LLM can interact with external Python functions through tool calling.

Instead of answering every question directly, the LLM can identify which system-monitoring tools are needed, request their execution, receive the results, and provide a response based on the collected information.

## Technologies Used

- Python
- Ollama
- Qwen 3 (0.6B)
- psutil
- Ollama Python library

## Features

- CPU usage monitoring
- Memory usage monitoring
- Disk usage monitoring
- LLM-based tool selection
- Multiple tool execution in one request
- Tool result collection
- Repeated tool-calling cycle
- Exception handling and error reporting
- Local LLM execution without cloud API dependencies

## Available Tools

| Tool | Function |
|---|---|
| CPU Monitoring | `get_cpu_usage()` |
| Memory Monitoring | `get_memory_usage()` |
| Disk Monitoring | `get_disk_usage()` |

## How It Works

1. The user submits a system-monitoring request.
2. Qwen receives the request and available tool definitions.
3. Qwen decides which tools to call.
4. Python executes the requested functions using psutil.
5. The program collects the function results.
6. Results are sent back to Qwen.
7. Qwen generates a final response.

## Project Workflow

User Request → Qwen Tool Selection → Python Function Execution → Tool Results → Qwen Final Response

## Installation

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd ai-tool-calling-assistant
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the environment (Windows PowerShell)

```powershell
.venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
pip install ollama psutil
```

### 5. Download the Qwen model

```bash
ollama pull qwen3:0.6b
```

Ensure Ollama is running before starting the application.

## Run the Application

```bash
python main.py
```

## Example Request

```text
My VM is extremely slow.
Check CPU, memory and disk usage using the available tools.
```

The assistant can request all three monitoring tools and return their collected readings.

## Error Handling

The project uses Python exception handling:

- `try` and `except` to catch errors.
- `isinstance()` to identify exception objects.
- `str()` to convert errors into readable text.
- Error messages are returned through the tool response flow.

## Execution Environment

- Operating System: Windows
- LLM Runtime: Ollama
- Model: Qwen 3 (0.6B)
- Execution: Local machine

## Learning Outcomes

Through this project, I implemented and practised:

- LLM tool calling
- Function definitions and tool schemas
- Dynamic tool selection
- Python function execution based on LLM requests
- Handling multiple tool calls
- Message management between Python and an LLM
- Exception handling
- Local LLM integration

## Future Scope

- Add additional system-monitoring tools.
- Support monitoring of remote machines and VMs.
- Improve structured reporting of system metrics.

---

**Author:** Balram