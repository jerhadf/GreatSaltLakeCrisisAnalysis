# define the keywords to use to search for articles 
keywords = [
    "Great Salt Lake watershed",
    "Utah saline lake desiccation",
    "opinions on Great Salt Lake water use", 
    "solutions to the Great Salt Lake drying crisis", 
    "Aral Sea Syndrome Great Salt Lake",
    "water balance Great Salt Lake",
    "Great Salt Lake climate adaptation",
    "Great Salt Lake ecosystem collapse",
    "Great Salt Lake water withdrawals",
    "Great Salt Lake terminal lake management",
    "Great Salt Lake consumptive water uses",
    "Great Salt Lake water conservation policy",
    "Great Salt Lake wetland restoration",
    "Great Salt Lake water rights allocation",
    "Great Salt Lake lake level projections",
    "Great Salt Lake drying up",
    "Great Salt Lake dessication crisis",
    "Great Salt Lake water management",
    "Utah Valley water saving",
    "Great Salt Lake ecosystem",
    "Great Salt Lake wildlife",
    "Great Salt Lake industry",
    "Great Salt Lake tourism",
    "Great Salt Lake climate change",
    "Great Salt Lake water level",
    "Great Salt Lake salinity",
    "Great Salt Lake dust storms",
    "Great Salt Lake air quality",
    "Great Salt Lake brine shrimp",
    "Great Salt Lake mineral extraction",
    "Great Salt Lake Native American tribes",
    "Great Salt Lake research",
    "Great Salt Lake policy",
    "Great Salt Lake stakeholders"
]

with open('data/keywords.txt', 'w') as f:
    for keyword in keywords:
        f.write(f"{keyword}\n")