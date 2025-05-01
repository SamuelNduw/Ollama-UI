![Ollama Image](https://ollama.com/public/blog/embedding-models.png)

# Ollama-UI
This project is an AI chat application that utilizes streamlit for the UI and Ollama for running and interacting with the models.
- Message memory, allowing the model to remember and have context of the chat.
- Document Parsing, the model can now take documents such as PDFs and users can ask questions in the context of the document inputted.

# Ollama Setup
Ollama needs to be installed and you need to have downloaded a model before setting up the project. 
- Ollama executable can be found here [Ollama](https://ollama.com/)
- Ollama [models](https://ollama.com/search) \
_**I recommend using any model less than 3B parameters, For testing and low compute power machines/devices.
These will run at a decent speed.**_

# Project Setup

### Prerequisites
Ollama \
Python 3.8 and above \
Pip

### Step 1: Clone the Repository
```
git clone https://github.com/SamuelNduw/Ollama-UI.git
cd Ollama-UI
```


### Step 2: Create a virtual environment in the root directory 
```
python -m venv virt
```

### Step 3: Activate your Virtual Environment
- On windows
```
.\virt\Scripts\activate
```
- On Linux/macOS
```
source virt/bin/activate
```

### Step 4: Install Dependencies
```
pip install -r requirements.txt
```

### Step 5: Run the Streamlit Server
```
streamlit run main.py
```

### The application should provide a link and run in the browser.