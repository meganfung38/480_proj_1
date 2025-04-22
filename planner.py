import sys

if __name__=="__main__":
    if len(sys.argv) != 3:
        print("Usage: planner.py takes 2 arguments-- <algorithm> <world-file>")
        sys.exit(1)

    algorithm = sys.argv[1] # search algorithm to execute
    world_file = sys.argv[2] # world file to vacuum clean

    # check for valid search algorithm argument
    if algorithm not in ["uniform-cost", "depth-first"]:
        print("Error: algorithm must be 'uniform-cost' or 'depth-first'")
        sys.exit(1)

    # check for valid .txt world file 
    if not world_file.endswith(".txt"):
        print("Error: world file must be a .txt file")
        sys.exit(1)