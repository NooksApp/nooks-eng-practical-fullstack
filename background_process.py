import subprocess
import time

CHROME_URL_TO_APP = {
  "notion.so": "Notion",
  "github.com": "Github",
  "docs.google.com/document": "Google Docs",
  "docs.google.com/spreadsheets": "Google Sheets",
  "docs.google.com/presentation": "Google Slides",
  "app.asana.com": "Asana",
  "confluence.atlassian.com": "Confluence",
  "mixpanel.com": "Mixpanel",
  "app.logrocket.com": "LogRocket",
  "stackoverflow.com": "Stack Overflow",
  "intercom.com": "Intercom",
  "figma.com": "Figma",
  "slack.com": "Slack",
  "calendar.google.com": "Calendar",
  "mail.google.com": "Mail"
}

def get_current_process():
    cmd = """
        tell application "System Events"
            set frontApp to name of first application process whose frontmost is true
        end tell
        return frontApp
    """
    result = subprocess.run(['osascript', '-e', cmd], capture_output=True)
    return result.stdout.strip().decode("utf-8") 

def get_application_path():
    cmd = """
        tell application "System Events"
            set frontApp to application file of first application process whose frontmost is true
        end tell
        return frontApp
    """
    result = subprocess.run(['osascript', '-e', cmd], capture_output=True)
    return result.stdout.strip().decode("utf-8") 

def get_application_URL():
    cmd = """
        tell application "Google Chrome"
            set currentTabUrl to URL of active tab of front window
        end tell
        return currentTabUrl
    """
    result = subprocess.run(['osascript', '-e', cmd], capture_output=True)
    return result.stdout.strip().decode("utf-8") 

def get_current_application():
    process = get_current_process();
    if process == "Electron":
        path = get_application_path()
        if "Visual Studio Code" in path:
            return "Visual Studio Code"
    if process == "Google Chrome":
        URL = get_application_URL()
        for url in CHROME_URL_TO_APP:
            if url in URL:
                return CHROME_URL_TO_APP[url]
    return process

while True:
    print(get_current_application())
    time.sleep(5)
