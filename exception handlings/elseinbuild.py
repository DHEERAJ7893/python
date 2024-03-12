a=[1,2.3,'python',3,44,56,0]
for ele in a:
    try:
        print(1/ele)
    except TypeError:
        print("Please pass correct type of data")
    except ZeroDivisionError:
        print("Denominator should not be 0")
    except:
        print("Some Error Occured!")
    else:
        print("Else Info")