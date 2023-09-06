def sort_dvds(ammount_of_dvds, dvd_stack):

    for elememnt in dvd_stack:
        
        if elememnt > dvd_stack[-1]:
            taken_dvd = dvd_stack.pop(dvd_stack.index(elememnt))
            dvd_stack.append(taken_dvd)
        

    return dvd_stack

sort_dvds(7, [1, 4, 5, 2, 3, 6, 7])
