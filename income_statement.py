from company import Company

def others_calculations():
    pass


def income_statement(c1, scenario):
    if scenario == "A":
        gross_profit = round((c1.unit_income -c1.unit_cost)*c1.sales, 2)
        admin_cost = c1.payroll + c1.publicity + c1.rent + c1.services
        profits_and_extras = others_calculations(c1, gross_profit, admin_cost)
    elif scenario == "N":
        gross_profit = round((c1.unit_income -c1.unit_cost)*(c1.sales*1.15), 2)
        admin_cost = c1.payroll + (c1.publicity*2) + c1.rent + c1.services
        profits_and_extras = others_calculations(c1, gross_profit, admin_cost)

if __name__=='__main__':
    company_1 = Company("Oreo", 3500, 2.5, 0.2, 1600, 800, 100, 1000, 0.18)
    income_statement(company_1, "A") #A = Actual scenary
    income_statement(company_1, "N") #N = New scenary
