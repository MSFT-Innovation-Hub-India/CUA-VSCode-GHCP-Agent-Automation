# Contributing to CUA-VSCode-GHCP Agent Automation

Thank you for your interest in contributing to this project! This document provides guidelines and best practices for contributing to the CUA-VSCode-GHCP Agent Automation framework.

## 🚀 Getting Started

### Prerequisites
- Python 3.8 or higher
- Visual Studio Code with GitHub Copilot
- Azure OpenAI access with Computer Use Agent model
- Windows 10/11 environment (primary development platform)

### Development Environment Setup
1. Fork the repository
2. Clone your fork locally
3. Create a virtual environment:
   ```bash
   python -m venv venv
   venv\Scripts\activate  # Windows
   ```
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
5. Copy and configure environment variables:
   ```bash
   cp .env.example .env
   # Edit .env with your Azure OpenAI credentials
   ```

## 📝 Development Guidelines

### Code Style
- Follow PEP 8 Python style guidelines
- Use meaningful variable and function names
- Add docstrings for all functions and classes
- Keep functions focused and under 50 lines when possible
- Use type hints where appropriate

### Error Handling
- Always wrap UI automation code in try-catch blocks
- Provide descriptive error messages with context
- Implement fallback strategies for critical operations
- Log errors with appropriate severity levels

### Configuration Management
- Use environment variables for all configurable parameters
- Provide sensible defaults for all settings
- Document all configuration options in README
- Validate configuration values at startup

### Security Best Practices
- Never commit API keys, tokens, or credentials
- Use Azure DefaultAzureCredential for authentication
- Validate all user inputs and file paths
- Implement proper error handling for API failures
- Follow principle of least privilege for permissions

## 🧪 Testing Guidelines

### Manual Testing
Since this project involves UI automation, thorough manual testing is required:

1. **Environment Testing**:
   - Test on clean Windows installations
   - Verify with different VS Code versions
   - Test with various screen resolutions (1920x1080, 2560x1440, etc.)
   - Validate with different VS Code themes

2. **Automation Testing**:
   - Test the complete workflow end-to-end
   - Verify error handling with invalid configurations
   - Test timeout scenarios
   - Validate screenshot capture and processing

3. **API Integration Testing**:
   - Test Azure OpenAI API connectivity
   - Verify Computer Use Agent model responses
   - Test authentication with different credential types
   - Validate error handling for API failures

### Test Scenarios
Create test cases for:
- VS Code detection and launching
- Package installation monitoring
- GitHub Copilot interaction
- Screenshot capture and analysis
- Button detection and clicking
- Error recovery and fallbacks

## 🐛 Bug Reports

### Before Submitting
- Search existing issues to avoid duplicates
- Test with the latest version
- Verify the issue occurs consistently

### Bug Report Template
Include the following information:
- **Environment**: OS version, Python version, VS Code version
- **Configuration**: Azure OpenAI model, screen resolution
- **Steps to Reproduce**: Detailed step-by-step instructions
- **Expected Behavior**: What should happen
- **Actual Behavior**: What actually happens
- **Screenshots**: If UI-related issues
- **Logs**: Relevant error messages or console output
- **Workarounds**: Any temporary solutions found

## 💡 Feature Requests

### Feature Request Process
1. Check existing issues and discussions
2. Create a detailed feature request issue
3. Discuss the feature with maintainers
4. Wait for approval before implementing

### Feature Request Template
- **Problem Statement**: What problem does this solve?
- **Proposed Solution**: Detailed description of the feature
- **Alternatives Considered**: Other approaches evaluated
- **Implementation Notes**: Technical considerations
- **Breaking Changes**: Any compatibility impacts

## 🔧 Pull Request Process

### Before Submitting
1. Create a feature branch from main
2. Test your changes thoroughly
3. Update documentation if needed
4. Ensure code follows style guidelines

### Pull Request Guidelines
- **Title**: Clear, descriptive title
- **Description**: Detailed explanation of changes
- **Testing**: Describe testing performed
- **Screenshots**: For UI-related changes
- **Breaking Changes**: Document any breaking changes
- **Related Issues**: Link to related issues

### Review Process
1. Automated checks must pass
2. Manual review by maintainers
3. Address feedback and requested changes
4. Final approval and merge

## 📚 Documentation Standards

### Code Documentation
- Add docstrings to all public functions
- Include parameter and return type descriptions
- Document any complex algorithms or logic
- Add inline comments for non-obvious code

### README Updates
- Update feature lists for new capabilities
- Add configuration options for new settings
- Include troubleshooting for common issues
- Update installation instructions if needed

### API Documentation
- Document any new API integrations
- Include example requests and responses
- Describe error conditions and handling
- Update model version information

## 🚦 Coding Standards

### Python Best Practices
```python
# Good: Descriptive function name with docstring
def take_screenshot_and_convert_to_base64(screenshot_counter: int) -> str:
    """
    Take a screenshot, convert it to base64, and return the base64 string.
    
    Args:
        screenshot_counter: The counter for the screenshot for logging purposes
        
    Returns:
        Base64 encoded screenshot as a string, or None if there was an error
    """
    try:
        # Implementation here
        pass
    except Exception as e:
        print(f"Error taking screenshot: {e}")
        return None
```

### Error Handling Pattern
```python
# Good: Comprehensive error handling
try:
    # Main operation
    result = perform_operation()
except SpecificException as e:
    print(f"Specific error occurred: {e}")
    # Attempt fallback
    result = fallback_operation()
except Exception as e:
    print(f"Unexpected error: {e}")
    # Log and reraise or handle gracefully
    raise
```

### Configuration Pattern
```python
# Good: Environment-based configuration with defaults
azure_endpoint = os.getenv(
    "AZURE_OPENAI_ENDPOINT", 
    "https://default-endpoint.openai.azure.com/"
)
```

## 🔄 Release Process

### Version Management
- Use semantic versioning (MAJOR.MINOR.PATCH)
- Update version in relevant files
- Create release notes for each version
- Tag releases in Git

### Release Checklist
- [ ] All tests pass
- [ ] Documentation updated
- [ ] Version numbers updated
- [ ] Release notes created
- [ ] Breaking changes documented
- [ ] Migration guide provided (if needed)

## 🤝 Community Guidelines

### Code of Conduct
- Be respectful and inclusive
- Welcome newcomers and help them learn
- Focus on constructive feedback
- Respect different perspectives and experiences

### Communication Channels
- Use GitHub Issues for bug reports and feature requests
- Use GitHub Discussions for general questions
- Keep discussions focused and on-topic
- Search before posting to avoid duplicates

## 📊 Performance Considerations

### UI Automation Performance
- Minimize unnecessary screenshots
- Use efficient polling intervals
- Implement smart waiting strategies
- Cache window handles when possible

### API Usage Optimization
- Batch API calls when possible
- Implement retry logic with exponential backoff
- Monitor API usage and costs
- Use connection pooling for HTTP clients

### Memory Management
- Process screenshots in memory when possible
- Clean up temporary resources
- Monitor memory usage during long operations
- Implement garbage collection hints for large objects

## 🔐 Security Considerations

### Authentication Security
- Use Azure managed identities when possible
- Implement proper credential rotation
- Never log sensitive information
- Use secure credential storage

### API Security
- Validate all API responses
- Implement rate limiting
- Use HTTPS for all communications
- Handle API errors gracefully

Thank you for contributing to this project! Your efforts help make AI-powered development automation accessible to more developers.