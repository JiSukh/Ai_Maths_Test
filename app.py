from huggingface_hub import InferenceClient
import questionary
import matplotlib.pyplot as plt

client = InferenceClient()

def get_user_preferences():
    topic = questionary.select(
        "Choose a topic:",
        choices=["Arithmetic", "Algebra", "Trigonometry", "Geometry", "Calculus"]
    ).ask().lower()

    difficulty = questionary.select(
        "Choose a difficulty:",
        choices=["A-levels (UK)", "AS-level (UK)", "University (UK)"]
    ).ask().lower()

    return topic, difficulty

def get_user_next_action():
    action = questionary.select(
        "Options:",
        choices=["Reveal Answer.","Exit application.", "Choose New topic."]
        
    ).ask()
    
    return action

def generate_question(topic, difficulty):
    prompt = f"Generate a {difficulty} level math question on {topic}. Only return the question, e.g., 'What is 7 + 5?'. Do not include anything other than Latex. Do not include prefixes or suffixes, e.g., '**Question**:...'"
    response = client.chat.completions.create(
        model="deepseek-ai/DeepSeek-V3-0324",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.8,
    )

    question = response.choices[0].message.content.strip()

    return question

def solve_question(question):
    prompt = f"Solve this math problem and give only the final answer as a number or expression: {question}. Do not include anything other than Latex. Do not include prefixes or suffixes, e.g., '**Answer**:...'. Explain everything in steps, using Latex to properly space the different steps."
    response = client.chat.completions.create(
        model="deepseek-ai/DeepSeek-V3-0324",
        messages=[{"role": "user", "content": prompt}],
    )
    
    return response.choices[0].message.content.strip()

import markdown

def show_latex(question, answer, filename="output.html"):
    
    question_str = "Question: " + question
    answer_str ="Answer: " + answer

    # Wrap in HTML with MathJax for LaTeX rendering
    html_template = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8" />
      <script id="MathJax-script" async
        src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js">
      </script>
      <style>
        body {{
          font-family: Arial, sans-serif;
          padding: 20px;
          font-size: 18px;
          line-height: 1.5;
        }}
      </style>
    </head>
    <body>
      <p>{question_str}</p>
      </br>
      </br>
      <p>{answer_str}</p>
    </body>
    </html>
    """

    # Save to file
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html_template)




def main():
    topic, difficulty = get_user_preferences()
    
    
    while True:
        question = generate_question(topic, difficulty)
        ai_answer = solve_question(question)
        show_latex(question, ai_answer)
        action = get_user_next_action()
        
        
        if action == "Exit application.":
            break
        elif action == "Choose New topic.":
            topic, difficulty = get_user_preferences()
            continue
            
        

if __name__ == "__main__":
    main()
