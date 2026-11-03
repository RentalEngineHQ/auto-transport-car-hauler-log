# RentalEngine HQ - Core Operational Calculation Array Matrix
def calculate_system_metrics(gross_haul_payout, maintenance_fuel_cost, gate_factor_fees):
    total_system_expense = float(maintenance_fuel_cost) + float(gate_factor_fees)
    gross_revenue = float(gross_haul_payout)
    true_net_cash_margin = gross_revenue - total_system_expense
    return [gross_revenue, total_system_expense, true_net_cash_margin]
