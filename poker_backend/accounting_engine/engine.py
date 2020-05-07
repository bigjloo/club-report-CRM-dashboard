from agents.models import Account
from decimal import Decimal


def createAccountReport(data):
    for row in data:
        account_id = row["player_id"]
        # check if account exist in database
        try:
            account = Account.objects.get(club_account_id=account_id)
        except Account.DoesNotExist:
            raise Http404("account does not exist")
        # get data from parsed_data
        total_winnings = Decimal(row["total_winnings"])
        insurance = Decimal(row["insurance"])
        jackpot = Decimal(row["jackpot"])
        hands = int(row["hands"])
        total_rake = Decimal(row["fee"])
        # calculate engine
        gross_winloss = total_winnings
        rakeback_earnings = round((account.rakeback * total_rake), 2)
        net_winloss = round(
            (gross_winloss + rakeback_earnings + insurance + jackpot), 2)
        print(f"{gross_winloss} | {total_rake} | {rakeback_earnings} | {net_winloss} | {insurance} | {jackpot} | {hands} | {account}")
        # create AccountReport
        try:
            account_report = AccountReport(gross_winloss=gross_winloss, total_rake=total_rake, rakeback_earnings=rakeback_earnings,
                                           net_winloss=net_winloss, insurance=insurance, jackpot=jackpot, hands=hands, account=account)
        except:
            raise Http404("error creating account report")
        account_report.save()
