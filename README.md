# Project Setup

### Prerequisites
Ollama \
Python 3.8 and above

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