from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline
import torch

model_name = "facebook/blenderbot-400M-distill"

print(f"Loading conversational model: {model_name}...")
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

print("Loading safety classifier (Toxicity ML Model)...")
toxicity_classifier = pipeline("text-classification", model="martin-ha/toxic-comment-model")

def is_unsafe(text):
    results = toxicity_classifier(text)
    # The classifier returns results like [{'label': 'toxic', 'score': 0.98}]
    if results and results[0]['label'] == 'toxic' and results[0]['score'] > 0.6:
        return True
    return False

conversation_history = []

def generate_response(user_input):
    global conversation_history
    if is_unsafe(user_input):
        return "I am an AI, and I cannot provide the help you need. If you or someone you know is going through a difficult time, please reach out to a professional, emergency services, or a crisis helpline immediately."
        
    conversation_history.append(user_input)
    # Keep the context window short to avoid generic confusion (last 5 messages)
    if len(conversation_history) > 5:
        conversation_history = conversation_history[-5:]
        
    # Inject profound empathy instructions natively via BlenderBot's persona tokening 
    persona = "your persona: i am a deeply empathetic, caring, and supportive listener who gives long thoughtful answers.\n"
    history_string = "\n".join(conversation_history)
    
    inputs = tokenizer([persona + history_string], return_tensors="pt")
    
    reply_ids = model.generate(
        **inputs,
        max_length=128,
        do_sample=True,
        temperature=1.2,
        top_p=0.9,
        repetition_penalty=2.0
    )
    
    response = tokenizer.batch_decode(reply_ids, skip_special_tokens=True)[0]
    conversation_history.append(response)
    return response

    
    
