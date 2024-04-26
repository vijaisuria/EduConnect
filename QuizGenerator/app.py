import os
from flask import Flask, request, render_template
import google.generativeai as genai
import re

app = Flask(__name__)

# Load the Gemini API model
gemini_model = genai.GenerativeModel('gemini-pro')


def generate_questions(topics):
  """Generate quiz questions based on user topics using the Gemini API."""
  questions = []

  for idx, topic in enumerate(topics, start=1):
    query = f"What are some questions related to '{topic}'? I need you to give the question, along with options and answers to be fed to the quiz app. For example: Question: '....'\nOptions: '1)... ' \nAnswer: '...'"
    response = gemini_model.generate_content(query).text.strip()

    # Parse the response for question, options, and answer
    question_text = ""
    options = []
    answer = ""

    try:
      for response_line in response.splitlines():
        if response_line.startswith("Question:"):
          question_text = response_line.split(":")[1].strip()
        elif response_line.startswith("Options:"):
          options = response_line.split(":")[1].strip().split(",")
          options = [option.strip() for option in options]  # Remove leading/trailing whitespaces
        elif response_line.startswith("Answer:"):
          answer = response_line.split(":")[1].strip()
    except Exception as e:
      print(f"Error parsing response for topic '{topic}': {e}")

    # Create the question dictionary and append it if all parts are extracted
    if question_text and options and answer:
      question = {
          'numb': idx,
          'question': question_text,
          'answer': answer,
          'options': options,
      }
      questions.append(question)

  return questions


@app.route('/', methods=['GET', 'POST'])
def index():
  if request.method == 'POST':
    topics = request.form.getlist('topic')

    # Generate questions based on user-entered topics
    generated_questions = generate_questions(topics)

    return render_template('quiz.html', questions=generated_questions)
  return render_template('index.html')


if __name__ == '__main__':
  app.run(debug=True)
