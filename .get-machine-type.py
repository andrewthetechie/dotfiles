import json
import socket

def get_hostname():
    return socket.gethostname()

def main():
    try:
        with open('.chezmoi-machine-data.json', 'r') as file:
            machine_data = json.load(file)
    except Exception as e:
        print(f"An error occurred while loading machine type: {e}. Will prompt for data.")
        machine_data = {}
    if 'hostname' not in machine_data:
        machine_data['hostname'] = get_hostname()
    if 'machine_type' not in machine_data:
        machine_data['machine_type'] = input("What is the machine type? ")

    with open('.chezmoi-machine-data.json', 'w') as file:
        json.dump(machine_data, file, indent=4)

if __name__ == "__main__":
    main()