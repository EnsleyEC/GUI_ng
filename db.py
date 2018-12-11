from neo4jrestclient.client import GraphDatabase

class Database(object):

    def __init__(self, uri, user, password_): 
        self.db = GraphDatabase(uri, username=user, password=password_)
        
    def close(self):
        self.db.close()

    def _create_node(self,_label,_name):
        # Create one node without relationship 
        node = self.db.labels.create(_label)
        n1 = self.db.nodes.create(name=_name)
        node.add(n1)
    def _create_two_nodes(self,_label1,_name1,_label2,_name2,_relationship):
        # Create some nodes with labels and relationship between then
        node_1 = self.db.labels.create(_label1)
        node_2 = self.db.labels.create(_label2)
        n1 = self.db.nodes.create(name=_name1)
        node_1.add(n1)
        n2 = self.db.nodes.create(name=_name2)
        node_2.add(n2)
 
        n1.relationships.create(_relationship,n2)
