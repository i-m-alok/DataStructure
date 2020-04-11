def diameter_of_binary_tree(root):
    return diameter_of_binary_tree_func(root)[1]
        
def  diameter_of_binary_tree_func(root):
    """
    :param: root - Root of binary tree
    TODO: Complete this method and return diameter (int) of binary tree
    """
    if root is None:
        return 0, 0
    left_height, left_dia= diameter_of_binary_tree_func(root.left)
    right_height, right_dia= diameter_of_binary_tree_func(root.right)
    current_height=max(left_height,right_height)+1
    return current_height, max(left_height+right_height, max(left_dia,right_dia))
