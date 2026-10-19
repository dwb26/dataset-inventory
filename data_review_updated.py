# Consolidated datasets list (23 unique datasets)

import html

data = [
    {
        "Dataset": "2021 Census",
        "Organisation": "ONS",
        "Country": "England/Wales",
        "Years available": "2021 (2011 for comparison)",
        "Update frequency": "10-yearly",
        "Geographical level": "OA, LSOA, MSOA, LA",
        "Unit of observation": "Individual/Household (aggregated)",
        "Population covered": "Whole population",
        "Main domains/variables": "Age, sex, ethnicity, education, tenure, household type, employment",
        "Access": "Open",
        "Typical role": "Population frame / Constraints",
        "Workflow stage": "Population frame",
        "PHI theme": "Air pollution/Healthy places/Food/Health inequalities",
        "Strengths": "Complete coverage",
        "Limitations": "Infrequent updates",
        "Example applications": "Base population synthesis",
    },
    {
        "Dataset": "Adult Psychiatric Morbidity Survey (APMS)",
        "Organisation": "NHS England & NatCen Social Research",
        "Country": "England",
        "Years available": "1993, 2000, 2007, 2014, 2023–2024",
        "Update frequency": "Periodic (~every 7 years)",
        "Geographical level": "National and Regional (Strategic Health Authority level / Postcode Sector primary sampling units)",
        "Unit of observation": "Individual adult survey respondent",
        "Population covered": "Private household residents in England aged 16 and over",
        "Main domains/variables": "Screening & diagnostic assessments for common mental disorders (CMD), PTSD, psychosis, ADHD, autism, self-harm, suicidal ideation, alcohol/drug dependencies, service use, and medication",
        "Access": "Restricted",
        "Typical role": "Health Outcomes/Validation",
        "Workflow stage": "Health outcomes",
        "PHI theme": "Public mental health",
        "Strengths": "Gold-standard national benchmark for psychiatric prevalence in the community, capturing untreated mental illness that never appears in primary or secondary care records",
        "Limitations": "Low sample frequency (every 7 years), excludes institutional populations (prisons, care homes, communal establishments), and relies on self-reported symptoms/screening tools",
        "Example applications": "Validating baseline mental health distributions, comorbidities, and untreated psychiatric illness prevalence across synthetic sub-demographics",
    },
    {
        "Dataset": "Clinical Practice Research Datalink (CPRD)",
        "Organisation": "MHRA & NIHR",
        "Country": "UK-wide (England, Scotland, Wales, NI)",
        "Years available": "1987–present",
        "Update frequency": "Continuous (updated monthly/daily)",
        "Geographical level": "GP Practice level mapped to national/regional boundaries; linkable to LSOA deprivation measures",
        "Unit of observation": "Individual longitudinal patient record",
        "Population covered": "Over 60 million total anonymised patients (~20% active UK population coverage across participating GP practices)",
        "Main domains/variables": "Clinical diagnoses (Read/Snomed codes), primary care prescriptions, lab tests, immunisations, symptoms, secondary care referrals, and linked HES/cancer registration/mortality data",
        "Access": "Restricted",
        "Typical role": "Health Outcomes/Validation",
        "Workflow stage": "Health outcomes",
        "PHI theme": "Public mental health",
        "Strengths": "Unrivalled real-world longitudinal coverage with deep medical histories, multi-decade follow-ups, and individual-level linkage across primary, hospital, and death registries",
        "Limitations": "Requires rigorous protocol approval (RDG) and license fees; subject to variable clinical coding quality, missing secondary care nuance, and potential GP practice sampling bias",
        "Example applications": "Primary ground-truth data for parameterising disease incidence transitions, co-morbidity matrices, and validating synthetic longitudinal patient trajectories",
    },
    {
        "Dataset": "Defra Data Services Platform",
        "Organisation": "Department for Environment, Food & Rural Affairs & Environment Agency",
        "Country": "England (with links provided to parallel services in Scotland, Wales, and Northern Ireland)",
        "Years available": "Variable. Generally covers active asset registers, real-time gauges, and historical modelling series spanning the last few decades",
        "Update frequency": "Variable, depending on the dataset. Ranges from real-time/live feeds to annual administrative releases",
        "Geographical level": "Highly granular spatial data.",
        "Unit of observation": "Spatial features (points, lines, polygons) or individual localised monitoring metrics (e.g., water quality test sample, local permit ratings)",
        "Population covered": "N/A (Physical environmental, land, and asset tracking)",
        "Main domains/variables": "Flood risk areas, river and sea levels, water quality monitoring indices, biodiversity and ecosystem tracking, waste management permits, and industrial pollution inventories",
        "Access": "Open",
        "Typical role": "Exposure/Contextual Enrichment. For example, once your synthetic population has residential addresses, you can overlay the Environmental Agency's flood risk maps to determine which simulated households face high environmental or climate vulnerabilities",
        "Workflow stage": "Contextual enrichment",
        "PHI theme": "Air pollution",
        "Strengths": "Provides official regulatory data on corporate pollution and catchment health",
        "Limitations": "Requires significant GIS/spatial data processing skills to clean and filter for health modelling",
        "Example applications": "Spatially joining localised flood risk zones or water catchment pollution profiles to synthetic household locations to evaluate the intersection of environmental hazards with socioeconomic deprivation",
    },
    {
        "Dataset": "English Prescribing Data (EPD)",
        "Organisation": "NHS Business Services Authority (NHSBSA)",
        "Country": "England",
        "Years available": "2014-present",
        "Update frequency": "Monthly",
        "Geographical level": "GP Practice level",
        "Unit of observation": "Individual prescription item presentation per practice",
        "Population covered": "All patients issued a prescription in primary care in England that was successfully submitted for reimbursement",
        "Main domains/variables": "British National Formulary codes, chemical substance description, number of items prescribed, total quantity dispensed, and Net Ingredient Cost",
        "Access": "Open",
        "Typical role": "Health Outcomes/Validation. If your synthetic population predicts a spike in respiratory or alcohol-related issues in a specific region, you validate that against the real-world volume of inhalers or liver-related medications prescribed by local practices",
        "Workflow stage": "Health outcomes",
        "PHI theme": "Public mental health",
        "Strengths": "Universal coverage of all NHS community prescriptions",
        "Limitations": "Strictly practice-level aggregated statistics, meaning you cannot see individual patient demographics (age, gender, ethnicity) or cross-reference comorbid conditions on a single person",
        "Example applications": "Evaluating the hyper-local financial and clinical impact of chronic illnesses within a synthetic population model by benchmarking against regional BNF therapeutic group prescribing rates",
    },
    {
        "Dataset": "General Practice Extraction Service (GPES)",
        "Organisation": "NHS England & NHS Business Services Authority",
        "Country": "England",
        "Years available": "Mid 2010s-present",
        "Update frequency": "Monthly (for EPD dispensing data) to periodic/fortnightly (for specific GPES research extractions)",
        "Geographical level": "Mapped from National summary datasets down to Sub-ICB/Primary Care Network and specific GP Practice locations",
        "Unit of observation": "Individual prescription item dispense or individual coded diagnostic/clinical marker extracted from GP electronic records",
        "Population covered": "All patients issued a prescription in primary care or included in specific national primary care audit extractions in England",
        "Main domains/variables": "Exact chemical/generic drug names, therapeutic classifications, dosage quantities, costs, and the anonymised age/sex metadata profiles of patients receiving the medications",
        "Access": "Mixed",
        "Typical role": "Health Outcomes/Validation. For example, if a simulation estimates a drop in local smoking rates or an uptick in respiratory illness due to local air pollution changes, researchers check the local prescribing trends for nicotine replacement therapies or inhalers to validate those behavioural shifts",
        "Workflow stage": "Health outcomes",
        "PHI theme": "Public mental health",
        "Strengths": "Captures the massive volume of healthcare management that never reaches a hospital room",
        "Limitations": "Prescribing datasets show what was dispensed at a pharmacy, but cannot guarantee the patient actually took the medication. Standard open files lack cross-linked clinical diagnostic histories (e.g. you can see an inhaler was prescribed, but not whether it was explicitly used for asthma or COPD)",
        "Example applications": "To simulate and evaluate primary care medication costs, or validating localised chronic illness rates within a synthetic population by cross-referencing targeted cardiovascular or respiratory prescription volumes",
    },
    {
        "Dataset": "Health Survey for England (HSE)",
        "Organisation": "NHS England & NatCen Social Research",
        "Country": "England",
        "Years available": "1991–present",
        "Update frequency": "Annual",
        "Geographical level": "National, Regional, and Local Authority levels (via Postcode Sector clusters)",
        "Unit of observation": "Individual survey respondent (adults and children)",
        "Population covered": "Representative sample of ~8,000 adults and ~2,000 children living in private households annually",
        "Main domains/variables": "Objective biological markers (blood pressure, BMI, blood/saliva samples), chronic health conditions, lifestyle choices (smoking, alcohol, diet), and general wellbeing",
        "Access": "Open",
        "Typical role": "Population Baseline / Health Outcomes",
        "Workflow stage": "Donor microdata",
        "PHI theme": "Food/Tobacco/Alcohol",
        "Strengths": "Combines self-reported lifestyle metrics with physical measurements (height, weight, blood tests), avoiding self-reporting bias for clinical markers like hypertension and obesity",
        "Limitations": "Cross-sectional design prevents longitudinal individual tracking; sample sizes are too small for granular hyper-local (LSOA) estimations without spatial micro-simulation",
        "Example applications": "Joint probability distributions for agent-based models (e.g., correlating BMI, smoking status, age, and chronic condition prevalence to populate realistic agent profiles)",
    },
    {
        "Dataset": "Hospital Episode Statistics (HES)",
        "Organisation": "NHS England",
        "Country": "England",
        "Years available": "1989-present for Admitted Patient Care (APC); 2003-present for Outpatients",
        "Update frequency": "Monthly provisional updates; finalised annual data refreshes",
        "Geographical level": "Patient residence mapped down to LSOA boundaries, Integrated Care Boards, and specific treating NHS Trust sites",
        "Unit of observation": "Episode/Admission (Specifically, a Finished Consultant Episode - FCE). A single patient can have multiple episodes or admissions over time",
        "Population covered": "All patients treated in NHS hospitals in England",
        "Main domains/variables": "Clinical diagnoses, surgical procedures/operations, type of admission, discharge destination, total bed days, and demographic data",
        "Access": "Restricted/Secure Lab: High-level aggregated summary tables are open, but individual record-level data requires a formal application",
        "Typical role": "Health Outcomes/Validation",
        "Workflow stage": "Health outcomes",
        "PHI theme": "Air pollution/Alcohol/Health inequalities/Public mental health",
        "Strengths": "Comprehensive coverage, large sample size allows for precise modelling of rare clinical conditions and long-term cohort linkage",
        "Limitations": "Lacks detailed primary care information, lifestyle parameters, or metrics on individuals who are sick but do not go to hospital",
        "Example applications": "Serving as the direct health outcome metric to model and evaluate the simulated impact of environmental air pollution spikes or regional alcohol control policies on emergency hospital admission trends",
    },
    {
        "Dataset": "Index of Multiple Deprivation (IMD)",
        "Organisation": "Ministry of Housing, Communities and Local Government",
        "Country": "England",
        "Years available": "2000, 2004, 2007, 2010, 2015, 2019, 2025",
        "Update frequency": "Every 4 to 5 years (irregular)",
        "Geographical level": "LSOA",
        "Unit of observation": "Area-level aggregate",
        "Population covered": "The entire population of England",
        "Main domains/variables": "Income, Employment, Education/Skills, Health/Disability, Crime, Barriers to Housing & Services, and the Living Environment",
        "Access": "Open",
        "Typical role": "Exposure/Contextual Enrichment; look up a simulated individual's LSOA's IMD decile to understand the level of socioeconomic deprivation they are exposed to in daily life",
        "Workflow stage": "Contextual enrichment",
        "PHI theme": "Health inequalities",
        "Strengths": "Granular local geography, breaks down overall deprivation into specific themes",
        "Limitations": "It is a relative ranking measure, not an absolute one (e.g. LSOA ranked 100 is not twice as poor as one ranked 200). It is area level, meaning it can suffer from ecological fallacy (not everyone in a deprived neighbourhood is personally deprived)",
        "Example applications": "Track, simulate and validate health inequalities by grouping a synthetic population into national deprivation deciles",
    },
    {
        "Dataset": "Labour Force Survey (LFS)",
        "Organisation": "ONS",
        "Country": "UK",
        "Years available": "1992–present",
        "Update frequency": "Quarterly",
        "Geographical level": "Standard government regions (e.g. North West, South West)",
        "Unit of observation": "Individual and Household",
        "Population covered": "People living in households in the UK",
        "Main domains/variables": "Employment status, unemployment, economic inactivity, occupation, industry sector, hours worked, job training, qualifications, and core demographic details",
        "Access": "End User Licence for standard anonymised research files",
        "Typical role": "Donor microdata",
        "Workflow stage": "Donor microdata",
        "PHI theme": "Healthy places/Health inequalities",
        "Strengths": "Large sample size; gives a highly detailed, multi-dimensional look at an individual's working life",
        "Limitations": "Sample survey",
        "Example applications": "Serving as the primary microdata source to simulate employment-related exposures, income distributions, and economic activity within a simulated regional workforce",
    },
    {
        "Dataset": "Living Costs and Food Survey (LCFS)",
        "Organisation": "ONS & DEFRA",
        "Country": "UK-wide",
        "Years available": "1957–present (formerly Family Expenditure Survey)",
        "Update frequency": "Annual (continuous collection)",
        "Geographical level": "National and UK Region / Country level",
        "Unit of observation": "Household and individual diary keeper",
        "Population covered": "~5,000 private households in the UK per year keeping detailed 2-week spending diaries",
        "Main domains/variables": "Detailed household income, expenditure items (food, alcohol, tobacco, utilities, transport), quantities of food purchased, and household demographic composition",
        "Access": "Open",
        "Typical role": "Socioeconomic / Behavioural Baseline",
        "Workflow stage": "Donor microdata",
        "PHI theme": "Food/Alcohol",
        "Strengths": "Gold standard for granular household financial choices, expenditure patterns, and physical food purchasing quantities linked directly to income brackets",
        "Limitations": "High survey burden leads to potential non-response bias; small annual sample size restricts hyper-local spatial disaggregation",
        "Example applications": "Modelling economic determinants of health within synthetic populations (e.g., spending capacity on healthy food, tobacco/alcohol expenditure, energy poverty)",
    },
    {
        "Dataset": "Met Office Climate Data Portal",
        "Organisation": "Met Office",
        "Country": "UK",
        "Years available": "Historical records for the 19th/20th century to present",
        "Update frequency": "Historical observations are updated annually",
        "Geographical level": "Grid boxes from 1km^2 up to 60km^2",
        "Unit of observation": "Gridded spatial cells or specific meteorological station coordinates",
        "Population covered": "N/A (Geographic/climate landmass monitoring)",
        "Main domains/variables": "Daily/monthly temperature, precipitation/rainfall frequency, wind speed, solar radiation, humidity, and projected extreme weather events",
        "Access": "Open",
        "Typical role": "Exposure/Contextual Enrichment; e.g. you can simulate how individuals react to a localised 10-day heatwave",
        "Workflow stage": "Contextual enrichment",
        "PHI theme": "Climate",
        "Strengths": "Fine spatial resolution, allowing for realistic localised modelling",
        "Limitations": "Climate projections are probabilistic scenarios, not guaranteed weather forecasts",
        "Example applications": "Layering onto a synthetic population to estimate future spikes in heat-related CV hospitalisations or checking how climate change disproportionately impacts vulnerable, poorly insulated households",
    },
    {
        "Dataset": "National Survey for Wales",
        "Organisation": "Welsh Government",
        "Country": "Wales",
        "Years available": "2012–present (successor to Welsh Health Survey)",
        "Update frequency": "Annual (continuous fieldwork)",
        "Geographical level": "National, Local Authority, and Local Health Board (LHB) levels",
        "Unit of observation": "Individual survey respondent",
        "Population covered": "~12,000 adults aged 16+ living in private households in Wales annually",
        "Main domains/variables": "General health, illness/disability, GP/hospital service satisfaction, smoking, drinking, physical activity, diet, active travel, and socioeconomic circumstances",
        "Access": "Open",
        "Typical role": "Population Baseline / Validation",
        "Workflow stage": "Donor microdata",
        "PHI theme": "Alcohol/Tobacco/Food/Healthy places",
        "Strengths": "Large sample size relative to Welsh population size allows robust breakdown across Welsh Local Authorities and Health Boards",
        "Limitations": "Limited to Wales; relies primarily on self-reported health behaviours and status without physical health measurements",
        "Example applications": "Validating health indicators and policy impacts within Welsh subpopulations",
    },
    {
        "Dataset": "National Diet and Nutrition Survey (NDNS)",
        "Organisation": "OHID (DHSC) & Food Standards Agency (FSA)",
        "Country": "UK-wide",
        "Years available": "2008–present (rolling programme)",
        "Update frequency": "Annual continuous rolling program",
        "Geographical level": "National UK level (with periodic nation boosts for Scotland, Wales, NI)",
        "Unit of observation": "Individual survey participant (aged 1.5 years and over)",
        "Population covered": "~1,000 participants per year (500 adults, 500 children) keeping 4-day dietary diaries",
        "Main domains/variables": "Exact nutrient intakes, macronutrient/micronutrient breakdowns, food group consumption, blood/urine nutritional status biomarkers, height, weight, and physical activity",
        "Access": "Open",
        "Typical role": "Socioeconomic / Behavioural Baseline",
        "Workflow stage": "Donor microdata",
        "PHI theme": "Food",
        "Strengths": "Provides precise quantitative dietary intake data and biological nutritional validation rather than high-level general estimates",
        "Limitations": "Small annual sample size (requires combining multi-year waves for statistical power); 4-day diary may suffer from temporary under-reporting",
        "Example applications": "Parameterising detailed metabolic or nutritional attributes in synthetic agents to model dietary interventions, sodium/sugar reduction, or malnutrition risk factors",
    },
    {
        "Dataset": "National Travel Survey",
        "Organisation": "Department for Transport",
        "Country": "Great Britain",
        "Years available": "1972–present",
        "Update frequency": "Annual",
        "Geographical level": "Broad government regions, urban/rural indicators",
        "Unit of observation": "Individual, Household, Vehicle, and individual 'Trips' (derived from a 7 day travel diary)",
        "Population covered": "Private households in Great Britain",
        "Main domains/variables": "Travel frequency, purpose of journeys, mode of transport used, distance travelled, time spent travelling, vehicle ownership, and basic socio-demographics",
        "Access": "End User Licence",
        "Typical role": "Donor Microdata, allowing researchers to assign realistic, daily behavioural routines to simulated individuals",
        "Workflow stage": "Donor microdata",
        "PHI theme": "Air pollution/Health places",
        "Strengths": "Includes a detailed 7-day travel diary component, making it reliable for capturing actual travel behaviour patterns",
        "Limitations": "Excludes commercial travel and only covers private households",
        "Example applications": "Evaluate exposure to environmental traffic pollution or to model changes in active travel habits across demographic groups",
    },
    {
        "Dataset": "Nomis (Official Labour Market Statistics/ONS Data Portal)",
        "Organisation": "ONS",
        "Country": "UK",
        "Years available": "Variable. Covers historic censuses (going back decades) up to contemporary, near real-time monthly data.",
        "Update frequency": "Variable depending on the underlying set. Ranges from Monthly (e.g. Claimant Counts) to Quarterly/Annual (e.g. Annual Population Survey) to 10-yearly (Census data)",
        "Geographical level": "Scalable from Country/Regional down to Local Authority, Ward, and Output Area (OA/LSOA/MSOA) levels.",
        "Unit of observation": "Primarily Aggregated data (counts, rates and percentages for specific geographic boundaries), though derived from individual microdata responses",
        "Population covered": "Whole UK population/UK resident workforce.",
        "Main domains/variables": "Employment rates, unemployment dynamics, earnings, qualifications, industry/occupational sectors, benefit claimants, and local household characteristics.",
        "Access": "Open",
        "Typical role": "Donor Microdata proxy/Population Frame Constraints/Policy Application",
        "Workflow stage": "Population frame",
        "PHI theme": "Healthy places/Health inequalities",
        "Strengths": "Free, offers granular local-area geographic breakdowns",
        "Limitations": "Data is strictly aggregated to preserve privacy. Cannot download the raw microdata without secure lab access.",
        "Example applications": "Providing localised socioeconomic benchmarks to constrain geographic weights when building or validating regional synthetic populations.",
    },
    {
        "Dataset": "ONS Mortality Statistics",
        "Organisation": "ONS",
        "Country": "England and Wales",
        "Years available": "Continuous historical series dating back to 1838",
        "Update frequency": "Weekly and annually",
        "Geographical level": "Scalable from national down to Region, Local Authority, and individual LSOA boundaries",
        "Unit of observation": "Individual death registration record",
        "Population covered": "The entire population of England and Wales",
        "Main domains/variables": "Date of death, underlying cause of death, contributory causes of death, age, sex, place of death, and geographic area of residence",
        "Access": "Mixed",
        "Typical role": "Health Outcomes/Validation",
        "Workflow stage": "Health outcomes",
        "PHI theme": "Tobacco/Alcohol/Food",
        "Strengths": "Near 100 pct complete coverage due to strict legal requirement to register deaths in the UK",
        "Limitations": "It only records the final event; it lacks data on long-term disease progression, behavioural habits, or socioeconomic variables outside of geographic area metrics",
        "Example applications": "Used to populate baseline mortality risks or to validate synthetic population health outcomes by verifying that simulated death rates from specific diseases match local ONS geographic trends",
    },
    {
        "Dataset": "Ordnance Survey Data Products",
        "Organisation": "Ordnance Survey",
        "Country": "Great Britain (England, Scotland, Wales)",
        "Years available": "Continuous active mapping",
        "Update frequency": "Variable, depending on the product. Bi-annually/annually for some products, Monthly/Quarterly for others",
        "Geographical level": "Scales from high-level national boundaries down to exact postcode coordinates and individual building structures",
        "Unit of observation": "Spatial features (vector points, polygons, lines) representing buildings, property polygons, road links, or green spaces",
        "Population covered": "N/A (Geographic landmass and infrastructure tracking)",
        "Main domains/variables": "Building footprints, road and transport networks, administrative boundaries, public parks, sports facilities, play areas, topography/elevation, and address/postcode mapping data",
        "Access": "Mixed. A massive portfolio is completely Open Access, while highly granular datasets require a paid license or academic institutional access",
        "Typical role": "Exposure/Contextual Enrichment/Policy Application. It builds the physical map your simulated people live on",
        "Workflow stage": "Contextual enrichment",
        "PHI theme": "Healthy places",
        "Strengths": "Provides exact Unique Property Reference Numbers that allow seamless linking of health records to precise physical properties",
        "Limitations": "Purely structural and geographic data; it contains zero demographic, behavioural, or health information, meaning it must be joined to Census or health survey data to be useful",
        "Example applications": "Calculating physical proximity to active travel infrastructure (cycle paths, paths) and public green spaces to enrich synthetic populations under the 'Healthy Places' and urban policy themes",
    },
    {
        "Dataset": "Quality and Outcomes Framework (QOF)",
        "Organisation": "NHS England",
        "Country": "England (with parallel frameworks managed independently in Wales, Scotland and Northern Ireland)",
        "Years available": "2004-present",
        "Update frequency": "Annual",
        "Geographical level": "GP Practice level, Integrated Care Boards, regional and national levels",
        "Unit of observation": "GP Practice aggregate (disease register counts, prevalence percentages, and treatment achievement rates)",
        "Population covered": "All patients registered at participating general practices in England (roughly 97 to 98 pct of the total registered population)",
        "Main domains/variables": "Disease prevalence registers across over 20 clinical areas (e.g. asthma, COPD, obesity, hypertension, diabetes, depression); public health indicators tracking local smoking prevalence and blood pressure monitoring metrics",
        "Access": "Open",
        "Typical role": "Health Outcomes/Validation. If your synthetic population estimates that 14 pct of people in a town have asthma due to air pollution, you check your model against the local GP practices' QOF asthma registers to see if your simulation aligns with reality",
        "Workflow stage": "Health outcomes",
        "PHI theme": "Air pollution/Tobacco",
        "Strengths": "Massive, near-universal sample size, useful for tracking public health behaviours like smoking or obesity at a hyper-local level",
        "Limitations": "You cannot see individual patient journeys or overlapping conditions.",
        "Example applications": "Serving as a local benchmarking target to validate simulated geographic distributions of chronic respiratory conditions, CV diseases, and local smoking rates within a synthetic workforce model",
    },
    {
        "Dataset": "Scottish Health Survey (SHeS)",
        "Organisation": "Scottish Government & Public Health Scotland",
        "Country": "Scotland",
        "Years available": "1995–present",
        "Update frequency": "Annual",
        "Geographical level": "National, NHS Board, and Local Authority levels",
        "Unit of observation": "Individual survey respondent (adults and children)",
        "Population covered": "~4,000 adults and ~1,000 children living in private households in Scotland annually",
        "Main domains/variables": "Cardiovascular disease, respiratory illness, mental wellbeing, diet, physical activity, alcohol, smoking, biological measurements, and dental health",
        "Access": "Open",
        "Typical role": "Population Baseline / Validation",
        "Workflow stage": "Donor microdata",
        "PHI theme": "Air pollution/Health place/Food/Tobacco/Health inequalities",
        "Strengths": "Includes biological module (blood/urine samples, blood pressure) alongside detailed lifestyle questions tailored to Scottish health priorities",
        "Limitations": "Restricted to Scottish population; cross-sectional snapshots cannot track individual trajectory histories directly over time",
        "Example applications": "Benchmarking chronic disease prevalence and health behaviors in Scottish synthetic populations, enabling cross-devolved nation comparisons",
    },
    {
        "Dataset": "UK-AIR",
        "Organisation": "DEFRA",
        "Country": "UK",
        "Years available": "Variable. Near real-time hourly data up to continuous historical records dating back to the 1970s for some pollutant types",
        "Update frequency": "Hourly/real-time for AURN, Annual for PCM models and the NAEI",
        "Geographical level": "Highly granular spatial resolution, includes exact coordinate points for over 1,500 local monitoring stations, as well as 1km^2 grid squares for modelled background pollution maps across the UK",
        "Unit of observation": "Concentration levels of specific particles/gases at a given geographic coordinate or grid point",
        "Population covered": "N/A (covers the physical land mass of the UK)",
        "Main domains/variables": "Key outdoor air pollutants; Particulate Matter, Nitrogen Dioxide, Ozone, Sulphur Dioxide, Carbon Monoxide",
        "Access": "Open",
        "Typical role": "Exposure/Contextual Enrichment",
        "Workflow stage": "Contextual enrichment",
        "PHI theme": "Air pollution",
        "Strengths": "Accurate local ambient data, high-frequency raw measurements",
        "Limitations": "Captures macro-outdoor environment levels only; it cannot tell you indoor air exposure, nor can it account for individual behavior differences (e.g. whether someone uses an air purifier)",
        "Example applications": "Spatially joining localised annual pollutant concentrations to simulated home addresses in a synthetic population to model long-term respiratory and CV disease development",
    },
    {
        "Dataset": "Understanding Society (USoc) / UK Household Longitudinal Study (UKHLS)",
        "Organisation": "ISER",
        "Country": "UK",
        "Years available": "2009–present",
        "Update frequency": "Annual",
        "Geographical level": "Individual (geo under licence)",
        "Unit of observation": "Individual",
        "Population covered": "Household survey",
        "Main domains/variables": "Health, income, education, employment, wellbeing",
        "Access": "Secure licence",
        "Typical role": "Donor microdata",
        "Workflow stage": "Donor microdata",
        "PHI theme": "Food/Tobacco/Alcohol/Health inequalities/Public mental health",
        "Strengths": "Rich longitudinal data",
        "Limitations": "Sample survey",
        "Example applications": "Synthetic population enrichment",
    },
]


