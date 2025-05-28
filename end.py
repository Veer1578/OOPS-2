class employee():
    def __init__(self):
        print('Employee Created')
    def  __del__(self):
        print("Destructor Called")

def create_obj():
    print('Making Object...')
    obj = employee()
    print('Function ended...')
    return obj

print('Calling create_oobj function...')
obj = create_obj()
print('Program end')