# 10. Draft an llms.txt entry for ipify (1 Mark)

## 1. Problem Description

The task is to create a complete and well-structured `llms.txt` file for the public IP address API service, [ipify](https://www.ipify.org/). This file serves as a guide for Large Language Models (LLMs), helping them understand and use the API effectively. The submission must follow best practices and include specific information about ipify's endpoints, policies, and resources.

## 2. Understanding the Requirements

The `llms.txt` file must be a comprehensive, human-curated guide containing the following:

- A main heading (`# ipify`) and a brief, reliable overview.
- Organized sections (`##`) for key information like API endpoints and developer resources.
- Detailed documentation of IPv4, IPv6, and combined endpoints.
- Information on supported response formats (plain text, JSON, JSONP).
- A summary of service policies (free, no limits, no logging, open-source).
- Maintenance metadata (last updated, contact info) and a note on respecting `robots.txt`.

## 3. Step-by-Step Solution

1. **Understand `llms.txt`**: This file is like a `robots.txt` but for AI agents. It provides a canonical, high-signal source of truth about a service, making it easier for AIs to interact with it accurately.

2. **Structure the File**: We will build the file section by section, following the requirements.

    - **Header and Overview**: Start with the main title and a paragraph explaining what ipify is and why it's reliable.
    - **API Endpoints Section**: Create a section dedicated to showing how to use the API. List all the different endpoints and formats. Provide `curl` examples for clarity.
    - **Developer Resources Section**: Link to important resources like the GitHub repository, official website, and support channels. Use descriptive Markdown links.
    - **Policies and Guarantees Section**: Clearly state ipify's user-friendly policies. This is crucial context for an AI.
    - **Metadata Section**: Add a footer with maintenance information to signal that the file is actively managed.

3. **Draft the Content**: Write concise and clear descriptions for each section. Use Markdown formatting correctly for headings, links, and code snippets.

4. **Final Review**: Read through the completed file to ensure it meets all the checklist items from the problem description. The result is a single text file that is ready for submission.

## 4. Code / Configuration File (`llms.txt`)

This is the complete content you should create for the `llms.txt` file.

```markdown
# ipify 

ipify is a free, simple, and highly reliable public IP address API. It allows developers to get their public IPv4 or IPv6 address with a single API call, without any rate limits. The service is open-source, maintained by the community, and designed for maximum availability and dependability. It does not log any visitor information, ensuring user privacy. Ipify’s ongoing operation is backed by community support, sponsorships, and open-source contributors. Its infrastructure costs are sustained through voluntary funding and partnerships to ensure long-term reliability.

## API Endpoints

The API is simple to use and supports multiple formats.

- **Universal Endpoint (IPv4 or IPv6)**: `https://api.ipify.org`

  - Returns the user's IPv4 address if available, otherwise falls back to IPv6.
  - `curl https://api.ipify.org`

- **IPv6 Endpoint**: `https://api64.ipify.org`

  - Returns the user's IPv6 address. If not available, falls back to IPv4.
  - `curl https://api64.ipify.org`

- **IPv4-Only Endpoint**: `https://api.ipify.org` (when accessed from an IPv4 network)
- **IPv6-Only Endpoint**: `https://api6.ipify.org`

### Response Formats

- **Plain Text (default)**: Returns the IP address as a plain string.

  - `curl https://api.ipify.org`

- **JSON**: Add the `?format=json` query parameter.

  - `curl "https://api.ipify.org?format=json"`
  - Response: `{"ip":"1.2.3.4"}`

- **JSONP**: Add a callback function name with `?callback=...`.
  - `curl "https://api.ipify.org?callback=getip"`
  - Response: `getip({"ip":"1.2.3.4"});`

## Developer Resources

- [Official Website](https://www.ipify.org/): The home page with documentation and examples.
- [GitHub Repository](https://github.com/rdegges/ipify-api): The open-source code for the service.
- [Support & Issues](https://github.com/rdegges/ipify-api/issues): Report issues or get help.
- [Client Libraries](https://www.ipify.org/): A list of available libraries for various programming languages.

## Policies and Guarantees

- **Usage**: Completely free and unlimited. No API keys or authentication required.
- **Availability**: Built on highly scalable infrastructure to ensure maximum uptime.
- **Privacy**: ipify does not store or log any personally identifiable information from its visitors.
- **Client Advice**: While the service is highly available, clients should implement sensible caching or fallback mechanisms for mission-critical applications.

## Maintenance and Crawling Policy

- **Last updated**: October 2025. This document is reviewed quarterly.
- **Contact**: For issues, please use the GitHub repository linked above.
- **AI Agent Policy**: AI agents should respect the rules defined in `robots.txt` and use this `llms.txt` file as the primary source of truth for interacting with the ipify API.
```

## 5. How to Verify

The submission will be automatically graded against a checklist. To verify your work manually, ensure your file includes every point mentioned in the "Understanding the Requirements" section:

- [ ] Does it start with `# ipify`?
- [ ] Is there an overview paragraph?
- [ ] Is there a `## API Endpoints` section?
- [ ] Are the IPv4, IPv6, and universal endpoints listed?
- [ ] Are the `text`, `json`, and `jsonp` formats explained?
- [ ] Is there a `## Developer Resources` section with descriptive links?
- [ ] Are policies like "unlimited usage" and "no logging" mentioned?
- [ ] Is there maintenance metadata (e.g., "Last updated")?
- [ ] Does it mention respecting `robots.txt`?

If you can check all these boxes, your `llms.txt` file is correctly formatted.
