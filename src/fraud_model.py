import openai

def predict_fraud(transaction):
    client = openai.OpenAI()
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": f"Is this fraud? {transaction}"}],
    )
    decision = response.choices[0].message.content
    execute_transaction(transaction, decision)
    return decision
