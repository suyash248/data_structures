from Tree.commons import insert

def distance_from_root_v1(root, key, distance=0):
    """
    Distance from root is same as the level at which key is present.
    :param root:
    :param key:
    :param distance:
    :return:
    """
    if root == None:
        return -1

    if root.key == key:
        return distance
    else:
        ld = distance_from_root_v1(root.left, key, distance+1)
        rd = distance_from_root_v1(root.right, key, distance+1)
    return ld if ld > 0 else rd

def distance_from_root_v2(root, key, level=0):
    """
    :param root:
    :param key:
    :param level:
    :return:
    """
    if root is None:
        return -1
    if root.key == key:
        global distance_v2
        distance_v2 = level
        return level

    ld = distance_from_root_v2(root.left, key, level+1)
    # if key found in left-subtree, return it.
    if ld != -1:
        return ld
    # if key is not found in left-subtree, try searching for key in right-subtree
    else:
        rd = distance_from_root_v2(root.right, key, level+1)
        return rd


def distance_from_root_v3(root, key, distance=0):
    if root is None:
        return -1

    if key > root.key:
        return distance_from_root_v3(root.right, key, distance+1)
    elif key < root.key:
        return distance_from_root_v3(root.left, key, distance+1)
    else:
        return distance

# Driver program to test above function
if __name__ == "__main__":
    """ Let us create following BST
            50
         /		 \
        30		  70
       /  \     / 	 \
      20   40  60 	  80
     /   \
    15   25
    """
    root = None
    root = insert(root, 50)
    insert(root, 30)
    insert(root, 20)
    insert(root, 15)
    insert(root, 25)
    insert(root, 40)
    insert(root, 70)
    insert(root, 60)
    insert(root, 80)

    print("\n---- Using V1 ----\n")
    key = 25
    distance = distance_from_root_v1(root, key)
    print("Distance from root({root}) to {key} is {distance}".format(root=root.key, key=key, distance=distance))

    print("\n---- Using V2 ----\n")
    distance_v2 = distance_from_root_v2(root, key, level=0)
    print("Distance from root({root}) to {key} is {distance}".format(root=root.key, key=key, distance=distance_v2))

    print("\n---- Using V3 ----\n")
    distance_v3 = distance_from_root_v3(root, key)
    print("Distance from root({root}) to {key} is {distance}".format(root=root.key, key=key, distance=distance_v3))