# --- Additions following Eleonora Fichera's review (major comment 1 + APS minor comment) ---
# NOTE: content below was drafted from general knowledge plus Eleonora's email; items marked
# "To be confirmed" or flagged in the hand-over note should be checked before publishing.
NOT_USED = "Not currently used by a PHI theme"
TBC = "To be confirmed"


def cohort_row(name, birth_pop, years, sweeps, role_note):
    return {
        "Dataset": name,
        "Organisation": "Centre for Longitudinal Studies (CLS), UCL",
        "Country": "UK" if "Millennium" in name else ("England" if "Next Steps" in name else "Great Britain"),
        "Years available": years,
        "Update frequency": sweeps,
        "Geographical level": "Individual (cohort member); geographic identifiers under special licence",
        "Unit of observation": "Individual cohort member (plus parents/partners/children in some sweeps)",
        "Population covered": birth_pop,
        "Main domains/variables": "Health (including biomedical measures in some sweeps), education, employment, income, family and housing, behaviours, wellbeing, cognitive development",
        "Access": "Open to registered researchers via the UK Data Service (End User Licence; some content under Special Licence)",
        "Typical role": role_note,
        "Workflow stage": "Donor microdata",
        "PHI theme": NOT_USED,
        "Strengths": "Follows the same individuals from childhood through adult life, allowing life-course and intergenerational analysis",
        "Limitations": "Single-cohort sample with attrition over time; cohort-specific experiences limit generalisation to other birth years",
        "Example applications": "Parameterising life-course trajectories (education, employment, health) for synthetic individuals",
    }


