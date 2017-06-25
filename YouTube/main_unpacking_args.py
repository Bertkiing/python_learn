def health_calculator(age,apples_ate,cigs_smoked):
    answer = (100-age)+(apples_ate * 3.5)-(cigs_smoked * 2)
    print(answer)

someOne_data = [27,20,0]

health_calculator(someOne_data[0],someOne_data[1],someOne_data[2])

# 自动拆箱，非常棒
health_calculator(*someOne_data)