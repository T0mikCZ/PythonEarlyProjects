import speedtest

test = speedtest.Speedtest()
test.get_best_server()

print("Please wait, your internet speed is being measured\n")

down = test.download()
upload = test.upload()
ping = test.results.ping

print(f"Download speed: {round(down/1000000, 2)}Mbps")
print(f"Upload speed: {round(upload/1000000, 2)}Mbps")
print(f"Latency: {ping}ms")

input()
exit()