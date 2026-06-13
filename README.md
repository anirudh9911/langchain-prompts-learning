# LangChain Prompts — Learning Practice

A collection of hands-on scripts exploring LangChain's prompt and messaging APIs with OpenAI's GPT-4.

## Files

| File | What it demonstrates |
|------|----------------------|
| [messages.py](messages.py) | Basic `SystemMessage`, `HumanMessage`, `AIMessage` usage and building a message list |
| [chatbot.py](chatbot.py) | Simple CLI chatbot that maintains conversation history across turns |
| [chat_prompt_template.py](chat_prompt_template.py) | `ChatPromptTemplate` with variable substitution (`{domain}`, `{topic}`) |
| [message_placeholder.py](message_placeholder.py) | `MessagesPlaceholder` for injecting dynamic chat history into a template |
| [prompts_generator.py](prompts_generator.py) | Building a `PromptTemplate` and saving it to `template.json` |
| [prompts_ui_static.py](prompts_ui_static.py) | Minimal Streamlit UI — free-text input sent directly to GPT-4 |
| [prompts_ui_dynamic.py](prompts_ui_dynamic.py) | Streamlit UI with dropdowns, loading the saved prompt template and chaining it with the model |

## Setup

**1. Clone the repo and create a virtual environment**

```bash
git clone <repo-url>
cd langchain_prompts
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

**2. Install dependencies**

```bash
pip install -r requirements.txt
```

**3. Set up environment variables**

```bash
cp .env.example .env
# Edit .env and add your OpenAI API key
```

## Running the scripts

**CLI scripts** — run directly:

```bash
python messages.py
python chatbot.py
python chat_prompt_template.py
python message_placeholder.py
```

**Generate the prompt template** (needed before running the dynamic UI):

```bash
python prompts_generator.py
```

**Streamlit apps:**

```bash
streamlit run prompts_ui_static.py
streamlit run prompts_ui_dynamic.py
```

## Requirements

- Python 3.9+
- OpenAI API key
