import pyautogui
import subprocess
import time
import os
import shutil
from io import BytesIO

from openai import OpenAI
from openai import AzureOpenAI

import base64
import json
from azure.identity import DefaultAzureCredential, get_bearer_token_provider
from azure.core.credentials import AzureKeyCredential

# Optional: Make sure failsafe is off if your cursor jumps to corner
pyautogui.FAILSAFE = False

token_provider = get_bearer_token_provider(
    DefaultAzureCredential(), "https://cognitiveservices.azure.com/.default"
)


### client = OpenAI(api_key=config.api_key)
client = AzureOpenAI(
    azure_endpoint="https://aoai-gpt4-001.openai.azure.com/",
    azure_ad_token_provider=token_provider,
    api_version="2025-03-01-preview",
)


user_prompt = """
The image provided as input is a screenshot in Visual Studio Code. 
A user prompt has been provided to the Agent Mode in the GitHub Copilot chat panel, instructing it to write code based on the prompt.
Once the code is generated and the copilot agent has finished processing, the "Keep" button will be enabled. Till the time it runs, the "Keep" button will be grayed out.

In your response, please provide the following JSON format:
{
    "button": "enabled" or "disabled"
}

When the 'keep' button is enabled, you must return "enabled" in the response.
If the button is disabled, return "disabled" in the response.
"""


def find_vscode_executable():
    """Find VS Code executable on Windows"""
    # Common VS Code installation paths
    username = os.getenv("USERNAME")
    common_paths = [
        # User installation
        f"C:\\Users\\{username}\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe",
        f"C:\\Users\\{username}\\AppData\\Local\\Programs\\Microsoft VS Code\\bin\\code.cmd",
        # System-wide installation
        "C:\\Program Files\\Microsoft VS Code\\Code.exe",
        "C:\\Program Files\\Microsoft VS Code\\bin\\code.cmd",
        "C:\\Program Files (x86)\\Microsoft VS Code\\Code.exe",
        "C:\\Program Files (x86)\\Microsoft VS Code\\bin\\code.cmd",
        # Insiders version
        f"C:\\Users\\{username}\\AppData\\Local\\Programs\\Microsoft VS Code Insiders\\Code - Insiders.exe",
        "C:\\Program Files\\Microsoft VS Code Insiders\\Code - Insiders.exe",
    ]

    # First, check if 'code' is in PATH
    code_cmd = shutil.which("code")
    if code_cmd:
        return code_cmd

    # Check common installation paths
    for path in common_paths:
        if os.path.exists(path):
            return path

    # Try to find VS Code using Windows registry (alternative approach)
    try:
        import winreg

        # Check user installation registry
        try:
            key = winreg.OpenKey(
                winreg.HKEY_CURRENT_USER,
                r"Software\Classes\Applications\Code.exe\shell\open\command",
            )
            value, _ = winreg.QueryValueEx(key, "")
            winreg.CloseKey(key)
            # Extract path from registry value (remove quotes and arguments)
            if value:
                path = value.split('"')[1] if '"' in value else value.split()[0]
                if os.path.exists(path):
                    return path
        except:
            pass

        # Check system installation registry
        try:
            key = winreg.OpenKey(
                winreg.HKEY_LOCAL_MACHINE,
                r"Software\Classes\Applications\Code.exe\shell\open\command",
            )
            value, _ = winreg.QueryValueEx(key, "")
            winreg.CloseKey(key)
            if value:
                path = value.split('"')[1] if '"' in value else value.split()[0]
                if os.path.exists(path):
                    return path
        except:
            pass
    except ImportError:
        pass

    return None


def take_screenshot_and_convert_to_base64(screenshot_counter):
    """
    Take a screenshot, convert it to base64, and return the base64 string.

    Args:
        screenshot_counter (int): The counter for the screenshot for logging purposes

    Returns:
        str: Base64 encoded screenshot as a string, or None if there was an error
    """
    try:
        # Take screenshot directly in memory
        screenshot = pyautogui.screenshot()

        # Convert screenshot to base64 directly in memory (no file I/O)
        img_buffer = BytesIO()
        screenshot.save(img_buffer, format="PNG")
        img_buffer.seek(0)
        base64_image = base64.b64encode(img_buffer.getvalue()).decode()

        print(f"Screenshot {screenshot_counter} captured in memory and converted to base64")

        # Optional: Save screenshot to disk for debugging (commented out by default)
        # images_folder = "images"
        # screenshot_filename = f"progress_{screenshot_counter:03d}.png"
        # screenshot_path = os.path.join(images_folder, screenshot_filename)
        # if not os.path.exists(images_folder):
        #     os.makedirs(images_folder)
        # screenshot.save(screenshot_path)
        # print(f"Screenshot {screenshot_counter} also saved to disk: {screenshot_filename}")

        return base64_image

    except Exception as e:
        print(f"Error taking screenshot: {e}")
        return None


