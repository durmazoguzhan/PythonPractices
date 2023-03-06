while True:
    try:
        num1=int(input("a: "))
        num2=int(input("b: "))
        print(num1/num2)
    except ZeroDivisionError:
        print("b number cannot be zero.")
    except ValueError:
        print("please enter only logical data")
    except(Exception) as e:
        print("something went wrong")
        print(e)
    else:
        print("process completed successfully.")
        break
    finally:
        print("worked finally block")