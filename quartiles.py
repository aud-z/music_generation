# raw valence inputs
import numpy as np

def get_quartiles(folder):

    with open("./results/" + folder + "_valence.csv") as file_name:
        raw_valence = np.loadtxt(file_name, delimiter=",")

    with open("./results/" + folder + "_arousal.csv") as file_name:
        raw_arousal = np.loadtxt(file_name, delimiter=",")

    emopia_inputs = []
    for i in range(len(raw_valence)):
        # low valence, low arousal = q3
        if raw_valence[i] <= 0 and raw_arousal[i] <= 0:
            emopia_inputs.append(3)
        # low valence, high arousal = q2
        elif raw_valence[i] <= 0 and raw_arousal[i] > 0:
            emopia_inputs.append(2)
        # high valence, low arousal = q4
        elif raw_valence[i] > 0 and raw_arousal[i] <= 0:
            emopia_inputs.append(4)
        # high valence, high arousal = q1
        elif raw_valence[i] > 0 and raw_arousal[i] > 0:
            emopia_inputs.append(1)

    print(emopia_inputs)

    np.savetxt('./results/' + folder + '_quartiles.csv', emopia_inputs, delimiter = ',')


if __name__ == "__main__":
    get_quartiles(folder='aladdin')