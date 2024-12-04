def task(input): # the value of input is an integer which is the total money available

    needs = input * 0.5

    wants = input * 0.3

    savings = input * 0.2

    result = {"Needs": int(needs), "Wants": int(wants), "Savings": int(savings)} 


    return result # result should be a dictionary wiht the correct values
