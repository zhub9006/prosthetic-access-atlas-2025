# Prosthetic Access Atlas

An open-access resource mapping prosthetic and orthotic care access gaps and clinical trial landscapes to improve prosthetic care equity in underserved regions of the United States.

## Mission

Millions of Americans with limb loss or limb differences face barriers to accessing prosthetic and orthotic care — particularly in rural and economically disadvantaged regions. This project aims to:
1. **Map the clinical trial landscape** for prosthetic interventions to identify where research is concentrated and where gaps exist.
2. **Identify coverage gaps** by locating prosthetic/orthotic providers relative to underserved populations.
3. **Provide actionable data** for policymakers, clinicians, researchers, and advocates working to improve prosthetic care access.

## Focus Regions

Three regions were selected for in-depth gap analysis due to documented healthcare access challenges:

| Region | Key Challenges |
|--------|---------------|
| **Rural West Virginia** | Highest rates of opioid-related amputations, limited rehab infrastructure, sparse specialist coverage |
| **Eastern Kentucky** | High poverty rates, limited transportation networks, few prosthetists per capita |
| **Mississippi Delta** | Persistent poverty, lowest health insurance coverage rates, critical shortage of rehabilitation services |

## Repository Structure

```
prosthetic-access-atlas-2025/
├── README.md                  ← Main overview
├── METHODOLOGY.md             ← Data collection methods
├── data/
│   ├── clinical_trials.md     ← Trial listings and trend analysis
│   ├── access_gaps.md         ← Regional provider gap analysis
│   └── provider_locations.csv ← Raw provider coordinate data
├── scripts/                   ← Data collection scripts
├── config/
│   └── regions.json           ← Region definitions
└── CONTRIBUTING.md            ← How to contribute
```

## Status

Initial data collection framework complete. Live API data ingestion pending service restoration.

## Get Involved
- Report access gaps via [Issues](https://github.com/zhub9006/prosthetic-access-atlas-2025/issues)
- Contribute data — See [CONTRIBUTING.md](CONTRIBUTING.md)

## License
CC BY 4.0 — Open and freely available.
