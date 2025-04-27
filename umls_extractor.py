import requests

# 🔑 Replace this with your actual UMLS API Key
API_KEY = "your_real_umls_api_key_here"

# Step 1: Get Ticket-Granting Ticket (TGT)
def get_tgt(api_key):
    auth_url = "https://utslogin.nlm.nih.gov/cas/v1/api-key"
    response = requests.post(auth_url, data={'apikey': api_key})
    tgt_url = response.text.split('action="')[1].split('"')[0]
    return tgt_url

# Step 2: Use TGT to get a service ticket
def get_service_ticket(tgt_url):
    response = requests.post(tgt_url, data={'service': "http://umlsks.nlm.nih.gov"})
    return response.text

# Step 3: Search for a phrase using the service ticket
def search_umls(term, ticket):
    url = f"https://uts-ws.nlm.nih.gov/rest/search/current?string={term}&ticket={ticket}"
    response = requests.get(url)
    return response.json()

# 📝 Your input sentence
sentence = "The patient was admitted to the ICU with sepsis secondary to a urinary tract infection and showed signs of hypotension, elevated lactate, and decreased urine output."

# 🔍 Manually defined key medical phrases to extract
phrases = [
    "ICU",
    "sepsis",
    "urinary tract infection",
    "hypotension",
    "elevated lactate",
    "decreased urine output"
]

# 🎫 Get your authentication ticket
tgt = get_tgt(API_KEY)

# 📤 Print to terminal
print(f"🔍 UMLS concepts found in sentence:")
print(f"📝 \"{sentence}\"\n" + "-" * 60)

# 📁 Save to text file
with open("results.txt", "w", encoding="utf-8") as f:
    f.write(f"🔍 UMLS concepts found in sentence:\n")
    f.write(f"📝 \"{sentence}\"\n")
    f.write("-" * 60 + "\n")

    for phrase in phrases:
        ticket = get_service_ticket(tgt)
        result = search_umls(phrase, ticket)
        hits = result["result"]["results"]

        if hits:
            top = hits[0]
            print(f"📘 Term: {phrase}")
            print(f"🧠 UMLS Match: {top['name']}")
            print(f"🆔 CUI: {top['ui']}")
            print("-" * 60)

            f.write(f"📘 Term: {phrase}\n")
            f.write(f"🧠 UMLS Match: {top['name']}\n")
            f.write(f"🆔 CUI: {top['ui']}\n")
            f.write("-" * 60 + "\n")
        else:
            print(f"❌ No match found for: {phrase}")
            print("-" * 60)

            f.write(f"❌ No match found for: {phrase}\n")
            f.write("-" * 60 + "\n")

print("✅ Results saved to results.txt")
