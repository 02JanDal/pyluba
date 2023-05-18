This directory contains some files related to the Protocol Buffer schema used in various ways by the Luba and app.

* `test_data.text` - A few sample base64 encoded messages that can be used for testing
* `protobuf_config.py` - Type hints for `protobuf-inspector` and code to generate `luba.proto`
* `luba.proto` - A protobuf schema file
* `compile.sh` - Compiles from `protobuf_config.py` to `luba.proto` and on to the Python file in the package

### Working with protobuf-inspector

[`protobuf-inspector`](https://github.com/mildsunrise/protobuf-inspector) is a great tool to verify types in
a Protobuf message. Use it like `echo "CPMBEAEYByACKJOTAjABYgQiAgg8" | base64 -d | protobuf_inspector`. When
invoked from this directory it will automatically pick up the types and field names provided by `protobuf_config.py`
for better results.
