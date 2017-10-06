def get_initials(fullname):
    """ Given a person's name, return the person's initials (uppercase) """
    # TODO your code here
    initial_str = ''
    for i in range(len(fullname)):
        cap_fullname = fullname.upper()
        if(i == 0):
            initial_str= initial_str + (cap_fullname[i])
            
        if cap_fullname[i] == ' ':
            initial_str = initial_str + (cap_fullname[i+1])
            
    return initial_str

def main():

    s = "zachary Sweet"

    st = "Zachary thomas Sweet"

    stt = "Zachary julio thomas roberto Sweet"

    print(get_initials(s))
    print(get_initials(st))
    print(get_initials(stt))
    

if __name__ == "__main__":
    main()