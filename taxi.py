
import requests
url = "https://d37ci6vzurychx.cloudfront.net/misc/taxi_zone_lookup.csv"
req = requests.get(url)
with open('taxi_zone_lookup.csv', 'r') as f:
    results = []
    next(f)  
    for line in f:
        if line.strip():
            words = line.split(',')  
            results.append(words)  
datas = len(results)
print("Total number of records:", datas)
boroughs = sorted(set(row[1].strip() for row in results)) 
print("Unique boroughs in sorted order:", boroughs)
brooklyn_count = 0 
for row in results:
    borough_name = row[1].strip().strip('"')  
    if borough_name == "Brooklyn":  
        brooklyn_count += 1
print("Number of records for Brooklyn:", brooklyn_count)

output_file_path = "root/taxi_zone_output.txt"
with open(output_file_path, "w") as output_file:
    output_file.write(f"Total number of records: {datas}\n")
    output_file.write(f"Unique boroughs: {', '.join(boroughs)}\n")
    output_file.write(f"Number of Brooklyn records: {brooklyn_count}\n")

print("Data processing complete, facts saved to taxi_zone_output.txt")
