import pylibmc
import json

mc = pylibmc.Client(["127.0.0.1"], binary=True, behaviors={"tcp_nodelay": True, "ketama": True})

expTime = 900

# set primitive
mc.set("key_python_1", "value_python_1", expTime)
mc.set("key_python_2", "value_python_2", expTime)
mc.set("key_python_3", "value_python_3", expTime)
mc.set("key_python_4", "value_python_4", expTime)

# set object
staff = {
    "name": "Elon Musk",
    "age": 45
}

mc.set("key_set_python_object", json.dumps(staff))


# add
result = mc.add("key_python_1", "value_python_1_another", expTime)
print "State of add command is " + str(result)

# Get values from single keys
print mc.get("key_python_1")
print mc.get("key_python_2")
print mc.get("key_python_3")
print mc.get("key_python_4")

# Get values from multiple keys
print mc.get_multi(["key_python_1", "key_python_2"])

# Get values from java client
java_object = json.loads(mc.get("key_set_java_object"))
print java_object

# delete, replace, append, append, incr, decr, gets, cas
# http://sendapatch.se/projects/pylibmc/reference.html
# token = mc.gets("key_python_1")
# mc.cas("key_python_1", "value_python_1_new", token)
