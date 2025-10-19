# Summary of all the questions

### **Question 1: LLM Sentiment Analysis**

- **What it Covered:** Writing a **Python** script to perform a sentiment analysis task. The script uses the `httpx` library to make a `POST` request to an OpenAI-compatible API, sending a system prompt and user text to the `gpt-4o-mini` model.
- **Why you need it:** This is a fundamental skill for using LLMs for classification. It demonstrates how to interact with an AI API programmatically, handle authentication, and structure prompts for specific tasks, a common pattern in many AI applications.

### **Question 2: LLM Token Cost**

- **What it Covered:** Using OpenAI's official **Tokenizer tool** to accurately calculate the number of input tokens for a given piece of text for the `gpt-4o-mini` model. The task includes adding the model-specific overhead tokens to get the final count.
- **Why you need it:** Understanding tokenization is crucial for managing API costs and staying within model context limits. Accurately predicting token count is a vital skill for building efficient and scalable applications on top of LLMs.

### **Question 3: Generate addresses with LLMs hjjjjjjjjjj**

- **What it Covered:** Constructing a complex **JSON request body** to force an LLM (`gpt-4o-mini`) to generate structured data. This involves using the `response_format` feature with a detailed `json_schema` to define the exact output structure for a list of addresses.
- **Why you need it:** This teaches how to get reliable, machine-readable data from an LLM. Forcing structured output via JSON schema is essential for building robust applications that can programmatically consume and validate AI-generated content without flaky parsing.

### **Question 4: LLM Vision**

- **What it Covered:** Crafting a **JSON request** for a multimodal vision model (`gpt-4o-mini`) to analyze an image. The prompt combines a text instruction with an image provided as a **base64 data URL** within a single API call.
- **Why you need it:** This demonstrates proficiency with multimodal AI. Being able to send both images and text to an AI for analysis is a key skill for building applications that can "see" and interpret the visual world.

### **Question 5: LLM Embeddings**

- **What it Covered:** Creating a **JSON request body** for the OpenAI Embeddings API. The request asks the `text-embedding-3-small` model to convert two sentences into their numerical vector representations (embeddings).
- **Why you need it:** This introduces the core concept of embeddings, which power semantic search, RAG, and recommendation systems. Knowing how to generate embeddings is the first step to building more advanced AI systems that understand meaning.

### **Question 6: Multimodal Embeddings**

- **What it Covered:** Using a multimodal API (**Jina AI**) to generate embeddings for both an image and a text phrase. The task required writing a **Python** script to make the API call and then use `numpy` to calculate the **dot product** (similarity score) between the two resulting vectors.
- **Why you need it:** This skill shows how to quantify the relationship between different types of data. Calculating similarity between text and image embeddings is fundamental to building cross-modal search engines (e.g., searching images with text) and other advanced multimodal applications.

### **Question 7: Embedding Similarity**

- **What it Covered:** Writing a **Python** function that calculates the **cosine similarity** between all pairs of embedding vectors in a given dictionary and returns the two text phrases that are most similar.
- **Why you need it:** This is the practical application of embeddings. This logic is the core engine behind semantic search, finding related documents, and clustering text based on meaning, demonstrating a key data science skill.

### **Question 8: Vector Databases**

- **What it Covered:** Building a semantic search web service using **FastAPI**. The API endpoint takes a list of documents and a query, uses the OpenAI API to generate embeddings, calculates **cosine similarity**, and returns the top 3 most relevant documents.
- **Why you need it:** This task simulates building a simple vector database search system from scratch. It's a foundational skill for creating RAG (Retrieval Augmented Generation) systems and AI-powered search features, combining API development with core AI concepts.

### **Question 9: RAG: TypeScript Book**

- **What it Covered:** Building a complete **Retrieval Augmented Generation (RAG)** system as a **FastAPI** service. The process involved indexing the content of the "TypeScript Book" into a local vector database, and then creating an API that retrieves relevant chunks to answer user questions based only on that context.
- **Why you need it:** RAG is a state-of-the-art technique for making LLMs more accurate and trustworthy. Building a full RAG pipeline demonstrates a highly valuable and practical skill for creating knowledgeable AI assistants, chatbots, and Q&A systems.

