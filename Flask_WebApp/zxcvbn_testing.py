from zxcvbn import zxcvbn

result = zxcvbn('mypassword123')
print(result['score'])
print(result['feedback'])