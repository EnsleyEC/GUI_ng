from db import Database

def main():
    
    ng = Database("http://localhost:11002/","neo4j","ensleyn")
    ng._create_two_nodes("User","Fernando","Arquitetura","NovaGenesis","USA")

if __name__ == "__main__":
    main()
