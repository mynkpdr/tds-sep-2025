# 10. Function Calling (1 Mark)

## 1. Problem Description

The task is to build a web API that acts as an "interpreter" between natural language and structured function calls. The API will receive a plain English request (e.g., "What is the status of ticket 12345?") and must determine which predefined software function should be executed and with what arguments.

## 2. Understanding the Requirements

- **Framework**: Use a Python web framework like **FastAPI**.

- **Model**: Use an **OpenAI GPT model** (e.g., `gpt-4.1-nano`) to interpret the user's request.

- **Endpoint**: It must have a `GET` endpoint, for example, `/execute`, that accepts a query parameter `q` containing the user's request (e.g., `/execute?q=Schedule meeting...`).

- **Predefined Functions**: Your API needs to be aware of a specific set of functions, which will be provided to the OpenAI model as "tools".

- **Parameter Extraction**: The OpenAI model will be responsible for parsing the request string `q` and extracting the necessary arguments.

- **Response Format**: The API must return a specific JSON format:

  ```json
  {
    "name": "function_name_to_call",
    "arguments": "{\"arg1\": \"value1\", \"arg2\": 12345}"
  }
  ```

  - `"name"`: The name of the matched function.
  - `"arguments"`: A **string** containing the JSON representation of the arguments.

- **CORS**: The API must have CORS enabled.

## 3. Step-by-Step Solution

Using an LLM like GPT simplifies the parsing logic significantly. Instead of writing complex rules, we describe our functions to the model, and it determines which one to call based on the user's query.

### Step 1: Set up the FastAPI Project & Dependencies

1. Create a project folder.
2. Install FastAPI, Uvicorn, and the OpenAI library: `pip install "fastapi[all]" openai`.
3. Create a Python file for your code (e.g., `main.py`).

### Step 2: Define "Tools" for the OpenAI API

The core of this approach is defining your functions in a format the OpenAI API understands. This is done by creating a "tool" specification for each function, which describes its name, purpose, and parameters using JSON Schema.

### Step 3: Write the API Logic

1. **Import and Setup**: Import `FastAPI`, `CORSMiddleware`, `HTTPException`, `Request`, and `OpenAI`. Create your FastAPI app, enable CORS, and initialize the OpenAI client.
2. **Define Endpoint**: Create the `/execute` `GET` endpoint. It's best practice to make it an `async` function since we are making a network call to the OpenAI API.
3. **API Call Logic**:
   - Inside the endpoint, call the OpenAI `chat.completions.create` method.
   - Provide the user's query `q` as the content of the user's message.
   - Pass the list of your defined tools in the `tools` parameter.
   - Set `tool_choice="auto"` to let the model decide whether to call a function or not.
4. **Process the Response**:
   - Check the response from OpenAI. If the model decided to call a function, its `finish_reason` will be `tool_calls`.
   - The `tool_calls` object will contain the `name` of the function it chose and the `arguments` as a JSON string.
   - This matches our required output format perfectly. We can directly use this information to build our response.
5. **Handle No Match**: If the model doesn't return a `tool_calls` object, it means it couldn't match the query to any of the provided functions. In this case, we should return an appropriate error (e.g., an HTTP 400 error).

### Step 4: Deploy and Submit

1. **Run the API**: `uvicorn main:app --reload --port 8002`.
2. **Submit**: Submit the URL of your `/execute` endpoint.

## 4. Code / Configuration File

Here is the example `main.py` demonstrating the OpenAI-based approach.

