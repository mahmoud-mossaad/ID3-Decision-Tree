root = strat_test_set.iloc[0][tree[0][0]]
print(tree[0][0])
print(strat_test_set.iloc[0][tree[0][0]])
if root == 0:
    bran1 = strat_test_set.iloc[0][tree[0][1][0]]
    print(tree[0][1][0])
    print(bran1)
    if bran1 == 2 and root == 0:
        bran2 = strat_test_set.iloc[0][tree[0][1][5][0]]
        print(tree[0][1][5][0])
        print(bran2)


        if bran2 == 2:
            bran3 = strat_test_set.iloc[0][tree[0][1][5][5][0]]
            print(tree[0][1][5][5][0])
            print(bran3)
            if bran3 == 2:
                bran4 = strat_test_set.iloc[0][tree[0][1][5][5][3][0]]
                print(tree[0][1][5][5][3][0])
                print(bran4)
            elif bran3 == 0:
                bran4 = strat_test_set.iloc[0][tree[0][1][5][5][1][0]]
                print(tree[0][1][5][5][1][0])
                print(bran4)
            elif bran3 == 1:
                bran4 = strat_test_set.iloc[0][tree[0][1][5][5][2][0]]
                print(tree[0][1][5][5][2][0])
                print(bran4)


        elif bran2 == 0:
            bran3 = strat_test_set.iloc[0][tree[0][1][5][1][0]]
            print(tree[0][1][5][1][0])
            print(bran3)
            if bran3 == 2:
                bran4 = strat_test_set.iloc[0][tree[0][1][5][1][3][0]]
                print(tree[0][1][5][1][3][0])
                print(bran4)
            elif bran3 == 0:
                bran4 = strat_test_set.iloc[0][tree[0][1][5][1][1][0]]
                print(tree[0][1][5][1][1][0])
                print(bran4)
            elif bran3 == 1:
                bran4 = strat_test_set.iloc[0][tree[0][1][5][1][2][0]]
                print(tree[0][1][5][1][2][0])
                print(bran4)


        elif bran2 == 1:
            bran3 = strat_test_set.iloc[0][tree[0][1][5][3][0]]
            print(tree[0][1][5][3][0])
            print(bran3)
            if bran3 == 2:
                bran4 = strat_test_set.iloc[0][tree[0][1][5][3][3][0]]
                print(tree[0][1][5][3][3][0])
                print(bran4)
            elif bran3 == 0:
                bran4 = strat_test_set.iloc[0][tree[0][1][5][3][1][0]]
                print(tree[0][1][5][3][1][0])
                print(bran4)
            elif bran3 == 1:
                bran4 = strat_test_set.iloc[0][tree[0][1][5][3][2][0]]
                print(tree[0][1][5][3][2][0])
                print(bran4)
    

    elif bran1 == 0 and root == 0:
        bran2 = strat_test_set.iloc[0][tree[0][1][1][0]]
        print(tree[0][1][1][0])
        print(bran2)
        if bran2 == 2:
            bran3 = strat_test_set.iloc[0][tree[0][1][1][5][0]]
            print(tree[0][1][1][5][0])
            print(bran3)
            if bran3 == 2:
                bran4 = strat_test_set.iloc[0][tree[0][1][1][5][3][0]]
                print(tree[0][1][1][5][3][0])
                print(bran4)
            elif bran3 == 0:
                bran4 = strat_test_set.iloc[0][tree[0][1][1][5][1][0]]
                print(tree[0][1][1][5][1][0])
                print(bran4)
            elif bran3 == 1:
                bran4 = strat_test_set.iloc[0][tree[0][1][1][5][2][0]]
                print(tree[0][1][1][5][2][0])
                print(bran4)


        elif bran2 == 0:
            bran3 = strat_test_set.iloc[0][tree[0][1][1][1][0]]
            print(tree[0][1][1][1][0])
            print(bran3)
            if bran3 == 2:
                bran4 = strat_test_set.iloc[0][tree[0][1][1][1][3][0]]
                print(tree[0][1][1][1][3][0])
                print(bran4)
            elif bran3 == 0:
                bran4 = strat_test_set.iloc[0][tree[0][1][1][1][1][0]]
                print(tree[0][1][1][1][1][0])
                print(bran4)
            elif bran3 == 1:
                bran4 = strat_test_set.iloc[0][tree[0][1][1][1][2][0]]
                print(tree[0][1][1][1][2][0])
                print(bran4)


        elif bran2 == 1:
            bran3 = strat_test_set.iloc[0][tree[0][1][1][3][0]]
            print(tree[0][1][1][3][0])
            print(bran3)
            if bran3 == 2:
                bran4 = strat_test_set.iloc[0][tree[0][1][1][3][3][0]]
                print(tree[0][1][1][3][3][0])
                print(bran4)
            elif bran3 == 0:
                bran4 = strat_test_set.iloc[0][tree[0][1][1][3][1][0]]
                print(tree[0][1][1][3][1][0])
                print(bran4)
            elif bran3 == 1:
                bran4 = strat_test_set.iloc[0][tree[0][1][1][3][2][0]]
                print(tree[0][1][1][3][2][0])
                print(bran4)




    elif bran1 == 1 and root == 0:
        bran2 = strat_test_set.iloc[0][tree[0][1][3][0]]
        print(tree[0][1][3][0])
        print(bran2)
        if bran2 == 2:
            bran3 = strat_test_set.iloc[0][tree[0][1][3][5][0]]
            print(tree[0][1][3][5][0])
            print(bran3)
            if bran3 == 2:
                bran4 = strat_test_set.iloc[0][tree[0][1][3][5][3][0]]
                print(tree[0][1][3][5][3][0])
                print(bran4)
            elif bran3 == 0:
                bran4 = strat_test_set.iloc[0][tree[0][1][3][5][1][0]]
                print(tree[0][1][3][5][1][0])
                print(bran4)
            elif bran3 == 1:
                bran4 = strat_test_set.iloc[0][tree[0][1][3][5][2][0]]
                print(tree[0][1][3][5][2][0])
                print(bran4)


        elif bran2 == 0:
            bran3 = strat_test_set.iloc[0][tree[0][1][3][1][0]]
            print(tree[0][1][3][1][0])
            print(bran3)
            if bran3 == 2:
                bran4 = strat_test_set.iloc[0][tree[0][1][3][1][3][0]]
                print(tree[0][1][3][1][3][0])
                print(bran4)
            elif bran3 == 0:
                bran4 = strat_test_set.iloc[0][tree[0][1][3][1][1][0]]
                print(tree[0][1][3][1][1][0])
                print(bran4)
            elif bran3 == 1:
                bran4 = strat_test_set.iloc[0][tree[0][1][3][1][2][0]]
                print(tree[0][1][3][1][2][0])
                print(bran4)


        elif bran2 == 1:
            bran3 = strat_test_set.iloc[0][tree[0][1][3][3][0]]
            print(tree[0][1][3][3][0])
            print(bran3)
            if bran3 == 2:
                bran4 = strat_test_set.iloc[0][tree[0][1][3][3][3][0]]
                print(tree[0][1][3][3][3][0])
                print(bran4)
            elif bran3 == 0:
                bran4 = strat_test_set.iloc[0][tree[0][1][3][3][1][0]]
                print(tree[0][1][3][3][1][0])
                print(bran4)
            elif bran3 == 1:
                bran4 = strat_test_set.iloc[0][tree[0][1][3][3][2][0]]
                print(tree[0][1][3][3][2][0])
                print(bran4)
