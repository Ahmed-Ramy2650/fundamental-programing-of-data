departuretime = input("Enter the departure time (hh:mm): ")
departure = departuretime.split(":")
departurehours = int(departure[0])
departureminutes = int(departure[1])

arrivaltime = input("Enter the arrival time (hh:mm): ")
arrival = arrivaltime.split(":")
arrivalhours = int(arrival[0])
arrivalminutes = int(arrival[1])

hours = arrivalhours - departurehours
minutes = arrivalminutes - departureminutes

if minutes < 0:
    hours -= 1
    minutes += 60
if hours < 0:
    hours += 12

print("The trip time",hours ,"hr")
print("The trip time",minutes ,"min")
