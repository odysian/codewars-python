# https://www.codewars.com/kata/554a44516729e4d80b000012/train/python


def nb_months(
    start_price_old, start_price_new, saving_per_month, percent_loss_by_month
):
    # Check if we can buy new car right away
    if start_price_old >= start_price_new:
        return [0, int(round(start_price_old - start_price_new))]

    old, new = start_price_old, start_price_new
    savings = 0
    deprec = percent_loss_by_month / 100.0
    months = 0

    # Monthly cycle, add month, if even we up deprec
    # Add savings to acc, update both car values
    # Check if our savings and old car are worth more
    # Clean up return
    while True:
        months += 1
        if months % 2 == 0:
            deprec += 0.5 / 100.0

        savings += saving_per_month
        old = old * (1 - deprec)
        new = new * (1 - deprec)

        if savings + old >= new:
            leftover = savings + old - new
            return [months, int(round(leftover))]
