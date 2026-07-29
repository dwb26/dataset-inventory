# # %%

# import pandas as pd

# # Define the columns requested by the PI
# columns = [
#     "Dataset", 
#     "Organisation", 
#     "Country", 
#     "Years available", 
#     "Update frequency",
#     "Geographical level", 
#     "Unit of observation", 
#     "Population covered", 
#     "Main domains/variables", 
#     "Access", 
#     "Typical role", 
#     "Strengths", 
#     "Limitations", 
#     "Example applications"
# ]

# # Seed data with the PI's examples
# data = [
#     {
#         "Dataset": "2021 Census",
#         "Organisation": "ONS",
#         "Country": "England/Wales",
#         "Years available": "2021 (2011 for comparison)",
#         "Update frequency": "10-yearly",
#         "Geographical level": "OA, LSOA, MSOA, LA",
#         "Unit of observation": "Individual/Household (aggregated)",
#         "Population covered": "Whole population",
#         "Main domains/variables": "Age, sex, ethnicity, education, tenure, household type, employment",
#         "Access": "Open",
#         "Typical role": "Population frame / Constraints",
#         "Strengths": "Complete coverage",
#         "Limitations": "Infrequent updates",
#         "Example applications": "Base population synthesis"
#     },
#     {
#         "Dataset": "Understanding Society",
#         "Organisation": "ISER",
#         "Country": "UK",
#         "Years available": "2009–present",
#         "Update frequency": "Annual",
#         "Geographical level": "Individual (geo under licence)",
#         "Unit of observation": "Individual",
#         "Population covered": "Household survey",
#         "Main domains/variables": "Health, income, education, employment, wellbeing",
#         "Access": "Secure licence",
#         "Typical role": "Donor microdata",
#         "Strengths": "Rich longitudinal data",
#         "Limitations": "Sample survey",
#         "Example applications": "Synthetic population enrichment"
#     },
#     {
#         "Dataset": "Nomis (Official Labour Market Statistics/ONS Data Portal)",
#         "Organisation": "ONS",
#         "Country": "UK",
#         "Years available": "Variable. Covers historic censuses (going back decades) up to contemporary, near real-time monthly data.",
#         "Update frequency": "Variable depending on the underlying set. Ranges from Monthly (e.g. Claimaint Counts) to Quarterly/Annual (e.g. Annual Population Survey) to 10-yearly (Census data)",
#         "Geographical level": "Scalable from Country/Regional down to Local Authority, Ward, and Output Area (OA/LSOA/MSOA) levels.",
#         "Unit of observation": "Primarily Aggregated data (counts, rates and percentages for specific geographic boundaries), though derived from individual microdata responses",
#         "Population covered": "Whole UK population/UK resident workforce.",
#         "Main domains/variables": "Employment rates, unemployment dynamics, earnings, qualifications, industry/occupational sectors, benefit claimaints, and local household characteristics.",
#         "Access": "Open",
#         "Typical role": "Donor Microdata proxy/Population Frame Constraints/Policy Application",
#         "Strengths": "Free, offers granular local-area geographic breakdowns",
#         "Limitations": "Data is strictly aggregated to preserve privacy. Cannot download the raw microdata without secure lab access.",
#         "Example applications": "Providing localised socioeconomic benchmarks to constrain geographic weights when building or validating regional synthetic populations."
#     },
#     {
#         "Dataset": "Labour Force Survey",
#         "Organisation": "ONS",
#         "Country": "UK",
#         "Years available": "1992=present",
#         "Update frequency": "Quarterly",
#         "Geographical level": "Standard government regions (e.g. North West, South West)",
#         "Unit of observation": "Individual and Household",
#         "Population covered": "People living in households in the UK",
#         "Main domains/variables": "Employment status, unemployment, economic inactivity, occuptaion, industry sector, hours worked, job training, qualifications, and core demographic details",
#         "Access": "End User Licence for standard anonymised research files",
#         "Typical role": "Donor microdata",
#         "Strengths": "Large sample size; gives a highly detailed, multi-dimensional look at an individual's working life",
#         "Limitations": "Sample survey",
#         "Example applications": "Serving as the primary microdata source to simulate employment-related exposures, income distributions, and economic activity within a simulated regional workforce"
#     },
#     {
#         "Dataset": "Health Survey for England (HSE)",
#         "Organisation": "NatCen Social Research and UCL",
#         "Country": "England",
#         "Years available": "1991–present",
#         "Update frequency": "Annual",
#         "Geographical level": "Government Office Regions",
#         "Unit of observation": "Individual (nested within households)",
#         "Population covered": "People living in private households in England",
#         "Main domains/variables": "Physical measurements, biosamples, general health status, LTCs, and lifestyle habits",
#         "Access": "End User Licence",
#         "Typical role": "Donor microdata/health outcomes/validation",
#         "Strengths": "HSE includes objective nurse visits with actual physical and biological data collection",
#         "Limitations": "Sample survey",
#         "Example applications": "Used to populate or validate baseline joint distributions of chronic diseases, smoking prevalance, and alcohol intake behaviours across a simulated digital population."
#     },
#     {
#         "Dataset": "National Trust Survey",
#         "Organisation": "Department for Transport",
#         "Country": "Great Britain",
#         "Years available": "1972–present",
#         "Update frequency": "Annual",
#         "Geographical level": "Broad government regions, urban/rural indicators",
#         "Unit of observation": "Individual, Household, Vehicle, and individual 'Trips' (derived from a 7 day travel diary)",
#         "Population covered": "Private households in Great Britain",
#         "Main domains/variables": "Travel frequency, purpose of journeys, mode of transport used, distance travelled, time spent travelling, vehicle ownership, and basic socio-demographics",
#         "Access": "End User Licence",
#         "Typical role": "Donor Microdata, allowing researchers to assign realistic, daily behavioural routines to simulated individuals",
#         "Strengths": "Includes a detailed 7-day travel diary component, making it reliable for capturing actual travel behaviour patterns",
#         "Limitations": "Excludes commercial travel and only covers private households",
#         "Example applications": "Evaluate exposure to environmental traffic pollution or to model changes in active travel habits across demographic groups"
#     },
#     {
#         "Dataset": "UK-AIR",
#         "Organisation": "DEFRA",
#         "Country": "UK",
#         "Years available": "Variable. Near real-time hourly data up to continuous historical records dating back to the 1970s for some pollutant types",
#         "Update frequency": "Hourly/real-time for AURN, Annual for PCM models and the NAEI",
#         "Geographical level": "Highly granular spatial resolution, includes exact coordinate points for over 1,500 local monitoring stations, as well as 1km^2 grid squares for modelled background pollution maps across the UK",
#         "Unit of observation": "Concentration levels of specific particles/gases at a given geographic coordinate or grid point",
#         "Population covered": "N/A (covers the physical land mass of the UK)",
#         "Main domains/variables": "Key outdoor air pollutants; Particulate Matter, Nitrogen Dioxide, Ozone, Sulphur Dioxide, Carbon Monoxide",
#         "Access": "Open",
#         "Typical role": "Exposure/Contextual Enrichment",
#         "Strengths": "Accurate local ambient data, high-frequency raw measurements",
#         "Limitations": "Captures macro-outdoor environment levels only; it cannot tell you indoor air exposure, nor can it account for individual behaviour differences (e.g. whether someone uses an air purifier)",
#         "Example applications": "Spatially joining localised annual pollutant concentrations to simulated home addresses in a synthetic population to model long-term respiratory and CV disease development"
#     },
#     {
#         "Dataset": "IMD",
#         "Organisation": "Ministry of Housing, Communities and Local Government",
#         "Country": "England",
#         "Years available": "2000, 2004, 2007, 2010, 2015, 2019, 2025",
#         "Update frequency": "Every 4 to 5 years (irregular)",
#         "Geographical level": "LSOA",
#         "Unit of observation": "Area-level aggregate",
#         "Population covered": "The entire population of England",
#         "Main domains/variables": "Income, Employment, Education/Skills, Health/Disability, Crime, Barriers to Housing & Services, and the Living Environment",
#         "Access": "Open",
#         "Typical role": "Exposure/Contextual Enrichment; look up a simulated individual's LSOA's IMD decile to understand the level of socioeconomic deprivation they are exposed to in daily life",
#         "Strengths": "Granular local geography, breaks down overall deprivation into specific themes",
#         "Limitations": "It is a relative ranking measure, not an absolute one (e.g. LSOA ranked 100 is not twice as poor as one ranked 200). It is area level, meaning it can suffer from ecological fallacy (not everyone in a deprived neighbourhood is personally deprived)",
#         "Example applications": "Track, simulate and validate health inequalities by grouping a synthetic population into national deprivation deciles"
#     },
#     {
#         "Dataset": "Met Office Climate Data Portal",
#         "Organisation": "Met Office",
#         "Country": "UK",
#         "Years available": "Historical records for the 19th/20th century to present",
#         "Update frequency": "Historical observations are updated annually",
#         "Geographical level": "Grid boxes from 1km^2 up to 60km^2",
#         "Unit of observation": "Gridden spatial cells or specific meteorological station coordinates",
#         "Population covered": "N/A (Geographic/climate landmass monitoring)",
#         "Main domains/variables": "Daily/mpnthly temperature, precipitation/rainfall frequency, wind speed, solar radiation, humidity, and projected extreme weather events",
#         "Access": "Open",
#         "Typical role": "Exposure/Contextual Enrichment; e.g. you can simulate how individuals react to a localised 10-day heatwave",
#         "Strengths": "Fine spatial resolution, allowing for realistic localised modelling",
#         "Limitations": "Climate projections are probabilistic scenarios, not guaranteed weather forecasts",
#         "Example applications": "Layering onto a synthetic population to estimate future spikes in heat-related CV hospitalisations or checking how climate change disproportionately impacts vulnerable, poorly insulated households"
#     },
#     {
#         "Dataset": "Defra Data Services Platform",
#         "Organisation": "Department for Environment, Food & Rural Affairs & Environment Agency",
#         "Country": "England (with links provided to parallel services in Scotland, Wales, and Northern Ireland)",
#         "Years available": "Variable. Generally covers active asset registers, real-time gauges, and historical modelling series spanning the last few decades",
#         "Update frequency": "Variable, depending on the dataset. Ranges from real-time/live feeds to annual administrative releases",
#         "Geographical level": "Highly granular spatial data.",
#         "Unit of observation": "Spatial features (points, lines, polygons) or individual localised monitoring metrics (e.g., water quality test sample, local permit ratings)",
#         "Population covered": "N/A (Physical environmental, land, and asset tracking)",
#         "Main domains/variables": "Flood risk areas, river and sea levels, water quality monitoring indices, biodiversity and ecosystem tracking, waste management permits, and industrial pollution inventories",
#         "Access": "Open/Publicly accessible",
#         "Typical role": "Exposure/Contextual Enrichment. For example, once your synthetic population has residential addresses, you can overlay the Environmental Agency's flood risk maps to determine which simulated households face high environmental  or climate vulnerabilities",
#         "Strengths": "Provides official regulatory data on corporate pollution and catchment health",
#         "Limitations": "Requires signiificant GIS/spatial data processing skills to clean and filter for health modelling",
#         "Example applications": "Spatially joining localised flood risk zones or water catchment pollution profiles to synthetic household locations to evaluate the intersection of environmental hazards with socioeconomic deprivation"
#     },
#     {
#         "Dataset": "Ordinance Survey Data Products",
#         "Organisation": "Ordinance Survey",
#         "Country": "Great Britain (England, Scotland, Wales)",
#         "Years available": "Continuous active mapping",
#         "Update frequency": "Variable, depending on the product. Bi-annually/annually for some products, Monthly/Quarterly for others",
#         "Geographical level": "Scales from high-level national boundaries down to exact postcode coordinates and individual building structures",
#         "Unit of observation": "Spatial features (vector points, polygons, lines) representing buildings, property polygons, road links, or green spaces",
#         "Population covered": "N/A (Geographic landmass and infrastructure tracking)",
#         "Main domains/variables": "Building footprints, road and transport networks, administrative boundaries, public parks, sports facilities, play areas, topography/elevation, and address/postcode mapping data",
#         "Access": "Mixed. A massive portfolio is completely Open Access, while highly granular datasets require a paid license or academic institutional access",
#         "Typical role": "Exposure/Contextual Enrichment/Policy Application. It builds the physical map your simulated people live on",
#         "Strengths": "Provides exact Unique Property Refernece Numbers that allow seamless linking of health records to precise physical properties",
#         "Limitations": "Purely structural and geographic data; it contains zero demographic, behavioural, or health information, meaning it must be joined to Census or health survey data to be useful",
#         "Example applications": "Calculating physical proximity to active travel infrastructure (cycle paths, paths) and public green spaces to enrich synthetic populations under the 'Healthy Places' and urban policy themes"
#     },
#     {
#         "Dataset": "Hospital Episode Statistics (HES)",
#         "Organisation": "NHS England",
#         "Country": "England",
#         "Years available": "1989-present for Admitted Patient Care (APC); 2003-present for Outpatients",
#         "Update frequency": "Monthly provisional updates; finalised annual data refreshes",
#         "Geographical level": "Patient residence mapped down to LSOA boundaries, Integrated Care Boards, and specific treating NHS Trust sites",
#         "Unit of observation": "Episode/Admission (Specifically, a Finished Consultant Episode - FCE). A single patient can have multiple episodes or admissions over time",
#         "Population covered": "All patients treated in NHS hospitals in England",
#         "Main domains/variables": "Clinical diagnoses, surgical procedures/operations, type of admission, discharge destination, total bed days, and demographic data",
#         "Access": "Restricted/Secure Lab: High-level aggregated summary tables are open, but individual record-level data requires a formal application",
#         "Typical role": "Health Outcomes/Validation",
#         "Strengths": "Comprehensive coverage, large sample size allows for precise modelling of rare clinical conditions and long-term cohort linkage",
#         "Limitations": "Lacks detailed primary care information, lifestyle parameters, or metrics on individuals who are sick but do not go to hospital",
#         "Example applications": "Serving as the direct health outcome metric to model and evaluate the simulated impact of environmental air pollution spikes or regional alcohol control policies on emergecny hopsital admission trends"
#     },
#     {
#         "Dataset": "Quality and Outcomes Framework",
#         "Organisation": "NHS England",
#         "Country": "England (with parallel frameworks managed independently in Wales, Scotland and Northern Ireland)",
#         "Years available": "2004-present",
#         "Update frequency": "Annual",
#         "Geographical level": "GP Practice level, Integrated Care Boards, regional and national levels",
#         "Unit of observation": "GP Practice aggregate (disease register counts, prevalence percentages, and treatment achievement rates)",
#         "Population covered": "All patients registered at participating general practices in England (roughly 97 to 98 pct of the total registered population)",
#         "Main domains/variables": "Disease prevalence registers across over 20 clinical areas (e.g. asthma, COPD, obesity, hypertension, diabetes, depression); public health indicators tracking local smoking prevalence and blood pressure monitoring metrics",
#         "Access": "Open",
#         "Typical role": "Health Outcomes/Validation. If your synthetic population estimates that 14 pct of people in a town have asthma due to air pollution, you check your model against the local GP practices' QOF asthma registers to see if your simulation aligns with reality",
#         "Strengths": "Massive, near-universal sample size, useful for tracking public health behaviours like smoking or obesity at a hyper-local level",
#         "Limitations": "You cannot see individual patient journeys or overlapping conditions.",
#         "Example applications": "Serving as a local benchmarking target to validate simulated geographic distributions of chronic respiratory conditions, CV diseases, and local smoking rates within a synthetic workforce model"
#     },
#     {
#         "Dataset": "ONS Mortality Statistics",
#         "Organisation": "ONS",
#         "Country": "England and Wales",
#         "Years available": "Continuous historical series dating back to 1838",
#         "Update frequency": "Weekly and annually",
#         "Geographical level": "Scalable from national down to Region, Local Authority, and individual LSOA boundaries",
#         "Unit of observation": "Individual death registration record",
#         "Population covered": "The entire population of England and Wales",
#         "Main domains/variables": "Date of death, underlying cause of death, contributory causes of death, age, sex, place of death, and geographic area of residence",
#         "Access": "Mixed",
#         "Typical role": "Health Outcomes/Validation",
#         "Strengths": "Near 100 pct complete coverage due to strict legal requirement to register deaths in the UK",
#         "Limitations": "It only records the final event; it lacks data on long-term disease progression, behavioural habits, or soci0economic variables outside of geographic area metrics",
#         "Example applications": "Used to populate baseline mortality risks or to validate synthetic population health outcomes by verifying that simulated death rates frfom specific diseases match local ONS geographic trends"
#     },
#     {
#         "Dataset": "GPES/EPD",
#         "Organisation": "NHS England & NHS Business Services Authority",
#         "Country": "England",
#         "Years available": "Mid 2010s-preseny",
#         "Update frequency": "Monthly (for EPD dispensing data) to periodic/fortnightly (for specific GPES research extractions)",
#         "Geographical level": "Mapped from National summary datasets down to Sub-ICB/Primary Care Network and specific GP Practice locations",
#         "Unit of observation": "Individual prescription item dispense or individual coded diagnostic/clinical marker extracted from GP electronic records",
#         "Population covered": "All patients issues a prescription in primary care or included in specific national primary care audit extractions in England",
#         "Main domains/variables": "Exact chemical/generic drug names, therapeutic classifications, dosage quantities, costs, and the anonymised age/sex metadata profiles of patients receiving the medications",
#         "Access": "Mixed",
#         "Typical role": "Health Outcomes/Validation. For example, if a simulation estimates a drop in local smoking rates or an uptick in respiratory illness due to local air pollution changes, researchers check the local prescribing trends for nicotine replacement therapies or inhalers to validate those behavioural shifts",
#         "Strengths": "Captures the massive volume of healthcare management that never reaches a hospital room",
#         "Limitations": "Prescribing datasets show what was dispensed at a pharmacy, but cannot guarantee the patient actually took the medication. Standard open files lack corss-linked clinical diagnostic histories (e.g. you can see an inhaler was prescribed, but not whether it was explicitly used for asthma or COPD)",
#         "Example applications": "To simulate and evaluate primary care medication costs, or validating localised chronic illness rates within a synthetic population by cross-referencing targeted cardiovascular or respiratory prescription volumes"
#     },
#     {
#         "Dataset": "English Prescribing Data (EPD)",
#         "Organisation": "NHS Business Services Authority (NHSBSA)",
#         "Country": "England",
#         "Years available": "2014-present",
#         "Update frequency": "Monthly",
#         "Geographical level": "GP Practice level",
#         "Unit of observation": "Individual prescription item preentation per practice ()",
#         "Population covered": "All patients issued a prescription in primary care in England that was successfully submitted for reimbursement",
#         "Main domains/variables": "British National Formulary codes, chemical substance description, number of items prescribed, total quality dispensed, and Net Ingredient Cost",
#         "Access": "Open",
#         "Typical role": "Health Outcomes/Validation. If your synthetic population predicts a spike in respiratory or alcohol-related issues in a specific region, you validate that against the real-world volume of inhalers or liver-related medications prescribed by local practices",
#         "Strengths": "Universal coverage of all NHS community prescriptions",
#         "Limitations": "Strictly practice-level aggregated statistics, meaning you cannot see individual patient demogaphics (age, gender, ethnicity) or cross-reference comorbid conditions on a single person",
#         "Example applications": "Evaluating the hyper-local financial and clinical impact of chronic illnesses within a synthetic population model by benchmarking against regional BNF therapeutic group prescribing rates"
#     },
#     {
#         "Dataset": "Adult Psychiatric Morbidity Survey (APMS)",
#         "Organisation": "",
#         "Country": "",
#         "Years available": "",
#         "Update frequency": "",
#         "Geographical level": "",
#         "Unit of observation": "",
#         "Population covered": "",
#         "Main domains/variables": "",
#         "Access": "",
#         "Typical role": "",
#         "Strengths": "",
#         "Limitations": "",
#         "Example applications": ""
#     },
#     {
#         "Dataset": "Clinical Practice Research Datalink",
#         "Organisation": "",
#         "Country": "",
#         "Years available": "",
#         "Update frequency": "",
#         "Geographical level": "",
#         "Unit of observation": "",
#         "Population covered": "",
#         "Main domains/variables": "",
#         "Access": "",
#         "Typical role": "",
#         "Strengths": "",
#         "Limitations": "",
#         "Example applications": ""
#     },
#     {
#         "Dataset": "Health Survey for England (HSE)",
#         "Organisation": "",
#         "Country": "",
#         "Years available": "",
#         "Update frequency": "",
#         "Geographical level": "",
#         "Unit of observation": "",
#         "Population covered": "",
#         "Main domains/variables": "",
#         "Access": "",
#         "Typical role": "",
#         "Strengths": "",
#         "Limitations": "",
#         "Example applications": ""
#     },
#     {
#         "Dataset": "National Survey for Wales",
#         "Organisation": "",
#         "Country": "",
#         "Years available": "",
#         "Update frequency": "",
#         "Geographical level": "",
#         "Unit of observation": "",
#         "Population covered": "",
#         "Main domains/variables": "",
#         "Access": "",
#         "Typical role": "",
#         "Strengths": "",
#         "Limitations": "",
#         "Example applications": ""
#     },
#     {
#         "Dataset": "Scottish Health Survey",
#         "Organisation": "",
#         "Country": "",
#         "Years available": "",
#         "Update frequency": "",
#         "Geographical level": "",
#         "Unit of observation": "",
#         "Population covered": "",
#         "Main domains/variables": "",
#         "Access": "",
#         "Typical role": "",
#         "Strengths": "",
#         "Limitations": "",
#         "Example applications": ""
#     },
#     {
#         "Dataset": "Living Costs and Food Survey",
#         "Organisation": "",
#         "Country": "",
#         "Years available": "",
#         "Update frequency": "",
#         "Geographical level": "",
#         "Unit of observation": "",
#         "Population covered": "",
#         "Main domains/variables": "",
#         "Access": "",
#         "Typical role": "",
#         "Strengths": "",
#         "Limitations": "",
#         "Example applications": ""
#     },
#     {
#         "Dataset": "National Diet and Nutrition Survey",
#         "Organisation": "",
#         "Country": "",
#         "Years available": "",
#         "Update frequency": "",
#         "Geographical level": "",
#         "Unit of observation": "",
#         "Population covered": "",
#         "Main domains/variables": "",
#         "Access": "",
#         "Typical role": "",
#         "Strengths": "",
#         "Limitations": "",
#         "Example applications": ""
#     }
# ]

