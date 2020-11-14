import csv
import speedtest

def write_dict(filename, dict_data):

    with open(filename, "a+") as f:
        w = csv.DictWriter(f, fieldnames=dict_data.keys())

        if f.tell() == 0:
            w.writeheader()

        w.writerow(dict_data)


st = speedtest.Speedtest()
server = st.get_best_server()
st.download()
st.upload()


results = st.results.dict()
del results["client"]
del results["server"]

client = dict(st.results.client)
client["timestamp"] = results["timestamp"]
server["timestamp"] = results["timestamp"]

write_dict("server.csv", server)
write_dict("client.csv", client)
write_dict("results.csv", results)
