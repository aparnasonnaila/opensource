def final_amount(bill_amount):
    disc_10_per = bill_amount *0.10
    amount_10_per_disc = bill_amount - disc_10_per
    amount_100_flat_disc = bill_amount - 100
    final_amount = min(amount_10_per_disc, amount_100_flat_disc)
    return final_amount
bill_amount = float(input())
print(int(final_amount(bill_amount)))