# Step 1: Launch VS Code with specific folder
# Construct the full path from home directory
home_directory = os.path.expanduser("~")
project_folder = os.path.join(home_directory, "pyauto-gui-samples", "project1")
print(f"Project folder path: {project_folder}")

vscode_path = find_vscode_executable()
print(f"DEBUG: Found VS Code path: {vscode_path}")

if vscode_path:
    print(f"DEBUG: Checking if path exists: {os.path.exists(vscode_path)}")
    try:
        # Launch VS Code with the specific project folder
        subprocess.Popen([vscode_path, project_folder])
        print(f"Launching VS Code with folder: {project_folder}")
    except FileNotFoundError as e:
        print(f"Error launching VS Code: {e}")
        print("Trying alternative method...")
        # Try using shell=True for .cmd files
        if vscode_path.endswith(".cmd"):
            subprocess.Popen([vscode_path, project_folder], shell=True)
        else:
            # Try finding VS Code manually
            print("Please manually locate your VS Code installation.")
            manual_path = input(
                "Enter the full path to Code.exe (or press Enter to skip): "
            )
            if manual_path and os.path.exists(manual_path):
                subprocess.Popen([manual_path, project_folder])
            else:
                print("Could not launch VS Code. Exiting.")
                exit(1)
else:
    print(
        "VS Code not found. Please ensure VS Code is installed and try one of these solutions:"
    )
    print(
        "1. Add VS Code to PATH by opening VS Code, pressing Ctrl+Shift+P, and running 'Shell Command: Install code command in PATH'"
    )
    print("2. Or manually specify the path to Code.exe in this script")

    # Let's also check what's actually installed
    print("\nDEBUG: Checking common VS Code paths:")
    common_debug_paths = [
        r"C:\Users\{}\AppData\Local\Programs\Microsoft VS Code\Code.exe".format(
            os.getenv("USERNAME")
        ),
        r"C:\Program Files\Microsoft VS Code\Code.exe",
        r"C:\Program Files (x86)\Microsoft VS Code\Code.exe",
    ]
    for path in common_debug_paths:
        print(f"  {path}: {'EXISTS' if os.path.exists(path) else 'NOT FOUND'}")

    exit(1)

time.sleep(5)  # wait for VS Code to fully load

# Maximize VS Code window to fullscreen
print("Maximizing VS Code window to fullscreen...")
try:
    # Method 1: Use pygetwindow to find and maximize the VS Code window
    try:
        import pygetwindow as gw

        # Find VS Code windows
        vscode_windows = [
            w
            for w in gw.getAllWindows()
            if "Visual Studio Code" in w.title or "Code" in w.title
        ]
        target_window = None

        # Find the window with our project
        for window in vscode_windows:
            if (
                "project1" in window.title.lower()
                or "pyauto-gui-samples" in window.title.lower()
            ):
                target_window = window
                break

        if not target_window and vscode_windows:
            # Use the most recent VS Code window
            target_window = vscode_windows[-1]

        if target_window:
            print(f"Found VS Code window: {target_window.title}")
            # Activate the window first
            target_window.activate()
            time.sleep(1)
            # Maximize the window
            target_window.maximize()
            print("VS Code window maximized to fullscreen")
            time.sleep(1)
        else:
            print("Could not find VS Code window, trying keyboard shortcut method")
            raise Exception("Window not found")

    except ImportError:
        print("pygetwindow not available, using keyboard shortcut method")
        raise Exception("pygetwindow not available")

except:
    # Fallback method: Use keyboard shortcuts
    try:
        print("Using keyboard shortcut to maximize window...")
        # First ensure VS Code window is focused
        pyautogui.hotkey("alt", "tab")
        time.sleep(0.5)

        # Use Windows key + Up arrow to maximize window
        pyautogui.hotkey("win", "up")
        time.sleep(1)
        print("VS Code window maximized using keyboard shortcut")

    except Exception as e:
        print(f"Could not maximize window: {e}")
        print("Continuing with current window size...")

