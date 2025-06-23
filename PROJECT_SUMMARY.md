# Project Summary: CUA-VSCode-GHCP Agent Automation

## Quick Overview
This project implements an intelligent automation framework that integrates Azure OpenAI's Computer Use Agent (CUA) with Visual Studio Code and GitHub Copilot to automate code generation workflows.

## Key Components
- **UI Automation**: PyAutoGUI-based automation for VS Code interaction
- **AI Vision**: Computer Use Agent for screenshot analysis and UI monitoring  
- **Code Generation**: GitHub Copilot integration for AI-powered coding
- **Process Monitoring**: Real-time tracking of installation and generation progress

## Primary Use Case
Automates the complete developer workflow:
1. Launch VS Code with specific project
2. Install Python dependencies automatically
3. Open GitHub Copilot Agent mode
4. Submit coding prompts
5. Monitor completion and auto-accept generated code

## Technical Stack
- **Language**: Python 3.8+
- **Platform**: Windows 10/11
- **AI Models**: Azure OpenAI Computer Use Agent, GitHub Copilot
- **Automation**: PyAutoGUI, PyGetWindow
- **Image Processing**: Pillow, OpenCV

## Requirements
- Azure OpenAI subscription with CUA model access
- GitHub Copilot subscription  
- Visual Studio Code
- Windows environment with 1920x1080+ resolution

## Files Structure
```
├── sample.py           # Main automation script
├── requirements.txt    # Python dependencies
├── .env.example       # Environment configuration template
├── README.md          # Comprehensive documentation
├── CONTRIBUTING.md    # Development guidelines
├── LICENSE           # MIT license
└── .gitignore        # Git ignore rules
```

This automation tool demonstrates advanced AI integration for developer productivity enhancement.