new_rows = [
    {
        "Dataset": "Annual Population Survey (APS)",
        "Organisation": "ONS",
        "Country": "UK",
        "Years available": "2004–present",
        "Update frequency": "Quarterly (rolling 12-month datasets)",
        "Geographical level": "Regional and Local Authority",
        "Unit of observation": "Individual and Household",
        "Population covered": "People living in private households in the UK (boosted sample drawn from the Labour Force Survey)",
        "Main domains/variables": "Employment, unemployment, economic inactivity, occupation, earnings, qualifications, ethnicity, health, and personal wellbeing measures (life satisfaction, anxiety, happiness)",
        "Access": "End User Licence for standard anonymised research files",
        "Typical role": "Donor microdata",
        "Workflow stage": "Donor microdata",
        "PHI theme": NOT_USED,
        "Strengths": "Larger sample than the LFS and a different frequency, giving more robust local estimates; includes wellbeing variables",
        "Limitations": "Sample survey drawn from the LFS so not independent of it; wellbeing measures are self-reported",
        "Example applications": "Local-level employment and wellbeing distributions for synthetic population enrichment",
    },
    {
        "Dataset": "British Household Panel Survey (BHPS)",
        "Organisation": "ISER, University of Essex",
        "Country": "UK (Great Britain at launch; Northern Ireland added in 2001)",
        "Years available": "1991–2009 (18 waves)",
        "Update frequency": "Closed (annual waves until 2009)",
        "Geographical level": "Individual (geo under licence)",
        "Unit of observation": "Individual and Household",
        "Population covered": "Nationally representative sample of private households (c. 5,500 households at wave 1)",
        "Main domains/variables": "Income, employment, housing, health, family, wellbeing, attitudes",
        "Access": "End User Licence via the UK Data Service",
        "Typical role": "Donor microdata (long historical series)",
        "Workflow stage": "Donor microdata",
        "PHI theme": NOT_USED,
        "Strengths": "Predecessor to Understanding Society; gives a much longer series from the 1990s",
        "Limitations": "Closed since 2009 as its sample was carried into Understanding Society; smaller than Understanding Society; panel attrition",
        "Example applications": "Long-run longitudinal trajectories where a much longer series is needed",
    },
    {
        "Dataset": "English Longitudinal Study of Ageing (ELSA)",
        "Organisation": "UCL, IFS, NatCen and University of Manchester (NIA-funded)",
        "Country": "England",
        "Years available": "2002–present",
        "Update frequency": "Biennial",
        "Geographical level": "Individual; Local Authority data under special access",
        "Unit of observation": "Individual (and household)",
        "Population covered": "People aged 50+ living in private households in England",
        "Main domains/variables": "Health, disability, cognition, wellbeing, income and wealth, employment and retirement, social participation; biennial nurse visit with objective health measures and biomarkers",
        "Access": "Mixed: main data via UK Data Service; Local Authority data, biomarkers and linkages restricted",
        "Typical role": "Donor microdata (older population) / Validation",
        "Workflow stage": "Donor microdata",
        "PHI theme": NOT_USED,
        "Strengths": "Similar in design to Understanding Society but for older people; objective health measures, biomarker data, and GP practice and HES linkages",
        "Limitations": "Restricted for the most useful content (linkages, local geography); covers only ages 50+",
        "Example applications": "Ageing, multimorbidity and healthy-life-expectancy trajectories for older synthetic individuals",
    },
    {
        "Dataset": "Community Life Survey (CLS)",
        "Organisation": "Department for Culture, Media and Sport (DCMS)",
        "Country": "England",
        "Years available": "2013/14–present",
        "Update frequency": "Annual",
        "Geographical level": "National and Regional",
        "Unit of observation": "Individual survey respondent",
        "Population covered": "Adults aged 16+ living in private households in England",
        "Main domains/variables": "Volunteering, charitable giving, community cohesion and belonging, loneliness, local area satisfaction, wellbeing",
        "Access": TBC + " (published tables are open; check microdata access)",
        "Typical role": "Behavioural / community baseline",
        "Workflow stage": "Donor microdata",
        "PHI theme": NOT_USED,
        "Strengths": "Used by researchers looking at place-based assets and interventions",
        "Limitations": "Self-reported measures; limited local geography",
        "Example applications": "Adding social-participation and community-belonging attributes for place-based policy modelling",
    },
    cohort_row(
        "1958 National Child Development Study (NCDS)",
        "c. 17,000 people born in Great Britain in one week of March 1958",
        "1958–present",
        "Periodic sweeps (every few years)",
        "Donor microdata (life-course)",
    ),
    cohort_row(
        "1970 British Cohort Study (BCS70)",
        "c. 17,000 people born in Great Britain in one week of April 1970",
        "1970–present",
        "Periodic sweeps (every few years)",
        "Donor microdata (life-course)",
    ),
    cohort_row(
        "Millennium Cohort Study (MCS)",
        "c. 19,000 children born across the UK in 2000–2002",
        "2000–present",
        "Periodic sweeps (infancy through adulthood)",
        "Donor microdata (life-course)",
    ),
    cohort_row(
        "Next Steps (Longitudinal Study of Young People in England)",
        "Young people in England born in 1989/90, first interviewed at age 13–14 in 2004",
        "2004–present",
        "Periodic sweeps",
        "Donor microdata (adolescence to adulthood)",
    ),
    {
        "Dataset": "Avon Longitudinal Study of Parents and Children (ALSPAC)",
        "Organisation": "University of Bristol",
        "Country": "England (South West: Bristol and surrounding area)",
        "Years available": "1990s–present (mothers recruited during pregnancy 1991–92)",
        "Update frequency": "Ongoing follow-up",
        "Geographical level": "South West England (Bristol area)",
        "Unit of observation": "Individual (children, parents and the next generation)",
        "Population covered": "Families from the Bristol area enrolled around pregnancy in 1991–92",
        "Main domains/variables": "Extensive biomarker, genetic, health and developmental data with health record linkages",
        "Access": "Restricted (application to the ALSPAC executive; costs apply)",
        "Typical role": "Validation / donor microdata for early-life determinants of health",
        "Workflow stage": "Donor microdata",
        "PHI theme": NOT_USED,
        "Strengths": "Exceptional depth of biomarker and health data linkages",
        "Limitations": "Costly; specific to the South West; focused on a relatively wealthy population",
        "Example applications": "Early-life determinants of later health in synthetic children and families",
    },
    {
        "Dataset": "Born in Bradford",
        "Organisation": "Bradford Institute for Health Research / Bradford Teaching Hospitals NHS Foundation Trust",
        "Country": "England (Bradford)",
        "Years available": "2007 recruitment onwards (ongoing follow-up)",
        "Update frequency": "Ongoing follow-up",
        "Geographical level": "City of Bradford",
        "Unit of observation": "Individual (children, parents)",
        "Population covered": "Families in Bradford, an ethnically diverse and relatively deprived population",
        "Main domains/variables": "Child and parent health, development, environment, and linked health records",
        "Access": "Restricted (application required)",
        "Typical role": "Validation / donor microdata for deprived urban populations",
        "Workflow stage": "Donor microdata",
        "PHI theme": "Healthy places (used by the Healthy Urban Places theme)",
        "Strengths": "Complements ALSPAC by covering a relatively deprived, ethnically diverse population",
        "Limitations": "Local to Bradford; restricted access",
        "Example applications": "Modelling health and environment effects in deprived urban populations",
    },
    {
        "Dataset": "Kantar Worldpanel (Worldpanel by Numerator)",
        "Organisation": "Kantar (commercial consultancy)",
        "Country": "UK",
        "Years available": TBC,
        "Update frequency": "Continuous",
        "Geographical level": TBC,
        "Unit of observation": "Household shopping purchases",
        "Population covered": "Representative panel of GB households (55,000 as of 2026, per the provider)",
        "Main domains/variables": "Food and grocery purchasing by household, linked to household characteristics",
        "Access": "Commercial licence (very expensive)",
        "Typical role": "Behavioural baseline (food purchasing)",
        "Workflow stage": "Donor microdata",
        "PHI theme": "Used by the Sheffield team",
        "Strengths": "Incredibly rich food data on all shopping; recently linked to health data in work with the Department of Health and other organisations",
        "Limitations": "Very expensive; commercial data managed by a consultancy; no public dataset page located",
        "Example applications": "Food purchasing behaviour for dietary-policy modelling",
    },
]
data.extend(new_rows)