elif root == 1:
    bran1 = strat_test_set.iloc[0][tree[0][3][0]]
    print(tree[0][3][0])
    print(bran1)
    if bran1 == 2 and root == 0:
        bran2 = strat_test_set.iloc[0][tree[0][3][5][0]]
        print(tree[0][3][5][0])
        print(bran2)


        if bran2 == 2:
            bran3 = strat_test_set.iloc[0][tree[0][3][5][5][0]]
            print(tree[0][3][5][5][0])
            print(bran3)
            if bran3 == 2:
                bran4 = strat_test_set.iloc[0][tree[0][3][5][5][3][0]]
                print(tree[0][3][5][5][3][0])
                print(bran4)
            elif bran3 == 0:
                bran4 = strat_test_set.iloc[0][tree[0][3][5][5][1][0]]
                print(tree[0][3][5][5][1][0])
                print(bran4)
            elif bran3 == 1:
                bran4 = strat_test_set.iloc[0][tree[0][3][5][5][2][0]]
                print(tree[0][3][5][5][2][0])
                print(bran4)


        elif bran2 == 0:
            bran3 = strat_test_set.iloc[0][tree[0][3][5][1][0]]
            print(tree[0][3][5][1][0])
            print(bran3)
            if bran3 == 2:
                bran4 = strat_test_set.iloc[0][tree[0][3][5][1][3][0]]
                print(tree[0][3][5][1][3][0])
                print(bran4)
            elif bran3 == 0:
                bran4 = strat_test_set.iloc[0][tree[0][3][5][1][1][0]]
                print(tree[0][3][5][1][1][0])
                print(bran4)
            elif bran3 == 1:
                bran4 = strat_test_set.iloc[0][tree[0][3][5][1][2][0]]
                print(tree[0][3][5][1][2][0])
                print(bran4)


        elif bran2 == 1:
            bran3 = strat_test_set.iloc[0][tree[0][3][5][3][0]]
            print(tree[0][3][5][3][0])
            print(bran3)
            if bran3 == 2:
                bran4 = strat_test_set.iloc[0][tree[0][3][5][3][3][0]]
                print(tree[0][3][5][3][3][0])
                print(bran4)
            elif bran3 == 0:
                bran4 = strat_test_set.iloc[0][tree[0][3][5][3][1][0]]
                print(tree[0][3][5][3][1][0])
                print(bran4)
            elif bran3 == 1:
                bran4 = strat_test_set.iloc[0][tree[0][3][5][3][2][0]]
                print(tree[0][3][5][3][2][0])
                print(bran4)
    

    elif bran1 == 0 and root == 0:
        bran2 = strat_test_set.iloc[0][tree[0][3][1][0]]
        print(tree[0][3][1][0])
        print(bran2)
        if bran2 == 2:
            bran3 = strat_test_set.iloc[0][tree[0][3][1][5][0]]
            print(tree[0][3][1][5][0])
            print(bran3)
            if bran3 == 2:
                bran4 = strat_test_set.iloc[0][tree[0][3][1][5][3][0]]
                print(tree[0][3][1][5][3][0])
                print(bran4)
            elif bran3 == 0:
                bran4 = strat_test_set.iloc[0][tree[0][3][1][5][1][0]]
                print(tree[0][3][1][5][1][0])
                print(bran4)
            elif bran3 == 1:
                bran4 = strat_test_set.iloc[0][tree[0][3][1][5][2][0]]
                print(tree[0][3][1][5][2][0])
                print(bran4)


        elif bran2 == 0:
            bran3 = strat_test_set.iloc[0][tree[0][3][1][1][0]]
            print(tree[0][3][1][1][0])
            print(bran3)
            if bran3 == 2:
                bran4 = strat_test_set.iloc[0][tree[0][3][1][1][3][0]]
                print(tree[0][3][1][1][3][0])
                print(bran4)
            elif bran3 == 0:
                bran4 = strat_test_set.iloc[0][tree[0][3][1][1][1][0]]
                print(tree[0][3][1][1][1][0])
                print(bran4)
            elif bran3 == 1:
                bran4 = strat_test_set.iloc[0][tree[0][3][1][1][2][0]]
                print(tree[0][3][1][1][2][0])
                print(bran4)


        elif bran2 == 1:
            bran3 = strat_test_set.iloc[0][tree[0][3][1][3][0]]
            print(tree[0][3][1][3][0])
            print(bran3)
            if bran3 == 2:
                bran4 = strat_test_set.iloc[0][tree[0][3][1][3][3][0]]
                print(tree[0][3][1][3][3][0])
                print(bran4)
            elif bran3 == 0:
                bran4 = strat_test_set.iloc[0][tree[0][3][1][3][1][0]]
                print(tree[0][3][1][3][1][0])
                print(bran4)
            elif bran3 == 1:
                bran4 = strat_test_set.iloc[0][tree[0][3][1][3][2][0]]
                print(tree[0][3][1][3][2][0])
                print(bran4)




    elif bran1 == 1 and root == 0:
        bran2 = strat_test_set.iloc[0][tree[0][3][3][0]]
        print(tree[0][3][3][0])
        print(bran2)
        if bran2 == 2:
            bran3 = strat_test_set.iloc[0][tree[0][3][3][5][0]]
            print(tree[0][3][3][5][0])
            print(bran3)
            if bran3 == 2:
                bran4 = strat_test_set.iloc[0][tree[0][3][3][5][3][0]]
                print(tree[0][3][3][5][3][0])
                print(bran4)
            elif bran3 == 0:
                bran4 = strat_test_set.iloc[0][tree[0][3][3][5][1][0]]
                print(tree[0][3][3][5][1][0])
                print(bran4)
            elif bran3 == 1:
                bran4 = strat_test_set.iloc[0][tree[0][3][3][5][2][0]]
                print(tree[0][3][3][5][2][0])
                print(bran4)


        elif bran2 == 0:
            bran3 = strat_test_set.iloc[0][tree[0][3][3][1][0]]
            print(tree[0][3][3][1][0])
            print(bran3)
            if bran3 == 2:
                bran4 = strat_test_set.iloc[0][tree[0][3][3][1][3][0]]
                print(tree[0][3][3][1][3][0])
                print(bran4)
            elif bran3 == 0:
                bran4 = strat_test_set.iloc[0][tree[0][3][3][1][1][0]]
                print(tree[0][3][3][1][1][0])
                print(bran4)
            elif bran3 == 1:
                bran4 = strat_test_set.iloc[0][tree[0][3][3][1][2][0]]
                print(tree[0][3][3][1][2][0])
                print(bran4)


        elif bran2 == 1:
            bran3 = strat_test_set.iloc[0][tree[0][3][3][3][0]]
            print(tree[0][3][3][3][0])
            print(bran3)
            if bran3 == 2:
                bran4 = strat_test_set.iloc[0][tree[0][3][3][3][3][0]]
                print(tree[0][3][3][3][3][0])
                print(bran4)
            elif bran3 == 0:
                bran4 = strat_test_set.iloc[0][tree[0][3][3][3][1][0]]
                print(tree[0][3][3][3][1][0])
                print(bran4)
            elif bran3 == 1:
                bran4 = strat_test_set.iloc[0][tree[0][3][3][3][2][0]]
                print(tree[0][3][3][3][2][0])
                print(bran4)







if bran4 == 3:
    print("When it's 0, class 0")
    
if bran4 == 4:
    print("When it's 0, class 1")
    
if bran4 == 5:
    print("When it's 1, class 0")

if bran4 == 6:
    print("When it's 1, class 1")

if bran4 == 7:
    print("When it's 2, class 0")

if bran4 == 8:
    print("When it's 2, class 1")
