a=[1,2.3,'python',0,24,13,43]

# for ele in a:
#     print(1/ele)

for ele in a:
    try:
        print(1/ele)
    except:
        print("some error occured")