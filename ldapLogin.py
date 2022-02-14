from ldap3 import Server, Connection, ALL

def tryLdap(host, port, username, password):
    try:
        server = Server(host, port, get_info=ALL)
        conn = Connection(
            server,
            user=username,
            password=password,
            auto_bind=True)
        conn.unbind()
        return True
    except Exception as e:
        return False