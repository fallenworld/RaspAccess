all : server client
server : access.c access_svc.c access.h
	c++ -o server access.c access_svc.c access.h -lnsl
client : client.c access_clnt.c access.h
	c++ -o client client.c access_clnt.c access.h -lnsl
clean:
	rm server client
