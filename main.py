from time import sleep
from playwright.sync_api import Playwright, sync_playwright
from openai import OpenAI
import keyboard
import sys

client = OpenAI(api_key="[ENCRYPTION_KEY]", base_url="https://api.deepseek.com") # Or any other ai which work with openai sdk
history = ""

def typewriter_print(text, delay=0.02):
    """Prints text one character at a time for a 'terminal' feel."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        sleep(delay)
    print()

CYAN = "\033[96m"
GREEN = "\033[92m"
RESET = "\033[0m"
BOLD = "\033[1m"
RED = "\033[91m"

art = f"""
{CYAN}{BOLD}
  _______                      ___   _ 
 |__   __|                    / _ \ (_)
    | | _____      ___ __    / /_\ \ _ 
    | |/ _ \ \ /\ / / '_ \   |  _  || |
    | | (_) \ V  V /| | | |  | | | || |
    |_|\___/ \_/\_/ |_| |_|  \_| |_/|_|
{RESET}
"""
def display_art():     
    print(art)
    typewriter_print(f"{GREEN}>>> Initializing Townsend Press AI Assistant...{RESET}")
    try:
        client.models.list()
        typewriter_print(f"{GREEN}>>> Connection established. Status: READY.{RESET}")
        return True
    except Exception as e:
        typewriter_print(f"{RED}>>> Connection failed. Status: ERROR {e}.{RESET}", delay=0.01)
        return False
    

def ask_ai(question, options):
    global history
    prompt = f"\n\nHistory of the previous questions and tour answers: {history}\nQuestion: {question}\nOptions: {', '.join(options)}\nReturn ONLY the exact text of the correct answer."
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": "You are a helpful assistant. Output only the raw answer text."},
            {"role": "user", "content": prompt},
        ],
        stream=False
    )
    history += f'Question: {question}\nOptions: {options}\nAnswer: {response.choices[0].message.content.strip()}\n\n'
    return response.choices[0].message.content.strip()

url = "https://www.townsendpress.net/sign-in"

if display_art() is True:
    typewriter_print(f"{GREEN}>>> Starting automation...{RESET}")
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        page = browser.new_page(viewport={'width': 1600, 'height': 900})
        sleep(1)
        page.goto(url)
        sleep(1)
        title = page.title()
        print(f"url: {url}, title: {title}")
        username = page.locator("#txtUserNameOrEmail")
        password = page.locator("#txtPassword")
        username.fill("kstaline1@gmail.com")
        password.fill("@Marie1982")
        sign_in = page.locator("#btnLogOn")
        sign_in.click()
        sleep(1)
        input(f"Press Enter {CYAN}to continue...{RESET}")
        #page.goto("https://www.townsendpress.net/class/252651/assignments/208777092")
        sleep(1)
        while True:
            options = page.locator(".answer-option")
            count = options.count()
            for i in range(count):
                print(options.nth(i).inner_text())
            question = page.locator("#directions").inner_text()
            options_list = [options.nth(i).inner_text() for i in range(count)]
            ai_answer = ask_ai(question,options_list)
            print("\n\n")
            print(ai_answer)
            print("\n\n")
            for i in range(count):
                if options.nth(i).inner_text() == ai_answer:
                    options.nth(i).click()
                    break
            sleep(1)
            try:
                next_button = page.locator("#continue").click(timeout=300)
            except:
                pass
            sleep(1)

        

        browser.close()