# --- Dynamic Link Mapping ---
url_map = {
    "2021 Census": (
        "https://www.ons.gov.uk/census"
    ),
    "Understanding Society (USoc) / UK Household Longitudinal Study (UKHLS)": (
        "https://www.understandingsociety.ac.uk/"
    ),
    "Nomis (Official Labour Market Statistics/ONS Data Portal)": (
        "https://www.nomisweb.co.uk/"
    ),
    "Labour Force Survey (LFS)": (
        "https://datacatalogue.ukdataservice.ac.uk/series/series/2000026#abstract"
    ),
    "National Travel Survey": (
        "https://www.gov.uk/government/collections/national-travel-survey-statistics"
    ),
    "UK-AIR": (
        "https://uk-air.defra.gov.uk/"
    ),
    "Index of Multiple Deprivation (IMD)": (
        "https://www.gov.uk/government/collections/english-indices-of-deprivation"
    ),
    "Met Office Climate Data Portal": (
        "https://www.metoffice.gov.uk/research/climate/maps-and-data/data"
    ),
    "Defra Data Services Platform": (
        "https://uk-air.defra.gov.uk/data/"
    ),
    "Ordnance Survey Data Products": (
        "https://www.ordnancesurvey.co.uk/products"
    ),
    "Hospital Episode Statistics (HES)": (
        "https://digital.nhs.uk/data-and-information/data-tools-and-services/data-services/hospital-episode-statistics"
    ),
    "Quality and Outcomes Framework (QOF)": (
        "https://digital.nhs.uk/data-and-information/data-tools-and-services/data-services/general-practice-data-hub/quality-outcomes-framework-qof"
    ),
    "ONS Mortality Statistics": (
        "https://www.ons.gov.uk/peoplepopulationandcommunity/birthsdeathsandmarriages/deaths/methodologies/mortalitystatisticsinenglandandwalesqmi"
    ),
    "General Practice Extraction Service (GPES)": (
        "https://digital.nhs.uk/services/general-practice-extraction-service"
    ),
    "English Prescribing Data (EPD)": (
        "https://www.nhsbsa.nhs.uk/prescription-data/prescribing-data/english-prescribing-data-epd"
    ),
    "Adult Psychiatric Morbidity Survey (APMS)": (
        "https://digital.nhs.uk/data-and-information/publications/statistical/adult-psychiatric-morbidity-survey/survey-of-mental-health-and-wellbeing-england-2023-24/dataset"
    ),
    "Clinical Practice Research Datalink (CPRD)": (
        "https://www.cprd.com/data"
    ),
    "Health Survey for England (HSE)": (
        "https://digital.nhs.uk/data-and-information/publications/statistical/health-survey-for-england"
    ),
    "National Survey for Wales": (
        "https://www.gov.wales/national-survey-wales"
    ),
    "Scottish Health Survey (SHeS)": (
        "https://publichealthscotland.scot/resources-and-tools/health-intelligence-and-data-management/national-data-catalogue/national-datasets/search-the-datasets/scottish-health-survey-shes/"
    ),
    "Living Costs and Food Survey (LCFS)": (
        "https://www.ons.gov.uk/peoplepopulationandcommunity/personalandhouseholdfinances/incomeandwealth/methodologies/livingcostsandfoodsurvey"
    ),
    "National Diet and Nutrition Survey (NDNS)": (
        "https://www.gov.uk/government/collections/national-diet-and-nutrition-survey"
    ),
}