```python
from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from openai import OpenAI

# --- FastAPI App Initialization ---
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], allow_methods=["*"], allow_headers=["*"],
)


# Add Private Network header
@app.middleware("http")
async def add_pna_header(request: Request, call_next):
    response = await call_next(request)
    response.headers["Access-Control-Allow-Private-Network"] = "true"
    return response


# --- OpenAI Client Initialization ---
client = OpenAI(api_key="<AIPIPE_KEY>", base_url="https://aipipe.org/openai/v1")

# --- Tool Definitions ---
# Define the tools (functions) that the model can call.
# Each tool includes its name, description, and JSON schema for parameters.
# The "strict": True flag ensures that the model adheres to the schema strictly.
TOOLS_DEFINITION = [
    {
        "type": "function",
        "function": {
            "name": "get_ticket_status",
            "description": "Get the current status of a support ticket",
            "parameters": {
                "type": "object",
                "properties": {
                    "ticket_id": {
                        "type": "integer",
                        "description": "The unique ID of the support ticket, e.g., 83742"
                    }
                },
                "required": ["ticket_id"],
                "additionalProperties": False
            },
            "strict": True
        }
    },
    {
        "type": "function",
        "function": {
            "name": "schedule_meeting",
            "description": "Schedule a meeting on a specific date, time, and in a specific room",
            "parameters": {
                "type": "object",
                "properties": {
                    "date": {"type": "string", "description": "The date for the meeting, e.g., '2025-10-26'"},
                    "time": {"type": "string", "description": "The time for the meeting, e.g., '15:00'"},
                    "meeting_room": {"type": "string", "description": "The name or ID of the meeting room"}
                },
                "required": ["date", "time", "meeting_room"],
                "additionalProperties": False
            },
            "strict": True
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_expense_balance",
            "description": "Get expense balance for an employee",
            "parameters": {
                "type": "object",
                "properties": {
                    "employee_id": {
                        "type": "integer",
                        "description": "Employee ID number"
                    }
                },
                "required": ["employee_id"],
                "additionalProperties": False
            },
            "strict": True
        }
    },
    {
        "type": "function",
        "function": {
            "name": "calculate_performance_bonus",
            "description": "Calculate yearly performance bonus for an employee",
            "parameters": {
                "type": "object",
                "properties": {
                    "employee_id": {
                        "type": "integer",
                        "description": "Employee ID number"
                    },
                    "current_year": {
                        "type": "integer",
                        "description": "Year to calculate bonus for"
                    }
                },
                "required": ["employee_id", "current_year"],
                "additionalProperties": False
            },
            "strict": True
        }
    },
    {
        "type": "function",
        "function": {
            "name": "report_office_issue",
            "description": "Report an office issue to the relevant department",
            "parameters": {
                "type": "object",
                "properties": {
                    "issue_code": {
                        "type": "integer",
                        "description": "The unique code of the office issue"
                    },
                    "department": {
                        "type": "string",
                        "description": "The department responsible for handling the issue, e.g., 'Facilities'"
                    }
                },
                "required": ["issue_code", "department"],
                "additionalProperties": False
            },
            "strict": True
        }
    }
]


# --- API Endpoint ---
@app.get("/execute")
async def execute_function_call(q: str):
    """
    Receives a natural language query and uses OpenAI's GPT model
    to determine the corresponding function call.
    """
    try:
        response = client.chat.completions.create(
            model="gpt-4.1-nano",
            messages=[{"role": "user", "content": q}],
            tools=TOOLS_DEFINITION,
            tool_choice="auto" # "auto" is the default, but we're explicit for clarity
        )

        response_message = response.choices[0].message
        tool_calls = response_message.tool_calls

        if tool_calls:
            # The model decided to call a function.
            function_call = tool_calls[0].function
            function_name = function_call.name
            function_args_str = function_call.arguments

            # The problem requires returning the name and the stringified arguments.
            # The OpenAI API already provides the arguments as a JSON string, which is exactly what we need.
            return {
                "name": function_name,
                "arguments": function_args_str
            }
        else:
            # The model did not find a suitable function to call.
            raise HTTPException(status_code=400, detail="Could not interpret the command or find a matching function.")

    except Exception as e:
        # Handle potential API errors or other issues
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")
```

## 5. How to Verify

The platform will send `GET` requests to your URL with various queries. Because you are using an LLM, your endpoint can now handle much more varied language.

- **Original Regex Query**: `.../execute?q=Status update for ticket 99887, please.`
- **More Natural Queries**:
  - `.../execute?q=what's happening with ticket 99887`
  - `.../execute?q=can I get a status on ticket number 99887`
  - `.../execute?q=book the 'Aquarium' room for a meeting tomorrow at 4pm`
  - `.../execute?q=show me the expense balance for employee 102`

In all cases, the platform will check your API's JSON response for the correct function `name` and correctly formatted `arguments` string.
