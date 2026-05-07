Campus Q&A

Problem  Statement:
Campus Event Q&A Assistant that answers students' questions about upcoming campus events. The assistant must connect to Gemini via an API call, send the student's query along with event data, and return structured responses.

Unlike complex systems, this assistant focuses on basic API integration with structured JSON responses for event-related queries and conversational responses for off-topic questions.



Scenario



Your campus assistant needs to:



Answer student questions about upcoming campus events
Provide structured information including dates, locations, and details
Return JSON responses for event queries
Handle off-topic queries with conversational responses


The assistant should:



Return structured JSON (for event-related queries)
Provide conversational responses (for off-topic questions)
Use campus event database (curated event information)


Expected JSON Response Format



For event-related queries, return this exact JSON structure:

{
  "event_name": "Tech Fest",
  "date": "2025-09-15",
  "location": "Main Auditorium",
  "response": "The Tech Fest will be held on 15th September at the Main Auditorium."
}
For non-event queries (e.g., "Tell me a joke"), respond with plain text only (no JSON).



Available Campus Events Database



The assistant has access to these upcoming campus events:



Tech Fest: 2025-09-15 at Main Auditorium - Annual technology festival featuring coding competitions, tech talks, and innovation showcases
Career Fair: 2025-10-20 at Student Center - Connect with top companies and explore internship and job opportunities
Hackathon: 2025-11-10 at Computer Science Building - 48-hour coding competition with prizes and networking opportunities
Music Concert: 2025-12-05 at Campus Amphitheater - End-of-semester concert featuring student bands and guest artists
Science Exhibition: 2025-11-25 at Science Hall - Showcase of student research projects and scientific innovations
Sports Day: 2025-10-15 at Sports Complex - Annual sports competition with various athletic events and team competitions
Art Gallery Opening: 2025-09-30 at Fine Arts Building - Opening of the student art gallery featuring works from various art programs
Research Symposium: 2025-11-18 at Conference Center - Graduate and undergraduate research presentations across all departments
Cultural Night: 2025-12-12 at Student Union - Celebration of diverse cultures with food, performances, and cultural displays
Workshop Series: 2025-10-08 at Library Conference Room - Professional development workshops on resume building, interview skills, and career planning


Implementation Requirements



You need to implement an assistant that can:



Connect to Gemini API – establish proper API connection with authentication
Process Event Queries – identify when students ask about specific campus events
Return Structured Data – format event responses with exact required fields
Handle Off-Topic Queries – provide conversational responses for non-event questions
Manage API Errors – handle failures and timeouts gracefully


Your assistant must:



Read API key from environment variable *GEMINI_API_KEY*
Include the complete event database in system prompts
Return valid JSON for event-related queries
Provide conversational responses for off-topic queries
Handle API errors with appropriate error messages


Expected Outputs


1. Event Query Examples

User: "Where is the Tech Fest happening?"
→ Output: {
    "event_name": "Tech Fest",
    "date": "2025-09-15",
    "location": "Main Auditorium",
    "response": "The Tech Fest will be held on 15th September at the Main Auditorium."
  }

User: "When is the Career Fair?"
→ Output: {
    "event_name": "Career Fair",
    "date": "2025-10-20",
    "location": "Student Center",
    "response": "The Career Fair will be held on 20th October at the Student Center."
  }


2. Off-Topic Query Examples

User: "Tell me a joke"
→ Output: "Sure! Here's one: Why don't programmers like nature? It has too many bugs!"

User: "What's the weather like?"
→ Output: "I'm here to help with campus events! Are you looking for information about any upcoming events?"


Implementation Notes



Use prompt.txt for the system prompt with complete event database
Include clear JSON formatting instructions for the model
Handle API errors gracefully with appropriate error messages
Implement retry logic for better reliability
Test both successful and error scenarios
Ensure structured responses for event queries only


Test Locally Before Submitting



Run at least 4-5 test queries before submitting
Test different event information requests (dates, locations, details)
Test off-topic queries to ensure conversational responses
Verify JSON structure matches exactly
Test API error handling (invalid keys, network issues)
Check that all event details are accurate


Hints


Include the entire event database in your system prompt for context
Be explicit about JSON formatting requirements in the prompt
Use environment variables for secure API key management
Test with various event request phrasings: "when", "where", "tell me about"
Remember: only event queries should return JSON, everything else is conversational