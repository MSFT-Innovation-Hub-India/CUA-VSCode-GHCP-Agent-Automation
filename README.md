# CUA-VSCode-GHCP Agent Automation

An intelligent automation framework that combines Azure OpenAI's Computer Use Agent (CUA) with Visual Studio Code and GitHub Copilot to create a seamless, AI-powered code generation workflow.

## 🚀 Overview

This project automates the entire code generation process by intelligently monitoring Visual Studio Code's GitHub Copilot interface using computer vision and AI. It automatically launches VS Code, installs dependencies, interacts with GitHub Copilot's Agent mode, and monitors the completion of code generation tasks.

## ✨ Features

### Core Automation Capabilities
- **Automated VS Code Launch**: Intelligently finds and launches Visual Studio Code with specified project folders
- **Dependency Management**: Automatically installs Python packages from `requirements.txt` using pip
- **GitHub Copilot Integration**: Opens and interacts with GitHub Copilot's Agent mode
- **Smart UI Monitoring**: Uses Azure OpenAI's Computer Use Agent to monitor UI state changes
- **Code Generation Workflow**: Sends developer prompts to Copilot and monitors completion status
- **Intelligent Button Detection**: Automatically detects when the "Keep" button is enabled and clicks it
- **Real-time Screenshot Analysis**: Captures and analyzes screenshots for process monitoring

### Advanced Features  
- **Multi-step Installation Monitoring**: Tracks pip installation progress using AI vision
- **Error Handling & Fallbacks**: Robust error handling with multiple fallback strategies
- **Configurable Timeouts**: Customizable wait times for different automation phases
- **Cross-Platform VS Code Detection**: Automatically locates VS Code across different installation paths
- **Memory-Efficient Processing**: Processes screenshots in memory without disk I/O

## 🏗️ Architecture & Components

### AI Models & Tools
- **Azure OpenAI Computer Use Agent (CUA)**: Primary AI model for visual UI monitoring and interaction
  - Model: `computer-use-preview`
  - Capabilities: Screenshot analysis, UI element detection, state monitoring
- **GitHub Copilot**: Code generation and development assistance
- **Azure Cognitive Services**: Authentication and API access management

### Core Components
- **UI Automation Engine**: Built on `pyautogui` for keyboard/mouse interactions
- **Screenshot Processing**: Real-time screen capture with base64 encoding
- **API Integration Layer**: Azure OpenAI SDK integration with proper authentication
- **Configuration Management**: Environment-based configuration using `python-dotenv`
- **Window Management**: Cross-platform window detection and control

### Technical Stack
- **Language**: Python 3.x
- **UI Automation**: PyAutoGUI, PyGetWindow
- **Image Processing**: Pillow, OpenCV
- **API Client**: Azure OpenAI Python SDK
- **Authentication**: Azure Identity (DefaultAzureCredential)
- **Configuration**: python-dotenv for environment management

## 📋 Prerequisites

### Hardware Requirements
- **Operating System**: Windows 10/11 (primary support)
- **RAM**: Minimum 8GB (16GB recommended for optimal performance)
- **CPU**: Multi-core processor (Intel i5/AMD Ryzen 5 or better)
- **Display**: Minimum 1920x1080 resolution
- **Network**: Stable internet connection for API calls
- **Storage**: At least 2GB free space for dependencies and temporary files

### Software Dependencies

#### Essential Software
- **Python**: Version 3.8 or higher
- **Visual Studio Code**: Latest stable version
- **GitHub Copilot**: Active subscription and VS Code extension installed
- **Git**: For repository management

#### Azure Services
- **Azure OpenAI Service**: Access to Computer Use Agent model
- **Azure Subscription**: With appropriate permissions for Cognitive Services
- **Azure CLI**: For authentication (optional but recommended)

#### Python Package Dependencies
See `requirements.txt` for complete list:
```
pyautogui          # UI automation and screen control
pygetwindow        # Window management and detection  
pyscreeze          # Screenshot capture utilities
pillow             # Image processing and manipulation
opencv-python      # Computer vision processing
openai             # Azure OpenAI API client
azure-identity     # Azure authentication
azure-core         # Azure SDK core functionality
python-dotenv      # Environment variable management
requests           # HTTP client for API calls
```

## 🛠️ Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/MSFT-Innovation-Hub-India/CUA-VSCode-GHCP-Agent-Automation.git
cd CUA-VSCode-GHCP-Agent-Automation
```

### 2. Set Up Python Environment
```bash
# Create virtual environment (recommended)
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 3. Configure Azure OpenAI Access

#### Option A: Environment Variables
Create a `.env` file in the project root:
```bash
cp .env.example .env
```

Edit `.env` with your Azure OpenAI configuration:
```env
AZURE_OPENAI_ENDPOINT="https://your-endpoint.openai.azure.com/"
AZURE_API_VERSION="2025-03-01-preview"
CUA_MODEL_NAME="computer-use-preview"
COGNITIVE_SERVICES_SCOPE="https://cognitiveservices.azure.com/.default"
```

#### Option B: Azure CLI Authentication
```bash
# Login to Azure
az login

# Set subscription (if needed)
az account set --subscription "your-subscription-id"
```

### 4. Verify GitHub Copilot Setup
1. Open Visual Studio Code
2. Ensure GitHub Copilot extension is installed and activated
3. Verify you can access Agent mode with `Ctrl+Shift+I`
4. Test basic Copilot functionality

### 5. Set Up Project Structure
The automation expects a specific project structure:
```
~/pyauto-gui-samples/
└── project1/
    ├── requirements.txt
    └── [your project files]
```

