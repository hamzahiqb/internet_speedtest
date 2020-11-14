import argparse
import csv
import os
import speedtest

def write_dict(filename, dict_data):

    mode = "a+" if os.path.exists(filename) else "w+"
    with open(filename, mode) as f:
        w = csv.DictWriter(f, fieldnames=dict_data.keys())

        if f.tell() == 0:
            w.writeheader()

        w.writerow(dict_data)

# Get path where files are saved
parser = argparse.ArgumentParser()
parser.add_argument("-d", nargs="?", default="~")
args = parser.parse_args()

# Run speed test
st = speedtest.Speedtest()
server = st.get_best_server()
st.download()
st.upload()

# Parse and separate data
results = st.results.dict()
del results["client"]
del results["server"]

# Add timestamp to all as unique identifier
client = dict(st.results.client)
client["timestamp"] = results["timestamp"]
server["timestamp"] = results["timestamp"]

# Save speed test
write_dict(f"{args.d}/server.csv", server)
write_dict(f"{args.d}/client.csv", client)
write_dict(f"{args.d}/results.csv", results)
