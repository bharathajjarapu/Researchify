import os
import streamlit as st
from dotenv import load_dotenv
from groq import Groq
from tavily import TavilyClient

load_dotenv()
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
tavily = TavilyClient(api_key=os.getenv('TAVILY_API_KEY'))

st.set_page_config(
    page_title="Research Assistant",
    page_icon=":book:",
)

st.title(":book: Research Assistant")

def generate_report(topic, search_results):
    description = "You are a Senior NYT Editor tasked with writing a NYT cover story worthy report due tomorrow, Report should be as human as it can be."
    instructions = [
        "You will be provided with a topic and search results from junior researchers.",
        "Carefully read the results and generate a final - NYT cover story worthy report.",
        "Make your report engaging, informative, and well-structured.",
        "Your report should follow the format provided below.",
        "Remember: you are writing for the New York Times, so the quality of the report is important.",
    ]
    report_format = """
## Title

- **Overview** Brief introduction of the topic.

- **Importance** Why is this topic significant now?

### Section 1
- **Detail 1**
- **Detail 2**
- **Detail 3**

### Section 2
- **Detail 1**
- **Detail 2**
- **Detail 3**

### Section 3
- **Detail 1**
- **Detail 2**
- **Detail 3**

## Conclusion
- **Summary of report:** Recap of the key findings from the report.
- **Implications:** What these findings mean for the future.

## References
- [Reference 1](Link URL to Source)
- [Reference 2](Link URL to Source)

"""
    prompt = f"{description}\n\nInstructions: {', '.join(instructions)}\n\nReport Format:\n{report_format}\n\nTopic: {topic}\n\nSearch Results:\n"
    for result in search_results:
        prompt += f"- {result['url']}\n{result['content']}\n\n"

    chat_completion = client.chat.completions.create(
        messages=[{"role": "user", "content": prompt}],
        model="llama3-8b-8192",
    )

    return chat_completion.choices[0].message.content

def main() -> None:
    input_topic = st.text_input("Enter a topic", value="The importance of Research Assistance in Research")
    generate_report_btn = st.button("Generate Report")

    if generate_report_btn:
        st.session_state["topic"] = input_topic
        report_topic = st.session_state["topic"]
        tavily_search_results = None

        with st.status("Searching Web", expanded=True) as status:
            tavily_search_results = tavily.search(report_topic, search_depth="advanced")
            if tavily_search_results:
                context = tavily_search_results.get('results', [])
            status.update(label="Web Search Complete", state="complete", expanded=False)

        if not context:
            st.write("Sorry report generation failed. Please try again.")
            return

        with st.spinner("Generating Report"):
            final_report = generate_report(report_topic, context)
            st.markdown(final_report)

if __name__ == "__main__":
    main()
