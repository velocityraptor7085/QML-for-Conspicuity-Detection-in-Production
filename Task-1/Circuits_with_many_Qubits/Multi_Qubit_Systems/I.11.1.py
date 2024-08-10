num_wires = 3
dev = qml.device("default.qubit", wires=num_wires)


@qml.qnode(dev)
def make_basis_state(basis_id):
    """Produce the 3-qubit basis state corresponding to |basis_id>.

    Note that the system starts in |000>.

    Args:
        basis_id (int): An integer value identifying the basis state to construct.

    Returns:
        np.array[complex]: The computational basis state |basis_id>.
    """

    ##################
    # YOUR CODE HERE #
    ##################

    # CREATE THE BASIS STATE:
    basis_id_binary = np.base_repr(basis_id).zfill(3)
    list_1 = list(basis_id_binary)
    final_list = [int(x) for x in list_1]

    for i in range(len(final_list)):
        if final_list[i] == 1:
            qml.PauliX(wires=i)

    return qml.state()


basis_id = 3
print(f"Output state = {make_basis_state(basis_id)}")
