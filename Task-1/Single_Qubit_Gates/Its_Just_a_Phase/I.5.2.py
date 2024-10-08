dev = qml.device("default.qubit", wires=1)


@qml.qnode(dev)
def fake_z():
    """Use RZ to produce the same action as Pauli Z on the |+> state.

    Returns:
        np.array[complex]: The state of the qubit after the operations.
    """

    ##################
    # YOUR CODE HERE #
    ##################

    # CREATE THE |+> STATE:
    qml.Hadamard(wires=0)

    # APPLY RZ:
    qml.RZ(3.14159265359, wires=0)
    # RETURN THE STATE:
    return qml.state()
