from twscrape import API

api = API()

# ✅ Replace with your actual Twitter session cookie (auth_token)
auth_token = "919e3c287d06515ea59108e0eb9b97a8c68c5da1"  # <-- REPLACE THIS

# ✅ Add the token
api.add_token(auth_token)

# ✅ Save tokens to a file (for future use)
api.save("twitter_tokens.json")

print("✅ Twitter session saved successfully!")
