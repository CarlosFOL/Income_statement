class Company:
    name: str;
    sales: int;
    unit_income: float;
    unit_cost: float;
    payroll: int;
    publicity: int;
    services: int;
    rent: int;
    taxes: float;

    def __init__(self, name, sales, unit_income, unit_cost, payroll, publicity, services, rent, taxes):
        self.name = name
        self.sales = sales
        self.unit_income = unit_income
        self.unit_cost = unit_cost
        self.payroll = payroll
        self.publicity = publicity
        self.services = services
        self.rent = rent
        self.taxes = taxes