# Step 2: Open PowerShell terminal (Ctrl+Shift+`)
pyautogui.hotkey("ctrl", "shift", "`")
print("Opened PowerShell terminal")
time.sleep(2)  # wait for terminal to open

# Step 2.5: Install packages from requirements.txt
print("Installing packages from requirements.txt...")
# Read requirements.txt file
try:
    project_requirements_path = os.path.join(project_folder, "requirements.txt")
    if os.path.exists(project_requirements_path):
        with open(project_requirements_path, "r") as f:
            requirements = f.read().strip()

        if requirements:
            # Type the pip install command (PowerShell compatible)
            pip_command = f"pip install -r requirements.txt"
            pyautogui.typewrite(pip_command, interval=0.05)
            pyautogui.press("enter")
            print(f"Executed: {pip_command}")            # Use CUA model to intelligently detect installation completion
            print("Monitoring package installation using CUA model...")

            # Count the number of packages for reference
            package_count = len(
                [
                    line
                    for line in requirements.split("\n")
                    if line.strip() and not line.strip().startswith("#")
                ]
            )
            print(f"Installing {package_count} packages...")

            # Define prompt for CUA model to detect installation completion
            installation_prompt = """
The image provided is a screenshot of a PowerShell/Command Prompt terminal window where pip install is running.
I need to determine if the package installation has completed or is still in progress.

When installation is complete, the terminal will show an empty prompt (like "PS C:\path>" or "C:\path>") waiting for the next command.
When installation is in progress, you'll see output like:
- "Collecting package_name..."
- "Downloading..."
- "Installing collected packages..."
- "Successfully installed..."
- Progress bars or percentage indicators

In your response, please provide the following JSON format:
{
    "installation_status": "complete" or "in_progress"
}

Return "complete" when you see an empty command prompt ready for input.
Return "in_progress" when you see any installation activity or output.
"""

            installation_complete = False
            screenshot_counter = 1
            max_wait_time = 300  # Maximum 5 minutes timeout
            start_time = time.time()

            # Initial wait to let installation start
            print("Waiting 5 seconds for installation to begin...")
            time.sleep(5)

            while not installation_complete and (time.time() - start_time) < max_wait_time:
                print(f"📸 Taking screenshot {screenshot_counter} to check installation status...")
                
                # Take screenshot and convert to base64
                base64_image = take_screenshot_and_convert_to_base64(screenshot_counter)
                
                if base64_image is not None:
                    try:
                        print(f"🔍 Analyzing screenshot with CUA model...")

                        # Create request to Computer Use Agent model
                        response = client.responses.create(
                            model="computer-use-preview",
                            tools=[
                                {
                                    "type": "computer_use_preview",
                                    "display_width": 1920,  # Adjust based on your screen resolution
                                    "display_height": 1080,
                                    "environment": "windows",
                                }
                            ],
                            input=[
                                {
                                    "type": "message",
                                    "role": "user",
                                    "content": [
                                        {"type": "input_text", "text": installation_prompt},
                                        {
                                            "type": "input_image",
                                            "image_url": f"data:image/png;base64,{base64_image}",
                                        },
                                    ],
                                }
                            ],
                            truncation="auto",
                        )
                        
                        # Extract the actual text content from the response object
                        response_text = None
                        
                        # Check if response.output is a list of ResponseOutputMessage objects
                        if hasattr(response.output, '__iter__') and len(response.output) > 0:
                            # Get the first message in the output
                            first_message = response.output[0]
                            
                            # Extract text content from the message
                            if hasattr(first_message, 'content') and len(first_message.content) > 0:
                                first_content = first_message.content[0]
                                if hasattr(first_content, 'text'):
                                    response_text = first_content.text
                        
                        # Fallback to string conversion if above doesn't work
                        if response_text is None:
                            response_text = str(response.output)
                            # Try to find JSON content in the response
                            start_idx = response_text.find('{')
                            end_idx = response_text.rfind('}') + 1
                            
                            if start_idx != -1 and end_idx > start_idx:
                                response_text = response_text[start_idx:end_idx]
                        
                        print(f"🔍 CUA response: {response_text}")
                        
                        # Parse the JSON content
                        response_data = json.loads(response_text)
                        
                        # Check installation status
                        if 'installation_status' in response_data:
                            status = response_data['installation_status']
                            
                            if status == "complete":
                                print("✅ Package installation detected as COMPLETE!")
                                installation_complete = True
                                break
                            elif status == "in_progress":
                                print("⏳ Installation still in progress, continuing to monitor...")
                            else:
                                print(f"⚠️ Unexpected status: {status}")
                        else:
                            print("⚠️ Response missing expected 'installation_status' field")
                            
                    except json.JSONDecodeError as e:
                        print(f"⚠️ Error parsing JSON response: {e}")
                        print(f"Raw response: {response.output}")
                    except Exception as e:
                        print(f"⚠️ Error calling CUA model: {e}")
                        print("Continuing with monitoring...")
                else:
                    print("⚠️ Failed to capture screenshot, skipping this iteration...")

                # If installation not complete, wait before next check
                if not installation_complete:
                    print("⏸️ Waiting 10 seconds before next check...")
                    time.sleep(10)
                    screenshot_counter += 1

            if installation_complete:
                print("🎉 Package installation completed successfully!")
            else:
                print("⏰ Installation monitoring timed out - assuming installation is complete")
                print(f"Waited for {max_wait_time} seconds")

            # Brief additional wait to ensure terminal is ready
            print("Waiting 3 seconds for terminal to be ready...")
            time.sleep(3)

        else:
            print("requirements.txt is empty, skipping package installation")
    else:
        print(
            f"requirements.txt not found at {project_requirements_path}, skipping package installation"
        )

