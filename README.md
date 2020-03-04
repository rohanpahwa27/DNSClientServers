# DNSClientServers

Names: 
Abhishek Modoor (avm67)
Rohan Pahwa (rp930)


Recursive functionality: 
Our project implements recursive client functionality through the path the client takes to communicate with the Root and Top Level servers. The client first connects to the Root server to match its hostname to the server. If there is no match, our recursive functionality will cause the Root server to send an acknowledgement back to the client with the TSHostname that the client will need to connect to the Top Level server. Once client connects to the TS server, only then can it determine if its hostname is located within the TS server. 

Known issues:
As of currently, there are no issues as the code follows the recursive functionality of the DNS Client servers. Not only that, but we have also ensured that it can run on multiple machines because RS is able to store the TSHostname and return it to the client whenever there is no match. 

Problems during development:
Recursive functionality: Ensuring that ts.py is able to rewrite the hostname of DNSRS with its own so that rs.py has the tshostname whenever a client doesn't find a match
Collaboration: Ensuring that partner is keeping code clear with comments so other partner may understand what was added
Python: Keeping functionality within 2.7 and getting used to python syntax
Bugs: executing sleep method when client sends data so that data is sent and received in order
Structure: Storing the hostname, IP addresses, and Flags from text file in appropriate python dictionary structure
Testing: Testing between multiple machines

Lessons:
How client communicates with multiple servers based on understanding of root and top level servers hierarchies.
Ensuring that recursive functionality works + not to confuse it with iterative function
Ensuring that functionality works between multiple machines



Internet Technology: Creating a simplified Root DNS server and a top level DNS server both connected to a client

