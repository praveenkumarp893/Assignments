import json

json_str = '{"a":{"b":{"c":"d"}}}';
sobj = json.loads(json_str);
key = "a/b";
def getValue(obj, path):
    if not path:
        return obj
    props = path.split("/")
    return getValue(obj[props.pop(0)], "/".join(props))
print(getValue(sobj, key))
