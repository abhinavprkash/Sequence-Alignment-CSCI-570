import sys
# Initialise cost matrix for gap penalties and delta in order A, C, G, T
cost_for_alignment = [
    [0, 110, 48, 94],
    [110, 0, 118, 48],
    [48, 118, 0, 110],
    [94, 48, 110, 0]
]
 
def seq_alignUtils(s1, s2):
    # implement basic algorithm here
    return 'string_inputs'

def getString(s, index):
    modified_string = s[:index + 1] + s + s[index + 1:]  
    return modified_string

def seq_alignment(string_inputs, randomize1, randomize2):
    s1 = string_inputs[0]
    for index in randomize1:
        s1 = getString(s1, index)
    print(s1)
    s2 = string_inputs[1]
    for inde in randomize2:
        s2 = getString(s2, index)
    print(s2)
    return seq_alignUtils(s1, s2)

def main():
    if len(sys.argv) != 3:
        print("Usage: python3 basic.py input_file output_file")
        return

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    try:
        with open(input_file, 'r') as f:
            data = f.read()
            lines = data.splitlines()
            string_inputs = [] 
            randomize1 = []
            randomize2 = []
            for line in lines:
                if line.strip() and line[0].isalpha(): 
                    string_inputs.append(line) 
                else:
                    if len(string_inputs) == 1:
                        randomize1.append(int(line))
                    else:
                        randomize2.append(int(line))
            print(string_inputs)  
            print(randomize1)
            print(randomize2)
    except FileNotFoundError:
        print("Input file not found.")
        return
    
    try:
        with open(output_file, 'w') as f:
            f.write(seq_alignment(string_inputs,randomize1,randomize2)) 
        print("Output file created:", output_file)
    except Exception as e:
        print("Error occurred while writing to the output file:", e)

if __name__ == "__main__":
    main()
