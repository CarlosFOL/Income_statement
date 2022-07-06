from company import Company

def income_statement(company_1, scenario):
    if scenario == "A":
        pass
    elif scenario == "N":
        pass

if __name__=='__main__':
    company_1 = Company("Oreo", 3500, 2.5, 0.2, 1600, 800, 100, 1000, 0.18)
    income_statement(company_1, "A") #A = Actual scenary
    income_statement(company_1, "N") #N = New scenary
    