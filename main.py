
import psutil
import ollama


# 1. Define Python functions
def get_cpu_usage():
    try:
        cpu = psutil.cpu_percent(interval=1)
        return cpu
    except Exception as e:
        return e


def get_memory_usage():
    try:
        memory = psutil.virtual_memory()
        return memory
    except Exception as e:
        return e


def get_disk_usage():
    try:
        disk = psutil.disk_usage("C:/")
        return disk
    except Exception as e:
        return e


# 2. Define available tools

tools = [
    {
        "type": "function",
        "function": {
            "name": "get_cpu_usage",
            "description": "Checks CPU usage when a computer or VM is running slowly or applications are responding slowly.",
            "parameters": {
                "type": "object",
                "properties": {},
                "required": []
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_memory_usage",
            "description": "Checks memory usage when a computer or VM is lagging, applications are slow, or tasks take too long.",
            "parameters": {
                "type": "object",
                "properties": {},
                "required": []
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_disk_usage",
            "description": "Checks disk space when storage is nearly full, downloads fail, or files cannot be created or saved.",
            "parameters": {
                "type": "object",
                "properties": {},
                "required": []
            }
        }
    }
]


# 3. Initialize conversation

messages = [
    {
        "role": "user",
        "content": "My VM is extremely slow. Check CPU, memory and disk usage using the available tools"
    }
]

"My VM is extremely slow. Check CPU, memory and disk usage using the available tools"

# 4. Initialize tool results

tool_result = []


# 5. First call to Qwen

response = ollama.chat(
    model="qwen3:0.6b",
    messages=messages,
    tools=tools,
    think=False,
    stream=False
)

tool_calls = response.message.tool_calls or []


# 6. Repeat tool-calling cycle

while len(tool_calls) > 0:

    messages.append(response.message)

    # Execute requested Python functions

    for n in range(0, len(tool_calls)):

        b = tool_calls[n].function.name

        if b == "get_cpu_usage":
            a = get_cpu_usage()
            result = a
            if isinstance(a , Exception):
                    result = str(a)

        elif b == "get_memory_usage":
            e = get_memory_usage()
            result = e
            if isinstance(e,Exception):
                result= str(e)

        elif b == "get_disk_usage":
            c = get_disk_usage()
            result = c
            if isinstance(c,Exception):
                result = str(c)

        else:
            continue

        # Store function name and result

        temp = {
            "name": b,
            "result": result
        }

        tool_result.append(temp)

        # Send tool result to Qwen

        messages.append({
            "role": "tool",
            "content": str(result),
            "tool_name": b
        })

    # 7. Call Qwen again

    response = ollama.chat(
        model="qwen3:0.6b",
        messages=messages,
        tools=tools,
        think=False,
        stream=False
    )

    # 8. Check whether Qwen requests more tools

    tool_calls = response.message.tool_calls or []

# 9. Display final response

print("Final response:")
print(response.message.content)


# 10. Display collected tool results

print("\nTool results:")

for u in range(0, len(tool_result)):

    print(tool_result[u])
    print(tool_result[u]["name"])
    print(tool_result[u]["result"])
