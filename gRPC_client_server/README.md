
# gRPC Client/Server over mTLS

Needed to learn gRPC for work on capstone.
gRPC (Google Remote Procedure Call) is a new protocol for sending structured data
over the mTLS. 

### gRPC ###

Define formats in *.proto files that contain the structure of what data can be sent.
These protobuf files consist of messages, which are data formats,
and services, that can run code.

```protobuf
message Person {
  required string name = 1;
}

service Contacts {
  rpc sayHello(Person) returns (HelloResponse) {};
}
```

Quick reminder: mTLS is a two-way handshake.

Define an IDL (Interface Definition Language)
- https://developers.google.com/protocol-buffers/docs/proto3

Nice writeup from someone here that helped me with generating keys
- https://www.handracs.info/blog/grpcmtlsgo/

Generate a CA certificate and a CA key.
I did all these bash commands to generate client/server keys 
and to define a certificate.

```
$ openssl ecparam -name prime256v1 -genkey -noout -out cakey.key
$ openssl req -x509 -new -nodes -key cakey.key -subj "/CN=TestCA/C=MY" -days 730 -out cacert.pem
$ openssl ecparam -name prime256v1 -genkey -noout -out server.key
$ cat > csr.conf << EOF [config contents] 
$ openssl req -new -key server.key -out server.csr -config csr.conf
$ openssl x509 -req -in server.csr -CA cacert.pem -CAkey cakey.key -CAcreateserial -out server.pem -days 90 -extfile csr.conf -extensions req_ext
$ openssl ecparam -name prime256v1 -genkey -noout -out client.key
$ cat > csrclient.conf << EOF [config contents]
$ openssl req -new -key client.key -out client.csr -config csrclient.conf
$ openssl x509 -req -in client.csr -CA cacert.pem -CAkey cakey.key -CAcreateserial -out client.pem -days 90 -extfile csrclient.conf -extensions req_ext
```