except Exception as e:
    print(f"Error reading requirements.txt: {e}")

# Step 3: Open GitHub Copilot panel in Agent mode (Ctrl+Shift+I)
print("Clicking on Copilot chat panel input area...")

# First, click on the approximate location where the Copilot chat input area should be
# This is typically on the right side of the VS Code window
try:
    screen_width, screen_height = pyautogui.size()

    # Calculate approximate position for Copilot chat input area
    # Typically it's on the right side of VS Code, towards the bottom of the panel
    chat_input_x = int(screen_width * 0.85)  # 85% across the screen (right side)
    chat_input_y = int(
        screen_height * 0.7
    )  # 70% down the screen (lower area of chat panel)

    print(
        f"Clicking at approximate chat input location: ({chat_input_x}, {chat_input_y})"
    )
    pyautogui.click(chat_input_x, chat_input_y)
    time.sleep(1)  # Wait for click to register

except Exception as e:
    print(f"Error clicking chat input area: {e}")
    print("Proceeding with opening Copilot panel...")

# Now open the Copilot panel
pyautogui.hotkey("ctrl", "shift", "i")
print("Opened Copilot Chat Panel in Agent mode")
time.sleep(2)

# Additional click to ensure focus is in the input area after panel opens
try:
    # Click again in the chat input area to ensure cursor is positioned correctly
    screen_width, screen_height = pyautogui.size()
    input_area_x = int(screen_width * 0.85)
    input_area_y = int(screen_height * 0.75)  # Slightly lower after panel is open

    print(f"Ensuring cursor focus in chat input area: ({input_area_x}, {input_area_y})")
    pyautogui.click(input_area_x, input_area_y)
    time.sleep(1)

except Exception as e:
    print(f"Error focusing chat input area: {e}")

# Step 4: Pass developer prompt
developer_prompt = "Write a Python function to calculate factorial using recursion."
pyautogui.typewrite(developer_prompt, interval=0.05)
pyautogui.press("enter")
print("Prompt sent to Copilot")

# Step 5: Take screenshots and monitor for completion
print("Starting screenshot capture and monitoring for code generation completion...")


max_wait_time = 120  # Maximum 2 minutes wait for code generation
screenshot_interval = 3  # Take screenshot every 3 seconds
elapsed_time = 0
keep_button_found = False
screenshot_counter = 1

