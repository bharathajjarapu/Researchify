import os
import streamlit as st
from langchain import hub
from dotenv import load_dotenv
from langchain.memory import ConversationBufferMemory
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_community.utilities import DuckDuckGoSearchAPIWrapper
from langchain_community.callbacks import StreamlitCallbackHandler
from langchain.agents import AgentExecutor, Tool, create_react_agent, AgentType, initialize_agent
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain_community.tools.pubmed.tool import PubmedQueryRun

load_dotenv()
genai = GoogleGenerativeAIEmbeddings(model="gemini-pro", api_key=os.getenv("GOOGLE_API_KEY"))

def setup_agent():
    llm = ChatGoogleGenerativeAI(model="gemini-pro", temperature=0.7)
    wrapper = DuckDuckGoSearchAPIWrapper(max_results=2)
    ddg_search = DuckDuckGoSearchRun(api_wrapper=wrapper)
    wiki = WikipediaAPIWrapper()
    pubmed = PubmedQueryRun()
    tools = [
        Tool(
            name="WikipediaQueryRun",
            func=wiki.run,
            description="Look up things in Wikipedia for people, movies, series and information",
        ),
        Tool(
            name='Pubmed Science and Medical Journal Research Tool',
            func=pubmed.run,
            description='Useful for Searching Scientifically Legit Information from Pubmed science and medical research\nPubMed comprises more than 35 million citations for biomedical literature from MEDLINE, life science journals, and online books. Citations may include links to full text content from PubMed Central and publisher web sites.'
        ),
        Tool(
            name="DuckDuckGoSearch",
            func=ddg_search.run,
            description="Useful for when you need to answer questions about current events or realtime information. You should ask targeted questions",
        )
    ]

    prompt = hub.pull("hwchase17/react-chat")
    llm = ChatGoogleGenerativeAI(model="gemini-pro", temperature=0.7)
    memory = ConversationBufferMemory(memory_key="chat_history")
    agent = create_react_agent(llm, tools, prompt)
    agent_executor = AgentExecutor(agent=agent, tools=tools, memory=memory, verbose=True)
    return agent_executor, memory

def main():
    agent_executor, memory = setup_agent()
    if "messages" not in st.session_state:
        st.session_state.messages = []

    user_query = st.text_input(label="Ask me anything!", placeholder="Type your query here...")
    if user_query:
        st.session_state.messages.append({"role": "user", "content": user_query})
        with st.chat_message("user"):
            st.write(user_query)

        with st.chat_message("assistant"):
            st_cb = StreamlitCallbackHandler(st.container())
            result = agent_executor.invoke(
                {"input": user_query, "chat_history": st.session_state.messages},
                {"callbacks": [st_cb]}
            )
            response = result["output"]
            st.session_state.messages.append({"role": "assistant", "content": response})
            st.write(response)

if __name__ == "__main__":
    st.set_page_config(page_title="Researchify", page_icon=":book:")
    main()
