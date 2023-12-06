import csv

def load_ip_addresses(file_path):
    with open(file_path, 'r') as file:
        ip_addresses = {row[0] for row in csv.reader(file, delimiter=',')}
    return ip_addresses

def find_matching_ips(main_csv_path, user_csv_path):
    main_ips = load_ip_addresses(main_csv_path)
    user_ips = load_ip_addresses(user_csv_path)

    matching_ips = user_ips.intersection(main_ips)

    if matching_ips:
        print("Matching IP Addresses:")
        for ip in matching_ips:
            print(ip)
    else:
        print("No matching IP addresses")

if __name__ == "__main__":
    main_csv_path = input("Enter the path to the main CSV file: ")
    user_csv_path = input("Enter the path to the user CSV file: ")

    find_matching_ips(main_csv_path, user_csv_path)
