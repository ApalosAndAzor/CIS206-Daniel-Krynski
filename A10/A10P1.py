import json
from urllib.request import urlopen

with urlopen("https://wikimedia.org/api/rest_v1/metrics/pageviews/top/en.wikipedia/all-access/2024/03/all-days") as response:
  source = response.read()

data = json.loads(source)

print(json.dumps(data, indent=2))

with urlopen("https://wikimedia.org/api/rest_v1/metrics/pageviews/top/en.wikipedia/all-access/2024/02/all-days") as response1:
  source1 = response1.read()

data1 = json.loads(source1)

print(json.dumps(data1, indent=2))

with urlopen("https://wikimedia.org/api/rest_v1/metrics/pageviews/top/en.wikipedia/all-access/2024/01/all-days") as response2:
  source2 = response2.read()

data2 = json.loads(source2)

print(json.dumps(data2, indent=2))

with urlopen("https://wikimedia.org/api/rest_v1/metrics/pageviews/top/en.wikipedia/all-access/2023/12/all-days") as response3:
  source3 = response3.read()

data3 = json.loads(source3)

print(json.dumps(data3, indent=2))

with urlopen("https://wikimedia.org/api/rest_v1/metrics/pageviews/top/en.wikipedia/all-access/2023/11/all-days") as response4:
  source4 = response4.read()

data4 = json.loads(source4)

print(json.dumps(data4, indent=2))

with urlopen("https://wikimedia.org/api/rest_v1/metrics/pageviews/top/en.wikipedia/all-access/2023/10/all-days") as response5:
  source5 = response5.read()

data5 = json.loads(source5)

print(json.dumps(data5, indent=2))

with urlopen("https://wikimedia.org/api/rest_v1/metrics/pageviews/top/en.wikipedia/all-access/2023/09/all-days") as response6:
  source6 = response6.read()

data6 = json.loads(source6)

print(json.dumps(data6, indent=2))

with urlopen("https://wikimedia.org/api/rest_v1/metrics/pageviews/top/en.wikipedia/all-access/2023/08/all-days") as response7:
  source7 = response7.read()

data7 = json.loads(source7)

print(json.dumps(data7, indent=2))

with urlopen("https://wikimedia.org/api/rest_v1/metrics/pageviews/top/en.wikipedia/all-access/2023/07/all-days") as response8:
  source8 = response8.read()

data8 = json.loads(source8)

print(json.dumps(data8, indent=2))

with urlopen("https://wikimedia.org/api/rest_v1/metrics/pageviews/top/en.wikipedia/all-access/2023/06/all-days") as response9:
  source9 = response9.read()

data9 = json.loads(source9)

print(json.dumps(data9, indent=2))

with urlopen("https://wikimedia.org/api/rest_v1/metrics/pageviews/top/en.wikipedia/all-access/2023/05/all-days") as response10:
  source10 = response10.read()

data10 = json.loads(source10)

print(json.dumps(data10, indent=2))

with urlopen("https://wikimedia.org/api/rest_v1/metrics/pageviews/top/en.wikipedia/all-access/2023/04/all-days") as response11:
  source11 = response11.read()

data11 = json.loads(source11)

print(json.dumps(data11, indent=2))