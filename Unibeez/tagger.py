import os, json, re, sys
from openai import OpenAI
from sentence_transformers import SentenceTransformer

client = OpenAI()
rules = json.load(open(os.path.join(os.path.dirname(__file__), "rules.json")))
SentenceTransformer("all-MiniLM-L6-v2")  # load lightweight embeddings

def tag_text(txt):
    for r in rules["rules"]:
        if any(re.search(k, txt, re.I) for k in r["keywords"]):
            return [r["tag"]]
    return [client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role":"system","content":f"Choose one from {[x['tag'] for x in rules['rules']]}"},
                  {"role":"user","content":txt}]
    ).choices[0].message.content]

if __name__ == "__main__":
    print(tag_text(sys.argv[1] if len(sys.argv)>1 else "I am ready to buy today"))