# --- Links for newly added datasets ---
url_map.update({
    "Annual Population Survey (APS)": "https://www.ons.gov.uk/employmentandlabourmarket/peopleinwork/employmentandemployeetypes/methodologies/annualpopulationsurveyapsqmi",
    "British Household Panel Survey (BHPS)": "https://www.understandingsociety.ac.uk/about/british-household-panel-survey/",
    "English Longitudinal Study of Ageing (ELSA)": "https://datacatalogue.ukdataservice.ac.uk/series/series/200011#abstract",
    "Community Life Survey (CLS)": "https://www.gov.uk/government/collections/community-life-survey--2",
    "1958 National Child Development Study (NCDS)": "https://cls.ucl.ac.uk/cls-studies/1958-national-child-development-study/",
    "1970 British Cohort Study (BCS70)": "https://cls.ucl.ac.uk/cls-studies/1970-british-cohort-study/",
    "Millennium Cohort Study (MCS)": "https://cls.ucl.ac.uk/cls-studies/millennium-cohort-study/",
    "Next Steps (Longitudinal Study of Young People in England)": "https://cls.ucl.ac.uk/cls-studies/next-steps/",
    "Avon Longitudinal Study of Parents and Children (ALSPAC)": "https://www.bristol.ac.uk/alspac/",
    "Born in Bradford": "https://borninbradford.nhs.uk/",
    "Kantar Worldpanel (Worldpanel by Numerator)": "https://worldpanelbynumerator.com/europe/uk",
})