while elapsed_time < max_wait_time and not keep_button_found:
    time.sleep(screenshot_interval)
    elapsed_time += screenshot_interval

    # Take screenshot directly in memory and convert to base64
    try:
        # Modular function to take screenshot and convert to base64
        base64_image = take_screenshot_and_convert_to_base64(screenshot_counter)

        if base64_image is not None:
            # Use Azure OpenAI Computer Use Agent to check if Keep button is enabled
            try:
                # Debug: Print what we're sending to the model
                print(f"🔍 Debug - Sending screenshot to Computer Use Agent model...")

                # Create initial request to Computer Use Agent model
                response = client.responses.create(
                    model="computer-use-preview",
                    tools=[
                        {
                            "type": "computer_use_preview",
                            "display_width": 1920,  # Adjust based on your screen resolution
                            "display_height": 1080,
                            "environment": "windows",
                        }
                    ],
                    input=[
                        {
                            "type": "message",
                            "role": "user",
                            "content": [
                                {"type": "input_text", "text": user_prompt},                                {
                                    "type": "input_image",
                                    "image_url": f"data:image/png;base64,{base64_image}",
                                },
                            ],
                        }
                    ],
                    truncation="auto",
                )
                print(f"🔍 Debug - Model response received {response.output}")
                
                # Extract the actual text content from the response object
                response_text = None
                
                # Check if response.output is a list of ResponseOutputMessage objects
                if hasattr(response.output, '__iter__') and len(response.output) > 0:
                    # Get the first message in the output
                    first_message = response.output[0]
                    
                    # Extract text content from the message
                    if hasattr(first_message, 'content') and len(first_message.content) > 0:
                        first_content = first_message.content[0]
                        if hasattr(first_content, 'text'):
                            response_text = first_content.text
                
                # Fallback to string conversion if above doesn't work
                if response_text is None:
                    response_text = str(response.output)
                    # Try to find JSON content in the response
                    start_idx = response_text.find('{')
                    end_idx = response_text.rfind('}') + 1
                    
                    if start_idx != -1 and end_idx > start_idx:
                        response_text = response_text[start_idx:end_idx]
                
                print(f"🔍 Extracted text: {response_text}")
                
                # Parse the JSON content
                response_data = json.loads(response_text)
                print(f"🔍 Parsed response: {response_data}")
                  # Check if button is enabled
                if 'button' in response_data:
                    button_status = response_data['button']
                    
                    if button_status == "enabled":
                        print("✅ Keep button is ENABLED!")
                        
                        # Press Ctrl+Enter to accept the code (cursor is already in chat input area)
                        print("⌨️ Pressing Ctrl+Enter to accept the generated code...")
                        pyautogui.hotkey('ctrl', 'enter')
                        
                        keep_button_found = True
                        print("🎉 Successfully executed Ctrl+Enter to accept the code!")
                        break
                        
                    elif button_status == "disabled":
                        print("⏳ Keep button is still disabled, continuing to monitor...")
                        
                    else:
                        print(f"⚠️ Unexpected button status: {button_status}")
                else:                    print("⚠️ Response missing expected 'button' field")
                    
            except json.JSONDecodeError as e:
                print(f"⚠️ Error parsing JSON response: {e}")
                print(f"Raw response: {response.output}")
            except Exception as e:
                print(f"⚠️ Error processing model response: {e}")
                
            except Exception as e:
                print(f"Error calling Computer Use Agent model: {e}")
                print("Continuing with screenshot monitoring...")
        else:
            print("⚠️ Failed to capture screenshot, skipping this iteration...")

        # If keep button still not found, pause for 5 seconds before next iteration
        if not keep_button_found:
            print("⏸️ Keep button not enabled yet, pausing for 5 seconds before next iteration...")
            time.sleep(5)

        screenshot_counter += 1
    except Exception as e:
        print(f"Error saving screenshot: {e}")

    # Progress update every 15 seconds
    if elapsed_time % 15 == 0:
        print(
            f"Still monitoring... ({elapsed_time}s elapsed, {screenshot_counter-1} screenshots taken)"
        )

# Handle any errors during the monitoring loop
try:
    pass  # Monitoring loop logic is above
except Exception as e:
    print(f"Error during monitoring: {e}")

# Final status report
if keep_button_found:
    print("\n🎉 SUCCESS: GitHub Copilot has finished generating code!")
    print("✅ The 'Keep' button was detected as enabled and automatically clicked!")
    print(f"📊 Total monitoring time: {elapsed_time}s")
    print(f"📸 Screenshots captured: {screenshot_counter-1}")
    print("🚀 The generated code should now be accepted in your VS Code editor.")
else:
    print(f"\n⏰ Monitoring completed after {max_wait_time}s")
    print("❓ Keep button status was not definitively detected as enabled")
    print(f"📸 Screenshots captured: {screenshot_counter-1}")
    print("💡 You may need to check the GitHub Copilot Chat panel manually")

print(f"� Total screenshots processed: {screenshot_counter-1}")
# Note: Screenshots were processed in memory and sent directly to the API
# Uncomment the folder creation and saving code above if you want to save screenshots for debugging

# Optional: Move mouse to neutral area
pyautogui.moveTo(100, 100)
