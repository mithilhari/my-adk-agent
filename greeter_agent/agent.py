from google.adk.agents import Agent
from google.adk.tools import google_search
from google.adk.runner import LocalRunner
from pydantic import BaseModel, Field

# 1. DEFINE THE STRUCTURED OUTPUT (Pydantic Model)
class FactCheckResult(BaseModel):
    """The result of the fact-checking process."""
    is_correct: bool = Field(description="True if the user's statement is factually correct, False otherwise.")
    verified_fact: str = Field(description="The factual information verified by the search tool.")
    explanation: str = Field(description="A brief explanation of why the statement is correct or incorrect.")


# 2. DEFINE THE AGENT WITH A TOOL AND STRUCTURED OUTPUT
root_agent = Agent(
    name="fact_checker_agent",
    model="gemini-2.5-flash",
    description="A factual assistant that checks the truth of user statements.",
    instruction=(
        "You are an objective fact-checker. Your task is to use the 'google_search' tool "
        "to verify the factual correctness of the user's statement. "
        "Then, you MUST return the final answer using the FactCheckResult JSON schema."
    ),
    # Add the built-in tool
    tools=[google_search],
    # Specify the desired output structure
    output_schema=FactCheckResult
)

if __name__ == '__main__':
    print("--- Running ADK Fact-Checker Agent Locally ---")

    # 3. INITIALIZE AND RUN
    runner = LocalRunner()
    session = runner.create_session(root_agent)

    user_input = "The capital of Australia is Sydney."
    print(f"User Statement: {user_input}")

    # Run the agent
    try:
        response_event = runner.run_session(session, user_input)

        # 4. HANDLE THE STRUCTURED RESPONSE
        fact_check = response_event.content.struct

        print("\n--- Agent Result (Parsed JSON Object) ---")
        print(f"Is Correct: {fact_check.is_correct}")
        print(f"Verified Fact: {fact_check.verified_fact}")
        print(f"Explanation: {fact_check.explanation}")

    except Exception as e:
        print(f"\nAn error occurred during agent execution: {e}")
        print("Ensure your GOOGLE_API_KEY is set correctly in greeter_agent/.env.")
