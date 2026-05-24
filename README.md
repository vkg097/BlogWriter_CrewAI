# BlogWriter_CrewAI
This project establishes an automated AI Content Generation Desk built using the CrewAI multi-agent framework. It orchestrates two specialized AI agents to autonomously research and write compelling, publication-ready technology articles on a given topic, initialized here for the AI in Finance sector.

# ✍️ Autonomous Tech Blog Writer & Researcher Crew

An automated, multi-agent content generation workflow powered by **CrewAI** and **Google Gemini 2.5 Flash**. This project coordinates a specialized research agent and a writing agent to track industry-defining tech trends and generate clean, engaging markdown blog posts using real-time search data.

---

## 🏗️ System Architecture

The project runs a sequential multi-agent execution thread:

---

## 📂 Project Structure

*   `agents.py`: Initializes the `gemini/gemini-2.5-flash` model and sets up the roles, goals, memories, and capabilities for the **Senior Researcher** and **Writer**.
*   `tasks.py`: Outlines the expectations, paragraph constraints, and file export parameters (`news-blog-post.md`) for both operations.
*   `tools.py`: Connects the environment keys and provisions the Google-powered `SerperDevTool` for active web scraping.
*   `crew.py`: Assembles the crew, schedules a sequential process, and triggers execution with the dynamic input parameters (`{'topic': 'AI in Finance'}`).

---

## 🚀 Getting Started

### Prerequisites

*   Python 3.10 to 3.12
*   A Gemini API Key (Google AI Studio)
*   A Serper API Key (for Google Search scraping)

### 1. Installation

Clone this repository and install the mandatory dependencies:

```bash
git clone [https://github.com/your-username/your-repo-name.git](https://github.com/your-username/your-repo-name.git)
cd your-repo-name
pip install crewai crewai-tools langchain-google-genai python-dotenv


### 2. Environment
GOOGLE_API_KEY=your_gemini_api_key_here
SERPER_API_KEY=your_serper_dev_api_key_here

### 3. Run Program
python crew.py
