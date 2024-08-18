from semantic_spotter import query_response
import pandas as pd

questions = ['What does the author say about AirbNb?', "I want to be a billionaire. What does Paul Graham say about that?",
             'What is the opinion of the author on India?']

def testing_pipeline(questions):
  test_feedback  = []
  for i in questions:
    print(i)
    print(query_response(i))
    print('\n Please provide your feedback on the response provided by the bot')
    user_input = input()
    test_feedback.append((i,query_response(i),user_input))
  feedback_df = pd.DataFrame(test_feedback, columns =['Question', 'Response', 'Good or Bad'])
  return feedback_df