Create this structure or modify the `project_folder` path in `sample.py`.

## 🎯 Usage

### Basic Usage
1. **Prepare your environment**:
   ```bash
   # Ensure VS Code is closed
   # Have your project ready in the expected location
   ```

2. **Run the automation**:
   ```bash
   python sample.py
   ```

3. **Monitor the process**:
   - The script will automatically launch VS Code
   - Install dependencies from requirements.txt
   - Open GitHub Copilot Agent mode
   - Send a demo prompt (factorial function)
   - Monitor for completion and auto-click "Keep"

### Customizing the Automation

#### Modify the Developer Prompt
Edit the `developer_prompt` variable in `sample.py`:
```python
developer_prompt = "Your custom coding task here"
```

#### Adjust Project Path
Change the `project_folder` path:
```python
project_folder = os.path.join(home_directory, "your-path", "your-project")
```

#### Configure Timeouts
Modify timing parameters:
```python
max_wait_time = 120        # Maximum wait for code generation
screenshot_interval = 3    # Screenshot frequency
```

### Advanced Configuration

#### Custom VS Code Path
If VS Code is not automatically detected:
```python
# Modify the find_vscode_executable() function or set path directly
vscode_path = r"C:\path\to\your\Code.exe"
```

#### Display Resolution Adjustment
For non-1920x1080 displays, update the CUA model configuration:
```python
"display_width": 1920,   # Your screen width
"display_height": 1080,  # Your screen height
```

## 🔧 API Configuration

### Azure OpenAI Computer Use Agent
The project uses Azure OpenAI's Computer Use Agent model for visual monitoring:

- **Model Name**: `computer-use-preview`
- **API Version**: `2025-03-01-preview`
- **Required Permissions**: Read access to Azure OpenAI resources
- **Authentication**: Azure DefaultAzureCredential (recommended)

### Request Format
The CUA model receives:
- Screenshot images as base64-encoded data
- Specific prompts for UI element detection
- Display resolution information
- Environment context (Windows)

### Response Handling
The automation processes JSON responses containing:
- Button state information ("enabled"/"disabled")
- Installation status ("complete"/"in_progress")
- Error handling for malformed responses

## 🐛 Troubleshooting

### Common Issues

#### VS Code Not Found
```
Error: VS Code not found
```
**Solutions**:
1. Install VS Code from official website
2. Add VS Code to PATH: Open VS Code → `Ctrl+Shift+P` → "Shell Command: Install code command in PATH"
3. Manually specify path in script

#### Azure Authentication Errors
```
Error: Azure authentication failed
```
**Solutions**:
1. Run `az login` to authenticate
2. Verify Azure subscription access
3. Check .env file configuration
4. Ensure proper IAM permissions

#### Screenshot/UI Detection Issues
```
Error: Could not detect UI elements
```
**Solutions**:
1. Ensure display resolution matches configuration
2. Check VS Code theme (some themes may affect detection)
3. Verify GitHub Copilot is properly installed
4. Try running with administrator privileges

#### Package Installation Hangs
```
Error: Installation monitoring timeout
```
**Solutions**:
1. Check internet connectivity
2. Verify requirements.txt format
3. Try manual pip install first
4. Check for package conflicts

### Debug Mode
Enable detailed logging by modifying the script:
```python
# Add at the top of sample.py
import logging
logging.basicConfig(level=logging.DEBUG)
```

## 🤝 Contributing

### Development Setup
1. Fork the repository
2. Create a feature branch
3. Follow the existing code style
4. Add appropriate error handling
5. Test thoroughly on Windows environment

### Code Style Guidelines
- Follow PEP 8 for Python code formatting
- Use descriptive variable names
- Add docstrings for functions
- Include error handling for all automation steps
- Comment complex UI automation sequences

### Testing
- Test on multiple Windows versions
- Verify with different VS Code themes
- Test with various screen resolutions
- Validate Azure authentication methods

### Pull Request Process
1. Update documentation for any new features
2. Add error handling and logging
3. Test the complete automation workflow
4. Update this README if needed

## 📝 Development Best Practices

### Error Handling
- Always wrap UI automation in try-catch blocks
- Provide meaningful error messages
- Include fallback strategies for critical operations
- Log errors with sufficient context

### Configuration Management
- Use environment variables for sensitive data
- Provide sensible defaults
- Document all configuration options
- Validate configuration at startup

### Security Considerations
- Never commit API keys or credentials
- Use Azure authentication best practices
- Implement proper error handling for API failures
- Validate all user inputs

### Performance Optimization
- Process screenshots in memory when possible
- Implement efficient polling intervals
- Use connection pooling for API calls
- Monitor resource usage during automation

### Monitoring & Logging
- Implement comprehensive logging
- Use structured log formats
- Monitor API usage and costs
- Track automation success rates

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Azure OpenAI team for Computer Use Agent capabilities
- GitHub Copilot team for AI-powered code generation
- Microsoft Innovation Hub India for project sponsorship
- Open source community for the Python automation libraries

## 📞 Support

For issues and questions:
1. Check the [Troubleshooting](#troubleshooting) section
2. Search existing [GitHub Issues](https://github.com/MSFT-Innovation-Hub-India/CUA-VSCode-GHCP-Agent-Automation/issues)
3. Create a new issue with detailed information
4. Include logs, screenshots, and system information

---

**Note**: This automation tool is designed for development and testing purposes. Ensure you have appropriate licenses for all software components and Azure services used.