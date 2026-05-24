from crewai import Task
from tools import tool
from agents import news_researcher,news_writer

research_task=Task(
    description=("Identify the next big trend in {topic}. Focus on Identifyinng pros and cons amd the overall narrative. Your final report should clearly articulate the key points, its markett oppurtunities,and the potencial risks."
),
expected_output='A comprehensive 3 paragraph long report on the latest AI trends.',
tools=[tool],
agent=news_researcher,
)
write_task=Task(
    description=("Compose an insightful article on {topic}. Focus on the latest trends and how it is impacting the industry. This article should be easy to understand, engaging and positive."
),
expected_output='A 4 paragraoh article on {topic} advancements formatted as markdown,',
tools=[tool],
agent=news_writer,
async_execution=False,
output_file='news-blog-post.md'
)