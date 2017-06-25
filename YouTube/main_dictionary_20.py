# Python 的 dictionary

classmates = {'Tony':'cool but smells',
              'Emma':'sit behind me',
              'Luck':'asks too many questions'
              }

print(classmates)
print(classmates['Emma'])
print(classmates['Luck'])
print(classmates['Tony'])

# 注意这里 items()
for k,v in classmates.items():
    print(k+ v)

