import streamlit as st
from crewai import Agent, Task, Crew, Process, LLM
from crewai_tools import SerperDevTool, CodeInterpreterTool
from agents import get_researcher
import os
from dotenv import load_dotenv
from styles import apply_custom_styles, display_header, display_about, tool_card
from config import MODELS, TOOLS, TASK_TYPES, OUTPUT_FORMATS

# Set page config must be the first Streamlit command
st.set_page_config(
    page_title="CrewAI × Cerebras",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load environment variables
load_dotenv()

# Apply custom styles
apply_custom_styles()

# Display header
st.markdown("""
    <div style="padding: 2rem 0;">
        <h1 style="
            color: #FF6B2B;
            text-shadow: 
                0 0 20px rgba(255, 107, 43, 0.9),
                0 0 40px rgba(255, 107, 43, 0.7),
                0 0 60px rgba(255, 107, 43, 0.5),
                0 0 80px rgba(255, 107, 43, 0.3);
            font-weight: 800;
            font-size: 4rem;
            letter-spacing: 2px;
            margin-bottom: 0.5rem;
            background: transparent;">CrewAI × Cerebras</h1>
        <p style="
            color: #FF8F3F;
            text-shadow: 
                0 0 10px rgba(255, 143, 63, 0.8),
                0 0 20px rgba(255, 143, 63, 0.4);
            font-size: 1.2rem;
            letter-spacing: 1px;
            opacity: 0.9;
            background: transparent;">Advanced Multi-Agent Research & Analysis Platform</p>
    </div>
""", unsafe_allow_html=True)

# Display about section
st.markdown("""
    <div class="about-section" style="background: linear-gradient(135deg, rgba(13, 17, 23, 0.95) 0%, rgba(33, 37, 43, 0.90) 100%); border: 1px solid rgba(78, 205, 196, 0.2);">
        <h2 class="about-title" style="color: #4ECDC4; text-shadow: 0 0 10px rgba(78, 205, 196, 0.3);">
            About This Project 
            <span style="font-size: 1.8rem; margin-left: 8px; filter: drop-shadow(0 0 5px rgba(78, 205, 196, 0.5));">🧪</span>
        </h2>
        <p class="about-description" style="color: #E0E0E0; text-shadow: 0 0 2px rgba(224, 224, 224, 0.1);">
            This platform combines the power of CrewAI's multi-agent framework with Cerebras's lightning-fast inference capabilities. 
            It enables sophisticated AI workflows where multiple agents collaborate to perform complex research and analysis tasks.
        </p>
        <div class="features-grid">
            <div class="feature-card" style="background: linear-gradient(135deg, rgba(33, 37, 43, 0.8) 0%, rgba(43, 47, 53, 0.8) 100%); border: 1px solid rgba(78, 205, 196, 0.15); backdrop-filter: blur(10px);">
                <div class="feature-icon" style="color: #4ECDC4; font-size: 24px; text-shadow: 0 0 10px rgba(78, 205, 196, 0.5);">🤖</div>
                <div class="feature-title" style="color: #4ECDC4; font-weight: 600;">Advanced Research Analysis</div>
                <div class="feature-description" style="color: #B8B8B8;">
                    Multiple specialized agents working together to deliver comprehensive insights
                </div>
            </div>
            <div class="feature-card" style="background: linear-gradient(135deg, rgba(33, 37, 43, 0.8) 0%, rgba(43, 47, 53, 0.8) 100%); border: 1px solid rgba(78, 205, 196, 0.15); backdrop-filter: blur(10px);">
                <div class="feature-icon" style="color: #4ECDC4; font-size: 24px; text-shadow: 0 0 10px rgba(78, 205, 196, 0.5);">💻</div>
                <div class="feature-title" style="color: #4ECDC4; font-weight: 600;">Code Analysis</div>
                <div class="feature-description" style="color: #B8B8B8;">
                    Intelligent code interpretation and improvement suggestions
                </div>
            </div>
            <div class="feature-card" style="background: linear-gradient(135deg, rgba(33, 37, 43, 0.8) 0%, rgba(43, 47, 53, 0.8) 100%); border: 1px solid rgba(78, 205, 196, 0.15); backdrop-filter: blur(10px);">
                <div class="feature-icon" style="color: #4ECDC4; font-size: 24px; text-shadow: 0 0 10px rgba(78, 205, 196, 0.5);">🔍</div>
                <div class="feature-title" style="color: #4ECDC4; font-weight: 600;">SerperDev Integration</div>
                <div class="feature-description" style="color: #B8B8B8;">
                    Powerful web search capabilities for comprehensive research
                </div>
            </div>
            <div class="feature-card" style="background: linear-gradient(135deg, rgba(33, 37, 43, 0.8) 0%, rgba(43, 47, 53, 0.8) 100%); border: 1px solid rgba(78, 205, 196, 0.15); backdrop-filter: blur(10px);">
                <div class="feature-icon" style="color: #4ECDC4; font-size: 24px; text-shadow: 0 0 10px rgba(78, 205, 196, 0.5);">⚡</div>
                <div class="feature-title" style="color: #4ECDC4; font-weight: 600;">Cerebras Powered</div>
                <div class="feature-description" style="color: #B8B8B8;">
                    State-of-the-art language models for superior performance
                </div>
            </div>
        </div>
    </div>
""", unsafe_allow_html=True)

# Sidebar configuration
with st.sidebar:
    st.markdown("""
        <div style='text-align: center; margin-bottom: 1.5rem;'>
            <h2 style='color: #4ECDC4; font-size: 2.2rem; font-weight: 600; text-shadow: 0 0 10px rgba(78, 205, 196, 0.3);'>Configuration</h2>
        </div>
    """, unsafe_allow_html=True)

    # Model selection with icons and descriptions
    st.markdown("<h3 style='color: #FF6B6B;'>🤖 Model Selection</h3>", unsafe_allow_html=True)
    model_name = st.selectbox(
        "Choose your model",
        options=list(MODELS.keys()),
        format_func=lambda x: f"{MODELS[x]['icon']} {MODELS[x]['name']}",
        help="Select the model to use for research"
    )
    st.markdown(f"<p style='font-size: 0.9em; color: #B8B8B8;'>{MODELS[model_name]['description']}</p>", unsafe_allow_html=True)

    # Task Type Selection
    st.markdown("<h3 style='color: #FF6B6B; margin-top: 2rem;'>🎯 Task Type</h3>", unsafe_allow_html=True)
    task_type = st.radio(
        "Select your task",
        options=list(TASK_TYPES.keys()),
        format_func=lambda x: f"{TASK_TYPES[x]['icon']} {TASK_TYPES[x]['name']}",
        help="Choose between research analysis or code interpretation"
    )
    is_code_task = task_type == "code"

# Get and validate API keys
try:
    cerebras_api_key = os.environ["CEREBRAS_API_KEY"]
except KeyError:
    st.error("🔑 Cerebras API key not found in .env file.")
    st.info("Please add CEREBRAS_API_KEY to your .env file.")
    st.stop()

# Configure LLM
llm = LLM(
    model=model_name,
    api_key=cerebras_api_key,
    base_url="https://api.cerebras.ai/v1",
    temperature=0.5
)

# Initialize tools
tools = []

# Tool selection (only for research task)
selected_tools = []
if not is_code_task:
    with st.sidebar:
        st.markdown("<h3 style='color: #FF6B6B; margin-top: 2rem;'>🛠️ Tools</h3>", unsafe_allow_html=True)
        
        for tool_id, tool_config in TOOLS.items():
            use_tool = st.checkbox(
                f"{tool_config['icon']} {tool_config['name']}",
                value=tool_config['default'],
                help=tool_config['description']
            )
            
            if use_tool:
                if tool_id == "serper":
                    try:
                        serper_api_key = os.environ["SERPER_API_KEY"]
                        selected_tools.append(SerperDevTool(api_key=serper_api_key))
                    except KeyError:
                        st.warning("⚠️ SerperDev API key missing")

# Main content area
if is_code_task:
    st.markdown(f"<h2 style='color: #4ECDC4; margin-top: 2rem;'>{TASK_TYPES['code']['icon']} Code Analysis</h2>", unsafe_allow_html=True)
    research_goal = st.text_area(
        "Enter your code",
        value="def example(x, y):\n    return x + y",
        height=200,
        help="Enter the Python code you want to analyze"
    )
    output_format = "Code Analysis"
else:
    st.markdown(f"<h2 style='color: #4ECDC4; margin-top: 2rem;'>{TASK_TYPES['research']['icon']} Research Configuration</h2>", unsafe_allow_html=True)
    research_goal = st.text_area(
        "Research Goal",
        value="Analyze recent developments and key trends.",
        height=100,
        help="What should the research aim to achieve?"
    )
    
    # Output format selection with icons
    output_format = st.selectbox(
        "Select Output Format",
        options=list(OUTPUT_FORMATS.keys()),
        format_func=lambda x: f"{OUTPUT_FORMATS[x]['icon']} {OUTPUT_FORMATS[x]['name']}",
        help="Choose how you want the research to be presented"
    )
    st.markdown(f"<p style='font-size: 0.9em; color: #B8B8B8;'>{OUTPUT_FORMATS[output_format]['description']}</p>", unsafe_allow_html=True)

# Run button with loading animation
if st.button("🚀 " + ("Analyze Code" if is_code_task else "Start Research"), type="primary"):
    if not research_goal:
        st.error("Please provide the " + ("code" if is_code_task else "research goal") + ".")
        st.stop()
        
    with st.spinner("🔄 " + ("Analyzing code..." if is_code_task else "Conducting research...")):
        try:
            if is_code_task:
                # Code analysis setup - static analysis only
                code_analyst = Agent(
                    role="Python Code Analyst",
                    goal="Analyze Python code for quality, structure, and best practices",
                    backstory="Expert Python developer specializing in code analysis, optimization, and best practices",
                    llm=LLM(
                        model=model_name,
                        api_key=cerebras_api_key,
                        base_url="https://api.cerebras.ai/v1",
                        temperature=0.5
                    ),
                    verbose=True
                )
                
                analysis_task = Task(
                    description=f"Analyze this Python code:\n{research_goal}",
                    expected_output="Analysis report with code quality assessment and recommendations",
                    agent=code_analyst
                )
            else:
                # Research setup
                researcher = Agent(
                    role="Research Analyst",
                    goal="Conduct comprehensive research and analysis on emerging trends and developments",
                    backstory="""Expert research analyst with deep expertise in analyzing market trends, technological developments, and industry patterns. 
                    Skilled at synthesizing complex information from multiple sources to provide actionable insights.""",
                    tools=selected_tools,
                    llm=LLM(
                        model=model_name,
                        api_key=cerebras_api_key,
                        base_url="https://api.cerebras.ai/v1",
                        temperature=0.5
                    ),
                    verbose=True
                )

                research_task = Task(
                    description=research_goal,
                    expected_output=f"{OUTPUT_FORMATS[output_format]['name']}",
                    agent=researcher
                )

            # Simplified crew setup
            crew = Crew(
                agents=[code_analyst if is_code_task else researcher],
                tasks=[analysis_task if is_code_task else research_task],
                process=Process.sequential,
                verbose=True
            )
            
            # Progress tracking with custom styling
            col1, col2, col3 = st.columns([1,2,1])
            with col2:
                progress_bar = st.progress(0)
                status_text = st.empty()
                
            for i in range(4):
                progress_bar.progress((i + 1) * 25)
                status_text.markdown(f"<div style='text-align: center; color: #4ECDC4;'>Phase {i+1}/4: {['Initializing', 'Research', 'Analysis', 'Finalizing'][i]}</div>", unsafe_allow_html=True)
                
            # Get results
            result = crew.kickoff()
            
            # Clear progress indicators
            progress_bar.empty()
            status_text.empty()
            
            # Display results in a styled container
            st.success("✨ " + ("Analysis completed!" if is_code_task else "Research completed!"))
            
            # Custom styling for the results container
            st.markdown("""
            <style>
            .results-container {
                background: linear-gradient(135deg, rgba(13, 17, 23, 0.95) 0%, rgba(33, 37, 43, 0.90) 100%);
                border: 1px solid rgba(78, 205, 196, 0.2);
                border-radius: 10px;
                padding: 2rem;
                margin: 1rem 0;
            }
            .results-title {
                color: #4ECDC4;
                font-size: 2rem;
                font-weight: 600;
                margin-bottom: 1.5rem;
                text-shadow: 0 0 10px rgba(78, 205, 196, 0.3);
            }
            .results-content {
                color: #E0E0E0;
                font-size: 1.1rem;
                line-height: 1.6;
            }
            .results-content h1, .results-content h2, .results-content h3 {
                color: #FF6B6B;
                margin-top: 1.5rem;
                margin-bottom: 1rem;
                text-shadow: 0 0 10px rgba(255, 107, 107, 0.3);
            }
            .results-content ul {
                list-style-type: none;
                padding-left: 0;
            }
            .results-content li {
                margin: 1rem 0;
                padding: 1rem;
                background: linear-gradient(135deg, rgba(33, 37, 43, 0.8) 0%, rgba(43, 47, 53, 0.8) 100%);
                border: 1px solid rgba(78, 205, 196, 0.15);
                border-radius: 8px;
                transition: all 0.3s ease;
            }
            .results-content li:hover {
                transform: translateX(5px);
                border-color: rgba(78, 205, 196, 0.3);
                box-shadow: 0 0 15px rgba(78, 205, 196, 0.1);
            }
            .results-content strong {
                color: #FF8F3F;
                font-weight: 600;
            }
            </style>
            """, unsafe_allow_html=True)

            # Display results with custom styling
            st.markdown(f"""
            <div class="results-container">
                <div class="results-title">
                    {TASK_TYPES['code']['icon'] if is_code_task else OUTPUT_FORMATS[output_format]['icon']} 
                    {TASK_TYPES['code']['name'] if is_code_task else OUTPUT_FORMATS[output_format]['name']}
                </div>
                <div class="results-content">
                    {result}
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            # Footer
            st.markdown("""
            <div style="text-align: center; margin-top: 2rem; padding: 1rem; color: #4ECDC4; font-size: 0.9rem;">
                Powered by CrewAI and Cerebras 🚀
            </div>
            """, unsafe_allow_html=True)
            
        except Exception as e:
            st.error(f"❌ An error occurred: {str(e)}")
            if "API key" in str(e):
                st.info("🔑 Please check your API key configuration.")
            else:
                st.info("💡 Try narrowing the scope or selecting a briefer output format.") 