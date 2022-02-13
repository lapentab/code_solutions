# PROMPT: From this youtube video: https://www.youtube.com/watch?v=4tYoVx0QoN0 . I tried the problem on my own before seeing the given solution.
# "Imagine you have 2D matrix composed of only numbers 0 and 1. 1 represents a black pixel, 0 represents a white pixel.
#  The function should remove all of the black pixels that are not connected to the boarder of the image. Only vertical and horizontal, not diagonal"


# Logic: Originally, I had explored creating this recursively. However, I feel an iterative approach is more compact.
# An iterative approach does not require looking at any 0 more than once. Since all we care about are the 1's in the image, those are the indices we should look at.
# Once we get the indices of all the 1's, we can ignore any 0 from here on out, we don't even need to look at them!
# Once we get the indices of all 1's, we should separate it into 2 groups. Those on the boarder, and those not on the boarder.
# Once we have our 1's separated, we can go through each boarder pixel and compare it to the rest of our non-edge pixels.
# If we find a neighbor, that neighbor essentially becomes another 'edge' pixel, so we add that to the 'edge' array. This lets us crawl down a path.
# After the end of that operation, the only 1's left in the original array of 1's are islands. They had no connecting edges.

def remove_islands(array):
    #Pull out the 1's from the array.
    ones = []
    for i in range(0, len(array)):
        for j in range(0, len(array[0])):
            if array[i][j] == 1:
              ones+=[(i,j)]
    # Pick out the selected 1's that lie on the boarder.
    edges = [items for items in ones if items[0]==0 or items[0]==len(array)-1 or items[1] == 0 or items[1] == len(array[0])-1]
    # Select all remaining 1's that are not an edge
    check = [one for one in ones if one not in edges]
    
    # Helper function to test if two given coordinates are adjacent
    def check_adjacency(x1, y1, x2, y2):
        return ((x2==x1-1 or x2==x1+1) and y1==y2) or ((y2==y1-1 or y2==y1+1) and (x1==x2))
    
    # Go through each known edge and compare it to each non-edge.
    # We will be mutating the edges array, but we want to modify the list itself to run to completion. edges will be added to, but not removed, so the array is not copied.
    for edge in edges:
        # Since we will be modifying/shortening check, the array is copied in this case
        for tocheck in check[:]:
            # If an non-edge is connected to a edge, it functionally becomes an edge itself
            if(check_adjacency(edge[0], edge[1], tocheck[0], tocheck[1])):
                edges.append(tocheck)
                check.remove(tocheck)
    # Anything left in 'check' is an island, so we set it to zero.
    for items in check:
        array[items[0]][items[1]] = 0
    return array
