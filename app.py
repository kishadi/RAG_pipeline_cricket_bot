from context_builder.context_builder import create_context
from prompt_assistant.assistant import prompt_response

def chat_bot(question):

    # if question == 'N' or question == 'n':
    #     print("Thank you!!")
    #     return 0

    context += create_context(question)
    response = prompt_response(question, context)
    print(response)
    context += '\n' + response

    return response

if __name__ == "__main__":

    context = ''
    print("INFO: Press N/n to end conversation       ")
    print("-----------------")

    while True:

        question = input("User: ")

        if question == "N" or question == "n":
            break

        context += create_context(question)
        response = prompt_response(question, context)
        print(response)
        context += '\n' + response

