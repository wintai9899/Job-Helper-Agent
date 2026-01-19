"""Web search utilities for extracting job posting details using OpenAI."""

import os

from dotenv import load_dotenv
from openai import OpenAI
from langchain_core.tools import tool

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@tool
def search_job_posting(job_url: str) -> str:
    """Fetch and summarize a job posting from a URL using GPT-4o search.

    Args:
        job_url: URL of the job posting to analyze.

    Returns:
        Summary of the job posting including title, company,
        requirements, and responsibilities.
    """
    completion = client.chat.completions.create(
        model="gpt-4o-search-preview",
        web_search_options={
            "search_context_size": "medium",
        },
        messages=[
            {
                "role": "system",
                "content": "You are a helpful tool that visits job postings and extracts key details.",
            },
            {
                "role": "user",
                "content": f"""Visit this job posting and extract details: {job_url}
                Extract and summarize all key information including:
                - Job title
                - Company name
                - Location
                - Employment type (full-time, part-time, contract, etc.)
                - Salary or compensation (if available)
                - Required qualifications/skills
                - Primary responsibilities
                - Benefits offered
                - Application instructions
                - Posting date (if available)

                Format: Respond with a clear, structured bullet-point list.
                Use exact factual information from the posting.
                If the posting is missing or inaccessible, respond with:
                "Job posting unavailable or contains no job details."
                """,
            },
        ],
    )

    return completion.choices[0].message.content


if __name__ == "__main__":
    job_url = "https://www.linkedin.com/jobs/view/4353434335"
    print(search_job_posting(job_url))
