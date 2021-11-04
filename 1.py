from typing import Union


def average_profit(companies: dict) -> int:
    avg_profit = 0
    for company in companies.values():
        avg_profit += sum(company)
    return round(avg_profit / len(companies))


def non_average_sorting(companies: dict) -> Union[dict, dict, int]:
    avg_profit = average_profit(companies)
    lt_avg = {}
    ge_avg = {}
    for company, company_profit in companies.items():
        if avg_profit <= sum(company_profit):
            ge_avg.setdefault(company, sum(company_profit))
        else:
            lt_avg.setdefault(company, sum(company_profit))
    return lt_avg, ge_avg, avg_profit


if __name__ == '__main__':
    companies = {
        'UBS': [122033, 233443, 222111, 332343],
        'Mickle Kors': [234322, 234323, 111223, 112322],
        'IBM': [223222, 321832, 111232, 23111],
        'Apple': [343212, 234452, 343233, 222111]
    }
lt_avg, ge_avg, avg_profit = non_average_sorting(companies)
print(f'Average profit: {avg_profit}')
print(f'Companies with average:{ge_avg}')
print(f'Companies without average:{lt_avg}')
