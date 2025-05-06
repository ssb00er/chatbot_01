# 🤖 AI Chatbot with Rasa

A fully customizable AI-powered chatbot built using the [Rasa Open Source](https://rasa.com/) framework. 
This project demonstrates how to design conversational agents with machine learning, natural language understanding (NLU), dialogue management, and custom Python actions.
  
---
  
# 📌 Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Training the Model](#training-the-model)
- [Running the Bot](#running-the-bot)
- [Custom Actions](#custom-actions)
- [Testing](#testing)
- [Examples](#examples)
- [Deployment](#deployment)
- [Customization](#customization)
- [License](#license)

---

# 🚀 Features

- ☑️ Intent recognition and entity extraction
- 🧠 Dialogue management using stories and rules
- 🔁 Context-aware conversations
- ⚙️ Custom Python actions for dynamic responses
- 💬 Easy integration with messaging platforms (Telegram, Slack, Web)
- 🧪 Built-in conversation testing

---

# 🛠️ Tech Stack

- **Language**: Python 3.8+
- **Framework**: Rasa Open Source
- **Data Format**: YAML
- **Optional Tools**: ngrok (for tunneling), Docker (for deployment), Flask (for integration)

---


# 📁 Project Structure

├── actions/        &nbsp;&nbsp;&nbsp;&nbsp;    # Custom actions in Python  
├── data/  
│   ├── ```nlu.yml```    &nbsp;&nbsp;&nbsp;&nbsp;         # Intent and entity training examples  
│   ├── ```stories.yml```    &nbsp;&nbsp;&nbsp;&nbsp;     # Conversation training stories  
│   ├── ```rules.yml```         &nbsp;&nbsp;&nbsp;&nbsp;  # Rule-based conversation flows  
│   └── ```test_stories.yml```  &nbsp;&nbsp;&nbsp;&nbsp;  # Automated test conversations  
├── models/           &nbsp;&nbsp;&nbsp;&nbsp;      # Trained model files  
├── ```config.yml```      &nbsp;&nbsp;&nbsp;&nbsp;        # NLU pipeline and policy config  
├── ```domain.yml```        &nbsp;&nbsp;&nbsp;&nbsp;      # Intents, entities, slots, responses  
├── ```credentials.yml```    &nbsp;&nbsp;&nbsp;&nbsp;     # Messaging platform credentials  
├── ```endpoints.yml```      &nbsp;&nbsp;&nbsp;&nbsp;     # Action server and tracker endpoints  
└── README.md         &nbsp;&nbsp;&nbsp;&nbsp;      # Project documentation    

---

# 💻 Installation


## 1. Clone the repository  
  
```bash git clone https://github.com/ssb00er/chatbot_01.git```  
```cd chatbot_01```

## 2. Create a virtual environment (recommended)  
  
```python -m venv venv```  
```venv/bin/activate  # On Windows: venv\Scripts\activate```  
  
## 3. Install dependencies  
  
```pip install -r requirements.txt```  
  
If requirements.txt isn't available, just install Rasa:  
```pip install rasa```  
  
---
  
# 🧠 Training the Model  
  
To train your chatbot using the NLU and story data:  
```rasa train```  
  
---  
  
# ▶️ Running the Bot  
  
Run NLU and Core (Chatbot only):  
```rasa shell```  
  
Run with custom actions:  
## Terminal 1: Run custom actions  
```rasa run actions```  
  
## Terminal 2: Run the bot  
```rasa shell```  
  
---  
  
# ⚙️ Custom Actions  
  
Custom actions allow your bot to execute Python code (e.g., call APIs, perform logic):  
1. Edit ```actions/actions.py```  
2. Register the action in ```domain.yml```  
3. Run the action server:  
  
```rasa run actions```  
  
---  
  
  
# 🧪 Testing  

To test conversation flow:  
```rasa test```  
  
To manually test the chatbot:  
```rasa shell```  
  
---  
  
# 🔧 Customization  

To adapt the bot to your own use case:  

1. Add new intents and training examples in ```nlu.yml```  
  
2. Add corresponding responses in ```domain.yml```  
  
3. Define story paths in ```stories.yml``` or ```rules.yml```  
  
4. Add any logic in ```actions/actions.py```  
  
5. Retrain the model using ```rasa train```  
  
---  
  
# 📄 License  
This project is licensed under the MIT License — see the LICENSE file for details.  
  
---  
  
🙋‍♀️ Contact  
For questions, issues, or collaboration ideas:  
  
Email: sagar.bisht376@gmail.com  
