# AI Job Automation - Multi-Agent System 🤖

AI-powered job application automation with **collaborative multi-agent architecture** featuring Steve Jobs (UX), Warren Buffett (Business), and Elon Musk (Technical).

## 🎯 Features

- **Phase 1: CV Optimization** - Claude AI analyzes and improves CV + generates cover letters
- **Phase 2: LinkedIn Integration** - Auto-update profile via MCP server
- **Phase 3: Job Search Automation** - Autonomous LinkedIn job search with filters
- **Phase 4: Auto-Application** - Playwright automation for form filling
- **Phase 5: Email Management** - Gmail monitoring + calendar scheduling

## 🏗️ Architecture

```
┌─────────────────────────────────────────┐
│   3 COLLABORATIVE AI AGENTS             │
│   • Steve Jobs (UX/Design)              │
│   • Warren Buffett (Business)           │
│   • Elon Musk (Technical)               │
└──────────┬──────────────────────────────┘
           │
           ├──> Claude API (Anthropic)
           ├──> MCP Server: LinkedIn
           ├──> MCP Server: Playwright
           ├──> n8n Orchestrator
           └──> PostgreSQL Database
```

## 🚀 Quick Start

### Prerequisites
- Python 3.12+
- Docker
- Claude API Key
- LinkedIn Cookie (`li_at`)

### Installation

```bash
# Clone repository
git clone https://github.com/dtlele/ai-job-automation-multiagent.git
cd ai-job-automation-multiagent

# Install dependencies
pip install anthropic

# Set your API key
export CLAUDE_API_KEY="your-key-here"

# Run multi-agent system
python multi_agent_collaborative.py
```

## 💡 Multi-Agent System

The system uses **3 AI agents** that communicate in real-time:

- **Steve Jobs** 🎨 - Focuses on UX, design, and user experience
- **Warren Buffett** 💼 - Analyzes business strategy, ROI, and costs
- **Elon Musk** 🚀 - Handles technical architecture and implementation

### Features:
✅ Real-time communication between agents  
✅ Budget limit control (`max_budget_usd`)  
✅ Time limit control (`max_time_minutes`)  
✅ Token limit per response  
✅ Shared memory for context  
✅ Cost tracking  
✅ Conversation transcript export

## 📊 Configuration

```python
system = CollaborativeAgentSystem(
    api_key="YOUR_CLAUDE_API_KEY",
    max_budget_usd=2.0,      # $2 budget limit
    max_time_minutes=5        # 5 minutes max
)
```

## 🔧 MCP Servers

### LinkedIn MCP Server
```bash
docker run --rm -i \
  -e LINKEDIN_COOKIE="your_cookie" \
  stickerdaniel/linkedin-mcp-server:latest
```

### Playwright MCP Server
```bash
git clone https://github.com/Automata-Labs-team/MCP-Server-Playwright.git
cd MCP-Server-Playwright
npm install
npm start
```

## 📝 Output

The system generates:
- Real-time agent conversation in terminal
- Cost breakdown per agent
- `agent_conversation.json` - Full transcript

Example output:
```
🎨 Steve Jobs ($0.0023):
We need a clean REST API wrapper...

💼 Warren Buffett ($0.0019):
ROI calculation shows...

🚀 Elon Musk ($0.0031):
Here's the bridge code: ...
```

## 🛠️ Tech Stack

- **Claude Sonnet 4** - AI agents
- **Python AsyncIO** - Concurrent execution
- **n8n** - Workflow automation
- **Docker** - MCP server hosting
- **PostgreSQL** - Data storage
- **LinkedIn MCP** - Job search
- **Playwright MCP** - Browser automation

## 📈 Roadmap

- [x] Multi-agent communication system
- [x] Budget & time controls
- [ ] MCP-to-HTTP bridge
- [ ] n8n workflow integration
- [ ] Frontend dashboard
- [ ] Database integration
- [ ] Gmail monitoring
- [ ] Full automation pipeline

## 🤝 Contributing

Contributions welcome! Open an issue or submit a PR.

## 📄 License

MIT License - see [LICENSE](LICENSE)

## 🔗 Resources

- [LinkedIn MCP Server](https://github.com/stickerdaniel/linkedin-mcp-server)
- [Playwright MCP Server](https://github.com/Automata-Labs-team/MCP-Server-Playwright)
- [Claude API Docs](https://docs.anthropic.com)
- [n8n Documentation](https://docs.n8n.io)

## ⚠️ Disclaimer

This tool is for personal use only. Please respect LinkedIn's Terms of Service and rate limits.

---

**Made with ❤️ by the AI Job Automation Team**