### **Question 10: Function Calling**

- **What it Covered:** Creating a **FastAPI** endpoint that interprets natural language commands. The solution uses **regular expressions** to parse a user's query, identify which predefined function to call, extract the necessary arguments, and return a structured **JSON** response.
- **Why you need it:** This demonstrates the core principle behind AI agents and tools. Translating unstructured language into structured, executable commands is a critical skill for integrating AI into software workflows and building interactive assistants.

### **Question 11: Get an LLM to say Yes**

- **What it Covered:** A creative **prompt engineering** challenge. The goal was to bypass an AI model's strict instruction to never say the word "Yes" by crafting a clever prompt (a "jailbreak") that forces it to output the forbidden word.
- **Why you need it:** This teaches advanced prompt engineering and adversarial thinking. Understanding how to probe and bypass model restrictions is key to testing for security vulnerabilities, understanding model limitations, and becoming a more effective AI practitioner.

### **Question 12: LLM Image Generation**

- **What it Covered:** Constructing a **JSON request body** for the OpenAI Image Generation API. The task involved correctly specifying the `model`, `prompt`, number of images (`n`), `size`, and `response_format`.
- **Why you need it:** This shows how to programmatically generate visual content using AI. This skill is essential for applications in automated content creation, design tools, marketing, and creative arts.

### **Question 13: LLM Speech**

- **What it Covered:** Writing a **JSON request body** for OpenAI's Text-to-Speech (TTS) API. This required specifying the `model`, `input` text, `voice`, speaking `speed`, and audio `response_format`.
- **Why you need it:** This demonstrates how to integrate audio and voice into applications. Text-to-speech is a key feature for accessibility, voice assistants, podcast generation, and creating more engaging user experiences.

### **Question 14: LLM Evaluation**

- **What it Covered:** Creating a configuration file (`promptfooconfig.yaml`) for the **PromptFoo** testing framework. The configuration set up a test to compare three different LLMs on their ability to generate a `curl` command, using assertions like `contains` and `llm-rubric` to automatically verify the output.
- **Why you need it:** This introduces the critical skill of automated LLM evaluation. As you build AI systems, being able to systematically test, compare, and validate the performance of different prompts and models is essential for ensuring quality and reliability (a core concept in MLOps).


## To learn more about these

**Basic Usage**
* [Prompt engineering](https://tds.s-anand.net/#/prompt-engineering.md)
* [TDS TA Instructions](https://tds.s-anand.net/#/tds-ta-instructions.md)
* [TDS GPT Reviewer](https://tds.s-anand.net/#/tds-gpt-reviewer.md)

**Text Processing**
* [LLM Sentiment Analysis](https://tds.s-anand.net/#/llm-sentiment-analysis.md)
* [LLM Text Extraction](https://tds.s-anand.net/#/llm-text-extraction.md)
* [Base 64 Encoding](https://tds.s-anand.net/#/base64-encoding.md)

**Embeddings**
* [Embeddings](https://tds.s-anand.net/#/embeddings.md)
* [Multimodal Embeddings](https://tds.s-anand.net/#/multimodal-embeddings.md)
* [Topic modeling](https://tds.s-anand.net/#/topic-modeling.md)

**RAG**
* [Vector databases](https://tds.s-anand.net/#/vector-databases.md)
* [RAG with the CLI](https://tds.s-anand.net/#/rag-cli.md)
* [Hybrid RAG with TypeSense](https://tds.s-anand.net/#/hybrid-rag-typesense.md)

**Multimodal**
* [Vision Models](https://tds.s-anand.net/#/vision-models.md)
* [LLM Image Generation](https://tds.s-anand.net/#/llm-image-generation.md)
* [LLM Speech](https://tds.s-anand.net/#/llm-speech.md)

**LLM Applications**
* [Function Calling](https://tds.s-anand.net/#/function-calling.md)
* [LLM Agents](https://tds.s-anand.net/#/llm-agents.md)
* [Pydantic AI](https://tds.s-anand.net/#/pydantic-ai.md)
* [LLM Evals](https://tds.s-anand.net/#/llm-evals.md)