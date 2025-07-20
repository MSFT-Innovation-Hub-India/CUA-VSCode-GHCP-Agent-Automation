# CUA-VSCode-GHCP-Agent-Automation

## Autonomous VS Code Desktop Automation with GitHub Copilot using Computer Use Agent

This project demonstrates an approach to autonomous code generation using Computer Use Agent (CUA) model and PyAutoGUI to automate VS Code desktop interactions with GitHub Copilot in Agent mode. The system mimics a developer's workflow by autonomously launching VS Code, setting up the environment, and generating code through GitHub Copilot.

## 🎯 Project Overview

This automation scenario is particularly relevant in situations where:

1. **The codebase is not hosted on GitHub** - GitHub Agents on github.com are not applicable
2. **GitHub Codespaces cannot access the code** - VS Code in the browser is ruled out
3. **Desktop automation is required** - The automation must work with VS Code desktop client on a local computer, not browser-based solutions

## 🔑 Key Innovation: CUA Model + PyAutoGUI Integration

The project showcases how **Computer Use Agent (CUA) model** and **PyAutoGUI** work in tandem to create a deterministic autonomous system:

- **PyAutoGUI** performs physical desktop actions (launching applications, typing, clicking)
- **CUA Model** provides intelligent decision-making by analyzing screenshots and determining next actions
- **Deterministic Outcomes** - CUA enables autonomous outcome detection and corrective actions at every step

## 🚀 Complete Autonomous Workflow

### Phase 1: Environment Setup
1. **VS Code Launch**: PyAutoGUI autonomously launches VS Code desktop application
2. **Project Navigation**: Opens the specified project workspace directory
3. **Window Management**: Maximizes VS Code window for optimal automation
4. **Terminal Access**: Opens integrated PowerShell terminal using keyboard shortcuts

### Phase 2: Intelligent Package Management
1. **Requirements Analysis**: Reads `requirements.txt` from the project workspace
2. **Package Installation**: Executes `pip install -r requirements.txt` command
3. **Smart Monitoring**: 
   - Takes screenshots at regular intervals
   - CUA model analyzes terminal output to determine installation progress
   - Distinguishes between "in_progress" and "complete" states
   - PyAutoGUI waits for CUA confirmation before proceeding

### Phase 3: GitHub Copilot Integration
1. **Copilot Activation**: Opens GitHub Copilot chat panel using `Ctrl+Shift+I`
2. **Agent Mode Selection**: Automatically switches to Agent mode
3. **Prompt Submission**: Types and submits the developer prompt for code generation
4. **Intelligent Status Monitoring**:
   - Captures screenshots every 3 seconds
   - CUA model analyzes the "Keep" button status (enabled/disabled)
   - Waits for code generation completion
   - Automatically accepts generated code when ready

## 🔍 CUA Model Decision Points

The CUA model makes critical autonomous decisions at multiple stages:

### Package Installation Monitoring
```json
{
  "installation_status": "complete" | "in_progress"
}
```
- **In Progress**: Detects installation output, progress bars, package downloads
- **Complete**: Identifies empty command prompt ready for next input

### Code Generation Monitoring  
```json
{
  "button": "enabled" | "disabled"
}
```
- **Disabled**: GitHub Copilot is still generating code
- **Enabled**: Code generation complete, ready for acceptance

## 🎬 Automation Flow in Action

```
1. Agent launches VS Code desktop → Project workspace opens
2. Terminal opens → pip install executes
3. CUA monitors screenshots → Detects installation completion  
4. GitHub Copilot opens → Agent mode activated
5. Developer prompt submitted → Code generation begins
6. CUA monitors "Keep" button → Detects when enabled
7. PyAutoGUI accepts code → Automation complete
```

## 💡 Real-World Applications

### Development Scenarios
Imagine you have a project workspace on your computer where this automation needs to generate code. The system can:
- Clone repositories using git commands
- Create new branches autonomously  
- Generate code based on requirements
- Run tests and validation

### Regression Testing Use Cases
This approach is invaluable for scenarios requiring:
- **Routine Code Generation**: Automating repetitive coding tasks
- **Test Case Generation**: Creating comprehensive test suites
- **Documentation Updates**: Generating code documentation
- **Refactoring Tasks**: Systematic code improvements

## 🔧 Technical Architecture

### Core Components

1. **PyAutoGUI Engine**
   - Desktop interaction automation
   - Keyboard and mouse control
   - Window management
   - Screenshot capture

2. **Computer Use Agent (CUA) Model**
   - Image analysis and interpretation
   - Decision-making based on visual input
   - State detection and monitoring
   - Intelligent response generation

3. **Azure OpenAI Integration**
   - Token-based authentication
   - CUA model API calls
   - Real-time screenshot analysis

### Dependencies
```
pyautogui==0.9.54
openai==1.51.0
azure-identity==1.19.0
python-dotenv==1.0.0
Pillow==10.4.0
pygetwindow==0.0.9
```

## 🎯 Key Advantages

### Deterministic Automation
- **Reliable State Detection**: CUA model accurately identifies system states
- **Intelligent Waiting**: No blind timeouts - waits for actual completion
- **Error Recovery**: Can detect and respond to unexpected situations

### Scalable Solution
- **Headless Execution**: Agent runs without human intervention
- **Multiple Scenarios**: Handles simple to complex automation workflows
- **Dedicated Computer**: Runs on any Windows desktop with VS Code

### Flexible Integration
- **Any Git Repository**: Works with local, GitHub, Azure DevOps, or any git-enabled repo
- **Various Project Types**: Language and framework agnostic
- **Custom Prompts**: Adaptable to different code generation requirements

## 🚀 Getting Started

### Prerequisites
- Windows 10/11
- VS Code Desktop installed
- Azure OpenAI access with CUA model deployment
- Python 3.8+

### Environment Setup
```powershell
# Clone the repository
git clone https://github.com/MSFT-Innovation-Hub-India/CUA-VSCode-GHCP-Agent-Automation.git

# Navigate to project directory
cd CUA-VSCode-GHCP-Agent-Automation

# Install dependencies
pip install -r requirements.txt

# Configure environment variables
# Create .env file with your Azure OpenAI credentials
```

### Configuration
Create a `.env` file with the following variables:
```env
AZURE_OPENAI_ENDPOINT=your_endpoint_here
AZURE_API_VERSION=2024-10-01-preview
COGNITIVE_SERVICES_SCOPE=https://cognitiveservices.azure.com/.default
CUA_MODEL_NAME=your_cua_model_deployment_name
```

### Running the Automation
```powershell
python app.py
```

## 📈 Impact and Benefits

This autonomous approach transforms repetitive development tasks by:
- **Reducing Manual Effort**: Eliminates grunt work in routine coding tasks
- **Ensuring Consistency**: Standardized code generation and testing procedures
- **Improving Productivity**: Developers focus on complex problem-solving while automation handles routine tasks
- **24/7 Availability**: Continuous code generation and testing capabilities


**Note**: This automation system requires a dedicated computer to run VS Code desktop and should be used responsibly with appropriate safeguards and monitoring.
