import simplenote

def simplenote_login(username, password):
    simplenote_instance = simplenote.Simplenote(username, password)
    return (simplenote_instance, simplenote_instance.authenticate(username, password))