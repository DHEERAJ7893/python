
a=[1,2.3,'python',0,24,13,43]

# for ele in a:
#     print(1/ele)
import sys
for ele in a:
    try:
        print(1/ele)
        print(time.date)
    except TypeError:
            # print(sys.exc_info()[0])
            print("it seens your enterder wrong string")
    except ZeroDivisionError:
            print("it seens your entered not a divisible number wrong string")     
    except:
        print("some error occured")