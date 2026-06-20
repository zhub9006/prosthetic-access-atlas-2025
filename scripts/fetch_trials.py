#!/usr/bin/env python3
"""Fetch prosthetic clinical trials from ClinicalTrials.gov."""
import argparse, json, requests
BASE_URL = "https://clinicaltrials.gov/api/v2"
def search_trials(query, page_size=100):
    studies, page_token = [], None
    while True:
        params = {"query.term": query, "pageSize": page_size, "fields": "nctId,title,status,country,phase,startDate,completionDate,sponsor,condition"}
        if page_token: params["pageToken"] = page_token
        r = requests.get(f"{BASE_URL}/studies", params=params)
        if r.status_code != 200: break
        data = r.json(); studies.extend(data.get("studies", [])); page_token = data.get("nextPageToken")
        if not page_token: break
    return studies
def analyze_by_status(studies):
    c = {}; [c.update({s.get("status","Unknown"): c.get(s.get("status","Unknown"),0)+1}) for s in studies]; return c
def analyze_by_country(studies):
    c = {}; [c.update({co: c.get(co,0)+1}) for s in studies for co in s.get("country",[])] ; return c
def main():
    p = argparse.ArgumentParser(); p.add_argument("--query", default="prosthetic"); p.add_argument("--output", default="data/raw_trials.json"); p.add_argument("--analysis", default=""); p.add_argument("--page-size", type=int, default=100); a = p.parse_args()
    studies = search_trials(a.query, a.page_size)
    with open(a.output, "w") as f: json.dump(studies, f, indent=2)
    print(f"Saved {len(studies)} studies")
    if "status" in a.analysis: print(f"By Status: {json.dumps(analyze_by_status(studies), indent=2)}")
    if "country" in a.analysis: print(f"By Country: {json.dumps(analyze_by_country(studies), indent=2)}")
if __name__ == "__main__": main()
