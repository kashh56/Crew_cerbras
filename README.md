# CrewAI × Cerebras Research Platform

An advanced multi-agent research and analysis platform that combines CrewAI's collaborative agent framework with Cerebras's high-performance language models.

## Features

- 🤖 **Multi-Agent System**: Specialized agents working together for comprehensive research and analysis
- 🔍 **Web Research**: Integrated SerperDev search capabilities for real-time information gathering
- 💻 **Code Analysis**: Static code analysis with best practice recommendations
- ⚡ **High-Performance**: Powered by Cerebras's state-of-the-art language models
- 🎨 **Modern UI**: Streamlit-based interface with an intuitive and responsive design

## Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd <repository-name>
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables in a `.env` file:
```env
CEREBRAS_API_KEY=your_cerebras_api_key
SERPER_API_KEY=your_serper_api_key  # Optional, for web search functionality
```

## Usage

1. Start the application:
```bash
streamlit run app.py
```

2. Access the web interface at `http://localhost:8501`

3. Choose your task type:
   - Research Analysis: Investigate trends and developments
   - Code Analysis: Analyze Python code for improvements

4. Configure your preferences:
   - Select a Cerebras model
   - Choose output format
   - Enable/disable research tools

## Models

The platform supports various Cerebras models:
- Llama 4 Scout (17B)
- Llama 3.1 (8B)
- Llama 3.3 (70B)

## Dependencies

- streamlit
- crewai
- python-dotenv
- crewai-tools
- cerebras_cloud_sdk

