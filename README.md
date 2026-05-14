# Empathetic Conversation Generation

This project implements an empathetic chatbot using BlenderBot and analyzes the EmpatheticDialogues dataset.

## Setup

1.  **Install Requirements:**
    ```bash
    pip install -r requirements.txt
    ```

## Usage

### 1. Data Exploration
To download and inspect the EmpatheticDialogues dataset (which is downloaded from Facebook's servers):

```bash
python explore_data.py
```
This script will download the dataset, extract it, and print the first few examples.

### 2. Run the Chatbot
To start a conversation with the empathetic bot:

```bash
python chatbot.py
```
Type your message and press Enter. The bot will respond. Type `quit` or `exit` to stop.
