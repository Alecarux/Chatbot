# main.py

from chatbot.retrieval import LiteChatbot

if __name__ == "__main__":
    bot = LiteChatbot()
    bot.load_docs()

    print("🤖 Chatbot intelligente pronto! Fai una domanda.")
    while True:
        try:
            query = input("\nTu > ")
            result = bot.answer_query(query)
            print(f"\n📌 Risposta: {result['answer']} (sorgente: {result['source']}, conf: {result['confidence']})")
        except KeyboardInterrupt:
            print("\n👋 Fine sessione.")
            break
