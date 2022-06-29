def cal_x(age):
    if age <= 0:
        raise ZeroDivisionError("age value %s is not valid" % age)
    print(10 / age)


try:
    cal_x(0)
    cal_x(10)
# except ValueError as error:
#     print('value error age can not be zero')

except ZeroDivisionError as error:
    print('zero division error, age can not be zero')
    print(error)

else:
    cal_x(3.5)

finally:
    print('job is done')
