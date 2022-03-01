def encryptionValidity(instructionCount, validityPeriod, keys):
    maxDivision = 0
    numberOfKeys = len(keys)
    strength = 0
    maxTries = instructionCount * validityPeriod
    powerOf = pow(10, 5)

    for i in keys:
        divisionDegree = 0

        for counter in range(numberOfKeys):
            if i % keys[counter] == 0:
                divisionDegree += 1

        if maxDivision < divisionDegree:
            maxDivision = divisionDegree

    strength = maxDivision * powerOf

    if strength < maxTries:
        # print([1, strength])
        return [1, strength]
    else:
        # print([0, strength])
        return [0, strength]





encryptionValidity(100, 1000, [2 ,4])
# Answer: [0, 200000]
encryptionValidity(9677958, 50058356, [83315, 22089, 19068, 64911, 67636, 4640, 80192, 98971])
# Answer: [1, 100000]
encryptionValidity(200, 2000, [2, 2, 4, 4])
# Answer: [1, 400000]
