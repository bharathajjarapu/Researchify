# 📚 Researchify

Welcome to the **AI Researcher** project! This nifty tool harnesses the power of Large Language Models (LLMs) and advanced web searching to help you craft top-notch reports on any topic. 🤓✨

## 🌟 Features

- **Dynamic Topic Input:** Just type in your topic, and let the magic begin! 🧙‍♂️
- **Web Search Integration:** Uses **Tavily** to scour the web for the best sources. 🌐🔍
- **LLM-Powered Reports:** Employs **Groq**'s LLM to generate comprehensive, human-like reports. 📝🧠
- **Streamlit Interface:** User-friendly interface for seamless interaction. 🖥️✨

## 🚀 Getting Started

### Prerequisites

- **Python 3.8+**
- **Streamlit**
- **dotenv**
- **Gemini API Key**
- **Tavily API Key**

### Installation

Clone this repository and navigate to the project directory:

```bash
git clone https://github.com/bharathajjarapu/researchify.git
cd researchify
```

Install the required packages:

```bash
pip install -r requirements.txt
```

Create a `.env` file and add your API keys:

```plaintext
GOOGLE_API_KEY=your_gemini_api_key
TAVILY_API_KEY=your_tavily_api_key
```

### Running the App

Fire up the Streamlit app:

```bash
streamlit run app.py
```

## 🛠️ How It Works

1. **User Input:** Enter your topic in the text box.
2. **Web Search:** The app uses Tavily to perform an in-depth web search on the topic.
3. **PubMed Search:** The app uses PubMed Research Documents to cite the Relavent Information.
4. **Wikipedia Search:** The app uses Wikipedia Look up things for people, movies, series and information.
5. **Report Generation:** Groq's LLM takes the search results and crafts a well-structured, NYT-worthy report.
6. **Display:** The final report is displayed beautifully in the Streamlit interface.

### Code Breakdown

- **Environment Setup:** Loads API keys from `.env` file.
- **Streamlit Config:** Sets up the page title and icon.
- **Main Interface:** Provides an input box for the topic and a button to generate the report.
- **Web Search:** Uses TavilyClient to fetch search results.
- **PubMed Search:** The app uses PubMed Research Documents to cite the Relavent Information.
- **Wikipedia Search:** The app uses Wikipedia Look up things for people, movies, series and information.
- **Report Generation:** Groq's LLM processes the results and generates the report.
- **Output:** Displays the final report in Markdown format.

## 📖 Example Report Structure

Here's what a generated report looks like:

```
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
```

## 📬 Contributions & Issues

Feel free to contribute! Fork the repo, make your changes, and send a pull request. For issues or questions, open a ticket or hit me up directly.

## Acknowledgement

Use this project for learning not just copy pasting the repo for a hackathon, though you might win the hackathon but sure will never learn how it works.

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

Happy researching! 🎓🧐
