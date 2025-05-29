crypto_db = {
    "Bitcoin": {
        "price_trend": "rising",
        "market_cap": "high",
        "energy_use": "high",
        "sustainability_score": 3 / 10
    },
    "Ethereum": {
        "price_trend": "stable",
        "market_cap": "high",
        "energy_use": "medium",
        "sustainability_score": 6 / 10
    },
    "Cardano": {
        "price_trend": "rising",
        "market_cap": "medium",
        "energy_use": "low",
        "sustainability_score": 8 / 10
    }
}

def analyze_query(user_query):
    user_query = user_query.lower()

    if "trending" in user_query or "rising" in user_query:
        trending = [coin for coin, data in crypto_db.items() if data["price_trend"] == "rising"]
        return f"📈 These coins are trending up: {', '.join(trending)}"

    elif "sustainable" in user_query or "eco" in user_query:
        sustainable = [coin for coin, data in crypto_db.items()
                       if data["energy_use"] == "low" and data["sustainability_score"] > 0.7]
        if sustainable:
            best = max(sustainable, key=lambda x: crypto_db[x]["sustainability_score"])
            return f"🌱 Invest in {best}! It’s eco-friendly and has long-term potential!"
        else:
            return "♻️ No highly sustainable coins found at the moment."

    elif "profitable" in user_query or "best investment" in user_query:
        profitable = [coin for coin, data in crypto_db.items()
                      if data["price_trend"] == "rising" and data["market_cap"] == "high"]
        if profitable:
            return f"💰 For profitability, consider: {', '.join(profitable)}"
        else:
            return "📉 No highly profitable coins at the moment."

    elif "advice" in user_query or "recommend" in user_query:
        # Simple recommendation based on both profitability and sustainability
        best_combined = sorted(
            crypto_db.items(),
            key=lambda item: (
                (item[1]["price_trend"] == "rising"),
                (item[1]["market_cap"] == "high"),
                (item[1]["energy_use"] == "low"),
                item[1]["sustainability_score"]
            ),
            reverse=True
        )
        best_choice = best_combined[0][0]
        return f"🤖 I recommend {best_choice} based on overall profitability and sustainability."

    else:
        return "🤔 I didn't understand that. Try asking about trending coins, sustainability, or profitability."

# Sample chat simulation
while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        print("Bot: Goodbye! 👋")
        break
    response = analyze_query(user_input)
    print("Bot:", response)
