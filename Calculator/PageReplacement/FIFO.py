import copy


def FIFO(pageReplacementAlgorithm, pageReferences, numberOfFrames):
    print(pageReplacementAlgorithm)
    print(pageReferences)
    print(numberOfFrames)

    numberOfFrames = int(numberOfFrames)
    frames = [[] for _ in range(numberOfFrames)]
    hitOrFault = []

    blankCount = 0
    nonBlankCount = numberOfFrames

    for x in range(numberOfFrames):
        currentPage = pageReferences[x]
        # copy the first few pages directly into the storage
        for _ in range(blankCount):
            frames[x].append("_")

        for _ in range(nonBlankCount):
            frames[x].append(currentPage)

        blankCount += 1
        nonBlankCount -= 1
        hitOrFault.append("F")

    framesDetails = {"frames": frames, "hitOrFault": hitOrFault, "remark": "None."}

    framesDetailsSet = []
    framesDetailsSet.append(framesDetails)

    for y in range(numberOfFrames, len(pageReferences)):
        frames = copy.deepcopy(frames)
        hitOrFault = copy.deepcopy(hitOrFault)
        currentPage = pageReferences[y]
        doesExist = False

        # check if the page exists
        for z in range(numberOfFrames):
            if frames[z][-1] == currentPage:
                doesExist = True
            # append the frames with the latest pages. if it is a fault, the appropriate page will be replaced later
            frames[z].append(frames[z][-1])

        if not doesExist:
            # currentPage does not exist, so it is a fault
            minIndex = 1000  # initialization
            for x in range(numberOfFrames):
                # get the preceding column index of -1, which is -2 in this case. positive indices are used instead of negative ones so that we can check if the index is already out of bounds (the first condition).
                trav = y - 1
                while trav > 0 and frames[x][trav] == frames[x][trav - 1]:
                    trav -= 1

                if minIndex > trav:
                    minIndex = trav
                    indexReplace = x

            hitOrFault.append("F")
            remark = f"{frames[indexReplace][-1]} replaced by {currentPage}."
            # replace the number replaced by the algorithm
            frames[indexReplace][-1] = currentPage
        else:
            # currentPage exists in either of the frames, so it is a hit
            hitOrFault.append("H")
            remark = "None"

        framesDetails = {"frames": frames, "hitOrFault": hitOrFault, "remark": remark}
        framesDetailsSet.append(framesDetails)

        # calculate hits and faults
        numberOfHits = hitOrFault.count("H")
        numberOfFaults = hitOrFault.count("F")
        hitsPercentage = numberOfHits / len(pageReferences) * 100
        faultsPercentage = numberOfFaults / len(pageReferences) * 100

        statistics = {
            "numberOfHits": numberOfHits,
            "numberOfFaults": numberOfFaults,
            "hitsPercentage": hitsPercentage,
            "faultsPercentage": faultsPercentage,
        }

    print(framesDetailsSet)
    print(statistics)

    return framesDetailsSet, statistics

    # for frames[x]

    # else:
    #   # implement the FIFO algo
    #   # check if currentPage exists
