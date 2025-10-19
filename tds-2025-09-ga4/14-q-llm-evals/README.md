# 14. LLM Evaluation (1 Mark)

## 1. Problem Description

The task is to create a configuration file for **PromptFoo**, an open-source tool for evaluating and testing Large Language Models (LLMs). The configuration file, `promptfooconfig.yaml`, will set up a test to evaluate how well three different LLM providers can generate a specific `curl` command for interacting with the GitHub API. The command should fetch a specified number of top-starred repositories from a dynamically assigned GitHub organization.

## 2. Understanding the Requirements

- **File Format**: The output must be a single, valid `promptfooconfig.yaml` file.
- **Providers**: The configuration must test exactly three specific AI models:
  - `openrouter:openai/gpt-4o-mini`
  - `openrouter:openai/gpt-4.1-nano`
  - `openrouter:google/gemini-2.0-flash-lite-001`
- **Prompt**: A single prompt must be defined that instructs the models to generate a `curl` command for a specific organization and repository count (e.g., "google" and 15).
- **Tests (Assertions)**: The configuration must include tests to programmatically verify the correctness of the generated `curl` command. The validator requires at least 5 separate test cases.
- **LLM Rubric**: At least one test must be an `llm-rubric`, which uses another AI to grade the output based on a qualitative instruction.

## 3. Step-by-Step Solution

The key to solving this problem was understanding a specific structural requirement of the validator. The validator checks the number of **test cases** in the top-level `tests` list. Therefore, the correct approach is to define each assertion as its own separate test case.

1. **Define `providers` and `prompts`**: This part is straightforward. Define the three required providers, adding the `config` block for those needing `max_tokens`. Then, write a clear prompt using the `|` block scalar.

2. **Structure the `tests` Section**: This is the most critical step. Create a YAML list under the `tests` key. Each item in this list (denoted by a `-`) will be a complete, self-contained test case.

3. **Create Individual Test Cases**:
   - For each required check, create a new list item. Each test case will be an object containing an `assert` key.
   - The `assert` key itself points to an object that defines the assertion type and value.
   - Create the first test case for the API endpoint:

     ```yaml
     - assert:
         type: contains
         value: "https://api.github.com/orgs/..."
     ```

   - Create a second, separate test case for `per_page`:

     ```yaml
     - assert:
         type: contains
         value: "per_page=..."
     ```

   - Continue this pattern for `sort=stars`, `direction=desc`, and `Authorization`.

4. **Add the `llm-rubric` as a Separate Test**: Finally, add the `llm-rubric` as its own complete test case in the list. This brings the total number of items in the `tests` list to six, satisfying the validator's check.

## 4. Code / Configuration File

This is the final, correct `promptfooconfig.yaml` file. It structures each assertion as a separate test case, which passes the validation.

```yaml
prompts:
  - |
    Generate a curl command to fetch ONLY the top 15 most-starred repositories from the "google" organization. The request should use the GitHub API and be authenticated with a placeholder API key '$API_KEY'.

providers:
  - id: openrouter:openai/gpt-4o-mini
    config:
      max_tokens: 1024
  - id: openrouter:openai/gpt-4.1-nano
    config:
      max_tokens: 1024
  - id: openrouter:google/gemini-2.0-flash-lite-001

tests:
  - assert:
      type: contains
      value: "https://api.github.com/orgs/google/repos"
  - assert:
      type: contains
      value: "per_page=15"
  - assert:
      type: contains
      value: "sort=stars"
  - assert:
      type: contains
      value: "direction=desc"
  - assert:
      type: contains
      value: "Authorization: Bearer $API_KEY"
  - assert:
      type: llm-rubric
      rubric: Is the output a single, correct, and executable curl command that fulfills all requirements of the prompt?
```

## 5. How to Verify

You can check manually using the command `npx -y promptfoo eval -c promptfooconfig.yaml`.

The exam platform will parse your submitted `promptfooconfig.yaml` file and perform several checks:

- Is the YAML syntax valid?
- Are the `providers` and `prompts` sections correctly defined?
- Does the `tests` section contain at least 5 separate test cases, each with its own `assert`?
- Are the assertions correctly formatted and relevant to the prompt?
- Is there at least one `llm-rubric` test case included?

If all checks are satisfied, your submission will be marked correct.
