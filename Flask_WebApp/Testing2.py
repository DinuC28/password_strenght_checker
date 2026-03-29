from zxcvbn import zxcvbn
from strength_checker import password_validation, password_strength


def sample_test(sample = 1000):
    result = []

    with open('rockyou.txt', encoding = 'utf-8') as file:
        password_sample = [next(file).strip() for i in range(sample)]

    for password in password_sample:
        score = password_strength(password)
        validation = password_validation(password)
        zxcvbn_score = zxcvbn(password)

        result.append({
            'my_score': score,
            'my_validation': validation,
            'zxcvbn_score': zxcvbn_score['score'],
            'zxcvbn_validation': zxcvbn_score['feedback']
        })

    return result

def results_testing(result):
    agreements = 0
    disagreements = 0
    my_checker_rating = ""
    zxcvbn_rating = ""

    for i in result:

        if i['my_score'] <= 4:
            my_checker_rating = "weak"

        elif i['my_score'] <= 10:
            my_checker_rating = "medium"

        elif i['my_score'] <= 20:
            my_checker_rating = "strong"



        if i['zxcvbn_score'] <=1:
            zxcvbn_rating = "weak"

        elif i['zxcvbn_score'] == 2:
            zxcvbn_rating = "medium"

        elif  i['zxcvbn_score'] <= 4:
            zxcvbn_rating = "strong"

        if my_checker_rating == zxcvbn_rating:
            agreements += 1
        else:
            disagreements += 1

    total = len(result)
    print(f"Agreement rate: {agreements}/{total}" ({(agreements / total) * 100}))
    print(f"Disagreement rate: {disagreements}/{total}" ({(disagreements / total) * 100}))

if __name__ == '__main__':
    print("== RockYou testing ==")

    test = sample_test(1000)
    results_testing(test)
    print("== RockYou testing ==")

