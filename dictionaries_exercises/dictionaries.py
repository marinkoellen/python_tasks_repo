groceries = {
    "Baby Spinach": 2.78,
    "Hot Chocolate": 3.70,
    "Bacon": 9.00,
    "Carrots": 0.56,
    "Oranges": 3.08
}

print(groceries)

print(groceries["Baby Spinach"])


for item in groceries:
    print(item) # key to access info
    print(groceries[item])


for item, price in groceries.items():
    print(item, price)



cohorts = {
    "Perth": ["anna","ellen","hayley"],
    "Brisbane":["Emily","Eliza","Lucy"]
}

print(cohorts)


for cohort, peeps in cohorts.items():
    print(cohort)
    for peep in peeps:
        print(peep)
    print()    


all_cohorts = {
    2019: {
        "perth": ["Anna", "Sarah", "Nina", "Ellie"]
    },
    2020: {
        "perth": ["Anna", "Viv", "Nic", "Teagen"],
        "brisbane": ["Teagan", "Vivian", "Nic", "Joy"]
    }
}

for year, cohorts in all_cohorts.items():
    print(year)
    print()
    for city, cohort in cohorts.items():
        print(city)
        for peep in cohort:
            print(peep)
    print()
