from company import Company

def structure(company_data):
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
    def wrapper(company, scenario):
        company_data = func(company, scenario)
        if scenario == "A":
            print(f"""[Actual scenary] By calculating income statement of "{company.name}" business...""")
            structure(company_data)
        elif scenario == "N":
            print(f"""
[New scenary] By calculating income statement of "{company.name}" business...""")
            structure(company_data)
    return wrapper

def save_data(c1_data, scenario):
    with open(f"./{scenario}_scenary.txt","w", encoding="utf-8") as f:
        for element in c1_data:
            f.write(str(element))
            f.write("\n")

def others_calculations(c1, gross_profit, admin_cost):
    operative_profit = round(gross_profit - admin_cost, 2)
    net_profit = round(operative_profit - (operative_profit*c1.taxes), 2)
    c_m = c1.unit_income -c1.unit_cost
    break_even_point = int(admin_cost/c_m)
    gain_per_dollar = round(net_profit/(c1.sales*c1.unit_income), 2)
    return operative_profit, net_profit, c_m, break_even_point, gain_per_dollar 

def income_statement(c1, scenario):
    if scenario == "A":
        gross_profit = round((c1.unit_income -c1.unit_cost)*c1.sales, 2)
        admin_cost = c1.payroll + c1.publicity + c1.rent + c1.services
        profits_and_extras = others_calculations(c1, gross_profit, admin_cost)
        save_data(profits_and_extras, "actual")
        return gross_profit, profits_and_extras
    elif scenario == "N":
        gross_profit = round((c1.unit_income -c1.unit_cost)*(c1.sales*1.15), 2)
        admin_cost = c1.payroll + (c1.publicity*2) + c1.rent + c1.services
        profits_and_extras = others_calculations(c1, gross_profit, admin_cost)
        save_data(profits_and_extras, "actual")
        return gross_profit, profits_and_extras

if __name__=='__main__':
    company_1 = Company("Oreo", 3500, 2.5, 0.2, 1600, 800, 100, 1000, 0.18)
    income_statement(company_1, "A") #A = Actual scenary
    income_statement(company_1, "N") #N = New scenary
