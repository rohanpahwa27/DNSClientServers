# DNSClientServers

Recursive functionality: 
Our project implements recursive client functionality through the path the client takes to communicate with the Root and Top Level servers. The client first connects to the Root server to match its hostname to the DNS server. If there is no match, our recursive functionality will cause the Root server to send an acknowledgement back to the client with the TSHostname that the client will need to connect to the Top Level server. Only after the client receives a response from the Root server, can it connect to the top Top Level server. 



Internet Technology creating a simplified Root DNS server and a top level DNS server both connected to a client

