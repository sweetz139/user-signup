def sort_contacts(dictionary):
    keylist = sorted(dictionary)
    new_sorted_list =[]
    for name in keylist:
        for contact in range(len(keylist)):
            phone , email = dictionary[name]
        new_tuple =name , phone , email
        new_sorted_list.append(new_tuple)
    return new_sorted_list
            

