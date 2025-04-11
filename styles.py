import streamlit as st

def apply_custom_styles():
    st.markdown("""
        <style>
        /* Main container */
        .main {
            padding: 2rem;
        }
        
        /* Header styles */
        .header-container {
            background: linear-gradient(90deg, #1E1E1E 0%, #2D2D2D 100%);
            padding: 2rem;
            border-radius: 10px;
            margin-bottom: 2rem;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        
        .header-title {
            font-size: 2.5rem;
            font-weight: 700;
            background: linear-gradient(90deg, #FF6B6B 0%, #4ECDC4 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 1rem;
        }
        
        .header-subtitle {
            color: #B8B8B8;
            font-size: 1.2rem;
            margin-bottom: 1.5rem;
        }
        
        /* About section */
        .about-section {
            background: linear-gradient(135deg, rgba(30, 30, 30, 0.9) 0%, rgba(45, 45, 45, 0.8) 100%);
            padding: 2rem;
            border-radius: 15px;
            border: 1px solid rgba(255, 255, 255, 0.1);
            margin-bottom: 2rem;
            box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.2);
            backdrop-filter: blur(4px);
        }
        
        .about-title {
            font-size: 2rem;
            font-weight: 600;
            margin-bottom: 1.5rem;
            color: #4ECDC4;
            display: flex;
            align-items: center;
        }
        
        .about-description {
            color: #E0E0E0;
            font-size: 1.1rem;
            line-height: 1.6;
            margin-bottom: 2rem;
        }
        
        .features-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 1.5rem;
            margin-top: 1.5rem;
        }
        
        .feature-card {
            background: rgba(255, 255, 255, 0.05);
            padding: 1.5rem;
            border-radius: 10px;
            border: 1px solid rgba(255, 255, 255, 0.1);
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }
        
        .feature-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);
        }
        
        .feature-icon {
            margin-bottom: 1rem;
            color: #4ECDC4;
        }
        
        .feature-title {
            color: #4ECDC4;
            font-size: 1.2rem;
            font-weight: 600;
            margin: 0.5rem 0;
        }
        
        .feature-description {
            color: #B8B8B8;
            font-size: 0.95rem;
            line-height: 1.4;
            margin: 0;
        }
        
        /* Configuration section */
        .config-container {
            background: rgba(30, 30, 30, 0.4);
            padding: 1.5rem;
            border-radius: 8px;
            margin-bottom: 2rem;
        }
        
        /* Tool cards */
        .tool-card {
            background: rgba(45, 45, 45, 0.6);
            padding: 1rem;
            border-radius: 6px;
            border: 1px solid rgba(255, 255, 255, 0.05);
            margin-bottom: 1rem;
        }
        
        .tool-title {
            color: #FF6B6B;
            font-weight: 600;
            margin-bottom: 0.5rem;
        }
        
        /* Buttons */
        .stButton > button {
            background: linear-gradient(90deg, #FF6B6B 0%, #4ECDC4 100%);
            color: white;
            border: none;
            padding: 0.5rem 2rem;
            border-radius: 25px;
            font-weight: 600;
            transition: all 0.3s ease;
        }
        
        .stButton > button:hover {
            transform: translateY(-2px);
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        }
        
        /* Sidebar */
        .css-1d391kg {
            background: linear-gradient(180deg, #1E1E1E 0%, #2D2D2D 100%);
        }
        
        /* Progress bar */
        .stProgress > div > div {
            background: linear-gradient(90deg, #FF6B6B 0%, #4ECDC4 100%);
        }
        
        /* Custom radio buttons */
        .stRadio > div {
            background: rgba(45, 45, 45, 0.6);
            padding: 1rem;
            border-radius: 6px;
            margin-bottom: 0.5rem;
        }
        
        /* Footer */
        .footer {
            text-align: center;
            padding: 2rem;
            color: #B8B8B8;
            border-top: 1px solid rgba(255, 255, 255, 0.1);
        }
        </style>
    """, unsafe_allow_html=True)

def display_header():
    st.markdown("""
        <div class="header-container">
            <h1 class="header-title">CrewAI × Cerebras</h1>
            <p class="header-subtitle">Advanced Multi-Agent Research & Analysis Platform</p>
        </div>
    """, unsafe_allow_html=True)

def display_about():
    st.markdown("""
        <div class="about-section">
            <h2 class="about-title">
                About This Project 
                <span style="font-size: 1.8rem; margin-left: 8px;">🧪</span>
            </h2>
            
            <p class="about-description">
                This platform combines the power of CrewAI's multi-agent framework with Cerebras's lightning-fast inference capabilities. 
                It enables sophisticated AI workflows where multiple agents collaborate to perform complex research and analysis tasks.
            </p>
            
            <div class="features-grid">
                <div class="feature-card">
                    <div class="feature-icon" style="font-size: 24px;">🤖</div>
                    <h3 class="feature-title">Advanced Research Analysis</h3>
                    <p class="feature-description">
                        Multiple specialized agents working together to deliver comprehensive insights
                    </p>
                </div>
                
                <div class="feature-card">
                    <div class="feature-icon" style="font-size: 24px;">💻</div>
                    <h3 class="feature-title">Code Analysis</h3>
                    <p class="feature-description">
                        Intelligent code interpretation and improvement suggestions
                    </p>
                </div>
                
                <div class="feature-card">
                    <div class="feature-icon" style="font-size: 24px;">🔍</div>
                    <h3 class="feature-title">SerperDev Integration</h3>
                    <p class="feature-description">
                        Powerful web search capabilities for comprehensive research
                    </p>
                </div>
                
                <div class="feature-card">
                    <div class="feature-icon" style="font-size: 24px;">📂</div>
                    <h3 class="feature-title">Analysis Tools</h3>
                    <p class="feature-description">
                        Advanced file and website analysis capabilities
                    </p>
                </div>
                
                <div class="feature-card">
                    <div class="feature-icon" style="font-size: 24px;">⚡</div>
                    <h3 class="feature-title">Cerebras Powered</h3>
                    <p class="feature-description">
                        State-of-the-art language models for superior performance
                    </p>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)

def tool_card(title, description, icon="🔧"):
    return f"""
        <div class="tool-card">
            <div class="tool-title">{icon} {title}</div>
            <p>{description}</p>
        </div>
    """ 