MODELS = {
    "cerebras/llama-4-scout-17b-16e-instruct": {
        "name": "Llama 4 Scout",
        "description": "Latest Llama model optimized for instruction following",
        "icon": "🦙"
    },
    "cerebras/llama3.1-8b": {
        "name": "Llama 3.1 (8B)",
        "description": "Efficient model for faster inference",
        "icon": "⚡"
    },
    "cerebras/llama-3.3-70b": {
        "name": "Llama 3.3 (70B)",
        "description": "Largest model for most complex tasks",
        "icon": "🧠"
    }
}

TOOLS = {
    "serper": {
        "name": "SerperDev Search",
        "description": "Search the web for recent information and developments",
        "icon": "🔍",
        "default": True
    }
}

TASK_TYPES = {
    "research": {
        "name": "Research Analysis",
        "description": "Analyze trends and developments in a specific field",
        "icon": "📚"
    },
    "code": {
        "name": "Code Analysis",
        "description": "Analyze and improve Python code",
        "icon": "💻"
    }
}

OUTPUT_FORMATS = {
    "executive_summary": {
        "name": "Executive Summary",
        "description": "Concise overview of key findings and recommendations",
        "icon": "📊"
    },
    "detailed_report": {
        "name": "Detailed Report",
        "description": "Comprehensive analysis with in-depth explanations",
        "icon": "📑"
    },
    "bullet_points": {
        "name": "Bullet Points",
        "description": "Key points in an easy-to-read format",
        "icon": "🔍"
    }
} 