# # Create DataFrame
# df = pd.DataFrame(data, columns=columns, index=range(1, len(data) + 1))
# # print(df.to_markdown(index=False))
# # df.to_excel("data_table.xlsx", index=False)


# %%
import pandas as pd

# Define the columns requested by the PI
columns = [
    "Dataset",
    "Organisation",
    "Country",
    "Years available",
    "Update frequency",
    "Geographical level",
    "Unit of observation",
    "Population covered",
    "Main domains/variables",
    "Access",
    "Typical role",
    "Strengths",
    "Limitations",
    "Example applications",
]

# Consolidated datasets list (23 unique datasets)
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
        "Main domains/variables": (
            "Age, sex, ethnicity, education, tenure, household type, employment"
        ),
        "Access": "Open",
        "Typical role": "Population frame / Constraints",
        "Strengths": "Complete coverage",
        "Limitations": "Infrequent updates",
        "Example applications": "Base population synthesis",
    },
    {
        "Dataset": "Understanding Society",
        "Organisation": "ISER",
        "Country": "UK",
        "Years available": "2009–present",
        "Update frequency": "Annual",
        "Geographical level": "Individual (geo under licence)",
        "Unit of observation": "Individual",
        "Population covered": "Household survey",
        "Main domains/variables": (
            "Health, income, education, employment, wellbeing"
        ),
        "Access": "Secure licence",
        "Typical role": "Donor microdata",
        "Strengths": "Rich longitudinal data",
        "Limitations": "Sample survey",
        "Example applications": "Synthetic population enrichment",
    },
    {
        "Dataset": "Nomis (Official Labour Market Statistics/ONS Data Portal)",
        "Organisation": "ONS",
        "Country": "UK",
        "Years available": (
            "Variable. Covers historic censuses (going back decades) up to"
            " contemporary, near real-time monthly data."
        ),
        "Update frequency": (
            "Variable depending on the underlying set. Ranges from Monthly"
            " (e.g. Claimant Counts) to Quarterly/Annual (e.g. Annual"
            " Population Survey) to 10-yearly (Census data)"
        ),
        "Geographical level": (
            "Scalable from Country/Regional down to Local Authority, Ward, and"
            " Output Area (OA/LSOA/MSOA) levels."
        ),
        "Unit of observation": (
            "Primarily Aggregated data (counts, rates and percentages for"
            " specific geographic boundaries), though derived from individual"
            " microdata responses"
        ),
        "Population covered": "Whole UK population/UK resident workforce.",
        "Main domains/variables": (
            "Employment rates, unemployment dynamics, earnings, qualifications,"
            " industry/occupational sectors, benefit claimants, and local"
            " household characteristics."
        ),
        "Access": "Open",
        "Typical role": (
            "Donor Microdata proxy/Population Frame Constraints/Policy"
            " Application"
        ),
        "Strengths": "Free, offers granular local-area geographic breakdowns",
        "Limitations": (
            "Data is strictly aggregated to preserve privacy. Cannot download"
            " the raw microdata without secure lab access."
        ),
        "Example applications": (
            "Providing localised socioeconomic benchmarks to constrain"
            " geographic weights when building or validating regional synthetic"
            " populations."
        ),
    },
    {
        "Dataset": "Labour Force Survey",
        "Organisation": "ONS",
        "Country": "UK",
        "Years available": "1992–present",
        "Update frequency": "Quarterly",
        "Geographical level": (
            "Standard government regions (e.g. North West, South West)"
        ),
        "Unit of observation": "Individual and Household",
        "Population covered": "People living in households in the UK",
        "Main domains/variables": (
            "Employment status, unemployment, economic inactivity, occupation,"
            " industry sector, hours worked, job training, qualifications, and"
            " core demographic details"
        ),
        "Access": "End User Licence for standard anonymised research files",
        "Typical role": "Donor microdata",
        "Strengths": (
            "Large sample size; gives a highly detailed, multi-dimensional look"
            " at an individual's working life"
        ),
        "Limitations": "Sample survey",
        "Example applications": (
            "Serving as the primary microdata source to simulate"
            " employment-related exposures, income distributions, and economic"
            " activity within a simulated regional workforce"
        ),
    },
    {
        "Dataset": "National Travel Survey",
        "Organisation": "Department for Transport",
        "Country": "Great Britain",
        "Years available": "1972–present",
        "Update frequency": "Annual",
        "Geographical level": (
            "Broad government regions, urban/rural indicators"
        ),
        "Unit of observation": (
            "Individual, Household, Vehicle, and individual 'Trips' (derived"
            " from a 7 day travel diary)"
        ),
        "Population covered": "Private households in Great Britain",
        "Main domains/variables": (
            "Travel frequency, purpose of journeys, mode of transport used,"
            " distance travelled, time spent travelling, vehicle ownership, and"
            " basic socio-demographics"
        ),
        "Access": "End User Licence",
        "Typical role": (
            "Donor Microdata, allowing researchers to assign realistic, daily"
            " behavioural routines to simulated individuals"
        ),
        "Strengths": (
            "Includes a detailed 7-day travel diary component, making it"
            " reliable for capturing actual travel behaviour patterns"
        ),
        "Limitations": (
            "Excludes commercial travel and only covers private households"
        ),
        "Example applications": (
            "Evaluate exposure to environmental traffic pollution or to model"
            " changes in active travel habits across demographic groups"
        ),
    },
    {
        "Dataset": "UK-AIR",
        "Organisation": "DEFRA",
        "Country": "UK",
        "Years available": (
            "Variable. Near real-time hourly data up to continuous historical"
            " records dating back to the 1970s for some pollutant types"
        ),
        "Update frequency": (
            "Hourly/real-time for AURN, Annual for PCM models and the NAEI"
        ),
        "Geographical level": (
            "Highly granular spatial resolution, includes exact coordinate"
            " points for over 1,500 local monitoring stations, as well as 1km^2"
            " grid squares for modelled background pollution maps across the UK"
        ),
        "Unit of observation": (
            "Concentration levels of specific particles/gases at a given"
            " geographic coordinate or grid point"
        ),
        "Population covered": "N/A (covers the physical land mass of the UK)",
        "Main domains/variables": (
            "Key outdoor air pollutants; Particulate Matter, Nitrogen Dioxide,"
            " Ozone, Sulphur Dioxide, Carbon Monoxide"
        ),
        "Access": "Open",
        "Typical role": "Exposure/Contextual Enrichment",
        "Strengths": (
            "Accurate local ambient data, high-frequency raw measurements"
        ),
        "Limitations": (
            "Captures macro-outdoor environment levels only; it cannot tell you"
            " indoor air exposure, nor can it account for individual behavior"
            " differences (e.g. whether someone uses an air purifier)"
        ),
        "Example applications": (
            "Spatially joining localised annual pollutant concentrations to"
            " simulated home addresses in a synthetic population to model"
            " long-term respiratory and CV disease development"
        ),
    },
    {
        "Dataset": "IMD",
        "Organisation": (
            "Ministry of Housing, Communities and Local Government"
        ),
        "Country": "England",
        "Years available": "2000, 2004, 2007, 2010, 2015, 2019, 2025",
        "Update frequency": "Every 4 to 5 years (irregular)",
        "Geographical level": "LSOA",
        "Unit of observation": "Area-level aggregate",
        "Population covered": "The entire population of England",
        "Main domains/variables": (
            "Income, Employment, Education/Skills, Health/Disability, Crime,"
            " Barriers to Housing & Services, and the Living Environment"
        ),
        "Access": "Open",
        "Typical role": (
            "Exposure/Contextual Enrichment; look up a simulated individual's"
            " LSOA's IMD decile to understand the level of socioeconomic"
            " deprivation they are exposed to in daily life"
        ),
        "Strengths": (
            "Granular local geography, breaks down overall deprivation into"
            " specific themes"
        ),
        "Limitations": (
            "It is a relative ranking measure, not an absolute one (e.g. LSOA"
            " ranked 100 is not twice as poor as one ranked 200). It is area"
            " level, meaning it can suffer from ecological fallacy (not"
            " everyone in a deprived neighbourhood is personally deprived)"
        ),
        "Example applications": (
            "Track, simulate and validate health inequalities by grouping a"
            " synthetic population into national deprivation deciles"
        ),
    },
    {
        "Dataset": "Met Office Climate Data Portal",
        "Organisation": "Met Office",
        "Country": "UK",
        "Years available": (
            "Historical records for the 19th/20th century to present"
        ),
        "Update frequency": "Historical observations are updated annually",
        "Geographical level": "Grid boxes from 1km^2 up to 60km^2",
        "Unit of observation": (
            "Gridded spatial cells or specific meteorological station"
            " coordinates"
        ),
        "Population covered": (
            "N/A (Geographic/climate landmass monitoring)"
        ),
        "Main domains/variables": (
            "Daily/monthly temperature, precipitation/rainfall frequency, wind"
            " speed, solar radiation, humidity, and projected extreme weather"
            " events"
        ),
        "Access": "Open",
        "Typical role": (
            "Exposure/Contextual Enrichment; e.g. you can simulate how"
            " individuals react to a localised 10-day heatwave"
        ),
        "Strengths": (
            "Fine spatial resolution, allowing for realistic localised"
            " modelling"
        ),
        "Limitations": (
            "Climate projections are probabilistic scenarios, not guaranteed"
            " weather forecasts"
        ),
        "Example applications": (
            "Layering onto a synthetic population to estimate future spikes in"
            " heat-related CV hospitalisations or checking how climate change"
            " disproportionately impacts vulnerable, poorly insulated"
            " households"
        ),
    },
    {
        "Dataset": "Defra Data Services Platform",
        "Organisation": (
            "Department for Environment, Food & Rural Affairs & Environment"
            " Agency"
        ),
        "Country": (
            "England (with links provided to parallel services in Scotland,"
            " Wales, and Northern Ireland)"
        ),
        "Years available": (
            "Variable. Generally covers active asset registers, real-time"
            " gauges, and historical modelling series spanning the last few"
            " decades"
        ),
        "Update frequency": (
            "Variable, depending on the dataset. Ranges from real-time/live"
            " feeds to annual administrative releases"
        ),
        "Geographical level": "Highly granular spatial data.",
        "Unit of observation": (
            "Spatial features (points, lines, polygons) or individual"
            " localised monitoring metrics (e.g., water quality test sample,"
            " local permit ratings)"
        ),
        "Population covered": (
            "N/A (Physical environmental, land, and asset tracking)"
        ),
        "Main domains/variables": (
            "Flood risk areas, river and sea levels, water quality monitoring"
            " indices, biodiversity and ecosystem tracking, waste management"
            " permits, and industrial pollution inventories"
        ),
        "Access": "Open/Publicly accessible",
        "Typical role": (
            "Exposure/Contextual Enrichment. For example, once your synthetic"
            " population has residential addresses, you can overlay the"
            " Environmental Agency's flood risk maps to determine which"
            " simulated households face high environmental or climate"
            " vulnerabilities"
        ),
        "Strengths": (
            "Provides official regulatory data on corporate pollution and"
            " catchment health"
        ),
        "Limitations": (
            "Requires significant GIS/spatial data processing skills to clean"
            " and filter for health modelling"
        ),
        "Example applications": (
            "Spatially joining localised flood risk zones or water catchment"
            " pollution profiles to synthetic household locations to evaluate"
            " the intersection of environmental hazards with socioeconomic"
            " deprivation"
        ),
    },
    {
        "Dataset": "Ordnance Survey Data Products",
        "Organisation": "Ordnance Survey",
        "Country": "Great Britain (England, Scotland, Wales)",
        "Years available": "Continuous active mapping",
        "Update frequency": (
            "Variable, depending on the product. Bi-annually/annually for some"
            " products, Monthly/Quarterly for others"
        ),
        "Geographical level": (
            "Scales from high-level national boundaries down to exact postcode"
            " coordinates and individual building structures"
        ),
        "Unit of observation": (
            "Spatial features (vector points, polygons, lines) representing"
            " buildings, property polygons, road links, or green spaces"
        ),
        "Population covered": (
            "N/A (Geographic landmass and infrastructure tracking)"
        ),
        "Main domains/variables": (
            "Building footprints, road and transport networks, administrative"
            " boundaries, public parks, sports facilities, play areas,"
            " topography/elevation, and address/postcode mapping data"
        ),
        "Access": (
            "Mixed. A massive portfolio is completely Open Access, while highly"
            " granular datasets require a paid license or academic"
            " institutional access"
        ),
        "Typical role": (
            "Exposure/Contextual Enrichment/Policy Application. It builds the"
            " physical map your simulated people live on"
        ),
        "Strengths": (
            "Provides exact Unique Property Reference Numbers that allow"
            " seamless linking of health records to precise physical"
            " properties"
        ),
        "Limitations": (
            "Purely structural and geographic data; it contains zero"
            " demographic, behavioural, or health information, meaning it must"
            " be joined to Census or health survey data to be useful"
        ),
        "Example applications": (
            "Calculating physical proximity to active travel infrastructure"
            " (cycle paths, paths) and public green spaces to enrich synthetic"
            " populations under the 'Healthy Places' and urban policy themes"
        ),
    },
    {
        "Dataset": "Hospital Episode Statistics (HES)",
        "Organisation": "NHS England",
        "Country": "England",
        "Years available": (
            "1989-present for Admitted Patient Care (APC); 2003-present for"
            " Outpatients"
        ),
        "Update frequency": (
            "Monthly provisional updates; finalised annual data refreshes"
        ),
        "Geographical level": (
            "Patient residence mapped down to LSOA boundaries, Integrated Care"
            " Boards, and specific treating NHS Trust sites"
        ),
        "Unit of observation": (
            "Episode/Admission (Specifically, a Finished Consultant Episode -"
            " FCE). A single patient can have multiple episodes or admissions"
            " over time"
        ),
        "Population covered": "All patients treated in NHS hospitals in England",
        "Main domains/variables": (
            "Clinical diagnoses, surgical procedures/operations, type of"
            " admission, discharge destination, total bed days, and demographic"
            " data"
        ),
        "Access": (
            "Restricted/Secure Lab: High-level aggregated summary tables are"
            " open, but individual record-level data requires a formal"
            " application"
        ),
        "Typical role": "Health Outcomes/Validation",
        "Strengths": (
            "Comprehensive coverage, large sample size allows for precise"
            " modelling of rare clinical conditions and long-term cohort"
            " linkage"
        ),
        "Limitations": (
            "Lacks detailed primary care information, lifestyle parameters, or"
            " metrics on individuals who are sick but do not go to hospital"
        ),
        "Example applications": (
            "Serving as the direct health outcome metric to model and evaluate"
            " the simulated impact of environmental air pollution spikes or"
            " regional alcohol control policies on emergency hospital admission"
            " trends"
        ),
    },
    {
        "Dataset": "Quality and Outcomes Framework",
        "Organisation": "NHS England",
        "Country": (
            "England (with parallel frameworks managed independently in Wales,"
            " Scotland and Northern Ireland)"
        ),
        "Years available": "2004-present",
        "Update frequency": "Annual",
        "Geographical level": (
            "GP Practice level, Integrated Care Boards, regional and national"
            " levels"
        ),
        "Unit of observation": (
            "GP Practice aggregate (disease register counts, prevalence"
            " percentages, and treatment achievement rates)"
        ),
        "Population covered": (
            "All patients registered at participating general practices in"
            " England (roughly 97 to 98 pct of the total registered population)"
        ),
        "Main domains/variables": (
            "Disease prevalence registers across over 20 clinical areas (e.g."
            " asthma, COPD, obesity, hypertension, diabetes, depression);"
            " public health indicators tracking local smoking prevalence and"
            " blood pressure monitoring metrics"
        ),
        "Access": "Open",
        "Typical role": (
            "Health Outcomes/Validation. If your synthetic population"
            " estimates that 14 pct of people in a town have asthma due to air"
            " pollution, you check your model against the local GP practices'"
            " QOF asthma registers to see if your simulation aligns with"
            " reality"
        ),
        "Strengths": (
            "Massive, near-universal sample size, useful for tracking public"
            " health behaviours like smoking or obesity at a hyper-local level"
        ),
        "Limitations": (
            "You cannot see individual patient journeys or overlapping"
            " conditions."
        ),
        "Example applications": (
            "Serving as a local benchmarking target to validate simulated"
            " geographic distributions of chronic respiratory conditions, CV"
            " diseases, and local smoking rates within a synthetic workforce"
            " model"
        ),
    },
    {
        "Dataset": "ONS Mortality Statistics",
        "Organisation": "ONS",
        "Country": "England and Wales",
        "Years available": "Continuous historical series dating back to 1838",
        "Update frequency": "Weekly and annually",
        "Geographical level": (
            "Scalable from national down to Region, Local Authority, and"
            " individual LSOA boundaries"
        ),
        "Unit of observation": "Individual death registration record",
        "Population covered": "The entire population of England and Wales",
        "Main domains/variables": (
            "Date of death, underlying cause of death, contributory causes of"
            " death, age, sex, place of death, and geographic area of"
            " residence"
        ),
        "Access": "Mixed",
        "Typical role": "Health Outcomes/Validation",
        "Strengths": (
            "Near 100 pct complete coverage due to strict legal requirement to"
            " register deaths in the UK"
        ),
        "Limitations": (
            "It only records the final event; it lacks data on long-term"
            " disease progression, behavioural habits, or socioeconomic"
            " variables outside of geographic area metrics"
        ),
        "Example applications": (
            "Used to populate baseline mortality risks or to validate synthetic"
            " population health outcomes by verifying that simulated death"
            " rates from specific diseases match local ONS geographic trends"
        ),
    },
    {
        "Dataset": "GPES/EPD",
        "Organisation": "NHS England & NHS Business Services Authority",
        "Country": "England",
        "Years available": "Mid 2010s-present",
        "Update frequency": (
            "Monthly (for EPD dispensing data) to periodic/fortnightly (for"
            " specific GPES research extractions)"
        ),
        "Geographical level": (
            "Mapped from National summary datasets down to Sub-ICB/Primary Care"
            " Network and specific GP Practice locations"
        ),
        "Unit of observation": (
            "Individual prescription item dispense or individual coded"
            " diagnostic/clinical marker extracted from GP electronic records"
        ),
        "Population covered": (
            "All patients issued a prescription in primary care or included in"
            " specific national primary care audit extractions in England"
        ),
        "Main domains/variables": (
            "Exact chemical/generic drug names, therapeutic classifications,"
            " dosage quantities, costs, and the anonymised age/sex metadata"
            " profiles of patients receiving the medications"
        ),
        "Access": "Mixed",
        "Typical role": (
            "Health Outcomes/Validation. For example, if a simulation estimates"
            " a drop in local smoking rates or an uptick in respiratory illness"
            " due to local air pollution changes, researchers check the local"
            " prescribing trends for nicotine replacement therapies or"
            " inhalers to validate those behavioural shifts"
        ),
        "Strengths": (
            "Captures the massive volume of healthcare management that never"
            " reaches a hospital room"
        ),
        "Limitations": (
            "Prescribing datasets show what was dispensed at a pharmacy, but"
            " cannot guarantee the patient actually took the medication."
            " Standard open files lack cross-linked clinical diagnostic"
            " histories (e.g. you can see an inhaler was prescribed, but not"
            " whether it was explicitly used for asthma or COPD)"
        ),
        "Example applications": (
            "To simulate and evaluate primary care medication costs, or"
            " validating localised chronic illness rates within a synthetic"
            " population by cross-referencing targeted cardiovascular or"
            " respiratory prescription volumes"
        ),
    },
    {
        "Dataset": "English Prescribing Data (EPD)",
        "Organisation": "NHS Business Services Authority (NHSBSA)",
        "Country": "England",
        "Years available": "2014-present",
        "Update frequency": "Monthly",
        "Geographical level": "GP Practice level",
        "Unit of observation": (
            "Individual prescription item presentation per practice"
        ),
        "Population covered": (
            "All patients issued a prescription in primary care in England that"
            " was successfully submitted for reimbursement"
        ),
        "Main domains/variables": (
            "British National Formulary codes, chemical substance description,"
            " number of items prescribed, total quantity dispensed, and Net"
            " Ingredient Cost"
        ),
        "Access": "Open",
        "Typical role": (
            "Health Outcomes/Validation. If your synthetic population predicts"
            " a spike in respiratory or alcohol-related issues in a specific"
            " region, you validate that against the real-world volume of"
            " inhalers or liver-related medications prescribed by local"
            " practices"
        ),
        "Strengths": "Universal coverage of all NHS community prescriptions",
        "Limitations": (
            "Strictly practice-level aggregated statistics, meaning you cannot"
            " see individual patient demographics (age, gender, ethnicity) or"
            " cross-reference comorbid conditions on a single person"
        ),
        "Example applications": (
            "Evaluating the hyper-local financial and clinical impact of"
            " chronic illnesses within a synthetic population model by"
            " benchmarking against regional BNF therapeutic group prescribing"
            " rates"
        ),
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
        "Strengths": "Unrivalled real-world longitudinal coverage with deep medical histories, multi-decade follow-ups, and individual-level linkage across primary, hospital, and death registries",
        "Limitations": "Requires rigorous protocol approval (RDG) and license fees; subject to variable clinical coding quality, missing secondary care nuance, and potential GP practice sampling bias",
        "Example applications": "Primary ground-truth data for parameterising disease incidence transitions, co-morbidity matrices, and validating synthetic longitudinal patient trajectories",
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
        "Strengths": "Combines self-reported lifestyle metrics with physical measurements (height, weight, blood tests), avoiding self-reporting bias for clinical markers like hypertension and obesity",
        "Limitations": "Cross-sectional design prevents longitudinal individual tracking; sample sizes are too small for granular hyper-local (LSOA) estimations without spatial micro-simulation",
        "Example applications": "Joint probability distributions for agent-based models (e.g., correlating BMI, smoking status, age, and chronic condition prevalence to populate realistic agent profiles)",
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
        "Strengths": "Large sample size relative to Welsh population size allows robust breakdown across Welsh Local Authorities and Health Boards",
        "Limitations": "Limited to Wales; relies primarily on self-reported health behaviours and status without physical/biological sample validation",
        "Example applications": "Validating and parameterising synthetic individual health profiles, lifestyle behaviours, and public service utilization specifically for Welsh geographic cohorts",
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
        "Strengths": "Includes biological module (blood/urine samples, blood pressure) alongside detailed lifestyle questions tailored to Scottish health priorities",
        "Limitations": "Restricted to Scottish population; cross-sectional snapshots cannot track individual trajectory histories directly over time",
        "Example applications": "Benchmarking chronic disease prevalence and health behaviors in Scottish synthetic populations, enabling cross-devolved nation comparisons",
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
        "Strengths": "Gold standard for granular household financial choices, expenditure patterns, and physical food purchasing quantities linked directly to income brackets",
        "Limitations": "High survey burden leads to potential non-response bias; small annual sample size restricts hyper-local spatial disaggregation",
        "Example applications": "Modelling economic determinants of health within synthetic populations (e.g., spending capacity on healthy food, tobacco/alcohol expenditure, energy poverty)",
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
        "Strengths": "Provides precise quantitative dietary intake data and biological nutritional validation rather than high-level general estimates",
        "Limitations": "Small annual sample size (requires combining multi-year waves for statistical power); 4-day diary may suffer from temporary under-reporting",
        "Example applications": "Parameterising detailed metabolic or nutritional attributes in synthetic agents to model dietary interventions, sodium/sugar reduction, or malnutrition risk factors",
    },
]

