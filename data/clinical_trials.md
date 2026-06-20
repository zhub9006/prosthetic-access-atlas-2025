# Prosthetic Clinical Trials — Landscape Analysis

> **Note:** Live data ingestion from ClinicalTrials.gov was unavailable during the initial build phase due to API connectivity issues. The framework below is ready for automated population.

## Search Strategy

Primary terms: "prosthetic" OR "prosthesis" OR "limb prosthesis"
Secondary: "orthotic" OR "brace" OR "mobility device"
Conditions filtered: Amputation, Congenital Limb Deficiency, Diabetic Foot Complications

## Expected Trend Analysis

### By Status (Anticipated Distribution)
| Status | Expected Share | Notes |
|--------|---------------|-------|
| Recruiting | ~25% | Actively enrolling participants |
| Active, not recruiting | ~15% | Treatment phase complete, follow-up ongoing |
| Completed | ~40% | Finished without results posted |
| Terminated / Withdrawn | ~10% | Stopped early for safety/funding |
| Not yet recruiting | ~10% | Pre-clinical or planning phase |

### By Phase (Anticipated Distribution)
| Phase | Expected Share |
|-------|---------------|
| Phase I (Safety) | ~12% |
| Phase II (Efficacy) | ~20% |
| Phase III (Confirmatory) | ~35% |
| Phase IV (Post-market) | ~8% |
| Observational | ~25% |

### Key Research Themes (Current)
1. **Osseointegration** — Direct skeletal attachment of prostheses (increasing in trials)
2. **Targeted Muscle Reinnervation (TMR)** — Nerve mapping for improved prosthetic control
3. **Bionic/Myoelectric limbs** — Advanced control systems and sensory feedback
4. **Socket design & fit** — Comfort, pressure distribution, gait optimization
5. **Pediatric prosthetics** — Growth-adaptive devices, congenital limb deficiency
6. **Diabetic limb preservation** — Prosthetic interventions post-amputation
7. **Cost-effectiveness** — Comparing advanced vs. standard prosthetic options

### Geographic Concentration (Known Patterns)
- **High density:** Northeast corridor (Boston, Philadelphia, Baltimore), California, Texas
- **Moderate density:** Midwest academic centers, Southeast urban hubs
- **Low density:** Rural Appalachia, Deep South, Mountain West — coverage gap regions

## Replication Instructions

```bash
python scripts/fetch_trials.py --query "prosthetic" --output data/raw_trials.json
python scripts/analyze_trends.py --input data/raw_trials.json --analysis status,country,phase --output data/clinical_trials.md
```

---
*Last updated: Framework stage — awaiting live data connection*
