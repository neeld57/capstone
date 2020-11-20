import boto3
from calculator_system import calc_test
from calculator_system.calc import add, subtract, divide, multiply

sns = boto3.client('sns')

def lambda_handler(event, context):
    arth_operator = event["operator"]
    if arth_operator == "add":
        return add(event)
    if arth_operator == "subtract":
        return subtract(event)
    if arth_operator == "divide":
        return divide(event)
    if arth_operator == "multiply":
        return multiply(event)
    if arth_operator == "test":
        try:
            for x in ["test_add_1", "test_add_2", "test_add_3", "test_add_4", "test_add_5", "test_add_6", "test_add_7",
                      "test_add_8", "test_add_9", "test_subtract_1", "test_subtract_2", "test_subtract_3", "test_subtract_4",
                      "test_subtract_5","test_subtract_6","test_subtract_7","test_subtract_8","test_subtract_9",
                      "test_divide_1","test_divide_2","test_divide_3", "test_divide_4", "test_divide_5","test_divide_6",
                      "test_divide_7", "test_divide_8", "test_divide_9", "test_multiply_1", "test_multiply_2","test_multiply_3",
                      "test_multiply_4", "test_multiply_5","test_multiply_6", "test_multiply_7", "test_multiply_8",
                      "test_multiply_9"]:
                my_test_function = getattr(calc_test, x)
                my_test_function()
        except:
            response = sns.publish(
                TopicArn='INSERT_YOUR_SNS_ARN',
                Message="One or more tests failed. Please take a look at Lambda function bscs-capstone"
            )