# Create DataFrame
df = pd.DataFrame(data)[columns]

# --- Dynamic Link Mapping ---
url_map = {
    "2021 Census": "https://www.ons.gov.uk/census",
    "Understanding Society": "https://www.understandingsociety.ac.uk/",
    "Nomis (Official Labour Market Statistics/ONS Data Portal)": (
        "https://www.nomisweb.co.uk/"
    ),
    "Labour Force Survey": (
        "https://www.ons.gov.uk/surveys/informationforhouseholdsandindividuals/householdsurveys/labourforcesurveys"
    ),
    "National Travel Survey": (
        "https://www.gov.uk/government/collections/national-travel-survey-statistics"
    ),
    "UK-AIR": "https://uk-air.defra.gov.uk/",
    "IMD": (
        "https://www.gov.uk/government/collections/english-indices-of-deprivation"
    ),
    "Met Office Climate Data Portal": (
        "https://www.metoffice.gov.uk/services/data/dataportal"
    ),
    "Defra Data Services Platform": (
        "https://environment.data.gov.uk/"
    ),
    "Ordnance Survey Data Products": (
        "https://osdatahub.os.uk/"
    ),
    "Hospital Episode Statistics (HES)": (
        "https://digital.nhs.uk/data-and-information/data-tools-and-services/data-services/hospital-episode-statistics"
    ),
    "Quality and Outcomes Framework": (
        "https://digital.nhs.uk/data-and-information/publications/statistical/quality-and-outcomes-framework-achievement-prevalence-and-exceptions-data"
    ),
    "ONS Mortality Statistics": (
        "https://www.ons.gov.uk/peoplepopulationandcommunity/birthsdeathsandmarriages/deaths"
    ),
    "GPES/EPD": (
        "https://digital.nhs.uk/services/general-practice-extraction-service-gpes"
    ),
    "English Prescribing Data (EPD)": (
        "https://www.nhsbsa.nhs.uk/prescription-data/dispensing-data/english-prescribing-data-epd"
    ),
    "Adult Psychiatric Morbidity Survey (APMS)": (
        "https://digital.nhs.uk/data-and-information/publications/statistical/adult-psychiatric-morbidity-survey"
    ),
    "Clinical Practice Research Datalink (CPRD)": (
        "https://cprd.com/"
    ),
    "Health Survey for England (HSE)": (
        "https://digital.nhs.uk/data-and-information/publications/statistical/health-survey-for-england"
    ),
    "National Survey for Wales": (
        "https://www.gov.wales/national-survey-wales"
    ),
    "Scottish Health Survey (SHeS)": (
        "https://www.gov.scot/collections/scottish-health-survey/"
    ),
    "Living Costs and Food Survey (LCFS)": (
        "https://www.ons.gov.uk/surveys/informationforhouseholdsandindividuals/householdsurveys/livingcostsandfoodsurveylcfs"
    ),
    "National Diet and Nutrition Survey (NDNS)": (
        "https://www.gov.uk/government/collections/national-diet-and-nutrition-survey"
    ),
}

# Wrap Dataset names in HTML anchors using the map
df["Dataset"] = df["Dataset"].apply(
    lambda name: (
        f'<a href="{url_map[name]}" target="_blank" rel="noopener'
        f' noreferrer">{name}</a>'
        if name in url_map
        else name
    )
)

# Export to HTML string (escape=False ensures raw <a> tags are rendered by browsers)
html_output = df.to_html(escape=False, index=False)

# Write out to HTML file
with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_output)