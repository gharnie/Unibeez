import os, json, re
from openai import OpenAI

client = OpenAI()
rules = json.load(open(os.path.join(os.path.dirname(__file__), "rules.json")))

def evaluate(texts):
    cov, llm = 0, 0
    for t in texts:
        if any(re.search(k, t, re.I) for r in rules["rules"] for k in r["keywords"]):
            cov += 1
        else:
            llm += 1
            client.chat.completions.create(model="gpt-4o-mini",
                messages=[{"role":"system","content":f"Tags: {[r['tag'] for r in rules['rules']]}"},
                          {"role":"user","content":t}])
    n = len(texts)
    return {"precision": cov/n, "coverage": cov/n, "llm_usage": llm/n}

if __name__ == "__main__":
    print(evaluate(["I want to buy", "just browsing", "please sign me up"]))