# Cohort studies: access via UK Data Service; CLS overview
COHORT_NOTE = (
    'All CLS cohort studies are summarised at <a href="https://cls.ucl.ac.uk/cls-studies/" target="_blank">cls.ucl.ac.uk/cls-studies</a>; '
    'access is provided publicly by the <a href="https://ukdataservice.ac.uk/" target="_blank">UK Data Service</a>.'
)

# Rows that must sit directly under another dataset rather than in alphabetical order
PIN_AFTER = {"Annual Population Survey (APS)": "Labour Force Survey (LFS)"}

# --- Linkages section (major comment 2) ---
linkages = [
    ("ADR UK data linkage programmes",
     "Administrative Data Research UK funds linkage programmes across government data. Some are already available; others are work in progress.",
     "https://www.adruk.org/our-work/our-funded-projects/projects/data-linkage-programmes/"),
    ("ECHILD (Education and Child Health Insight from Linkage)",
     "Linked local data on children and young people; the ADR UK linkage most relevant to PHI themes. Already available.",
     "https://www.adruk.org/our-work/our-funded-projects/projects/data-linkage-programmes/"),
    ("Linkages within datasets in this inventory",
     "ELSA (GP practice and HES linkages, biomarkers), ALSPAC and Born in Bradford (health data linkages), CPRD (HES, cancer registration, mortality) and Kantar Worldpanel (recently linked to health data).",
     ""),
    ("Locally and institutionally produced linkages",
     "Linkages produced by individual local authorities (e.g. Greater Manchester linked records), government departments or research institutions (e.g. IFS). These are difficult to track and are not yet captured here.",
     ""),
]


