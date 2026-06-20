# Methodology

## Clinical Trial Data Collection

### Source
- **ClinicalTrials.gov API** — AACT database dump and live search endpoints
- **Search terms**: "prosthetic", "prosthesis", "limb prosthesis", "upper extremity prosthesis", "lower extremity prosthesis", "orthotic", "brace", "mobility device"

### Analysis Dimensions
1. Status trends — Count of studies by recruitment status (Recruiting, Active, Completed, Terminated, Withdrawn)
2. Geographic distribution — Count of studies by country, US state-level drill-down
3. Phase distribution — Breakdown by clinical trial phase (Phase I-IV, observational)
4. Temporal trends — Study start dates and completion dates over time
5. Sponsor analysis — Industry vs. academic vs. NIH-funded studies
6. Condition focus — Amputation, congenital limb deficiency, diabetic limb complications

### Tools
- `clinicaltrials_list_studies` — Search and filter studies
- `clinicaltrials_analyze_trends` — Aggregate by status, country, phase
- `clinicaltrials_get_study` — Retrieve full study details by NCT ID

## Access Gap Analysis

### Region Selection Criteria
- Health Professional Shortage Area (HPSA) designations
- Medically Underserved Areas (MUA) status
- Amputation prevalence data (CDC, state health departments)
- Transportation access indices
- Poverty and uninsured rates (Census ACS, Kaiser Family Foundation)

### Data Collection Steps
1. Geocode region centroids
2. Search for providers via OpenStreetMap and NPI Registry
3. Create 30-mile and 60-mile radius buffers
4. Flag zero-provider regions as critical gaps
5. Calculate provider-to-population ratios

### Target Provider Types
| Category | NPI Taxonomy |
|----------|-------------|
| Licensed Prosthetist | 26840W0001X |
| Licensed Orthotist | 26840X0005X |
| Prosthetic/Orthotic Facility | 26840P0220X |
| Rehabilitation Hospital | 26140A0300X |
| DME Supplier | 26140U0004X |

## Limitations
- OSM provider data may be incomplete in rural areas
- NPI data does not capture state scope-of-practice variations
- Travel estimates assume normal conditions
- Clinical trial location data may not reflect actual care delivery locations
