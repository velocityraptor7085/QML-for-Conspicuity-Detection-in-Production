def inner_product(state_1, state_2):
    """Compute the inner product between two states.

    Args:
        state_1 (np.array[complex]): A normalized quantum state vector
        state_2 (np.array[complex]): A second normalized quantum state vector

    Returns:
        complex: The value of the inner product <state_1 | state_2>.
    """

    ##################
    # YOUR CODE HERE #
    ##################

    # COMPUTE AND RETURN THE INNER PRODUCT

    #Find the complex conjugate of each element in state_1:
    state_1 = list(state_1)
    state_1 = [np.conj(c) for c in state_1]
    state_1 = np.array(state_1)

    #Find dot product:
    output = np.dot(state_1, state_2)
    return output

# Test your results with this code
ket_0 = np.array([1, 0])
ket_1 = np.array([0, 1])

print(f"<0|0> = {inner_product(ket_0, ket_0)}")
print(f"<0|1> = {inner_product(ket_0, ket_1)}")
print(f"<1|0> = {inner_product(ket_1, ket_0)}")
print(f"<1|1> = {inner_product(ket_1, ket_1)}")

'''
OUTPUT:
<0|0> = 1
<0|1> = 0
<1|0> = 0
<1|1> = 1
'''