def build_linkages_html():
    out = ['<div class="section-title">Data linkages</div>',
           '<div class="header-sub">Several of the datasets above have been linked to health or other data. '
           'This makes them more tractable for modelling and for constructing synthetic data. '
           'No PHI theme is currently using official linkages, but they are outlined here for awareness. '
           + COHORT_NOTE + '</div>',
           '<div class="table-container"><table><thead><tr><th>Linkage</th><th>Description</th></tr></thead><tbody>']
    for name, desc, link in linkages:
        label = f'<a href="{link}" target="_blank">{html.escape(name)}</a>' if link else html.escape(name)
        out.append(f"<tr><td>{label}</td><td>{html.escape(desc)}</td></tr>")
    out.append("</tbody></table></div>\n")
    return "\n".join(out)


linkages_html = build_linkages_html()


# Custom HTML generator with expand/collapse logic + themed table
def build_custom_html(data, columns, url_map):
    # Header styling matching screenshot
    html_str = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Data Mapping Framework Inventory for Synthetic Data in UKRI PHI </title>
    <style>
        body {
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Arial, sans-serif;
            margin: 0;
            padding: 20px;
            background-color: #f8f9fa;
            color: #333;
        }
        .header-title {
            font-size: 1.25rem;
            font-weight: 600;
            color: #1a0dab;
            margin-bottom: 4px;
        }
        .header-sub {
            font-size: 0.82rem;
            color: #70757a;
            margin-bottom: 16px;
        }
        .table-container {
            width: 100%;
            overflow-x: auto;
            background: #fff;
            box-shadow: 0 1px 3px rgba(0,0,0,0.12);
            border-radius: 4px;
        }
        table {
            border-collapse: collapse;
            width: 100%;
            font-size: 0.78rem;
            line-height: 1.35;
        }
        th {
            background-color: #1a73e8; /* Exact bright blue theme */
            color: white;
            font-weight: 600;
            text-align: left;
            padding: 8px 10px;
            white-space: nowrap;
            border-right: 1px solid rgba(255,255,255,0.2);
        }
        td {
            padding: 8px 10px;
            border-bottom: 1px solid #e0e0e0;
            border-right: 1px solid #f0f0f0;
            vertical-align: top;
            max-width: 200px;
        }
        /* Alternating zebra row shading */
        tr:nth-child(even) {
            background-color: #f4f8fd; /* Soft blue tint */
        }
        tr:nth-child(odd) {
            background-color: #ffffff;
        }
        tr:hover {
            background-color: #e8f0fe;
        }
        a {
            color: #1a73e8;
            text-decoration: none;
            font-weight: 500;
        }
        a:hover {
            text-decoration: underline;
        }
        /* Expandable text toggle styling matching screenshot 🔍 */
        .cell-truncated {
            display: -webkit-box;
            -webkit-line-clamp: 2;
            -webkit-box-orient: vertical;
            overflow: hidden;
        }
        .toggle-btn {
            color: #1a73e8;
            cursor: pointer;
            font-weight: bold;
            margin-right: 4px;
            user-select: none;
            display: inline-block;
        }
        .section-title { font-size: 1.1rem; font-weight: 600; color: #1a0dab; margin: 28px 0 4px; }
    </style>
</head>
<body>

<div class="header-title">Data Mapping Framework Inventory for Synthetic Data in UKRI PHI</div>
<div class="header-sub">Click on any condensed cell (🔍) to expand and view full narrative descriptions inline.</div>

<div class="table-container">
    <table>
        <thead>
            <tr>
"""
    # Build Table Header
    for col in columns:
        html_str += f"                <th>{col}</th>\n"
    html_str += "            </tr>\n        </thead>\n        <tbody>\n"

    # Build Rows
    for row in data:
        html_str += "            <tr>\n"
        for col in columns:
            val = str(row.get(col, ""))

            # Handle hyperlinked dataset column
            if col == "Dataset":
                dataset_name = val
                if dataset_name in url_map:
                    cell_html = f'<a href="{url_map[dataset_name]}" target="_blank">{html.escape(dataset_name)}</a>'
                else:
                    cell_html = html.escape(dataset_name)
                html_str += f"                <td>{cell_html}</td>\n"

            # Handle expandable long text cells (🔍 icon trigger)
            elif len(val) > 45:
                escaped_text = html.escape(val)
                cell_html = f'<span class="toggle-btn" onclick="toggleCell(this)">🔍</span><span class="cell-content cell-truncated">{escaped_text}</span>'
                html_str += f"                <td>{cell_html}</td>\n"

            else:
                html_str += f"                <td>{html.escape(val)}</td>\n"
        html_str += "            </tr>\n"

    html_str += """        </tbody>
    </table>
</div>

<script>
function toggleCell(btn) {
    const content = btn.nextElementSibling;
    if (content.classList.contains('cell-truncated')) {
        content.classList.remove('cell-truncated');
    } else {
        content.classList.add('cell-truncated');
    }
}
</script>

</body>
</html>
"""
    return html_str.replace("<script>", linkages_html + "\n<script>", 1)


# Generate HTML content
data.sort(key=lambda x: (PIN_AFTER.get(x["Dataset"], x["Dataset"]) + ("~" if x["Dataset"] in PIN_AFTER else "")).lower())
columns = list(data[0].keys())
output_html = build_custom_html(data, columns, url_map)

# Write to index.html (or datasets_summary.html)
with open("index.html", "w", encoding="utf-8") as f:
    f.write(output_html)
