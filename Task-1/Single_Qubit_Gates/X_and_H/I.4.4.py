##################
# YOUR CODE HERE #
##################

# CREATE A DEVICE
dev = qml.device('default.qubit', wires=1)

# CREATE A QNODE CALLED apply_hxh THAT APPLIES THE CIRCUIT ABOVE
@qml.qnode(dev)
def apply_hxh(state):

    #Initialize qubit according to input state:
    if state==1:
        qml.PauliX(wires=0)

    #Apply H, X, H:
    qml.Hadamard(wires=0)
    qml.PauliX(wires=0)
    qml.Hadamard(wires=0)

    #Return state:
    return qml.state()

# Print your results
print(apply_hxh(0))
print(apply_hxh(1))
