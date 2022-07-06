from company import Company

def analysis(func):
    """Here we discover which scenario is better than the other"""
    def wrapper(*args, **kwargs):
        print("""
Compare actual scenary with new scenario...""")
        scores = func(*args, **kwargs)
        if scores[0] > scores[1]:
            print(f"""
-------------------------
Actual scenario is better
-------------------------""")
        elif scores[0] < scores[1]:
            print(f"""
-----------------------
New scenario is better
-----------------------
""")
    return wrapper

@analysis
def check_scenarios(a_sc, n_sc):
    """Compare the two scenarios"""
    data_compare = {
        "Net profit": 1,
        "Margin contribution": 2,
        "Break even point": 3,
        "Dollar/ gain": 4
    }
    score_a_sc = 0
    score_n_sc= 0
    for k, v in data_compare.items():
            if a_sc[v] > n_sc[v]:
                print(f"* More {k}: ACTUAL SCENARIO")
                score_a_sc += 1
            elif a_sc[v] < n_sc[v]:
                print(f"* More {k}: NEW SCENARIO")
                score_n_sc += 1
    return score_a_sc, score_n_sc

def comparation():
    """Extract the files where data save of each scenario are"""
    actual_scenario = []
    with open("./actual_scenary.txt", "r", encoding="utf-8") as f:
           for i in f:
            actual_scenario.append(float(i.strip('\n')))
    new_scenario = []
    with open("./new_scenary.txt", "r", encoding="utf-8") as f:
            for i in f:
                new_scenario.append(float(i.strip('\n')))
    check_scenarios(actual_scenario, new_scenario)

def structure(company_data):
    """"Report's structure"""
    print(f"""
    -------------------------------
    Gross profit: ${company_data[0]}
    Operative profit: ${company_data[1][0]}
    Net profit: ${company_data[1][1]}
    -------------------------------
    Contribution margin: ${company_data[1][2]}
    Break_even_point: {company_data[1][3]} units
    Gain/dollar: ${company_data[1][4]}
    -------------------------------
            """)
    print("GET IT!")

def report(func):
    """Report the results of both scenarios"""
    def wrapper(company, scenario):
        company_data = func(company, scenario)
        if scenario == "A":
            print(f"""[Actual scenario] By calculating income statement of "{company.name}" business...""")
            structure(company_data)
        elif scenario == "N":
            print(f"""
[New scenario] By calculating income statement of "{company.name}" business...""")
            structure(company_data)
    return wrapper

def save_data(c1_data, type):
    """Save the company's datas in a file for then comparate them"""
    with open(f"./{type}_scenario.txt","w", encoding="utf-8") as f:
        for element in c1_data:
            f.write(str(element))
            f.write("\n")

def others_calculations(c1, gross_profit, admin_cost):
    """Calculate other company profits and additional data."""
    operative_profit = round(gross_profit - admin_cost, 2)
    net_profit = round(operative_profit - (operative_profit*c1.taxes), 2)
    c_m = c1.unit_income -c1.unit_cost
    break_even_point = int(admin_cost/c_m)
    gain_per_dollar = round(net_profit/(c1.sales*c1.unit_income), 2)
    return operative_profit, net_profit, c_m, break_even_point, gain_per_dollar 

@report
def income_statement(c1, scenario):
    """Calculate company's income statement."""
    if scenario == "A":
        gross_profit = round((c1.unit_income -c1.unit_cost)*c1.sales, 2)
        admin_cost = c1.payroll + c1.publicity + c1.rent + c1.services
        profits_and_extras = others_calculations(c1, gross_profit, admin_cost)
        save_data(profits_and_extras, "actual")
        return gross_profit, profits_and_extras
    elif scenario == "N":
        """If I'll double publicity, my sales increase by 15%"""
        gross_profit = round((c1.unit_income -c1.unit_cost)*(c1.sales*1.15), 2)
        admin_cost = c1.payroll + (c1.publicity*2) + c1.rent + c1.services
        profits_and_extras = others_calculations(c1, gross_profit, admin_cost)
        save_data(profits_and_extras, "actual")
        return gross_profit, profits_and_extras

if __name__=='__main__':
    company_1 = Company("Oreo", 3500, 2.5, 0.2, 1600, 800, 100, 1000, 0.18)
    income_statement(company_1, "A") #A = Actual scenario
    income_statement(company_1, "N") #N = New scenario