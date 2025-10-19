# 3. Generate addresses with LLMs (1 Mark)

## 1. Problem Description

The goal is to write the JSON body for a request to the OpenAI API. This request will ask the `gpt-4o-mini` model to generate 10 random U.S. addresses and return them in a strictly defined JSON format. This technique is called "structured output" and is essential for getting reliable, machine-readable data from an AI.

## 2. Understanding the Requirements

- **Model**: The AI model must be `gpt-4o-mini`.
- **Messages**: The request must contain two specific messages:
  1. A `system` message: `Respond in JSON`.
  2. A `user` message: `Generate 10 random addresses in the US`.
- **Structured Output**: The request must use the `response_format` feature with `type: "json_schema"` to enforce a specific structure.
- **JSON Schema**: The schema must define a root object containing an `addresses` key. This key should hold an array of address objects.
- **Address Object**: Each object in the `addresses` array must:
  - Contain the specific fields and data types listed in the question (e.g., `street` as a `string`, `zip` as a `number`).
  - Mark all these fields as `required`.
  - Forbid any other fields by setting `additionalProperties` to `false`.

**Special Challenge**: The answer box for this question is initially hidden. You will need to use your browser's developer tools to make it visible.

## 3. Step-by-Step Solution

1. **Reveal the Answer Box**:
   - Right-click on the text "There's no answer box above" and select "Inspect".
   - This will open the developer tools and highlight a `<textarea>` element just above it.
   - In the "Styles" panel, find and uncheck the CSS properties like `opacity: 0`, `pointer-events: none` and remove the `d-none` class. The text area will appear. After that, just remove the disabled attribute from the `<textarea>` tag.
   - Alternatively, you can copy this entire script and paste in the devtools console:

     ```javascript
     let t = document.querySelector(
       'textarea[name="q-generate-addresses-with-llms"]',
     );
     t.classList.remove("d-none");
     t.style.opacity = 1;
     t.style.pointerEvents = "auto";
     t.disabled = false;
     ```

2. **Start the JSON Structure**: Begin with the main curly braces `{}`. Inside, define the top-level keys: `"model"`, `"messages"`, and `"response_format"`.

3. **Fill in `model` and `messages`**:
   - `"model": "gpt-4o-mini"`
   - `"messages": [{"role": "system", "content": "Respond in JSON"}, {"role": "user", "content": "Generate 10 random addresses in the US"}]`

4. **Define `response_format`**:
   - `"response_format": {"type": "json_schema", "json_schema": { ... }}`

5. **Build the JSON Schema**: This is the most detailed part.
   - The schema's root must be an object: `"schema": {"type": "object", ...}`.
   - It has one property, "addresses": `"properties": {"addresses": { ... }}`.
   - The "addresses" property is an array: `"type": "array", "items": { ... }`.
   - The `items` in the array are objects: `"type": "object", ...}`.
   - Define the properties for each address object based on the question (e.g., `"street": {"type": "string"}, "zip": {"type": "number"}`).
   - List all required fields in the `required` array: `"required": ["street", "city", "state", "zip", ...]` (use the fields from your specific question).
   - Prevent extra fields: `"additionalProperties": false`.

6. **Assemble the Final JSON**: Combine all the pieces into one valid JSON object. Use an online JSON validator to check for syntax errors like missing commas or braces.

## 4. Code / Configuration File

This is the final JSON body you should construct and paste into the answer box.
_(Note: The `properties` and `required` fields below are examples. Use the ones specified in your unique version of the question.)_

```json
{
  "model": "gpt-4o-mini",
  "messages": [
    {
      "role": "system",
      "content": "Respond in JSON"
    },
    {
      "role": "user",
      "content": "Generate 10 random addresses in the US"
    }
  ],
  "response_format": {
    "type": "json_schema",
    "json_schema": {
      "name": "address_list",
      "schema": {
        "type": "object",
        "properties": {
          "addresses": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "zip": {
                  "type": "number"
                },
                "street": {
                  "type": "string"
                },
                "longitude": {
                  "type": "number"
                }
              },
              "required": ["zip", "street", "longitude"],
              "additionalProperties": false
            }
          }
        },
        "required": ["addresses"],
        "additionalProperties": false
      }
    }
  }
}
```

## 5. How to Verify

The exam platform will parse your submitted text as JSON and verify it against a series of checks:

- Is it valid JSON?
- Is the `model` correct?
- Are the `messages` exactly as required?
- Does it use `response_format` with a `json_schema`?
- Does the schema correctly define the structure (addresses, array of objects, required properties, types, etc.)?
