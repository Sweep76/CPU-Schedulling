import copy


def LFU(pageReplacementAlgorithm, pageReferences, numberOfFrames):
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

    # for lFU
    count = {}

    for y in range(numberOfFrames, len(pageReferences)):
        frames = copy.deepcopy(frames)
        hitOrFault = copy.deepcopy(hitOrFault)
        currentPage = pageReferences[y]
        doesExist = False

        existingPages = []
        # check if the page exists
        for z in range(numberOfFrames):
            latestPage = frames[z][-1]
            if latestPage == currentPage:
                doesExist = True
            # append the frames with the latest pages. if it is a fault, the appropriate page will be replaced later
            frames[z].append(latestPage)
            existingPages.append(latestPage)
            if not latestPage in count:
                count[latestPage] = 1

        if not doesExist:
            # currentPage does not exist, so it is a fault
            # get all keys with the least value
            min_value = min(count.values())
            keys_with_min_value = [
                key for key, value in count.items() if value == min_value
            ]

            if len(keys_with_min_value) > 1:
                # there are multiple pages that are least recently used, so use FIFO as the basis.
                minIndex = 1000  # initialization
                for x in range(len(keys_with_min_value)):
                    frameIndex = existingPages.index(keys_with_min_value[x])
                    trav = y - 1
                    while (
                        trav > 0
                        and frames[frameIndex][trav] == frames[frameIndex][trav - 1]
                    ):
                        trav -= 1

                    if minIndex > trav:
                        minIndex = trav
                        indexReplace = frameIndex
                # keys_with_min_value now only contains the key with the least value and the first to go in (FIFO)
                keys_with_min_value = [existingPages[indexReplace]]
            else:
                indexReplace = existingPages.index(keys_with_min_value[0])
            # delete key
            count.pop(keys_with_min_value[0])

            hitOrFault.append("F")
            remark = f"{frames[indexReplace][-1]} replaced by {currentPage}."
            # replace the number replaced by the algorithm
            frames[indexReplace][-1] = currentPage
        else:
            # currentPage exists in either of the frames, so it is a hit
            hitOrFault.append("H")
            remark = "None"

            # FOR LFU
            count[currentPage] += 1

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

    # print(framesDetailsSet)
    # print(statistics)

    return framesDetailsSet, statistics

    # for frames[x]

    # else:
    #   # implement the FIFO algo
    #   # check if currentPage exists
