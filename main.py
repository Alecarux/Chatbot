# main.py
from chatbot.retrieval import LiteChatbot

if __name__ == "__main__":
    bot = LiteChatbot()
    bot.load_docs()

    print("🤖 Chatbot pronto! Scrivi la tua domanda.")
    while True:
        try:
            query = input("\nTu > ")
            response, source, score = bot.search(query)
            print(f"\n🧠 Risposta (da '{source}', sim: {score:.2f}):\n{response}")
        except KeyboardInterrupt:
            print("\n👋 Ciao!")
            break
